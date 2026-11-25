"""Bind measured S12 footage to the established Tales chapter player."""

import argparse
import base64
import hashlib
import json
import math
import os
import re
import runpy
import shutil
import subprocess
import tempfile
import wave
from html import escape
from itertools import pairwise
from pathlib import Path

HERE = Path(__file__).resolve().parent
V3 = HERE.parent
SCENES = V3.parents[1]
BUILD = V3 / "build"
HANDOFF = V3 / "canonical"
S11 = Path("/workspace/scratch/s11-v2/player/final")
BASE_WEB = S11 / "app-work/restored-cold"
PRIOR = runpy.run_path(str(SCENES / "S09/production/player/build_player.py"))
require = PRIOR["require"]
FPS = 24
RATE = 24_000
SAMPLES_PER_FRAME = RATE // FPS
TITLE = "친구를 구한 진짜 아이"
PRIOR_TITLE = "같은 음악, 새로운 선택"

def read(path):
    return json.loads(path.read_text(encoding="utf-8"))

def manifest(path):
    definition = path.read_text(encoding="utf-8").strip()
    require(definition.startswith("const MEDIA = ") and definition.endswith(";"),
            f"Unexpected media declaration: {path}")
    return json.loads(definition.removeprefix("const MEDIA = ").removesuffix(";"))

def close(left, right):
    return math.isclose(left, right, abs_tol=1e-7, rel_tol=0)

def protected_ranges(authored, cues, events, duration, editing_shots, all_shots, cut_ends):
    gate_by_id = {gate["id"]: gate for gate in events}
    output = []
    for band in authored:
        key = band["from"]
        if key.endswith("_ACCEPTED"):
            gate_id = key.removesuffix("_ACCEPTED")
            if gate_id not in gate_by_id:
                # A legitimate excerpt cannot contain a gated reaction without its prompt.
                continue
            start = gate_by_id[gate_id]["at"]
        elif key in cues:
            start = cues[key]["start"]
        elif all_shots[key] < editing_shots[0]:
            start = 0
        else:
            continue
        last = band["to"]
        if last in cues:
            end = cut_ends[last] if last in {"S12-U033", "S12-U044"} else cues[last]["end"]
        elif all_shots[last] > editing_shots[-1]:
            end = duration
        else:
            continue
        if end <= start:
            continue
        require(not any(start < gate["at"] < end for gate in events),
                f"Learning activity interrupts {band['id']}")
        output.append({"id": band["id"], "start": start, "end": end})
    return output

def validate_edit(source, handoff=HANDOFF, *, excerpt=False):
    story = handoff / "story"
    paths = {"story": story / "scene_design_v2.json", "interaction": story / "interaction_map_v2.json",
             "voice_jobs": story / "S12_VOICE_JOBS.json"}
    design, turns, voice = map(read, paths.values())
    jobs = voice["jobs"]
    edit = read(source / "edit.json")
    require(edit["fixture"] is False and edit["contract"] == "S12_V3_71_50_10"
            and design["scene"] == turns["scene"] == edit["episode"] == "S12" and design["title"] == TITLE
            and edit["source_fingerprints"] == {kind: hashlib.sha256(path.read_bytes()).hexdigest()
                                                for kind, path in paths.items()},
            "S12 player requires real production inputs")
    require(edit["fps"] == design["target_fps"] == FPS and type(edit["frames"]) is int
            and edit["frames"] > 0 and close(edit["duration"], edit["frames"]/FPS),
            "Invalid measured picture clock")
    cuts = {cut["id"]: cut for cut in edit["cuts"]}
    require(len(cuts) == len(edit["cuts"]) and cuts, "Duplicate cut or empty edit")
    shot_ids = [shot["id"] for shot in design["shots"]]
    start_shot = shot_ids.index(next(iter(cuts)))
    end_shot = start_shot + len(cuts)
    require(list(cuts) == shot_ids[start_shot:end_shot], "Requires consecutive authored S12 cuts")
    if not excerpt:
        require(not edit.get("excerpt") and len(cuts) == len(shot_ids) == 50
                and edit["duration"] >= design["minimum_narrative_seconds"],
                "App release requires 50 S12 cuts and at least 360 measured narrative seconds")
    require(edit["cuts"][0]["first"] == 0 and edit["cuts"][-1]["end"] == edit["frames"]
            and all(cut["first"] < cut["end"] for cut in edit["cuts"])
            and all(a["end"] == b["first"] for a,b in pairwise(edit["cuts"])), "Cut clock is discontinuous")
    authored_dialogue = [job for job in jobs if job["kind"] != "EXTERNAL_MODEL"]
    authored_models = {job["job_id"]: job for job in jobs if job["kind"] == "EXTERNAL_MODEL"}
    dialogue = [(cut["id"], cue) for cut in edit["cuts"] for cue in cut["audio"]]
    expected = [(line["shot_id"], line["dialogue_id"], line["speaker"], line["spoken_text"])
                for line in authored_dialogue if line["shot_id"] in cuts]
    require([(shot, cue["id"], cue["speaker"], cue["text"]) for shot,cue in dialogue] == expected,
            "Measured spoken lines differ from the approved script")
    require(all(cuts[shot]["first"]/FPS <= cue["start"] + 1e-7 < cue["end"] + 1e-7
                <= cuts[shot]["end"]/FPS + 2e-7 for shot,cue in dialogue)
            and all(a["end"] <= b["start"] + 1e-7 for (_,a),(_,b) in pairwise(dialogue)),
            "A line is outside its shot or overlaps the next line")
    cues = {cue["id"]: cue for _, cue in dialogue}
    line_to_shot = {line["dialogue_id"]: line["shot_id"] for line in authored_dialogue}
    require(len(cues) == len(dialogue) and len(authored_dialogue) == 71 and len(authored_models) == 10,
            "Unexpected S12 production voice identifiers")
    authored_turns = []
    for gate in turns["events"]:
        prompt = gate["prompt_shot_id"]
        reaction = gate["reaction_shot_ids"]
        resume = line_to_shot[gate["resume_dialogue_id"]]
        touched = set([prompt, *reaction, resume]) & cuts.keys()
        if not touched:
            continue
        complete = {prompt, *reaction, resume} <= cuts.keys()
        # A review may end at a prompt or begin at a later reply after the whole reaction.
        # The actual reaction cannot appear unless its prompt is also included.
        require(complete or touched == {prompt} or (resume not in reaction and touched == {resume}),
                f"Excerpt truncates or disjoins {gate['id']}")
        if complete:
            authored_turns.append(gate)
    measured = edit["events"]
    require([e["id"] for e in measured] == [g["id"] for g in authored_turns]
            and (excerpt or len(measured) == 10), "Unexpected measured S12 gate order")
    for gate, spec in zip(measured, authored_turns, strict=True):
        ident = gate["id"]
        reaction_ids = spec["reaction_shot_ids"]
        require(all(gate[k] == spec[v] for k,v in (
            ("prompt_shot_id","prompt_shot_id"), ("question_dialogue_id","question_dialogue_id"),
            ("example_dialogue_id","model_job_id"), ("example_text","cue"), ("resume_dialogue_id","resume_dialogue_id")))
            and gate["react_shot_id"] == reaction_ids[0]
            and gate["reaction_shot_ids"] == reaction_ids, f"Wrong prompt, example, or reaction route for {ident}")
        question = cues[spec["question_dialogue_id"]]
        follow_up = cues[spec["resume_dialogue_id"]]
        prompt, first_reaction = cuts[spec["prompt_shot_id"]], cuts[reaction_ids[0]]
        frame = gate["frame"]
        require(type(frame) is int and prompt["end"] == frame == first_reaction["first"]
                and close(gate["at"], frame/FPS) and close(question["end"], frame/FPS)
                and gate["question_wav_exact_end_sample"] == frame*SAMPLES_PER_FRAME, f"Inexact question stop for {ident}")
        stop = gate["reaction_window_end"]
        require(frame/FPS < gate["reaction_end"] <= stop <= follow_up["start"] + 1e-7
                and stop <= cuts[reaction_ids[-1]]["end"]/FPS + 1e-7,
                f"Reaction or follow-up timing differs for {ident}")
        if ident == "I21":
            require(close(gate["reaction_end"], cuts[reaction_ids[-1]]["end"]/FPS)
                    and line_to_shot[follow_up["id"]] == "S12-C15", "I21 reaction must finish C14 before U011")
        elif len(reaction_ids) == 1:
            lead = first_reaction["action_windows"]["lead"]
            require(close(lead["start"], gate["at"]) and close(lead["end"], stop),
                    f"{ident} and its reaction use different clocks")
        model = authored_models[spec["model_job_id"]]
        require(model["event_id"] == ident and model["spoken_text"] == gate["example_text"], f"Wrong model for {ident}")
        PRIOR["check_asset"](source/"audio"/f"{model['job_id']}.wav")
        gate["repeat_example_after_no_response_seconds"] = turns["global_policy"]["repeat_example_after_no_response_seconds"]
    require(turns["protected_narrative"] == design["protected_narrative"], "Protected passages differ")
    edit["protected_ranges"] = protected_ranges(
        design["protected_narrative"], cues, measured, edit["duration"],
        (start_shot,end_shot-1), {ident: shot_ids.index(shot) for ident,shot in line_to_shot.items()},
        {cue["id"]: cuts[shot]["end"]/FPS for shot,cue in dialogue},
    )
    edit["protected_opening"] = {"end": 0}
    edit["protected_tail"] = {"first_shot_frame": edit["frames"]}
    edit["s12_excerpt"] = [next(iter(cuts)), next(reversed(cuts))] if excerpt else None
    return edit

def verify_chapters(master, media, edit):
    video = PRIOR["probe_video"](master)
    require((video["codec_name"],video["pix_fmt"],video["has_b_frames"],video["avg_frame_rate"],
             video["width"],video["height"],int(video["nb_frames"])) ==
            ("h264","yuv420p",0,"24/1",1920,1080,edit["frames"]),
            "S12 master needs 1920×1080 H.264 24 fps and exact clock")
    packets = PRIOR["packet_hashes"](master)
    require(len(packets) == edit["frames"], "Master packet clock is off")
    parts = manifest(media/"media.js")["parts"]
    borders = [0, *(e["frame"] for e in edit["events"]), edit["frames"]]
    for part, (first,last) in zip(parts,pairwise(borders),strict=True):
        path = media / part["src"]
        require(PRIOR["packet_hashes"](path) == packets[first:last]
                and close(part["start"],first/FPS) and close(part["end"],last/FPS),
                f"{part['src']}: picture or chapter boundaries differ from the master")
        audio = json.loads(subprocess.check_output([
            "ffprobe","-v","error","-show_entries","stream=codec_name,time_base,start_pts,duration_ts",
            "-select_streams","a:0","-of","json",str(path),
        ]))["streams"][0]
        require((audio["codec_name"],audio["time_base"],audio["start_pts"],audio["duration_ts"])
                == ("aac", f"1/{RATE}", 0, (last-first)*SAMPLES_PER_FRAME),
                f"{part['src']}: audio chapter sample boundary differs")
    return {"chapters":len(parts),"gates":len(edit["events"]),"frames":len(packets),"resolution":[1920,1080]}

def chapters(source, master, output, handoff=HANDOFF, *, excerpt=False):
    require(not output.exists(), "Set a fresh asset output directory")
    edit = validate_edit(source,handoff,excerpt=excerpt)
    mix = source/"mix.wav"
    with wave.open(str(mix),"rb") as wav:
        require((wav.getframerate(),wav.getnchannels(),wav.getsampwidth(),wav.getnframes())
                == (RATE,1,2,edit["frames"]*SAMPLES_PER_FRAME), "PCM mix must share the measured master clock")
    output.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".s12-chapters-",dir=output.parent) as tmp:
        media = Path(tmp)/"assets"
        PRIOR["encode_chapters"](media,master,mix,source/"audio",edit)
        data = manifest(media/"media.js")
        data["protectedRanges"] = edit["protected_ranges"]
        data["reviewExcerpt"] = edit["s12_excerpt"]
        cut_by_id = {cut["id"]:cut for cut in edit["cuts"]}
        for i, gate in enumerate(edit["events"]):
            data["parts"][i]["gateStart"] = cut_by_id[gate["prompt_shot_id"]]["first"]/FPS
            # The old helper calls only the first cut's lead. I21 runs C12–C14 before U011.
            start = data["parts"][i+1]["start"]
            data["parts"][i+1]["reactionEnd"] = gate["reaction_window_end"] - start
        (media/"media.js").write_text("const MEDIA = "+json.dumps(data,ensure_ascii=False)+";\n",encoding="utf-8")
        checks = verify_chapters(master,media,edit)
        media.rename(output)
    print("S12 measured chapter checks",checks)
    return edit, checks

def exact_replace(text, old, new):
    require(text.count(old) == 1, "The approved S11 player interface changed")
    return text.replace(old,new,1)

def player(source):
    source = exact_replace(source, 'let exampleGeneration = 0, hintTimer, micState = "idle";',
        'let exampleGeneration = 0, hintTimer, micState = "idle";\n'
        'const completedGates = new Set();\nlet pendingReaction = null;')
    source = exact_replace(source, 'function protectedNarrative() {',
        'function promptActive() {\n'
        '  return ["waiting", "example", "example-error"].includes(mode);\n'
        '}\n\nfunction protectedNarrative() {\n'
        '  if (promptActive()) return false;')
    source = exact_replace(source, 'function showPosition() {',
        'function finishReaction(clip, time) {\n'
        '  if (pendingReaction !== null && part === pendingReaction + 1\n'
        '      && !film.seeking && time + 1e-7 >= clip.reactionEnd) {\n'
        '    completedGates.add(MEDIA.parts[pendingReaction].id);\n'
        '    pendingReaction = null;\n'
        '  }\n}\n\nfunction showPosition() {')
    source = exact_replace(source, '  const text = ["playing", "paused"].includes(mode)',
        '  if (["playing", "paused"].includes(mode)) finishReaction(clip, time);\n'
        '  const text = ["playing", "paused"].includes(mode)')
    source = exact_replace(source, 'function seek(time) {',
        'function seek(time) {\n'
        '  if (pendingReaction !== null || (promptActive() && time >= MEDIA.parts[part].end)) {\n'
        '    showPosition();\n    return;\n  }\n'
        '  const unanswered = MEDIA.parts.find(clip => clip.id && !completedGates.has(clip.id));\n'
        '  if (unanswered && time >= unanswered.end) time = unanswered.gateStart;')
    source = exact_replace(source,
        '  if (!["waiting", "example", "example-error"].includes(mode) || suspended()) return;\n'
        '  void startPart(part + 1, 0, true);',
        '  if (!["waiting", "example", "example-error"].includes(mode) || suspended()) return;\n'
        '  pendingReaction = part;\n'
        '  void startPart(part + 1, 0, true);')
    source = exact_replace(source,
        '  if (mode !== "playing" || !film.ended) return;\n  clearPrompt();',
        '  if (mode !== "playing" || !film.ended) return;\n'
        '  const ending = MEDIA.parts[part];\n'
        '  finishReaction(ending, ending.end - ending.start);\n  clearPrompt();')
    source = exact_replace(source, '  } else {\n    mode = "waiting";\n    el("play").disabled = true;',
        '  } else if (completedGates.has(clip.id)) {\n'
        '    void startPart(part + 1, 0, true);\n'
        '  } else {\n    mode = "waiting";\n    el("play").disabled = true;')
    return exact_replace(source, '  } else if (["ready", "finished"].includes(mode)) {\n    void startPart(0, 0, true);',
        '  } else if (["ready", "finished"].includes(mode)) {\n'
        '    completedGates.clear();\n    pendingReaction = null;\n'
        '    void startPart(0, 0, true);')

def title_for(data):
    bounds = data["reviewExcerpt"]
    return f"{TITLE} · {bounds[0]}–{bounds[1]} 검수 구간" if bounds else TITLE

def card(poster,duration):
    minutes,seconds = divmod(int(duration),60)
    return f'''    <a class="episode-card" href="s12/index.html">
      <img src="{escape(poster,quote=True)}" alt="">
      <div class="details">
        <p class="series">피노키오 · 12화</p>
        <h2>{TITLE}</h2>
        <p class="language">{minutes}분 {seconds}초</p>
      </div>
    </a>
'''

def write_episode(base, media, target):
    prior = base/"s11"
    data = manifest(media/"media.js")
    title = title_for(data)
    page = (prior/"index.html").read_text(encoding="utf-8")
    require(page.count(PRIOR_TITLE)==3,"The existing S11 page layout changed")
    target.mkdir()
    (target/"index.html").write_text(page.replace(PRIOR_TITLE,title),encoding="utf-8")
    shutil.copyfile(prior/"voice.js",target/"voice.js")
    (target/"player.js").write_text(player((prior/"player.js").read_text(encoding="utf-8")),encoding="utf-8")
    for asset in ("media.js",*(part[key] for part in data["parts"] for key in ("src","example") if key in part)):
        path = target/asset
        path.parent.mkdir(exist_ok=True)
        try:
            os.link(PRIOR["check_asset"](media/asset),path)
        except OSError:
            shutil.copyfile(media/asset,path)

def stage_web(base, media, cover, output):
    require(not output.exists() and not output.resolve().is_relative_to(base.resolve()),"Choose a fresh web staging path")
    catalog = (base/"index.html").read_text(encoding="utf-8")
    require(re.findall(r'<a class="episode-card" href="([^"]+)"',catalog)
            == ["s01.html",*(f"s{n:02}/index.html" for n in range(2,12))],
            "S12 must preserve the authenticated S11 catalog")
    marker = "  </section>\n</main>"
    require(catalog.count(marker)==1,"Catalog insertion marker changed")
    data = manifest(media/"media.js")
    require(not data["reviewExcerpt"] and len(data["parts"]) == 11 and cover.suffix in (".jpg",".png"),
            "An app candidate requires a complete episode with its reviewed cover")
    output.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".s12-web-",dir=output.parent) as tmp:
        tree = Path(tmp)/"web"
        def link_or_copy(source,destination):
            try:
                os.link(source,destination)
            except OSError:
                shutil.copy2(source,destination)
        shutil.copytree(base,tree,copy_function=link_or_copy)
        write_episode(base,media,tree/"s12")
        poster = f"s12-cover{cover.suffix}"
        shutil.copyfile(cover,tree/poster)
        # Unlink copied index before writing. Never modify the S11 hardlink.
        (tree/"index.html").unlink()
        (tree/"index.html").write_text(catalog.replace(marker,card(poster,data["parts"][-1]["end"])+marker),
                                      encoding="utf-8")
        tree.rename(output)

def standalone(base, media, output):
    require(not output.exists(),"Choose a fresh stand-alone review output")
    output.parent.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".s12-review-",dir=output.parent) as tmp:
        tmp = Path(tmp)
        episode = tmp/"s12"
        write_episode(base,media,episode)
        parts = manifest(episode/"media.js")["parts"]
        page = (episode/"index.html").read_text(encoding="utf-8")
        css = (base/"style.css").read_text(encoding="utf-8")
        page = exact_replace(page,'<link rel="stylesheet" href="../style.css">',f"<style>\n{css}\n</style>")
        page = re.sub(r'    <a class="back-link"[^\n]+\n',"",page,count=1)
        for name in ("voice.js","../mic-turn.js","../live.js","../seekbar.js","media.js","player.js"):
            path = (base/name[3:]) if name.startswith("../") else episode/name
            script = ("function watchWebRevision() {}" if name == "../live.js" else path.read_text(encoding="utf-8"))
            if name == "media.js":
                script += PRIOR["EMBEDDED_MEDIA"]
            page = exact_replace(page,f'<script src="{name}"></script>',PRIOR["inline_script"](script))
        staged = tmp/output.name
        with staged.open("w",encoding="utf-8") as stream:
            stream.write(page.removesuffix("</html>\n"))
            for asset in (part[key] for part in parts for key in ("src","example") if key in part):
                stream.write(f'<script type="application/octet-stream" id="embedded-{escape(asset,quote=True)}">')
                with (episode/asset).open("rb") as file:
                    while block := file.read(3*256*1024):
                        stream.write(base64.b64encode(block).decode("ascii"))
                stream.write("</script>\n")
            stream.write("</html>\n")
        staged.rename(output)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest="command",required=True)
    split=sub.add_parser("chapters")
    split.add_argument("--source",type=Path,default=BUILD)
    split.add_argument("--master",type=Path,required=True)
    split.add_argument("--handoff",type=Path,default=HANDOFF)
    split.add_argument("--excerpt",action="store_true")
    web=sub.add_parser("web")
    web.add_argument("--cover",type=Path,required=True)
    review=sub.add_parser("standalone")
    for command in (web,review):
        command.add_argument("--base",type=Path,default=BASE_WEB)
        command.add_argument("--media",type=Path,required=True)
    for command in (split,web,review):
        command.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    if args.command=="chapters":
        chapters(args.source,args.master,args.output,args.handoff,excerpt=args.excerpt)
    elif args.command=="web":
        stage_web(args.base,args.media,args.cover,args.output)
    else:
        standalone(args.base,args.media,args.output)

if __name__=="__main__":
    main()
