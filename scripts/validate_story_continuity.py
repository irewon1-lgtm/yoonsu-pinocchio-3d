#!/usr/bin/env python3
"""Validate the S01-S12 continuity contract's data and S05 boundary references.

This does not judge natural storytelling or verify rendered match cuts/audio.
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
CONTRACT = "docs/series_v2/STORY_CONTINUITY_S01_S12.json"
DOCUMENT = "docs/series_v2/STORY_CONTINUITY_S01_S12.md"
STORY = "docs/series_v2/sources/01_STORY_MASTER_V1_1.md"
BOARD = "docs/series_v2/sources/01_STEP2_PRODUCTION_STORYBOARD_SPEC.md"
MANIFEST = "docs/series_v2/series_manifest_v2.json"
LOCKED_SHA256 = {
    STORY: "eb5ca04f5e4302d4a71726f1a24b6cead5cec682b96baee600f6eef8ee951d3e",
    BOARD: "b5ff72a4e6d889006eacc669a7c15c68a739ca1805117b8c79d79d4ab5181610",
}
DEPENDENCIES = [
    CONTRACT, DOCUMENT, STORY, BOARD, MANIFEST,
    "scenes/S04/scene_design_v2.json", "scenes/S05/scene_design_v2.json",
    "scenes/S05/interaction_map_v2.json",
]


def read_json(root: Path, path: str):
    return json.loads((root / path).read_text(encoding="utf-8"))


def populated(value):
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, list):
        return bool(value) and all(populated(v) for v in value)
    if isinstance(value, dict):
        return bool(value) and all(populated(v) for v in value.values())
    return value is not None


def source_dialogue(master: str, number: int):
    start = re.search(rf"(?m)^## 장면 {number}\. [^\n]+\n", master)
    if start is None:
        raise AssertionError(f"missing source scene {number}")
    section = master[start.end():]
    section = re.split(r"(?m)^## 장면 \d+\. ", section, maxsplit=1)[0]
    return [line[1:-1] for line in section.splitlines() if line.startswith('"') and line.endswith('"')]


def validate(root: Path = ROOT, emit=print) -> dict:
    def check(condition, label):
        if not condition:
            raise AssertionError(label)
        emit("PASS: " + label)

    contract = read_json(root, CONTRACT)
    check(contract["status"] == "REVIEW_REQUIRED" and contract["semantic_review"] == "DESIGN_REVIEW" and
          contract["rendered_continuity"] == "NOT_RUN",
          "design review and unperformed rendered continuity remain distinct")
    sources = contract["sources"]
    check(len(sources) == 2 and {s["path"]: s["sha256"] for s in sources} == LOCKED_SHA256,
          "both original source hashes are explicitly locked")
    for path, expected in LOCKED_SHA256.items():
        check(hashlib.sha256((root / path).read_bytes()).hexdigest() == expected,
              "source bytes match continuity reference: " + path)
    master = (root / STORY).read_text(encoding="utf-8")
    source_titles = re.findall(r"(?m)^## 장면 (\d+)\. ([^\n]+)", master)
    expected_scenes = [f"S{i:02}" for i in range(1, 13)]
    scenes = contract["scenes"]
    manifest = read_json(root, MANIFEST)
    check([s["scene"] for s in scenes] == expected_scenes and
          [s["id"] for s in manifest["scenes"]] == expected_scenes,
          "all twelve scenes occur once in canonical order")
    check([(str(i), s["title"]) for i, s in enumerate(scenes, 1)] == source_titles and
          [s["title"] for s in scenes] == [s["title"] for s in manifest["scenes"]],
          "scene titles agree with the immutable source and manifest")
    state_keys = {"location", "story_time", "characters", "pinocchio_form", "nose_state", "props",
                  "emotion", "objective", "knowledge"}
    for index, scene in enumerate(scenes, 1):
        check(scene["source_heading"] == f"## 장면 {index}. {scene['title']}" and
              populated(scene["story_day"]) and populated(scene["causal_role"]),
              scene["scene"] + " has its source heading, day and causal role")
        for direction in ("entry_state", "exit_state"):
            state = scene[direction]
            check(state_keys.issubset(state) and all(populated(state[k]) for k in state_keys) and
                  isinstance(state["characters"], list) and isinstance(state["props"], list),
                  scene["scene"] + " " + direction + " describes location, character, prop and intention state")
    check(all(s["story_day"] == "D1" for s in scenes[1:10]) and
          scenes[10]["story_day"] == scenes[11]["story_day"] == "D2",
          "first school day and the following morning remain distinct")
    check(all(s["entry_state"]["pinocchio_form"] == "WOODEN" for s in scenes[1:]) and
          all(s["exit_state"]["pinocchio_form"] == "WOODEN" for s in scenes[:-1]) and
          scenes[-1]["exit_state"]["pinocchio_form"] == "CHAR_YOONSU_HUMAN",
          "human appearance is reserved for the final S12 exit state")

    transitions = contract["transitions"]
    expected_edges = [(a, b) for a, b in zip(expected_scenes, expected_scenes[1:])]
    check(contract["coverage"] == {"scenes": 12, "transitions": 11} and len(transitions) == 11 and
          [(t["from"], t["to"]) for t in transitions] == expected_edges and
          [t["id"] for t in transitions] == [f"{a}_{b}" for a, b in expected_edges],
          "eleven unique consecutive transitions connect S01 through S12 without an orphan")
    for transition in transitions:
        check(all(populated(transition[k]) for k in ("cause", "carry", "time_change", "visual_bridge", "audio_bridge", "avoid")) and
              isinstance(transition["carry"], list) and isinstance(transition["avoid"], list),
              transition["id"] + " records causal, state, time, visual and audio handoff requirements")
    for left, right in zip(scenes, scenes[1:]):
        check(left["exit_state"]["pinocchio_form"] == right["entry_state"]["pinocchio_form"] and
              left["exit_state"]["nose_state"] == right["entry_state"]["nose_state"],
              left["scene"] + " -> " + right["scene"] + " preserves body and nose state at the boundary")

    motifs = contract["motifs"]
    check(len(motifs) > 0 and len({m["id"] for m in motifs}) == len(motifs),
          "causal motifs have unique IDs")
    for motif in motifs:
        check(motif["introduced_in"] in expected_scenes and populated(motif["rule"]) and
              isinstance(motif["payoff_in"], list) and bool(motif["payoff_in"]) and
              all(s in expected_scenes and expected_scenes.index(s) >= expected_scenes.index(motif["introduced_in"])
                  for s in motif["payoff_in"]),
              motif["id"] + " refers to existing later scenes")

    local = contract["local_handoffs"]
    check(set(local) == {"S04_S05", "S05_S06"}, "both immediate S05 handoffs have explicit contracts")
    for key, source_number, target_number in [("S04_S05", 4, 5), ("S05_S06", 5, 6)]:
        handoff = local[key]
        check(handoff["from_scene"] == f"S{source_number:02}" and handoff["to_scene"] == f"S{target_number:02}" and
              handoff["source_exit_line"] == source_dialogue(master, source_number)[-1] and
              handoff["source_entry_line"] == source_dialogue(master, target_number)[0],
              key + " preserves the exact canonical exit/entry spoken lines")
        check(handoff["review_status"] == "REVIEW_REQUIRED" and handoff["rendered_match"] == "NOT_RUN" and
              populated(handoff["state_lock"]) and populated(handoff["audio"]),
              key + " is a populated review contract, not a rendered match claim")
    before, after = local["S04_S05"], local["S05_S06"]
    check(before["from_shot"] == "B10-C05" and before["to_shot"] == "B01-C01" and
          after["from_shot"] == "B10-C05" and after["to_source_shot"] == "S06-C01",
          "boundary shot references point to the authored S04/S05 and canonical S06")
    entry_lock, exit_lock = before["state_lock"], after["state_lock"]
    check(all(lock.get("schoolbook_currently_open") is False and
              lock.get("schoolbook_viewed_with_geppetto_in_S03") is True and
              lock.get("schoolbook_opened_since_packed") is False and
              lock.get("schoolbook_used_in_class") is False and
              "schoolbook_opened" not in lock for lock in (entry_lock, exit_lock)),
          "book's current closed state is distinct from S03 viewing and later nonuse")
    visible = exit_lock.get("unnamed_puppets", {})
    check(visible.get("count") == 2 and visible.get("location") == "STAGE_FRONT_RIGHT_VISIBLE_WAITING_AREA" and
          visible.get("visible_through") == "S06-U003" and visible.get("pip_included") is False and visible.get("speaking") is False,
          "S06 first puppet observation has two visible unnamed targets without opening the curtain or introducing Pip")
    check(entry_lock["shoes"] == "DRY" and entry_lock["puppet_show_revealed"] is False and
          exit_lock["main_curtain"] == "CLOSED" and exit_lock["pip_introduced"] is False and
          exit_lock["puppet_rescued"] is False and exit_lock["school_missed"] is False and
          exit_lock["promise"] == "KNOWN_BUT_POSTPONED",
          "S05 retains dry shoes, delays the reveal and leaves S06 curtain/Pip/consequence events pending")
    check(all(entry_lock[k] == exit_lock[k] == expected for k, expected in {
        "story_day": "D1", "pinocchio_form": "WOODEN", "nose": "NORMAL",
        "red_hat": "WORN", "schoolbag": "CLOSED_WITH_SCHOOLBOOK",
    }.items()), "S05's two boundary contracts preserve day, body, nose, hat and schoolbook")

    previous = read_json(root, "scenes/S04/scene_design_v2.json")
    design = read_json(root, "scenes/S05/scene_design_v2.json")
    previous_spoken = [d for b in previous["scenes"] for d in b["dialogue"] if d["kind"] != "INTERACTION"]
    spoken = [d for b in design["scenes"] for d in b["dialogue"] if d["kind"] != "INTERACTION"]
    check(previous["scenes"][-1]["shots"][-1]["id"] == before["from_shot"] and
          previous_spoken[-1]["text"] == before["source_exit_line"] and
          design["scenes"][0]["shots"][0]["id"] == before["to_shot"] and
          spoken[0]["text"] == before["source_entry_line"] and
          design["scenes"][-1]["shots"][-1]["id"] == after["from_shot"] and
          spoken[-1]["text"] == after["source_exit_line"],
          "authored S04/S05 endpoints match the continuity contract")
    check(design["scenes"][0]["shots"][0]["dialogue_ids"][0] == "S05-U001" and
          design["scenes"][-1]["shots"][-1]["dialogue_ids"][-1] == "S05-U018",
          "S05 canonical entry/exit lines are assigned to the actual boundary shots")
    interaction_map = read_json(root, "scenes/S05/interaction_map_v2.json")
    events = {e["id"]: e for e in interaction_map["events"]}
    gates = before["legacy_event_gates"]
    check([g["id"] for g in gates] == ["I08", "I09"], "music and stage discovery each have a distinct legacy gate")
    for gate in gates:
        event = events[gate["id"]]
        check(gate["question_dialogue_id"] == event["question_dialogue_id"] and
              gate["resume_dialogue_id"] == event["resume_dialogue_id"] and populated(gate["reveals"]),
              gate["id"] + " continuity gate matches the authored interaction")

    document = (root / DOCUMENT).read_text(encoding="utf-8")
    check(all(scene in document for scene in expected_scenes) and
          all(t["id"] in document for t in transitions),
          "readable continuity document covers all twelve scenes and eleven boundary IDs")
    check(manifest["scenes"][0]["progress"] == "FROZEN_EXEMPT_NO_REWORK" and
          manifest["status"] == "SPEC_READY_NOT_PRODUCTION_COMPLETE",
          "S01 preservation and unfinished production status remain explicit")
    emit("CONTINUITY_DATA_PASS: 12 scenes / 11 links / S04-S05-S06 references. Naturalness REVIEW_REQUIRED; rendered continuity and audio NOT_RUN.")
    return {"scenes": 12, "transitions": 11, "local_handoffs": 2}


def mutation_checks(root: Path = ROOT, emit=print) -> None:
    with tempfile.TemporaryDirectory(prefix="continuity-validator-") as directory:
        copied = Path(directory)
        for name in DEPENDENCIES:
            target = copied / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(root / name, target)
        baseline = (copied / CONTRACT).read_text(encoding="utf-8")
        validate(copied, emit=lambda *_: None)

        def reject(label, mutate):
            value = json.loads(baseline)
            mutate(value)
            (copied / CONTRACT).write_text(json.dumps(value, ensure_ascii=False), encoding="utf-8")
            try:
                validate(copied, emit=lambda *_: None)
            except AssertionError as exc:
                emit(f"NEGATIVE_CHECK_PASS: {label} rejected ({exc})")
            else:
                raise AssertionError("mutation was not rejected: " + label)

        reject("missing S05-S06 link", lambda c: c["transitions"].pop(4))
        reject("reordered transition", lambda c: c["transitions"][4].__setitem__("to", "S07"))
        reject("premature curtain opening", lambda c: c["local_handoffs"]["S05_S06"]["state_lock"].__setitem__("main_curtain", "OPEN"))
        reject("wrong canonical entry line", lambda c: c["local_handoffs"]["S04_S05"].__setitem__("source_entry_line", "Welcome again!"))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true", help="also reject four broken contracts in temporary copies")
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
