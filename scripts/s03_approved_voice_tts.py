#!/usr/bin/env python3
"""Check S03 voice references; optionally generate up to N preview lines with Chatterbox Nano."""
from __future__ import annotations
import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
REGISTRY=R/"assets/voice_refs/v6/VOICE_REFERENCES.json"
VOICE={"내레이션":"narrator","피노키오":"pinocchio","제페토":"geppetto","파란 요정":"blue_fairy"}
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--synthesize",action="store_true",help="default is verify only; actual TTS only if explicit")
    p.add_argument("--limit",type=int,default=2,help="number of short preview lines")
    p.add_argument("--device",default="cpu",choices=["cpu","cuda","mps"])
    a=p.parse_args()
    book=json.loads(REGISTRY.read_text(encoding="utf-8"))
    design=json.loads((R/"scenes/S03/scene_design_v2.json").read_text(encoding="utf-8"))
    todo=[(beat["id"],item["speaker"],item["text"]) for beat in design["scenes"]
          for item in beat["dialogue"] if item["kind"] in ("ORIGINAL","NEW") and item.get("speaker") in VOICE]
    if not todo:raise RuntimeError("No S03 dialogue")
    for slug,info in book["voices"].items():
        ref=R/info["reference_mp3_path"]
        if not ref.is_file():raise RuntimeError(f"MISSING approved {slug}: {ref}")
        if hashlib.sha256(ref.read_bytes()).hexdigest()!=info["sha256"]:
            raise RuntimeError(f"SHA mismatch for approved voice {slug}")
        print("VOICE_REF_PASS",slug,info["approved_candidate"],ref)
    print("S03 voiced screenplay lines",len(todo))
    if not a.synthesize:
        print("DRY RUN: no voice generated. To render samples use --synthesize --limit 3")
        return
    if a.limit<=0 or a.limit>10:
        raise RuntimeError("Only 1-10 preview lines allowed in one call; avoid unwanted long CPU generations")
    from chatterbox.tts_turbo import ChatterboxTurboTTS
    import torchaudio as ta
    out=R/"scenes/S03/audio/voice_previews"
    cache=R/"scenes/S03/audio/reference_cache"
    out.mkdir(parents=True,exist_ok=True)
    cache.mkdir(parents=True,exist_ok=True)
    for slug,info in book["voices"].items():
        mp3=R/info["reference_mp3_path"]
        wav=cache/f"{slug}.wav"
        subprocess.run(["ffmpeg","-y","-v","error","-i",str(mp3),"-ar","24000","-ac","1",
                        "-c:a","pcm_s16le",str(wav)],check=True)
    model=ChatterboxTurboTTS.from_pretrained(device=a.device,nano=True)
    for n,(beat,speaker,text) in enumerate(todo[:a.limit],1):
        slug=VOICE[speaker]
        pcm=model.generate(text,audio_prompt_path=str(cache/f"{slug}.wav"))
        filename=out/f"S03-{n:03d}_{slug}.wav"
        ta.save(str(filename),pcm.cpu(),model.sr)
        print("PREVIEW_NOT_APPROVED",beat,speaker,text,filename)
    print("MUST compare with S01 V7 audio and obtain listening approval; not final S03 delivery.")
if __name__=="__main__":
    try:main()
    except Exception as e:
        print("FAIL",type(e).__name__,str(e),file=sys.stderr)
        raise
