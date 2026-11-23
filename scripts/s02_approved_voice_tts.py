#!/usr/bin/env python3
"""Validate approved voice reference pack and optionally synthesize a few S02 lines.
Default: dry-run. Actual TTS needs chatterbox-tts, torchaudio, local voice pack.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SPEAKERS = {"내레이션": "narrator", "피노키오": "pinocchio",
            "제페토": "geppetto", "파란 요정": "blue_fairy"}
def main():
    p = argparse.ArgumentParser()
    p.add_argument("--refs", type=Path, default=ROOT/"local_assets"/"approved_voice_refs")
    p.add_argument("--synthesize", action="store_true",
                   help="generate WAV previews; requires explicit user direction")
    p.add_argument("--dry-run", action="store_true", help="dry-run is also the default")
    p.add_argument("--limit", type=int, default=2)
    p.add_argument("--device", default="cpu")
    a = p.parse_args()
    design=json.loads((ROOT/"scenes/S02/scene_design_v2.json").read_text(encoding="utf-8"))
    tasks=[(b["id"],line["speaker"],line["text"])
           for b in design["scenes"] for line in b["dialogue"]
           if line["kind"] in ("ORIGINAL","NEW") and line.get("speaker") in SPEAKERS]
    print(f"S02 voiced lines: {len(tasks)}")
    if not a.synthesize:
        print("DRY-RUN only; no audio generated. Reference pack at:",a.refs)
        for x in tasks[:max(0,a.limit)]: print(*x,sep=" | ")
        if not (a.refs/"voice_manifest.json").is_file():
            print("Reference pack not mounted: provide separately from approved voice ZIP.")
        return
    if a.limit<=0: raise SystemExit("Refusing unrestricted batch; set a positive --limit")
    mpath=a.refs/"voice_manifest.json"
    if not mpath.is_file(): raise SystemExit(f"MISSING approved reference manifest: {mpath}")
    m=json.loads(mpath.read_text(encoding="utf-8"))
    for slug in set(SPEAKERS.values()):
        meta=m["voices"][slug]
        mp3=a.refs/meta["reference_mp3_path"]
        wav=a.refs/meta["reference_wav_path"]
        if not wav.is_file() or not mp3.is_file():
            raise SystemExit(f"MISSING approved WAV/MP3: {slug}")
        if hashlib.sha256(mp3.read_bytes()).hexdigest()!=meta["reference_mp3_sha256"]:
            raise SystemExit(f"APPROVED VOICE SHA FAIL: {slug}")
    import torchaudio as ta
    from chatterbox.tts_turbo import ChatterboxTurboTTS
    model=ChatterboxTurboTTS.from_pretrained(device=a.device,nano=True)
    dest=ROOT/"scenes/S02/audio/voice_previews"
    dest.mkdir(parents=True,exist_ok=True)
    for i,(beat,speaker,line) in enumerate(tasks[:a.limit],1):
        slug=SPEAKERS[speaker]
        ref=a.refs/m["voices"][slug]["reference_wav_path"]
        out=dest/f"S02-{i:03d}_{slug}.wav"
        wav=model.generate(line,audio_prompt_path=str(ref))
        ta.save(str(out),wav.cpu(),model.sr)
        print("GENERATED",beat,speaker,line,str(out))
    print("PREVIEWS ONLY: listening comparison to locked S01 is still REQUIRED")
if __name__=="__main__":
    main()
