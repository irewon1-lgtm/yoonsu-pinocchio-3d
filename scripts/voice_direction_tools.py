#!/usr/bin/env python3
"""Build and verify directed S03-S05 scripts/jobs. No TTS or audio approval.

Each job separates exact spoken text from actor instructions and locked voice
identity. Numerical duration is a planning budget, never a WAV measurement.
"""
from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import json
import math
from pathlib import Path
import re
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
BIBLE = "docs/series_v2/VOICE_PERFORMANCE_BIBLE_V2_1.json"
REGISTRY = "assets/voice_refs/v6/VOICE_REFERENCES.json"
MASTER = "docs/series_v2/sources/01_STORY_MASTER_V1_1.md"
BOARD = "docs/series_v2/sources/01_STEP2_PRODUCTION_STORYBOARD_SPEC.md"
LOCKED = {
    MASTER: "eb5ca04f5e4302d4a71726f1a24b6cead5cec682b96baee600f6eef8ee951d3e",
    BOARD: "b5ff72a4e6d889006eacc669a7c15c68a739ca1805117b8c79d79d4ab5181610",
}
CAST = {
    "피노키오": "PINOCCHIO_A", "제페토": "GEPPETTO_A",
    "내레이션": "NARRATOR_A", "파란 요정": "BLUE_FAIRY_C",
    "귀뚜라미": "CRICKET_DESIGN_V1", "마라": "MARA_DESIGN_V1", "핍": "PIP_DESIGN_V1",
}
COUNTS = {"S03": (22, 92), "S04": (32, 77), "S05": (18, 69)}
LEGACY = {"S03": ["I03", "I04"], "S04": ["I05", "I06", "I07"], "S05": ["I08", "I09"]}
FIXED_REFS = {
    "narrator": ("A", "ec7234237b687246af302db312994c6b9ddc46411c82085a5b1f3884bcfcbddf"),
    "pinocchio": ("A", "a32569705a717ac92c8ecbe1c515b9e31e389f508164458ed22a06adcbba0b3d"),
    "geppetto": ("A", "80237e647e1e480987a3cf0a6ac1dc33a3d6b3a40dc62d577f4a0290e338af55"),
    "blue_fairy": ("C", "c65e44b9c4d221c1fe9052ff201a3d3a0f5bc867c29460130fe2944f59c5965b"),
}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(root, name):
    return json.loads((Path(root) / name).read_text(encoding="utf-8"))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dump(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def words(text):
    return re.findall(r"[A-Za-z]+(?:['’][A-Za-z]+)*", text)


def planned_voice_seconds(text, direction):
    pauses = direction["pause_before_ms"] + direction["pause_after_ms"]
    pauses += sum(item["ms"] for item in direction["internal_pauses"])
    return len(words(text)) * 60 / direction["pace_wpm"] + pauses / 1000


def shot_budget(shot, by_id):
    spoken = sum(planned_voice_seconds(by_id[k]["text"], by_id[k]["voice_direction"])
                 for k in shot["dialogue_ids"])
    return (spoken + shot["action_lead_seconds"] + shot["action_tail_seconds"]
            + sum(a["seconds"] for a in shot.get("between_dialogue_actions", [])))


def canonical(root, scene):
    text = (Path(root) / MASTER).read_text(encoding="utf-8")
    number = int(scene[1:])
    start = re.search(rf"(?m)^## 장면 {number}\. [^\n]+\n", text)
    require(start is not None, "Canonical scene missing: " + scene)
    block = re.split(r"(?m)^## 장면 \d+\. ", text[start.end():], maxsplit=1)[0]
    who, lines = None, []
    for line in block.splitlines():
        match = re.fullmatch(r"\*\*([^*]+)\*\*", line)
        if match:
            who = match.group(1)
        if line.startswith('"') and line.endswith('"'):
            lines.append((who, line[1:-1]))
    return lines


def validate_bible(root):
    bible = read_json(root, BIBLE)
    registry = read_json(root, REGISTRY)["voices"]
    require(set(bible["profiles"]) == set(CAST.values()), "All seven cast profiles required")
    for profile_id, profile in bible["profiles"].items():
        require(CAST[profile["speaker"]] == profile_id, "Profile/speaker mismatch")
        require(len(profile["default_direction_en"]) >= 80, "Missing actor identity direction")
        slug = profile["reference_slug"]
        if slug:
            candidate, expected = FIXED_REFS[slug]
            ref = registry[slug]
            require(ref["approved_candidate"] == candidate and ref["sha256"] == expected,
                    "Approved reference identity changed: " + slug)
            require(profile["reference"] == ref, "Bible reference differs from registry: " + slug)
            require(sha(Path(root) / ref["reference_mp3_path"]) == expected,
                    "Approved voice MP3 bytes changed: " + slug)
        else:
            require(profile["production_voice_status"] == "BLOCKED_RESOURCE" and
                    profile["reference"] is None, "Pending actor must not borrow another voice")
    for path, expected in LOCKED.items():
        require(sha(Path(root) / path) == expected, "Immutable source changed: " + path)
    return bible


def validate_direction(direction, speaker, text, label):
    keys = {"profile_id", "listener", "intention", "emotion", "delivery_ko", "direction_en",
            "pace_wpm", "energy", "emphasis", "pause_before_ms", "pause_after_ms",
            "internal_pauses", "avoid", "timing_basis"}
    require(isinstance(direction, dict) and keys <= set(direction), label + " missing voice direction")
    require(direction["profile_id"] == CAST[speaker], label + " wrong character profile")
    for field in ("listener", "intention", "emotion", "delivery_ko", "direction_en"):
        require(isinstance(direction[field], str) and direction[field].strip(), label + " empty " + field)
    require(len(direction["delivery_ko"]) >= 18 and len(direction["direction_en"]) >= 35,
            label + " direction is only a generic label")
    require(65 <= direction["pace_wpm"] <= 140, label + " implausible planning pace")
    require(1 <= direction["energy"] <= 5, label + " energy must be 1..5")
    require(direction["timing_basis"] == "PLANNED_NOT_MEASURED", label + " false audio measurement")
    for key in ("pause_before_ms", "pause_after_ms"):
        require(isinstance(direction[key], (int, float)) and 0 <= direction[key] <= 1800,
                label + " invalid pause")
    require(isinstance(direction["emphasis"], list), label + " invalid emphasis list")
    for word in direction["emphasis"]:
        require(isinstance(word, str) and word and word in text, label + " emphasis absent from text: " + str(word))
    for pause in direction["internal_pauses"]:
        require(pause["after"] in text and 0 <= pause["ms"] <= 1200,
                label + " internal pause is not anchored to exact text")
    require(isinstance(direction["avoid"], list) and direction["avoid"], label + " missing avoidance direction")


def source_data(root, scene):
    return (read_json(root, f"scenes/{scene}/scene_design_v2.json"),
            read_json(root, f"scenes/{scene}/interaction_map_v2.json"))


def validate_scene(root, scene, emit=print, check_generated=True):
    require(scene in COUNTS, "Only the authorized S03-S05 revision is in scope")
    bible = validate_bible(root)
    design, imap = source_data(root, scene)
    beats = design["scenes"]
    require(design["scene"] == scene and design["base_engine_scene"] == "S02", "S02 contract lost")
    base = read_json(root, "scenes/S02/scene_design_v2.json")
    require(set(base) <= set(design), "S02 top-level data contract missing")
    require(design["stage"] == "G1_DESIGN_COMPLETE_REVIEW_REQUIRED", "No production or voice approval may be inferred")
    require(len(beats) == 10 and [b["id"] for b in beats] == [f"B{i:02}" for i in range(1, 11)], "10 ordered beats")
    full = [line for beat in beats for line in beat["dialogue"]]
    spoken = [line for line in full if line["kind"] in ("ORIGINAL", "NEW")]
    originals = [line for line in spoken if line["kind"] == "ORIGINAL"]
    require([(x["speaker"], x["text"]) for x in originals] == canonical(root, scene), "Canonical speech changed")
    original_count, new_count = COUNTS[scene]
    require(len(originals) == original_count and len(spoken) == original_count + new_count,
            "Reviewed spoken-line count changed")
    require(design["original_dialogue_count"] == original_count and design["new_dialogue_count"] == new_count,
            "Spoken-count metadata differs")
    require([x["source_index"] for x in originals] == list(range(1, original_count + 1)), "Original source indices changed")
    ids = [x["dialogue_id"] for x in spoken]
    require(len(ids) == len(set(ids)), "Duplicate speech ID")
    by_id = {x["dialogue_id"]: x for x in spoken}
    for line in spoken:
        validate_direction(line.get("voice_direction"), line["speaker"], line["text"], line["dialogue_id"])
        expected_prefix = scene + ("-U" if line["kind"] == "ORIGINAL" else "-N")
        require(line["dialogue_id"].startswith(expected_prefix), "Unstable speech ID")
    require(len({x["voice_direction"]["direction_en"] for x in spoken}) >= len(spoken) * .9,
            "Per-line actor instructions are mostly repeated")
    shots = [s for b in beats for s in b["shots"]]
    require(len(shots) == 50 and len({s["id"] for s in shots}) == 50, "50 unique shots required")
    require([k for s in shots for k in s["dialogue_ids"]] == ids, "Every spoken line must map once, in order, to a shot")
    require(beats[0]["start_seconds"] == 0, "Narrative must start at zero")
    previous_end = 0
    max_budget_ratio = 0
    for beat in beats:
        require(beat["start_seconds"] == previous_end and len(beat["shots"]) == 5, "Beat gap or wrong shot count")
        end = beat["start_seconds"]
        for shot in beat["shots"]:
            require(shot["start_seconds"] == end and shot["end_seconds"] > end, "Shot gap/overlap/nonpositive duration")
            require(shot["phase"] in {"NARRATIVE", "PROMPT", "REACT"}, "Pure WAIT must be outside narrative clock")
            require(shot.get("type") != "WAIT" and "WAIT" not in shot["camera"], "WAIT-only camera shot counted as narrative")
            require(shot["action_lead_seconds"] >= 0 and shot["action_tail_seconds"] >= 0, "Invalid action timing")
            budget = shot_budget(shot, by_id)
            duration = shot["end_seconds"] - shot["start_seconds"]
            require(budget <= duration + .001, f"Speech/action budget exceeds {scene}/{shot['id']}: {budget:.2f}>{duration}")
            max_budget_ratio = max(max_budget_ratio, budget / duration)
            end = shot["end_seconds"]
        require(end == beat["end_seconds"], "Beat/shot endpoint mismatch")
        previous_end = end
    total = design["duration_target_seconds"]
    require(total == previous_end and total >= 360 and design["wait_excluded"] is True, "Narrative duration accounting")
    timing = design["timing_contract"]
    require(timing["clock"] == "NARRATIVE_CLOCK_PLUS_EXTERNAL_PAUSES" and
            timing["narrative_seconds"] == total and timing["external_wait_seconds_counted"] == 0,
            "Separate narrative and input clocks required")
    require(timing["actual_audio_timing"] == timing["actual_mp4_duration"] == "NOT_RUN", "No audio/video measurement was made")
    events = imap["events"]
    markers = [x["id"] for x in full if x["kind"] == "INTERACTION"]
    require(imap["count"] == len(events) == 10 and [e["id"] for e in events] == markers, "Event order/count differs")
    require(imap["legacy_ids"] == LEGACY[scene], "Legacy events changed")
    rules = imap["rules"]
    require(rules["word_recognition"] is False and rules["pronunciation_scoring"] is False and rules["react_once"] is True,
            "Child must not require exact recognized words")
    for key in ("first_model_before_listen", "model_example_must_finish_before_rearming_vad",
                "wait_uses_separate_clock", "background_audio_must_not_trigger_vad",
                "parent_tap_can_finish_every_event", "early_input_during_question_is_ignored"):
        require(rules.get(key) is True, "Missing beginner/input rule " + key)
    require(rules["model_example_policy"] == "PLAY_ONCE_BEFORE_FIRST_INPUT_EACH_EVENT", "First model not guaranteed")
    shot_map = {s["id"]: s for s in shots}
    for index, (beat, event) in enumerate(zip(beats, events), 1):
        require(event["index"] == index and event["beat"] == beat["id"] and beat["interaction_id"] == event["id"], "Event/beat mismatch")
        seq = beat["dialogue"]
        pos = next(i for i, x in enumerate(seq) if x["kind"] == "INTERACTION")
        before, after = seq[pos - 1], seq[pos + 1]
        require((event["speaker"], event["prompt"], event["question_dialogue_id"]) ==
                (before["speaker"], before["text"], before["dialogue_id"]), "Prompt not immediately before marker")
        require((event["resume"], event["resume_dialogue_id"]) == (after["text"], after["dialogue_id"]), "Resume not immediately after marker")
        prompt_shot, react_shot = beat["shots"][2:4]
        require(prompt_shot["phase"] == "PROMPT" and react_shot["phase"] == "REACT", "Prompt/reaction cut boundary missing")
        require(prompt_shot["dialogue_ids"][-1] == before["dialogue_id"] and
                react_shot["dialogue_ids"][0] == after["dialogue_id"], "Prompt/resume cut anchors differ")
        require(prompt_shot["external_pause_after_event"] == event["id"] and
                prompt_shot["end_seconds"] == event["question_end_boundary_seconds"] == react_shot["start_seconds"],
                "Input pause is not at exact question-end narrative boundary")
        require(event["react_shot_id"] == react_shot["id"], "Wrong reaction cut mapping")
        require(event["demo_shot_id"] in {s["id"] for s in beat["shots"][:3]} and
                shot_map[event["demo_shot_id"]]["end_seconds"] <= event["question_end_boundary_seconds"],
                "Demonstration must be in the same beat before the external input pause")
        require(event["wait_time_counted"] is False and event["narrative_wait_seconds"] == 0 and
                event["model_example_narrative_counted"] is False, "WAIT/example counted in story duration")
        require(event["model_example_first_pass_required"] is True and event["parent_tap_can_skip_model_and_react"] is True,
                "First-model / parent-touch path missing")
        require(event["trigger"] == "QUESTION_AUDIO_ENDED_THEN_MODEL_EXAMPLE_ENDED_THEN_VAD_OR_PARENT_TAP", "Microphone can open before model finishes")
        require(len(words(event["cue"])) == 3 and event["example_text"] == event["cue"], "Cue must be exactly three words")
        validate_direction(event.get("example_voice_direction"), event["speaker"], event["example_text"], event["id"] + "-EXAMPLE")
        require(react_shot["action_lead_seconds"] > 0, "Reaction must finish before first resumed speech")
    # These assertions encode previously missed, concrete review defects.
    all_text = "\n".join(x["text"] for x in spoken)
    if scene == "S03":
        require("Now I can put the book in." not in all_text, "Book already packed before future-tense line")
        require("Did something red move down there?" not in all_text, "Stationary hat clue wrongly described as moving")
        require("가방" in beats[-1]["shots"][-1]["acting"] and
                any(t in beats[-1]["shots"][-1]["acting"] for t in ("메", "착용", "어깨")), "Bag wearing bridge missing")
    if scene == "S04":
        require("I'll stay beside the school sign." not in all_text, "Sign-staying line conflicts with walking")
        landing = [a for s in shots for a in s.get("before_dialogue_actions", []) if a["action_id"] == "CRICKET_FIRST_LANDING"]
        require(len(landing) == 1 and landing[0]["before_dialogue_id"] == "S04-U015", "First Cricket landing must precede greeting")
        frog = [a for s in shots for a in s.get("between_dialogue_actions", []) if a["action_id"] == "FROG_FIRST_HOP"]
        require(len(frog) == 1 and frog[0]["after_dialogue_id"] == "S04-U023" and frog[0]["before_dialogue_id"] == "S04-U024",
                "First frog hop must be between canonical U023 and U024")
        jump = next(e for e in events if e["id"] == "I07")
        require("반쯤" not in jump["wait"] and "준비 상태" not in jump["wait"], "I07 preparation occurs before input")
    if scene == "S05":
        require(by_id["S05-N052"]["text"] == "You made room for them.", "Completed passing action needs result wording")
    if check_generated:
        expected = outputs(root, scene, bible=bible)
        for name, content in expected.items():
            require((Path(root) / name).read_bytes() == content.encode("utf-8"), "Generated/readable asset drift: " + name)
    result = {"scene": scene, "original_lines": original_count, "new_lines": new_count,
              "directed_story_lines": len(spoken), "directed_model_examples": 10, "shots": 50,
              "narrative_seconds_planned": total, "largest_planning_budget_fraction": round(max_budget_ratio, 4),
              "status": "DIRECTED_DESIGN_PASS_ONLY", "audio_synthesis": "NOT_RUN", "listening_approval": "NOT_RUN"}
    emit(json.dumps(result, ensure_ascii=False))
    return result


def timecode(seconds):
    return f"{int(seconds)//60:02}:{int(seconds)%60:02}"


def direction_md(d):
    emphasis = " · ".join(d["emphasis"]) or "문장 전체를 자연스럽게"
    internal = "; ".join(f"{x['after']} 뒤 {x['ms']}ms" for x in d["internal_pauses"]) or "추가 내부 쉼 없음"
    return (f"**음성 연기:** {d['profile_id']} → {d['listener']} / 의도: {d['intention']} / 감정: {d['emotion']}  \n"
            f"**말하는 방식:** {d['delivery_ko']}  \n"
            f"**속도·쉼 계획:** {d['pace_wpm']}단어/분, 에너지 {d['energy']}/5, 앞 {d['pause_before_ms']}ms / 뒤 {d['pause_after_ms']}ms. "
            f"강조: {emphasis}. {internal}. 실제 음성 측정값 아님.  \n"
            f"**엔진 연기 지시(읽지 않음):** {d['direction_en']}  \n"
            f"**피할 연기:** {'; '.join(d['avoid'])}"
            + (f"  \n**상대 반응:** {d['listener_reaction']}" if d.get("listener_reaction") else ""))


def outputs(root, scene, bible=None):
    bible = bible or read_json(root, BIBLE)
    design, imap = source_data(root, scene)
    spoken = [x for b in design["scenes"] for x in b["dialogue"] if x["kind"] in ("ORIGINAL", "NEW")]
    by_id = {x["dialogue_id"]: x for x in spoken}
    position = {x["dialogue_id"]: i for i, x in enumerate(spoken)}
    events = {e["id"]: e for e in imap["events"]}
    jobs = []
    for beat in design["scenes"]:
        for shot in beat["shots"]:
            for line_id in shot["dialogue_ids"]:
                line = by_id[line_id]
                index = position[line_id]
                jobs.append(make_job(scene, beat, shot, line_id, line["kind"], line["speaker"], line["text"],
                                     line["voice_direction"], bible, False,
                                     spoken[index-1] if index else None,
                                     spoken[index+1] if index+1 < len(spoken) else None))
        event = events[beat["interaction_id"]]
        jobs.append(make_job(scene, beat, None, event["id"] + "-EXAMPLE", "MODEL_EXAMPLE", event["speaker"],
                             event["example_text"], event["example_voice_direction"], bible, True,
                             by_id[event["question_dialogue_id"]], by_id[event["resume_dialogue_id"]]))
    plan = {"schema_version": "2.1", "scene": scene, "source_revision": design.get("revision", "2.1_VOICE_DIRECTED_CORRECTION"),
            "source_hashes": {name: sha(Path(root)/name) for name in [f"scenes/{scene}/scene_design_v2.json", f"scenes/{scene}/interaction_map_v2.json", BIBLE, REGISTRY]},
            "story_line_count": len(spoken), "model_example_count": 10,
            "narrative_seconds_planned": design["duration_target_seconds"],
            "instructions_are_not_spoken_text": True, "model_audio_is_outside_story_clock": True,
            "audio_synthesis": "NOT_RUN", "actor_performance_listening_review": "NOT_RUN",
            "engine_instruction_adapter": "REQUIRED_NOT_IMPLEMENTED_BY_THIS_EXPORT",
            "jobs": jobs}
    md = [f"# {scene} 상세 대본 — 수정본·문장별 음성 연기 V2.1", "",
          f"**본편 계획:** {design['duration_target_seconds']}초 / 50컷 / 참여10회. 입력 대기·모델 예시는 별도 시간이다. 실제 영상·음성 길이 NOT_RUN.",
          "**수정 범위:** 사용자 요청에 따른 검토 지적 수정과 모든 발화의 연기 지시. 1·2화 완료본과 승인 성우 참조는 유지한다.",
          "**성우 기준:** [전체 캐릭터 음색·연기 기준](../../docs/series_v2/VOICE_PERFORMANCE_BIBLE_V2_1.md). 영어 대사만 읽고 연기 지시는 발화하지 않는다.",
          "**기계용 제작표:** [voice_direction_plan.json](voice_direction_plan.json) · [voice_direction_sheet.csv](voice_direction_sheet.csv)",
          "", "## 비트 시간표", "", "|비트|내용|본편 구간|참여|", "|---|---|---|---|"]
    for beat in design["scenes"]:
        md.append(f"|{beat['id']}|{beat['title']}|{timecode(beat['start_seconds'])}–{timecode(beat['end_seconds'])}|{beat['interaction_id']}|")
    for beat in design["scenes"]:
        md += ["", f"## {beat['id']}. {beat['title']}", "", f"**목적:** {beat['goal']}", "", f"**연속성:** {beat['continuity']}"]
        event = events[beat["interaction_id"]]
        for shot in beat["shots"]:
            md += ["", f"### {shot['id']} · {timecode(shot['start_seconds'])}–{timecode(shot['end_seconds'])} · {shot['phase']}", "",
                   f"**카메라:** {shot['camera']}", "", f"**자율 행동·연출:** {shot['acting']}", "",
                   f"**시간 배정:** 발화 전 행동 {shot['action_lead_seconds']}초 / 발화 뒤 행동 {shot['action_tail_seconds']}초. "
                   f"대사·쉼·지정 행동 계획 합계 {shot_budget(shot, by_id):.2f}초. 실제 합성 길이는 별도 확인."]
            for action in shot.get("before_dialogue_actions", []):
                md += ["", f"**원본 행동 경계:** {action['action_id']} → {action['before_dialogue_id']} 이전. 선행 행동 시간에 포함."]
            for line_id in shot["dialogue_ids"]:
                line = by_id[line_id]
                tag = line["kind"] + (f" #{line['source_index']}" if line["kind"] == "ORIGINAL" else "")
                md += ["", f"**[{line_id} · {tag}] {line['speaker']}:** “{line['text']}”", "", direction_md(line["voice_direction"])]
                for action in shot.get("between_dialogue_actions", []):
                    if action["after_dialogue_id"] == line_id:
                        md += ["", f"**대사 사이 행동:** {action['action_id']} — {action['seconds']}초. 다음 {action['before_dialogue_id']} 전에 완료."]
            if shot["phase"] == "PROMPT":
                md += ["", f"**윤수 참여 {event['index']}/10 · {event['id']} · 본편 밖 입력 대기**", "",
                       f"- 질문 종료 시점: {event['question_end_boundary_seconds']}초. 본편 시계를 멈춘다.",
                       f"- 첫 모델 예시: **“{event['example_text']}”** — {event['speaker']}의 같은 고정 목소리.",
                       "- 모델 예시를 한 번 들려준 뒤 마이크를 켠다. 정확한 단어·발음 채점은 하지 않는다.",
                       "- 보호자 터치는 예시를 생략하고 반응으로 진행할 수 있다. 무응답5초 뒤 다시 듣기/터치를 제시한다.",
                       f"- 시범: {event['demo']}", f"- 대기 상태: {event['wait']}", f"- 입력 뒤 한 번 실행: {event['react']}",
                       f"- 첫 재개: {event['resume_dialogue_id']} “{event['resume']}”", "", "**예시 음성 연기:**", "",
                       direction_md(event["example_voice_direction"])]
    md += ["", "## 실제 제작 상태", "", "위 대사·연기·시간은 설계다. 실제 합성·청취·립싱크·VAD·영상 재생은 NOT_RUN이다. 귀뚜라미의 승인 참조 음색은 BLOCKED_RESOURCE이며 다른 성우로 대체하지 않는다.", ""]
    stream = io.StringIO(newline="")
    fields = ["id", "kind", "scene", "beat", "shot", "speaker", "profile_id", "reference_slug", "voice_reference_status",
              "reference_path", "spoken_text", "listener", "intention", "emotion", "delivery_ko", "direction_en",
              "instruct_prompt_en", "pace_wpm", "energy", "emphasis", "pause_before_ms", "pause_after_ms",
              "internal_pauses", "avoid", "listener_reaction", "model_audio_outside_story_clock", "suggested_output", "synthesis_status"]
    writer = csv.DictWriter(stream, fields, lineterminator="\n")
    writer.writeheader()
    for job in jobs:
        d = job["voice_direction"]
        row = {key: job.get(key, "") for key in fields}
        for key in ("listener", "intention", "emotion", "delivery_ko", "direction_en", "pace_wpm", "energy", "pause_before_ms", "pause_after_ms"):
            row[key] = d[key]
        row["emphasis"] = json.dumps(d["emphasis"], ensure_ascii=False)
        row["internal_pauses"] = json.dumps(d["internal_pauses"], ensure_ascii=False)
        row["avoid"] = json.dumps(d["avoid"], ensure_ascii=False)
        row["listener_reaction"] = d.get("listener_reaction", "")
        row["reference_path"] = (job["approved_reference"] or {}).get("reference_mp3_path", "")
        writer.writerow(row)
    return {f"scenes/{scene}/script_v2_draft.md": "\n".join(md),
            f"scenes/{scene}/voice_direction_plan.json": dump(plan),
            f"scenes/{scene}/voice_direction_sheet.csv": "\ufeff" + stream.getvalue()}


def make_job(scene, beat, shot, job_id, kind, speaker, text, direction, bible, is_model, previous, following):
    profile = bible["profiles"][direction["profile_id"]]
    def context(line):
        return {key: line[key] for key in ("dialogue_id", "speaker", "text")} if line else None
    internal = "; ".join(f"after '{p['after']}': {p['ms']} ms" for p in direction["internal_pauses"]) or "none"
    prompt = (profile["default_direction_en"] + "\nFor this exact line: " + direction["direction_en"] +
              f"\nPlanning pace: {direction['pace_wpm']} words per minute; energy {direction['energy']}/5. " +
              f"Emphasis: {', '.join(direction['emphasis']) or 'natural phrase'}. " +
              f"Pause before: {direction['pause_before_ms']} ms; after: {direction['pause_after_ms']} ms; internal pauses: {internal}. " +
              "These are acting targets, not permission to time-stretch the voice. " +
              "Play the intent in relation to the previous and next line; do not read the context or these instructions. " +
              "Speak only spoken_text exactly, without added words or character labels. Preserve the locked speaker identity.")
    return {"id": job_id, "kind": kind, "scene": scene, "beat": beat["id"], "shot": shot["id"] if shot else "EXTERNAL_PAUSE",
            "speaker": speaker, "profile_id": direction["profile_id"], "reference_slug": profile["reference_slug"], "approved_reference": profile["reference"],
            "event_id": job_id.removesuffix("-EXAMPLE") if is_model else None,
            "voice_reference_status": profile["production_voice_status"], "spoken_text": text,
            "voice_direction": copy.deepcopy(direction), "instruct_prompt_en": prompt,
            "context_before_do_not_speak": context(previous), "context_after_do_not_speak": context(following),
            "estimated_voice_seconds_planned": round(planned_voice_seconds(text, direction), 3),
            "model_audio_outside_story_clock": is_model, "microphone_enabled_during_playback": False,
            "pause_application_policy": {"boundary_pauses": "TIMELINE_ONCE_AFTER_MEASURING_OR_TRIMMING_GENERATED_BOUNDARIES",
                                         "internal_pauses": "ENGINE_OR_CONTROLLED_EDIT_ONCE",
                                         "do_not_double_add_existing_silence": True},
            "suggested_output": f"scenes/{scene}/audio/directed/{job_id}.wav", "synthesis_status": "NOT_RUN",
            "listening_review": "NOT_RUN", "direction_application": "ENGINE_ADAPTER_REQUIRED"}


def voice_preflight(root, scene):
    from collections import Counter
    validate_scene(root, scene, emit=lambda *_: None)
    plan = read_json(root, f"scenes/{scene}/voice_direction_plan.json")
    jobs = plan["jobs"]
    blocked = sorted({j["speaker"] for j in jobs if j["approved_reference"] is None})
    story = [j for j in jobs if j["kind"] != "MODEL_EXAMPLE"]
    models = [j for j in jobs if j["kind"] == "MODEL_EXAMPLE"]
    return {"scene": scene, "audit_scope": "LOCKED_REFERENCES_AND_PER_LINE_DIRECTION_EXPORT_ONLY",
            "reference_integrity": "PASS", "direction_export_integrity": "PASS",
            "story_dialogue_count": len(story), "model_example_count": len(models),
            "first_pass_model_examples_required": len(models), "optional_example_count": 0,
            "example_replays_optional": True,
            "story_speaker_counts": dict(Counter(j["speaker"] for j in story)),
            "model_example_speaker_counts": dict(Counter(j["speaker"] for j in models)),
            "blocked_speakers": blocked,
            "full_scene_voice_gate": "BLOCKED_RESOURCE" if blocked else "REFERENCE_READY_AUDIO_NOT_RUN",
            "audio_synthesis": "NOT_RUN", "audio_duration_and_lipsync": "NOT_RUN",
            "direction_adapter_application": "NOT_RUN", "listening_review": "NOT_RUN",
            "voice_plan": f"scenes/{scene}/voice_direction_plan.json",
            "voice_assignments": [{"id": j["id"], "speaker": j["speaker"], "text": j["spoken_text"],
                                   "kind": j["kind"], "profile_id": j["profile_id"],
                                   "reference_slug": j["reference_slug"],
                                   "status": j["voice_reference_status"], "direction_present": True} for j in jobs]}


def legacy_voice_cli(scene):
    """Retain preflight entry point; refuse the previous flat synthesis path."""
    parser = argparse.ArgumentParser(description="Directed voice preflight; old text-only synthesis is retired.")
    parser.add_argument("--synthesize", action="store_true")
    parser.add_argument("--limit", type=int, default=2)
    parser.add_argument("--device", choices=["cpu", "cuda", "mps"], default="cpu")
    parser.add_argument("--json", type=Path)
    parser.add_argument("--export-jobs", type=Path)
    parser.add_argument("--require-ready", action="store_true")
    args = parser.parse_args()
    report = voice_preflight(ROOT, scene)
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(dump(report), encoding="utf-8")
    if args.export_jobs:
        args.export_jobs.parent.mkdir(parents=True, exist_ok=True)
        args.export_jobs.write_bytes((ROOT / report["voice_plan"]).read_bytes())
    print(json.dumps({k: v for k, v in report.items() if k != "voice_assignments"}, ensure_ascii=False))
    if args.synthesize:
        print("DIRECTED_ADAPTER_REQUIRED: the previous generate(text, audio_prompt_path) route did not pass per-line acting instructions. "
              "Use the exported voice_direction_plan.json and CODEX_VOICE_ACTING_HANDOFF.md; map directions to real supported engine controls. "
              "No audio generated and no parameters invented.", file=sys.stderr)
        return 2
    if args.require_ready and report["blocked_speakers"]:
        return 2
    return 0


def build(root, scenes):
    bible = validate_bible(root)
    for scene in scenes:
        validate_scene(root, scene, check_generated=False)
        files = outputs(root, scene, bible)
        for name, content in files.items():
            target = Path(root) / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8", newline="")
        print("BUILT_DIRECTED_DESIGN_ASSETS", scene, len(files), "audio NOT_RUN")


def negative_checks(root, scenes):
    # Every isolated bad input starts from the already-passing current source.
    for scene in scenes:
        validate_scene(root, scene, emit=lambda *_: None)
    checks = []
    with tempfile.TemporaryDirectory(prefix="directed-voice-check-") as directory:
        temp = Path(directory) / "repo"
        shutil.copytree(root, temp, ignore=shutil.ignore_patterns("__pycache__", ".git", "audio"))
        def reject(scene, label, file, mutate, expected):
            path = temp / file
            baseline = path.read_bytes()
            data = json.loads(baseline)
            mutate(data)
            path.write_text(dump(data), encoding="utf-8")
            try:
                validate_scene(temp, scene, emit=lambda *_: None, check_generated=False)
            except (ValueError, KeyError, AssertionError) as exc:
                require(expected in str(exc), label + " failed for wrong reason: " + str(exc))
                checks.append({"case": label, "status": "REJECTED_EXPECTED", "reason": str(exc)})
            else:
                raise ValueError("Invalid input accepted: " + label)
            finally:
                path.write_bytes(baseline)
        scene = scenes[0]
        path = f"scenes/{scene}/scene_design_v2.json"
        reject(scene, "missing per-line direction", path,
               lambda d: d["scenes"][0]["dialogue"][0].pop("voice_direction"), "missing voice direction")
        reject(scene, "wrong character identity", path,
               lambda d: d["scenes"][0]["dialogue"][0]["voice_direction"].update(profile_id="BLUE_FAIRY_C"), "wrong character profile")
        reject(scene, "canonical text polluted by acting note", path,
               lambda d: d["scenes"][0]["dialogue"][0].update(text="[happy] " + d["scenes"][0]["dialogue"][0]["text"]), "Canonical speech changed")
        reject(scene, "narrative WAIT shot", path,
               lambda d: d["scenes"][0]["shots"][2].update(phase="WAIT"), "Pure WAIT")
        reject(scene, "speech overrun hidden in cut", path,
               lambda d: d["scenes"][-1]["shots"][-1].update(action_lead_seconds=1000), "Speech/action budget exceeds")
        map_path = f"scenes/{scene}/interaction_map_v2.json"
        reject(scene, "four-word learning cue", map_path,
               lambda d: d["events"][0].update(cue="Look at the flower!", example_text="Look at the flower!"), "exactly three words")
        reject(scene, "microphone opens before first model", map_path,
               lambda d: d["rules"].update(first_model_before_listen=False), "Missing beginner/input rule")
        if "S04" in scenes:
            p = "scenes/S04/scene_design_v2.json"
            def wrong_landing(d):
                for beat in d["scenes"]:
                    for shot in beat["shots"]:
                        for a in shot.get("before_dialogue_actions", []):
                            if a["action_id"] == "CRICKET_FIRST_LANDING":
                                a["before_dialogue_id"] = "S04-U018"
            reject("S04", "Cricket landing after first greeting", p, wrong_landing, "First Cricket landing must precede greeting")
    print(json.dumps({"negative_checks": checks, "status": "PASS_EXPECTED_REJECTIONS"}, ensure_ascii=False))
    return checks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=["build", "validate", "self-test"])
    parser.add_argument("--scenes", nargs="+", choices=list(COUNTS), default=list(COUNTS))
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    if args.action == "build":
        build(ROOT, args.scenes)
        return 0
    results = [validate_scene(ROOT, scene) for scene in args.scenes]
    probes = negative_checks(ROOT, args.scenes) if args.action == "self-test" else []
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(dump({"scope": "DIRECTED_DESIGN_AND_JOB_EXPORT_ONLY", "results": results,
                                    "negative_checks": probes, "audio_synthesis": "NOT_RUN", "listening_review": "NOT_RUN"}), encoding="utf-8")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, KeyError, OSError, AssertionError) as exc:
        print("FAIL:", exc, file=sys.stderr)
        raise SystemExit(1)
