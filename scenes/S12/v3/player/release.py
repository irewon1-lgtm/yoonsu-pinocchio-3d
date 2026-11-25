"""Prepare an authenticated local S12 candidate without writing to the deployed app."""

import argparse
import hashlib
import json
import re
import runpy
import struct
import tempfile
from pathlib import Path

from build import BASE_WEB, BUILD, S11, SCENES, chapters, manifest, require, stage_web

PACKER = runpy.run_path(str(SCENES.parent / "android/pack_release.py"))
S11_RELEASE = S11 / "app-work"
VERSION = 17
KEY = Path("/workspace/shared/.english-tales-content/content.key")


def sha(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def locked_predecessors(cipher):
    evidence = json.loads((S11_RELEASE / "release.json").read_text(encoding="utf-8"))
    prior = S11_RELEASE / "prior.bundle"
    last = S11_RELEASE / "candidate/latest.bundle"
    require(evidence["fixture"] is False and sha(prior) == evidence["prior"]
            and sha(last) == evidence["catalog"], "Expected authenticated S11 production evidence")
    version, released = PACKER["open_catalog"](prior, cipher)
    last_version, prepared = PACKER["open_catalog"](last, cipher)
    require((version, last_version) == (15, 16)
            and len(prepared) == evidence["asset_count"]
            and released.keys() < prepared.keys(), "Expected local v15 and v16 catalogs")
    require(all(prepared[name] == digest for name, digest in released.items() if name != "index.html"),
            "The authenticated S11 predecessor changed existing episode files")
    return prior, released, prepared


def verify_catalog(web, entries, previous):
    media = manifest(web / "s12/media.js")
    episode_files = {"s12/index.html", "s12/media.js", "s12/player.js", "s12/voice.js"}
    episode_files.update(f"s12/{part['src']}" for part in media["parts"])
    episode_files.update(f"s12/{part['example']}" for part in media["parts"][:-1])
    poster = (entries.keys() - previous.keys()) - episode_files
    require(poster in ({"s12-cover.png"}, {"s12-cover.jpg"})
            and entries.keys() == previous.keys() | episode_files | poster
            and {name for name in previous if entries[name] != previous[name]} == {"index.html"},
            "S12 staging changed, omitted or added an unexpected file")
    without_s12, count = re.subn(rb'    <a class="episode-card" href="s12/index\.html">.*?    </a>\n', b"",
                                 (web / "index.html").read_bytes(), flags=re.DOTALL)
    require(count == 1 and hashlib.sha256(without_s12).hexdigest() == previous["index.html"].split("\t")[0],
            "The existing app home page differs beyond the S12 card")
    require(entries["s12/voice.js"] == previous["s11/voice.js"], "S12 changed the established microphone module")


def verify_delta(candidate, entries, public, cipher):
    published_digests = {entry.split("\t")[0] for entry in public.values()}
    required = {digest: int(size) for entry in entries.values() for digest, size in [entry.split("\t")]
                if digest not in published_digests}
    objects = candidate / "objects"
    require({path.name for path in objects.glob("*.bundle")} == {f"{digest}.bundle" for digest in required},
            "A v15 installation could not obtain all changed files, including S11")
    block_size = PACKER["BLOCK"]
    for digest, size in required.items():
        sha_plaintext = hashlib.sha256()
        path = objects / f"{digest}.bundle"
        with path.open("rb") as stream:
            prefix = stream.read(8)
            for number, offset in enumerate(range(0, size, block_size)):
                nonce = prefix + struct.pack(">I", number)
                aad = f"english-master-tales-file-v1\n{digest}\n{size}\n{number}".encode()
                block = stream.read(min(block_size, size - offset) + 16)
                sha_plaintext.update(cipher.decrypt(nonce, block, aad))
            require(not stream.read(1) and sha_plaintext.hexdigest() == digest,
                    f"Candidate object does not restore its locked content: {path.name}")
    return len(required)


def stage(source, master, cover, output, *, base=BASE_WEB, key=KEY):
    require(not output.exists(), "Choose a fresh local candidate directory")
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".s12-release-", dir=output.parent) as scratch:
        work = Path(scratch) / "candidate"
        work.mkdir()
        edit, checks = chapters(source, master, work / "chapters")
        web = work / "web"
        stage_web(base, work / "chapters", cover, web)
        cipher = PACKER["AESGCM"](key.read_bytes())
        prior, published, prepared = locked_predecessors(cipher)
        sealed = work / "bundles"
        PACKER["pack"](web, key, VERSION, sealed, prior, False)
        version, entries = PACKER["open_catalog"](sealed / "latest.bundle", cipher)
        require(version == VERSION, "Unexpected content version")
        verify_catalog(web, entries, prepared)
        object_count = verify_delta(sealed, entries, published, cipher)
        report = {
            "version": version,
            "deployed": False,
            "source_master_sha256": sha(master),
            "catalog_sha256": sha(sealed / "latest.bundle"),
            "upgrade_from_local_v15": {"asset_count": len(entries), "new_objects": object_count},
            "v16_preserved_except_app_card_index": len(prepared) - 1,
            "narrative_seconds": edit["duration"],
            "media": checks,
            "android_device_microphone": "NOT_RUN",
        }
        (work / "release.json").write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
        work.rename(output)
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=BUILD)
    parser.add_argument("--master", type=Path, required=True)
    parser.add_argument("--cover", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(stage(args.source, args.master, args.cover, args.output), indent=2))
