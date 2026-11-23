#!/usr/bin/env python3
"""Check S05 authored data, not engine execution, audio, animation or viewing QA.

The optional mutation checks prove that selected invalid drafts are rejected.
They run on temporary copies and never edit repository evidence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STORY = "docs/series_v2/sources/01_STORY_MASTER_V1_1.md"
BOARD = "docs/series_v2/sources/01_STEP2_PRODUCTION_STORYBOARD_SPEC.md"
DESIGN = "scenes/S05/scene_design_v2.json"
INTERACTIONS = "scenes/S05/interaction_map_v2.json"
SCRIPT = "scenes/S05/script_v2_draft.md"
MANIFEST = "docs/series_v2/series_manifest_v2.json"
LOCKED_SHA256 = {
    STORY: "eb5ca04f5e4302d4a71726f1a24b6cead5cec682b96baee600f6eef8ee951d3e",
    BOARD: "b5ff72a4e6d889006eacc669a7c15c68a739ca1805117b8c79d79d4ab5181610",
}
DEPENDENCIES = [
    STORY, BOARD, DESIGN, INTERACTIONS, SCRIPT, MANIFEST,
    "scenes/S02/scene_design_v2.json", "scenes/S04/scene_design_v2.json",
]
WORDS = re.compile(r"[A-Za-z]+(?:['’][A-Za-z]+)*")
LEGACY = {
    "I08": {
        "cue": "I hear music!", "question": "S05-U004", "resume": "S05-U005",
        "reaction": ["CRICKET_LISTEN", "PINOCCHIO_TURN", "LEAVES_MOVE"],
    },
    "I09": {
        "cue": "Look over there!", "question": "S05-U013", "resume": "S05-U014",
        "reaction": ["CAMERA_PAN", "TENT_REVEAL", "PINOCCHIO_WIDE_EYES"],
    },
}


def read_json(root: Path, path: str):
    return json.loads((root / path).read_text(encoding="utf-8"))


def validate(root: Path = ROOT, emit=print) -> dict:
    def check(condition, label):
        if not condition:
            raise AssertionError(label)
        emit("PASS: " + label)

    for path, expected in LOCKED_SHA256.items():
        check(hashlib.sha256((root / path).read_bytes()).hexdigest() == expected,
              "locked source SHA256: " + path)
    master = (root / STORY).read_text(encoding="utf-8")
    source = master.split("## 장면 5. 어디선가 들려오는 음악", 1)[1].split("## 장면 6.", 1)[0]
    originals = []
    speaker = None
    for line in source.splitlines():
        match = re.fullmatch(r"\*\*(피노키오|귀뚜라미|내레이션)\*\*", line)
        if match:
            speaker = match.group(1)
        if line.startswith('"') and line.endswith('"'):
            originals.append((speaker, line[1:-1]))
    check(len(originals) == 18, "canonical S05 contains 18 spoken lines")

    design = read_json(root, DESIGN)
    interactions = read_json(root, INTERACTIONS)
    for base_name in ("S02", "S04"):
        base = read_json(root, f"scenes/{base_name}/scene_design_v2.json")
        check(set(base).issubset(design), f"{base_name} root field coverage (data only; not an engine test)")
    check(design["scene"] == "S05" and design["base_engine_scene"] == "S02",
          "S05 uses the S02 data contract")
    check(design["base_engine_contract"] == "scenes/S02/scene_design_v2.json" and
          design["base_engine_implementation"] == "NOT_FOUND_IN_GITHUB_BRANCH",
          "runtime engine availability is not overstated")
    check(design["stage"] == "G1_DESIGN_COMPLETE_REVIEW_REQUIRED",
          "screenplay approval is still required")
    check(design["duration_target_seconds"] == 432 and design["target_fps"] == 24 and
          design["wait_excluded"] is True, "432 narrative seconds planned at 24 fps, excluding pauses")
    check(design["previous_scene_continuity"] == "scenes/S04/scene_design_v2.json",
          "S04 predecessor is explicitly referenced")
    check(bool(design["next_scene_continuity"]), "S06 successor reference is present for handoff review")
    check(design["unapproved_voice_speakers"] == ["귀뚜라미"],
          "Cricket remains an unapproved voice resource")

    beats = design["scenes"]
    check([b["id"] for b in beats] == [f"B{i:02}" for i in range(1, 11)], "ten ordered beats B01-B10")
    check(beats[0]["start_seconds"] == 0 and beats[-1]["end_seconds"] == 432 and
          all(a["end_seconds"] == b["start_seconds"] for a, b in zip(beats, beats[1:])),
          "beat timeline covers 0-432 seconds with no gap or overlap")
    shots = []
    for beat in beats:
        ss = beat["shots"]
        check([s["id"] for s in ss] == [f"{beat['id']}-C{i:02}" for i in range(1, 6)],
              beat["id"] + " has five uniquely ordered shots")
        check(ss[0]["start_seconds"] == beat["start_seconds"] and
              ss[-1]["end_seconds"] == beat["end_seconds"] and
              all(a["end_seconds"] == b["start_seconds"] for a, b in zip(ss, ss[1:])),
              beat["id"] + " shot boundaries are contiguous")
        check(all(isinstance(s["start_seconds"], (int, float)) and
                  not isinstance(s["start_seconds"], bool) and
                  isinstance(s["end_seconds"], (int, float)) and
                  not isinstance(s["end_seconds"], bool) and
                  s["end_seconds"] > s["start_seconds"] for s in ss),
              beat["id"] + " has positive shot durations")
        check(all(s.get("type", "") != "WAIT" and s.get("phase", "") != "WAIT" and
                  not re.match(r"^\s*WAIT\b", s["camera"]) for s in ss),
              beat["id"] + " has no timed WAIT shot")
        check(all(isinstance(s["camera"], str) and bool(s["camera"].strip()) and
                  isinstance(s["acting"], str) and bool(s["acting"].strip()) for s in ss),
              beat["id"] + " has authored camera and acting notes for every shot")
        shots.extend(ss)
    check(len(shots) == len({s["id"] for s in shots}) == 50,
          "50 unique shots account for the complete narrative target")

    dialogue = [d for b in beats for d in b["dialogue"]]
    check(all(d["kind"] in {"ORIGINAL", "NEW", "INTERACTION"} for d in dialogue),
          "only defined dialogue kinds are used")
    spoken = [d for d in dialogue if d["kind"] != "INTERACTION"]
    kept = [d for d in spoken if d["kind"] == "ORIGINAL"]
    added = [d for d in spoken if d["kind"] == "NEW"]
    check([(d["speaker"], d["text"]) for d in kept] == originals,
          "all 18 original speakers, words and relative order are preserved")
    check([d["source_index"] for d in kept] == list(range(1, 19)) and
          [d["dialogue_id"] for d in kept] == [f"S05-U{i:03}" for i in range(1, 19)],
          "source indices and original dialogue IDs are complete")
    check([d["new_index"] for d in added] == list(range(1, len(added) + 1)) and
          [d["dialogue_id"] for d in added] == [f"S05-N{i:03}" for i in range(1, len(added) + 1)],
          "added dialogue IDs are unique and ordered")
    check(design["original_dialogue_count"] == 18 and design["new_dialogue_count"] == len(added),
          "dialogue counts match authored data")
    check({d["speaker"] for d in spoken} <= {"피노키오", "귀뚜라미", "내레이션"},
          "Mara and Pip's spoken introductions remain in S06")
    check(spoken[0]["dialogue_id"] == "S05-U001" and spoken[-1]["dialogue_id"] == "S05-U018",
          "S05 starts and ends with its canonical boundary lines")
    by_line = {d["dialogue_id"]: d for d in spoken}
    check(len(by_line) == len(spoken), "every spoken line has a unique dialogue ID")
    assigned = [identifier for shot in shots for identifier in shot["dialogue_ids"]]
    check(assigned == [d["dialogue_id"] for d in spoken],
          "every line appears exactly once in chronological shot order")
    densities = []
    for shot in shots:
        count = sum(len(WORDS.findall(by_line[i]["text"])) for i in shot["dialogue_ids"])
        density = 60 * count / (shot["end_seconds"] - shot["start_seconds"])
        densities.append(density)
        if density > 165:
            raise AssertionError(f"authored speech-density estimate exceeds 165 wpm: {shot['id']} ({density:.1f})")
    emit(f"PASS: authored speech-density ceiling <=165 wpm; maximum={max(densities):.1f} (not audio measurement)")

    markers = [d["id"] for d in dialogue if d["kind"] == "INTERACTION"]
    expected_set = {"I08", "I09"} | {f"S05-P{i:02}" for i in range(1, 9)}
    check(len(markers) == len(set(markers)) == 10 and set(markers) == expected_set and
          markers.index("I08") < markers.index("I09"), "ten unique events: I08/I09 and eight new local IDs")
    check(interactions["scene"] == "S05" and interactions["count"] == 10 and
          interactions["legacy_count"] == 2 and interactions["new_count"] == 8 and
          interactions["legacy_ids"] == ["I08", "I09"] and
          interactions["wait_excluded"] is True and interactions["status"] == "REVIEW_REQUIRED",
          "interaction totals and review/pause statuses match the brief")
    events = interactions["events"]
    check([e["id"] for e in events] == markers and [b["interaction_id"] for b in beats] == markers,
          "script, beat and interaction-map event order agree")
    check([e["index"] for e in events] == list(range(1, 11)) and
          all(e["kind"] == ("LEGACY_LOCKED" if e["id"] in LEGACY else "NEW") for e in events),
          "event indices and legacy/new classifications match their IDs")
    rules = interactions["rules"]
    check(all(rules[k] is True for k in ["question_audio_must_end_before_listen", "react_once",
          "parent_tap_alternative", "sample_speech_while_microphone_disabled", "replay_does_not_increment_participation"]) and
          rules["word_recognition"] is False and rules["pronunciation_scoring"] is False and
          rules["model_example_after_no_response_seconds"] == 5,
          "accessible VAD/touch contract; no STT or scores; no duplicate participation")
    for beat, event in zip(beats, events):
        event_id = event["id"]
        ss = beat["shots"]
        check(event["beat"] == beat["id"] and len(WORDS.findall(event["cue"])) == 3,
              event_id + " has one beat and a three-word cue")
        check(event["wait_time_counted"] is False and event["react_once"] is True and
              event["scoring"] is False and
              event["trigger"] == "QUESTION_AUDIO_ENDED_THEN_VAD_OR_PARENT_TAP",
              event_id + " is an external pause, triggered after audio and reacted to once")
        qid, rid = event["question_dialogue_id"], event["resume_dialogue_id"]
        check(event["prompt"] == by_line[qid]["text"] and event["speaker"] == by_line[qid]["speaker"],
              event_id + " prompt/speaker matches its actual dialogue")
        check(event["question_end_boundary_seconds"] == ss[2]["end_seconds"] == ss[3]["start_seconds"] and
              ss[2]["dialogue_ids"][-1] == qid and ss[3]["dialogue_ids"][0] == rid and
              event["react_shot_id"] == ss[3]["id"] and
              event["demo_shot_id"] in {s["id"] for s in ss[:3]},
              event_id + " question/demo -> pause boundary -> react/resume is explicit")
        marker_positions = [i for i, d in enumerate(beat["dialogue"]) if d["kind"] == "INTERACTION"]
        check(len(marker_positions) == 1, event_id + " has exactly one local script marker")
        idx = marker_positions[0]
        check(idx > 0 and idx + 1 < len(beat["dialogue"]) and
              beat["dialogue"][idx - 1].get("dialogue_id") == qid and
              beat["dialogue"][idx + 1].get("dialogue_id") == rid,
              event_id + " prompt and resume are immediately adjacent to its marker")
        if event_id in LEGACY:
            locked = LEGACY[event_id]
            check(event["cue"] == locked["cue"] and qid == locked["question"] and rid == locked["resume"] and
                  event["reaction_order"] == locked["reaction"],
                  event_id + " original cue, question, resume and reaction sequence remain locked")

    script = (root / SCRIPT).read_text(encoding="utf-8")
    check(all(d["text"] in script and d["dialogue_id"] in script for d in spoken) and
          all(s["id"] in script for s in shots), "readable screenplay includes all dialogue and all 50 shot IDs")
    manifest = read_json(root, MANIFEST)
    entry = next(s for s in manifest["scenes"] if s["id"] == "S05")
    check(entry["progress"] == "DESIGN_COMPLETE_REVIEW_REQUIRED" and entry["expanded_script_approved"] is False and
          entry["design_runtime_target_seconds"] == 432 and entry["design_shot_count"] == 50 and
          entry["design_original_dialogue_count"] == 18 and entry["design_new_dialogue_count"] == len(added) and
          entry["design_interactions"] == 10,
          "S05 manifest matches the review-required draft")
    emit("DESIGN_DATA_PASS: structural checks only. Render/audio/device QA NOT_RUN; screenplay REVIEW_REQUIRED; Cricket voice BLOCKED_RESOURCE.")
    return {"seconds_planned": 432, "shots": 50, "original_lines": 18, "new_lines": len(added),
            "interactions": 10, "max_estimated_speech_wpm": round(max(densities), 1)}


def mutation_checks(root: Path = ROOT, emit=print) -> None:
    with tempfile.TemporaryDirectory(prefix="s05-validator-") as directory:
        copied = Path(directory)
        for name in DEPENDENCIES:
            target = copied / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(root / name, target)
        baseline_design = (copied / DESIGN).read_text(encoding="utf-8")
        baseline_map = (copied / INTERACTIONS).read_text(encoding="utf-8")
        validate(copied, emit=lambda *_: None)

        def reject(label, path, mutate):
            (copied / DESIGN).write_text(baseline_design, encoding="utf-8")
            (copied / INTERACTIONS).write_text(baseline_map, encoding="utf-8")
            value = read_json(copied, path)
            mutate(value)
            (copied / path).write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")
            try:
                validate(copied, emit=lambda *_: None)
            except AssertionError as exc:
                emit(f"NEGATIVE_CHECK_PASS: {label} rejected ({exc})")
            else:
                raise AssertionError("mutation was not rejected: " + label)

        def remove_original(draft):
            for beat in draft["scenes"]:
                for index, line in enumerate(beat["dialogue"]):
                    if line["kind"] == "ORIGINAL":
                        del beat["dialogue"][index]
                        return

        reject("missing original line", DESIGN, remove_original)
        reject("shot gap", DESIGN,
               lambda d: d["scenes"][0]["shots"][1].__setitem__("start_seconds", d["scenes"][0]["shots"][1]["start_seconds"] + 1))
        reject("pause before/after wrong boundary", INTERACTIONS,
               lambda m: m["events"][0].__setitem__("question_end_boundary_seconds", m["events"][0]["question_end_boundary_seconds"] + 1))
        reject("duplicate interaction", INTERACTIONS,
               lambda m: m["events"][1].__setitem__("id", m["events"][0]["id"]))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true", help="also reject four deliberately broken temporary drafts")
    args = parser.parse_args()
    validate()
    if args.self_test:
        mutation_checks()


if __name__ == "__main__":
    try:
        main()
    except (AssertionError, ValueError, KeyError, TypeError, OSError, IndexError, StopIteration) as exc:
        print("FAIL:", exc, file=sys.stderr)
        sys.exit(1)
