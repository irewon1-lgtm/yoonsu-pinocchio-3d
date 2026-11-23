#!/usr/bin/env python3
"""Validate locked V1.1 sources and approved series V2 targets, not actual video."""
from __future__ import annotations
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
V2 = ROOT / "docs" / "series_v2"

def ok(value: bool, label: str) -> None:
    if not value:
        raise AssertionError(label)
    print("PASS:", label)

def main() -> None:
    m = json.loads((V2 / "series_manifest_v2.json").read_text(encoding="utf-8"))
    ok(m["version"] == "2.0", "manifest version 2.0")
    src = m["canonical_sources"]
    for key in ("story_master", "storyboard"):
        p = ROOT / src[key]["path"]
        ok(p.is_file(), key + " source exists")
        ok(src[key]["status"] == "LOCKED_ORIGINAL", key + " immutable")
        ok(hashlib.sha256(p.read_bytes()).hexdigest() == src[key]["sha256"], key + " original SHA256")
    story = (ROOT / src["story_master"]["path"]).read_text(encoding="utf-8")
    board = (ROOT / src["storyboard"]["path"]).read_text(encoding="utf-8")
    titles = re.findall(r"^## 장면 (\d+)\. (.+)", story, flags=re.M)
    ok([int(i) for i, _ in titles] == list(range(1, 13)), "V1.1 12 scene titles")
    ok(len(re.findall(r"^### 🎤 윤수 참여 \d+", story, flags=re.M)) == 21, "original 21 voice events")
    ok(len(re.findall(r"^### S\d{2} —", board, flags=re.M)) == 12, "storyboard 12 sections")
    scenes = m["scenes"]
    ok([s["id"] for s in scenes] == ["S%02d" % x for x in range(1, 13)], "scene ordering S01-S12")
    ok(all(s["title"] == titles[n][1] for n, s in enumerate(scenes)), "original scene names unchanged")
    ok(sum(s["baseline_cuts"] for s in scenes) == 138 == m["baseline"]["cuts"], "138 original storyboard cuts")
    ids = [x for s in scenes for x in s["legacy_ids"]]
    ok(ids == ["I%02d" % x for x in range(1, 22)], "all 21 legacy IDs retained once")
    s01 = scenes[0]
    ok(s01["progress"] == "FROZEN_EXEMPT_NO_REWORK" and s01["min_narrative_seconds"] is None and s01["target_interactions"] is None, "S01 exempt and frozen")
    rest = scenes[1:]
    ok(len(rest) == 11 and all(s["target_interactions"] == 10 for s in rest), "S02-S12 exactly 10 target events each")
    ok(all(s["min_narrative_seconds"] >= 360 for s in rest), "S02-S12 each 360+ narrative seconds")
    ok(sum(s["target_interactions"] for s in rest) == 110, "110 target interactions")
    ok(sum(len(s["legacy_ids"]) for s in rest) == 20, "20 original events included in 110")
    ok(m["policy"]["planned_new_interactions_s02_s12"] == 90, "90 net new interactions")
    ok(m["next_scene"] == "S03" and m["status"] == "SPEC_READY_NOT_PRODUCTION_COMPLETE", "current S03-S05 revision not falsely marked rendered")
    ok(m.get("accepted_completed_scenes") == ["S01", "S02"] and m.get("current_revision_scope") == ["S03", "S04", "S05"], "user-completed S01/S02 excluded from current revision")
    print("PASS: source/policy integrity only; user-completed S01/S02 preserved, revised S03-S05 audio/video NOT_RUN.")

if __name__ == "__main__":
    try:
        main()
    except (AssertionError, ValueError, KeyError, OSError) as e:
        print("FAIL:", e, file=sys.stderr)
        sys.exit(1)
