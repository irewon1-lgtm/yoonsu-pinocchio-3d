#!/usr/bin/env python3
"""Audit S05 fixed reference voices and optional examples; never synthesize audio.

Default exit 0 certifies reference/assignment integrity only. Use --require-ready
as a production gate: any missing approved speaker then returns exit 2.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
FIXED_CAST = {
    "narrator": ("내레이션", "A", "ec7234237b687246af302db312994c6b9ddc46411c82085a5b1f3884bcfcbddf"),
    "pinocchio": ("피노키오", "A", "a32569705a717ac92c8ecbe1c515b9e31e389f508164458ed22a06adcbba0b3d"),
    "geppetto": ("제페토", "A", "80237e647e1e480987a3cf0a6ac1dc33a3d6b3a40dc62d577f4a0290e338af55"),
    "blue_fairy": ("파란 요정", "C", "c65e44b9c4d221c1fe9052ff201a3d3a0f5bc867c29460130fe2944f59c5965b"),
}


def audit(root: Path) -> dict:
    registry = json.loads((root / "assets/voice_refs/v6/VOICE_REFERENCES.json").read_text(encoding="utf-8"))
    design = json.loads((root / "scenes/S05/scene_design_v2.json").read_text(encoding="utf-8"))
    interactions = json.loads((root / "scenes/S05/interaction_map_v2.json").read_text(encoding="utf-8"))
    voices = registry["voices"]
    for slug, (speaker, candidate, expected_sha) in FIXED_CAST.items():
        if (voices[slug]["speaker"] != speaker or voices[slug]["approved_candidate"] != candidate
                or voices[slug]["sha256"] != expected_sha):
            raise ValueError(f"Fixed approved cast changed: {slug}")
    references = []
    by_speaker = {}
    for slug, ref in voices.items():
        if ref["speaker"] in by_speaker:
            raise ValueError(f"Ambiguous speaker mapping: {ref['speaker']}")
        path = root / ref["reference_mp3_path"]
        actual_sha = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual_sha != ref["sha256"]:
            raise ValueError(f"Reference MP3 SHA256 mismatch: {slug}")
        by_speaker[ref["speaker"]] = slug
        references.append({"slug": slug, "path": ref["reference_mp3_path"], "sha256": actual_sha, "status": "PASS"})

    lines = [
        {"id": item["dialogue_id"], "speaker": item["speaker"], "text": item["text"], "kind": item["kind"]}
        for beat in design["scenes"]
        for item in beat["dialogue"]
        if item["kind"] in ("ORIGINAL", "NEW")
    ]
    examples = [
        {"id": event["id"] + "-EXAMPLE", "speaker": event["speaker"],
         "text": event.get("example_text", event["cue"]),
         "kind": "OPTIONAL_EXAMPLE", "narrative_duration_counted": False,
         "microphone_enabled_during_playback": False}
        for event in interactions["events"]
    ]
    if len(examples) != 10:
        raise ValueError("Expected ten separately budgeted optional example prompts")
    all_lines = lines + examples
    blocked = sorted({line["speaker"] for line in all_lines if line["speaker"] not in by_speaker})
    if blocked != sorted(design["unapproved_voice_speakers"]):
        raise ValueError("Design voice blockers differ from actual script/example cast")
    for line in all_lines:
        line["reference_slug"] = by_speaker.get(line["speaker"])
        line["status"] = "REFERENCE_READY_AUDIO_NOT_RUN" if line["reference_slug"] else "BLOCKED_RESOURCE"

    return {
        "scene": "S05", "audit_scope": "REFERENCE_FILES_AND_CAST_ASSIGNMENTS_ONLY",
        "reference_integrity": "PASS", "story_dialogue_count": len(lines),
        "optional_example_count": len(examples),
        "story_speaker_counts": dict(Counter(line["speaker"] for line in lines)),
        "optional_example_speaker_counts": dict(Counter(line["speaker"] for line in examples)),
        "blocked_speakers": blocked,
        "full_scene_voice_gate": "BLOCKED_RESOURCE" if blocked else "REFERENCE_READY_AUDIO_NOT_RUN",
        "audio_synthesis": "NOT_RUN", "audio_duration_and_lipsync": "NOT_RUN",
        "references": references, "voice_assignments": all_lines,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", type=Path, help="Optionally write the complete voice assignment audit")
    parser.add_argument("--require-ready", action="store_true", help="Fail the production gate if an approved voice is missing")
    args = parser.parse_args()
    report = audit(ROOT)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("REFERENCE_INTEGRITY_PASS:", len(report["references"]), "approved MP3 hashes verified")
    print("S05 story dialogue:", report["story_dialogue_count"], report["story_speaker_counts"])
    print("S05 optional examples outside narrative:", report["optional_example_count"], report["optional_example_speaker_counts"])
    print("FULL_SCENE_VOICE_GATE:", report["full_scene_voice_gate"], report["blocked_speakers"])
    print("Audio synthesis, measured timing and lipsync: NOT_RUN")
    if report["blocked_speakers"]:
        print("No substitution by another character's approved voice is permitted.")
        if args.require_ready:
            print("Production gate blocked: an approved Cricket voice is required.", file=sys.stderr)
            return 2
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, KeyError, ValueError) as exc:
        print("FAIL:", exc, file=sys.stderr)
        raise SystemExit(1)
