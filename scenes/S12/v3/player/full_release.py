"""Stage and check the full S12 app update over an authenticated live catalog."""

import argparse
import json
import re
import shutil
import subprocess
import tempfile
import wave
from pathlib import Path
from urllib.parse import urlsplit

from build import RATE, TITLE, card, chapters, manifest, read, require, validate_edit, write_episode
from preview_release import link_or_copy
from release import KEY, PACKER, sha, verify_delta


BASELINE = Path("/workspace/scratch/s11-s12-app")
APP_ORIGIN = "https://appassets.androidplatform.net"
HOME = "index.html"
S12 = "s12/index.html"
PREVIEW_ROUTES = ("s12/opening/index.html", "s12/after-rescue/index.html")
PRESERVED_ROUTES = ("s01.html", *(f"s{episode:02d}/index.html" for episode in range(2, 12)))
CARD = re.compile(rb'    <a class="episode-card" href="s12/index\.html">.*?    </a>\n', re.DOTALL)


def write_json(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def asset_record(path):
    return f"{sha(path)}\t{path.stat().st_size}"


def open_baseline(baseline, cipher):
    activation = read(baseline / "activation.json")
    bundle = baseline / "live.bundle"
    require(sha(bundle) == activation["catalog_sha256"], "Live baseline differs from its activation evidence")
    version, entries = PACKER["open_catalog"](bundle, cipher)
    require(version == activation["version"] and version >= 18, "S12 needs an authenticated v18 or later baseline")
    require({*PRESERVED_ROUTES, HOME, S12, *PREVIEW_ROUTES} <= entries.keys(),
            "The active app lacks an earlier episode or S12 preview")
    web = baseline / "web"
    for name in (HOME, S12):
        require(asset_record(web / name) == entries[name], f"Live baseline {name} differs from its signed catalog")
    return version, entries, web, bundle, activation["catalog_commit"]


def dialogue_hashes(source, edit):
    story = [row["id"] for cut in edit["cuts"] for row in cut["audio"]]
    models = [gate["example_dialogue_id"] for gate in edit["events"]]
    require(len(story) == 71 and len(models) == 10 and len(set(story + models)) == 81,
            "Expected 71 distinct story lines and 10 distinct speaking models")
    hashes = {}
    for cue in story + models:
        wav = source / "audio" / f"{cue}.wav"
        with wave.open(str(wav), "rb") as source_pcm:
            require((source_pcm.getframerate(), source_pcm.getnchannels(), source_pcm.getsampwidth()) == (RATE, 1, 2)
                    and source_pcm.getnframes() > 0, f"Missing measured 24 kHz mono PCM for {cue}")
        hashes[cue] = sha(wav)
    return hashes


def stage(source, master, output, baseline=BASELINE, cover=None):
    require(not output.exists(), "Choose a fresh release work directory")
    cipher = PACKER["AESGCM"](KEY.read_bytes())
    previous, active, base, live, head = open_baseline(baseline, cipher)
    require(not output.resolve().is_relative_to(base.resolve()), "The staging directory must be outside the live web tree")
    original = (base / HOME).read_bytes()
    require(len(CARD.findall(original)) == 1 and "미리보기".encode() in CARD.search(original).group(),
            "Expected exactly one S12 preview card on the current home page")
    # Reject an excerpt or a planning clock before any expensive media work.
    edit = validate_edit(source)
    require(not edit.get("preview_only") and not edit.get("pilot"), "A preview or pilot cannot replace S12")
    voice = dialogue_hashes(source, edit)
    original_cover = "s12/opening/cover.jpg"
    if cover is not None:
        require(cover.is_file() and cover.suffix in (".png", ".jpg"), "Cover must be an existing PNG or JPG")
    else:
        require(original_cover in active, "Provide an approved cover or retain the existing S12 cover")

    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".s12-full-", dir=output.parent) as scratch:
        work = Path(scratch) / "work"
        work.mkdir()
        _, media_checks = chapters(source, master, work / "chapters")
        web = work / "web"
        shutil.copytree(base, web, copy_function=link_or_copy)
        episode = work / "episode"
        write_episode(base, work / "chapters", episode)
        additions = set()
        for item in episode.rglob("*"):
            if not item.is_file():
                continue
            relative = (Path("s12") / item.relative_to(episode)).as_posix()
            target = web / relative
            if relative == S12:
                target.unlink()
            else:
                require(relative not in active, f"Full S12 would overwrite an existing asset: {relative}")
                additions.add(relative)
            target.parent.mkdir(parents=True, exist_ok=True)
            item.rename(target)
        poster = original_cover
        if cover is not None:
            poster = f"s12-cover{cover.suffix}"
            require(poster not in active, f"Full S12 would overwrite an existing cover: {poster}")
            shutil.copyfile(cover, web / poster)
            additions.add(poster)
        (web / HOME).unlink()
        (web / HOME).write_bytes(CARD.sub(card(poster, edit["duration"]).encode("utf-8"), original, count=1))
        require(CARD.sub(b"", (web / HOME).read_bytes()) == CARD.sub(b"", original),
                "Existing home markup changed outside the S12 card")

        shutil.copyfile(live, work / "prior.bundle")
        candidate = work / "candidate"
        PACKER["pack"](web, KEY, previous + 1, candidate, work / "prior.bundle", False)
        version, entries = PACKER["open_catalog"](candidate / "latest.bundle", cipher)
        require(version == previous + 1 and entries.keys() == active.keys() | additions and
                {name for name in active if entries[name] != active[name]} == {HOME, S12},
                "The candidate changed a previous episode or preview asset")
        require(entries["s12/voice.js"] == active["s11/voice.js"], "S12 changed the established microphone module")
        object_count = verify_delta(candidate, entries, active, cipher)
        changed = additions | {HOME, S12}
        result = {
            "version": version, "previous": previous, "previous_head": head, "mode": "full", "deployed": False,
            "source_baseline": str(baseline.resolve()), "source_master_sha256": sha(master),
            "source_edit_sha256": sha(source / "edit.json"), "source_mix_sha256": sha(source / "mix.wav"),
            "source_fingerprints": edit["source_fingerprints"], "source_wav_sha256": voice,
            "narrative_seconds": edit["duration"], "cut_count": len(edit["cuts"]), "story_lines": 71,
            "speaking_models": 10, "chapter_checks": media_checks,
            "preserved_asset_count": len(active) - 2, "asset_count": len(entries),
            "prior_sha256": sha(work / "prior.bundle"), "catalog_sha256": sha(candidate / "latest.bundle"),
            "changed_assets": {name: entries[name] for name in sorted(changed)},
            "object_count": object_count,
            "objects": {f"objects/{path.name}": sha(path) for path in sorted((candidate / "objects").glob("*.bundle"))},
            # The existing publisher calls its browser route list previews.
            "previews": [{"route": "s11/index.html"}, {"route": S12}],
        }
        write_json(work / "candidate-proof.json", result)
        for name, paths in (("changed", changed), ("asset", entries), ("object", result["objects"])):
            (work / f"{name}-paths.txt").write_text("".join(f"{path}\n" for path in sorted(paths)), encoding="utf-8")
        work.rename(output)
    return result


def check_sealed(work):
    proof = read(work / "candidate-proof.json")
    require(proof["mode"] == "full" and proof["cut_count"] == 50 and proof["narrative_seconds"] >= 360
            and proof["chapter_checks"]["gates"] == 10 and proof["story_lines"] == 71 and proof["speaking_models"] == 10,
            "Full S12 release proof is missing")
    require(sha(work / "candidate/latest.bundle") == proof["catalog_sha256"]
            and sha(work / "prior.bundle") == proof["prior_sha256"], "Sealed candidate or predecessor moved")
    for name, record in proof["changed_assets"].items():
        require(asset_record(work / "web" / name) == record, f"Staged browser asset changed: {name}")
    return proof


def browse(work, chromium, screenshot=None):
    from playwright.sync_api import sync_playwright

    proof = check_sealed(work)
    root = (work / "web").resolve()
    data = manifest(root / "s12/media.js")
    require(data["reviewExcerpt"] is None and len(data["parts"]) == 11, "The app route must open the full episode")
    errors, failures, gate_results = [], [], []
    with sync_playwright() as session:
        browser = session.chromium.launch(executable_path=chromium, args=["--no-sandbox"])
        page = browser.new_page(viewport={"width": 1280, "height": 800})
        page.on("pageerror", lambda error: errors.append(str(error)))

        def serve(route):
            url = urlsplit(route.request.url)
            name = url.path.lstrip("/")
            path = (root / name).resolve()
            if url.netloc == "appassets.androidplatform.net" and path.is_relative_to(root) and path.is_file():
                route.fulfill(path=path, status=200)
            else:
                if name != "favicon.ico":
                    failures.append(route.request.url)
                route.fulfill(status=404, body="")

        page.route("**/*", serve)
        page.goto(f"{APP_ORIGIN}/{HOME}")
        routes = page.locator("a.episode-card").evaluate_all("(cards) => cards.map(card => card.getAttribute('href'))")
        require(routes == [*PRESERVED_ROUTES, S12], "Expected the existing 11 cards and a single full S12 card")
        episode = page.locator(f'a.episode-card[href="{S12}"]')
        require(episode.locator(".series").inner_text() == "피노키오 · 12화", "The S12 card still says preview")
        episode.click()
        page.wait_for_url(f"{APP_ORIGIN}/{S12}")
        page.get_by_role("heading", name=TITLE).wait_for()
        page.get_by_role("button", name="이야기 시작").click()
        for number, clip in enumerate(data["parts"]):
            page.wait_for_function("n => part === n && mode === 'playing' && film.readyState >= 2 && film.currentTime > 0",
                                   arg=number, timeout=20000)
            require(page.evaluate("[film.videoWidth, film.videoHeight]") == [1920, 1080],
                    f"Unexpected media dimensions in chapter {number + 1}")
            if number:
                timeout = int(clip["reactionEnd"] * 1000) + 15000
                page.wait_for_function("pendingReaction === null", timeout=timeout)
                require(page.evaluate("id => completedGates.has(id)", data["parts"][number - 1]["id"]),
                        "Reaction did not complete before the next turn")
            if screenshot is not None and number == 0:
                page.screenshot(path=screenshot)
            if "id" not in clip:
                page.evaluate("film.currentTime = Math.max(0, film.duration - 0.12)")
                page.get_by_role("button", name="다시 보기").wait_for(timeout=10000)
                break
            page.evaluate("""() => {
                window.modelEvents = [];
                promptAudio.addEventListener('playing', () => modelEvents.push('playing'), {once:true});
                promptAudio.addEventListener('ended', () => modelEvents.push('ended'), {once:true});
                film.currentTime = Math.max(0, film.duration - 0.12);
            }""")
            page.wait_for_function("mode === 'waiting' && modelEvents.includes('ended')", timeout=15000)
            require(page.evaluate("modelEvents") == ["playing", "ended"] and page.locator("#line").inner_text() == clip["cue"],
                    f"Actual model audio or prompt differs at {clip['id']}")
            page.locator("#parent").click()
            gate_results.append({"id": clip["id"], "model_playback": "PASS", "guardian": "PASS"})
        page.get_by_role("link", name="← 전체 목록").click()
        page.wait_for_url(f"{APP_ORIGIN}/{HOME}")
        require(len(gate_results) == 10, "The candidate did not play all ten participation turns")
        require(not errors and not failures, f"Candidate app fetch or playback errors: {errors}, {failures}")
        browser.close()
    report = {"result": "PASS", "version": proof["version"], "verified_catalog_sha256": proof["catalog_sha256"],
              "routes": proof["previews"], "chapters_decoded": len(data["parts"]), "gates": gate_results,
              "playback": "decoded each actual chapter, sought to the prompt, observed model playback end, ran each reaction",
              "android_device_microphone": "NOT_RUN"}
    write_json(work / "browser-navigation.json", report)
    return report


def prepare_updater(work, apk_assets, stubs, ecj):
    proof = check_sealed(work)
    baseline = Path(proof["source_baseline"])
    cipher = PACKER["AESGCM"](KEY.read_bytes())
    previous, entries, base, live, _ = open_baseline(baseline, cipher)
    require(previous == proof["previous"] and sha(live) == proof["prior_sha256"], "Updater baseline changed")
    _, seed = PACKER["open_catalog"](apk_assets / "_initial.bundle", cipher)
    cache = work / f"v{previous}-cache"
    (cache / "tales-assets").mkdir(parents=True, exist_ok=True)
    for name, record in entries.items():
        if record == seed.get(name):
            continue
        target = cache / "tales-assets" / record.partition("\t")[0]
        if not target.exists():
            link_or_copy(base / name, target)
        require(asset_record(target) == record, f"Corrupt warm updater cache asset: {name}")
    shutil.copyfile(live, cache / "tales-latest.bundle")

    java = (BASELINE / "S11S12LiveProbe.java").read_text(encoding="utf-8")
    # Version substitutions use one pass to avoid changing the predecessor twice.
    substitutions = {"S11S12LiveProbe": "S12FullLiveProbe", "v17": f"v{previous}", "v18": f"v{proof['version']}",
                     "== 17": f"== {previous}", "== 18": f"== {proof['version']}"}
    java = re.sub("|".join(map(re.escape, substitutions)), lambda match: substitutions[match[0]], java)
    probe = work / "S12FullLiveProbe.java"
    probe.write_text(java, encoding="utf-8")
    classes = work / "classes"
    classes.mkdir(exist_ok=True)
    source = Path(__file__).resolve().parents[4] / "android/src/main/java/kr/yoonsu/englishtales/TalesUpdates.java"
    subprocess.run(["java", "-jar", str(ecj), "-17", "-cp", str(stubs), "-d", str(classes),
                    str(source), str(probe)], check=True)
    runner = (BASELINE / "run_live_probe.py").read_text(encoding="utf-8")
    runner = runner.replace("S11S12LiveProbe", "S12FullLiveProbe")
    for old, new in (("/workspace/scratch/s12-app-preview/web", base),
                     ("/tmp/pin-mic/signed-apk/assets", apk_assets), ("/tmp/pin-mic/probe-classes", stubs)):
        runner = runner.replace(repr(old), repr(str(new)))
    (work / "run_live_probe.py").write_text(runner, encoding="utf-8")
    shutil.copyfile(BASELINE / "wait_for_app_endpoint.py", work / "wait_for_app_endpoint.py")
    return {"updater": "S12FullLiveProbe", "base": str(base), "warm_cache": str(cache),
            "post_activation_check": str(work / "wait_for_app_endpoint.py")}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_subparsers(dest="action", required=True)
    staging = actions.add_parser("stage")
    for option in ("source", "master", "output"):
        staging.add_argument(f"--{option}", type=Path, required=True)
    staging.add_argument("--baseline", type=Path, default=BASELINE)
    staging.add_argument("--cover", type=Path)
    browsing = actions.add_parser("browse")
    browsing.add_argument("--work", type=Path, required=True)
    browsing.add_argument("--chromium", default="/usr/bin/chromium")
    browsing.add_argument("--screenshot", type=Path)
    updater = actions.add_parser("prepare-updater")
    updater.add_argument("--work", type=Path, required=True)
    updater.add_argument("--apk-assets", type=Path, default=Path("/tmp/pin-mic/signed-apk/assets"))
    updater.add_argument("--stubs", type=Path, default=Path("/tmp/pin-mic/probe-classes"))
    updater.add_argument("--ecj", type=Path, default=Path("/tmp/english-tales-sdk/ecj.jar"))
    args = parser.parse_args()
    if args.action == "stage":
        result = stage(args.source, args.master, args.output, args.baseline, args.cover)
    elif args.action == "browse":
        result = browse(args.work, args.chromium, args.screenshot)
    else:
        result = prepare_updater(args.work, args.apk_assets, args.stubs, args.ecj)
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
