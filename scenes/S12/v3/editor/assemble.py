"""Measure the approved S12 cuts against selected native voice takes."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import runpy
import sys
import tempfile
import wave

import numpy as np

from soundtrack import arrange


V3 = Path(__file__).resolve().parents[1]
SCENES = V3.parents[1]
BUILD = V3 / "build"
VOICES = BUILD / "voices"
HANDOFF = V3 / "canonical"
RECEIPTS = Path("/workspace/scratch/s12-v3/voice/selected")
FPS, RATE, NATIVE = 24, 24_000, 22_050
TICK = RATE // FPS
GATE_IDS = ("S12-P01", "S12-P02", "I21", *(f"S12-P{i:02d}" for i in range(3, 10)))
TURN_FRAMES = {"S12-U005": 5, "S12-U029": 4, "S12-U031": 5, "S12-N020": 5,
               "S12-U034": 5, "S12-U037": 6, "S12-U039": 6}
ACTION_FIELDS = {"lead_frames", "tail_frames", "silent_frames", "between_frames", "marks"}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(path):
    with path.open("rb") as file:
        return hashlib.file_digest(file, "sha256").hexdigest()


def samples_window(start, end):
    return {"start": start / RATE, "end": end / RATE}


def end_frame(sample):
    return -(-sample // TICK)


def existing_audio_editor():
    root = SCENES / "S10/production/editor"
    sys.path.insert(0, str(root))
    try:
        return runpy.run_path(str(root / "assemble.py"))
    finally:
        sys.path.pop(0)


def plan(root):
    folder = root / "story"
    story_path = folder / "scene_design_v2.json"
    gate_path = folder / "interaction_map_v2.json"
    voice_path = folder / "S12_VOICE_JOBS.json"
    source, interactions, voice = (read(path) for path in (story_path, gate_path, voice_path))
    shots = source["shots"]
    dialogue = source["dialogue"]
    lines = {row["dialogue_id"]: row for row in dialogue}
    jobs = {job["job_id"]: job for job in voice["jobs"]}
    require(source["scene"] == interactions["scene"] == voice["scene"] == "S12", "S12 handoff required")
    require(source["target_fps"] == FPS and source["minimum_narrative_seconds"] == 360
            and source["narrative_seconds_planned"] == 468
            and len(shots) == 50 and len(lines) == len(dialogue) == 71 and len(jobs) == len(voice["jobs"]) == 81,
            "S12 approved counts and clock must match")
    require([cut["id"] for cut in shots] == [f"S12-C{i:02d}" for i in range(1, 51)]
            == [key for beat in source["scenes"] for key in beat["shot_ids"]], "S12 approved shot order changed")
    require([key for cut in shots for key in cut["dialogue_ids"]] == list(lines),
            "Every approved line must occur once in story order")
    require(source["protected_narrative"] == interactions["protected_narrative"],
            "Protected story scopes disagree")
    originals = [{"dialogue_id": row["dialogue_id"], "speaker": row["speaker"], "text": row["spoken_text"]}
                 for row in dialogue if row["kind"] == "ORIGINAL"]
    require(len(originals) == 44 and originals == read(folder / "S12_CANONICAL_LINES.json"),
            "An immutable original line or speaker changed")
    require(all(row == jobs[key] for key, row in lines.items()), "Synthesis jobs differ from the reviewed scene")
    require(sum(row["kind"] == "NEW" for row in dialogue) == 27, "Expected 27 approved new lines")
    require(shots[-1]["dialogue_ids"] == ["S12-U044"]
            and [row["dialogue_id"] for row in dialogue if row["spoken_text"] == "The end."] == ["S12-U044"],
            "The end must be the final utterance and occur once")
    require(tuple(event["id"] for event in interactions["events"]) == GATE_IDS, "S12 gate order changed")
    order = {row["id"]: index for index, row in enumerate(shots)}
    expected_models = {f"S12-M{i:03d}" for i in range(1, 11)}
    gates = {}
    for event in interactions["events"]:
        model, prompt, react = event["model_job_id"], event["prompt_shot_id"], event["reaction_shot_ids"]
        resume = event["resume_dialogue_id"]
        resume_shot = lines[resume]["shot_id"]
        p = order[prompt]
        span = [cut["id"] for cut in shots[p+1:p+1+len(react)]]
        question = event["question_dialogue_id"]
        require(shots[p]["dialogue_ids"][-1] == question and lines[question]["speaker"] == event["question_speaker"],
                f"{event['id']}: question is not the last prompt line")
        require(span == react and order[resume_shot] in (p+len(react), p+len(react)+1)
                and shots[order[resume_shot]]["dialogue_ids"][0] == resume,
                f"{event['id']}: reaction is not contiguous through the first follow-up")
        require((jobs[model]["kind"], jobs[model]["speaker"], jobs[model]["spoken_text"], jobs[model]["event_id"]) ==
                ("EXTERNAL_MODEL", event["external_model_speaker"], event["cue"], event["id"]),
                f"{event['id']}: external model differs from the gate")
        require(event["once_only"] is True and not event["exact_phrase_matching"], f"{event['id']}: invalid input mode")
        gates[prompt] = {**event, "react_shot_id": react[0], "resume_shot_id": resume_shot}
    require(set(jobs) - set(lines) == expected_models == {v["model_job_id"] for v in gates.values()},
            "The ten models must exist only in the external bank")
    require(next(g for g in gates.values() if g["id"] == "I21")["reaction_shot_ids"] ==
            ["S12-C12", "S12-C13", "S12-C14"], "I21 must keep all three physical rescue cuts")
    files = {"story": sha(story_path), "interaction": sha(gate_path), "voice_jobs": sha(voice_path)}
    return source, shots, lines, jobs, gates, files


def selected(voices, receipts, key):
    return (voices / f"{key}.wav").is_file() and (receipts / f"{key}.json").is_file()


def read_takes(voices, receipts, keys, legacy):
    missing = [key for key in keys if not selected(voices, receipts, key)]
    require(not missing, f"{len(missing)} accepted WAVs or receipts are pending: {', '.join(missing)}")
    takes, ledger, native = {}, {}, []
    accepted = {}
    for cue in keys:
        path = voices / f"{cue}.wav"
        receipt = read(receipts / f"{cue}.json")
        source_sha = sha(path)
        require(receipt["id"] == cue and receipt["sha256"] == source_sha,
                f"{cue}: WAV bytes must match their accepted selection receipt")
        accepted[cue] = {"selection_receipt_sha256": sha(receipts / f"{cue}.json"),
                         "human_listening_review": receipt.get("human_listening_review", "NOT_RECORDED")}
        with wave.open(str(path), "rb") as audio:
            rate = audio.getframerate()
        require(rate in (RATE, NATIVE), f"{cue}: unexpected sample rate {rate}")
        if rate == NATIVE:
            native.append(cue)
            ledger[cue] = source_sha
            continue
        pcm = legacy["read_pcm"](path, RATE)
        require(len(pcm) and np.max(np.abs(pcm.astype(np.int32))) < 32767, f"{cue}: empty or clipped audio")
        clock = legacy["clocks"](pcm, RATE)
        takes[cue] = pcm
        ledger[cue] = {"native_wav_sha256": source_sha, "native_rate": RATE,
                       "native_samples": len(pcm), "samples": len(pcm),
                       "pcm_sha256": hashlib.sha256(pcm.tobytes()).hexdigest(),
                       "native_edges": clock, "converted_edges": clock, "edge_guard_samples": [0, 0]}
    converted, proof = legacy["read_takes"](voices, native)
    require(all(proof[cue]["native_wav_sha256"] == ledger[cue] for cue in native),
            "A selected WAV changed while being converted")
    measured = ledger | proof
    return takes | converted, {cue: measured[cue] | accepted[cue] for cue in keys}


def motion_windows(shots, path):
    values = read(path) if path else {}
    if isinstance(values, dict) and values.keys() == {"cuts"}:
        values = values["cuts"]
    require(isinstance(values, dict) and values.keys() <= {shot["id"] for shot in shots},
            "Motion windows must key approved S12 shots")
    for key, value in values.items():
        cut = next(shot for shot in shots if shot["id"] == key)
        require(isinstance(value, dict), f"{key}: motion override must be an object")
        breaks = value.get("between_frames", {})
        marks = value.get("marks", {})
        require(value.keys() <= ACTION_FIELDS
                and isinstance(breaks, dict) and breaks.keys() <= set(cut["dialogue_ids"][:-1])
                and isinstance(marks, dict),
                f"{key}: invalid physical motion windows or marks")
        numbers = [value[k] for k in ("lead_frames", "tail_frames", "silent_frames") if k in value]
        require(all(type(n) is int and n >= 0 for n in [*numbers, *breaks.values(), *marks.values()]),
                f"{key}: physical action lengths and marks must be nonnegative integral frames")
        require("silent_frames" not in value or not cut["dialogue_ids"], f"{key}: spoken cuts need lead/tail windows")
    return values


def budgets(shot, measured):
    t = shot["timing_budget"]
    lead = round(t["action_lead_seconds_planned"] * FPS)
    tail = round(t["action_tail_seconds_planned"] * FPS)
    between = {"S12-N007": 24} if shot["id"] == "S12-C05" else {}
    if shot["id"] == "S12-C35":
        # N015 is the discovery line. The real adult palm demonstration follows
        # it and precedes N016, so move the authored lead budget inside the turn.
        between["S12-N015"] = lead - 12
        lead = 12
    lead, tail = measured.get("lead_frames", lead), measured.get("tail_frames", tail)
    between.update(measured.get("between_frames", {}))
    if shot["id"] in ("S12-C03", "S12-C05"):
        require(lead >= 48, f"{shot['id']}: authored meaning demonstration needs at least 48 lead frames")
    if shot["id"] == "S12-C05":
        require(tail >= 12 and between["S12-N007"] >= 24,
                "S12-C05: hat release and the gust require 24 between frames and 12 tail frames")
    return lead, tail, between


def schedule(shots, lines, gates, takes, ledger, measured):
    cuts, placement, evidence = [], [], []
    first = 0
    for authored in shots:
        cut_id = authored["id"]
        phrase_ids = authored["dialogue_ids"]
        physical = measured.get(cut_id, {})
        lead, tail, between = budgets(authored, physical)
        if cut_id in gates:
            require(not tail, f"{cut_id}: the prompt has no post-question hold")
        speaking_from = (first + lead) * TICK
        cursor = speaking_from
        gaps, clips = [], []
        for i, cue in enumerate(phrase_ids):
            pcm = takes[cue]
            start, stop = cursor, cursor + len(pcm)
            edges = ledger[cue]["converted_edges"]
            line = lines[cue]
            clips.append({"id": cue, "speaker": line["speaker"], "text": line["spoken_text"], "kind": line["kind"],
                          "sample_start": start, "sample_end_exclusive": stop, **samples_window(start, stop),
                          "audible_start": (start + edges["first_nonquiet_sample"]) / RATE,
                          "audible_release": (start + edges["last_nonquiet_sample"] + 1) / RATE})
            cursor = stop
            if i < len(phrase_ids)-1:
                frames = between.get(cue, TURN_FRAMES.get(cue, 5))
                length = frames * TICK
                gaps.append({"after_dialogue_id": cue, "before_dialogue_id": phrase_ids[i+1],
                             **samples_window(cursor, cursor + length), "frames": frames,
                             "physical_action": cue in between})
                cursor += length
        silent = None
        if not phrase_ids:
            silent = physical.get("silent_frames", round(authored["duration_seconds_planned"]*FPS))
            end = first + silent
            require(silent > 0, f"{cut_id}: silent physical action needs running frames")
            speaking_from = cursor = end*TICK
        else:
            end = end_frame(cursor+tail*TICK)
        if cut_id in gates:
            shift = end*TICK - cursor
            speaking_from += shift
            cursor += shift
            for clip in clips:
                for name in ("sample_start", "sample_end_exclusive"):
                    clip[name] += shift
                for name in ("start", "end", "audible_start", "audible_release"):
                    clip[name] = (round(clip[name]*RATE)+shift)/RATE
            for gap in gaps:
                for name in ("start", "end"):
                    gap[name] = (round(gap[name]*RATE)+shift)/RATE
        require(end > first, f"{cut_id}: zero-length shot")
        role = authored["events"][0]["role"] if authored["events"] else None
        landmarks = {}
        if role == "REACT":
            done = end if silent is not None else first+lead
            require(done > first, f"{cut_id}: reaction needs actual action before the follow-up")
            landmarks["action_complete"] = {"frame": done, "at": done/FPS, "offset_frames": done-first}
        for name, offset in physical.get("marks", {}).items():
            require(offset < end-first and name not in landmarks, f"{cut_id}: {name} outside its valid frame span")
            landmarks[name] = {"frame": first+offset, "at": (first+offset)/FPS, "offset_frames": offset}
        if silent is None:
            lead_end, story_start = speaking_from, speaking_from
        else:
            lead_end, story_start = cursor, first*TICK
        cut = {**authored, "first": first, "end": end, "audio": clips,
               "phase": "PROMPT" if role == "WAIT" else (role or "NARRATIVE"),
               "actual_duration_seconds": (end-first)/FPS, "action_landmarks": landmarks,
               "action_windows": {"lead": samples_window(first*TICK, lead_end),
                                  "story": samples_window(story_start, cursor),
                                  "tail": samples_window(cursor, end*TICK), "between": gaps}}
        if cut_id in gates:
            require(clips[-1]["sample_end_exclusive"] == end*TICK, f"{cut_id}: actual question end shifted")
        cuts.append(cut)
        placement.extend((clip["id"], clip["sample_start"]) for clip in clips)
        evidence.append({"id": cut_id, "first": first, "end": end, "speech_samples":
                         sum(len(takes[cue]) for cue in phrase_ids), "spoken_turns": len(phrase_ids),
                         "planned_seconds": authored["duration_seconds_planned"], "silent_action_frames": silent,
                         "measured_motion_override": bool(physical)})
        first = end
    return cuts, placement, evidence


def actual_events(cuts, gates, takes):
    index = {cut["id"]: cut for cut in cuts}
    by_line = {line["id"]: line for cut in cuts for line in cut["audio"]}
    complete, incomplete, quiet = [], [], []
    for row in gates.values():
        prompt = index.get(row["prompt_shot_id"])
        if prompt is None:
            continue
        question = prompt["audio"][-1]
        at = prompt["end"]
        require(question["id"] == row["question_dialogue_id"] and question["sample_end_exclusive"] == at*TICK,
                f"{row['id']}: actual question file does not end at the pause")
        model = row["model_job_id"]
        event = {**row, "frame": at, "at": at/FPS, "question_wav_exact_end_sample": at*TICK,
                 "reaction_start": at/FPS, "demo_shot_id": prompt["id"],
                 "example_dialogue_id": model, "example_speaker": row["external_model_speaker"],
                 "example_text": row["cue"], "example_duration": len(takes[model])/RATE if model in takes else None,
                 "required": True, "outside_story_clock": True, "wait_time_counted": False,
                 "model_example_narrative_counted": False, "require_speech_activity_not_phrase_match": True,
                 "timeout_hint_seconds": None, "repeat_example_after_no_response_seconds": None}
        quiet.append({"id": row["id"], "frame": at})
        if (not all(key in index for key in row["reaction_shot_ids"]) or row["resume_dialogue_id"] not in by_line
                or model not in takes):
            incomplete.append(event)
            continue
        first = index[row["react_shot_id"]]
        reaction = index[row["reaction_shot_ids"][-1]]
        done = reaction["action_landmarks"]["action_complete"]["at"]
        follow = by_line[row["resume_dialogue_id"]]
        require(first["first"] == at and at/FPS < done <= follow["start"],
                f"{row['id']}: first reply precedes reaction completion")
        require(row["id"] != "I21" or done == reaction["end"]/FPS == index[row["resume_shot_id"]]["first"]/FPS,
                "I21 must retain all silent rescue cuts through sign stability and release")
        complete.append({**event, "reaction_end": done, "reaction_window_end": done})
    return complete, incomplete, quiet


def protected_windows(source, cuts, events):
    by_line = {line["id"]: (cut, line) for cut in cuts for line in cut["audio"]}
    by_shot = {cut["id"]: cut for cut in cuts}
    result = []
    for scope in source["protected_narrative"]:
        begin, end = scope["from"], scope["to"]
        if end not in by_line or (begin not in by_line and begin != "I21_ACCEPTED"):
            continue
        if begin == "I21_ACCEPTED":
            if "S12-C12" not in by_shot:
                continue
            first = by_shot["S12-C12"]["first"]*TICK
        else:
            first = by_line[begin][1]["sample_start"]
        final_cut, final_line = by_line[end]
        last = final_line["sample_end_exclusive"]
        if end in ("S12-U033", "S12-U044"):
            last = final_cut["end"]*TICK
        require(not any(first <= event["frame"]*TICK < last and not
                        (begin == "I21_ACCEPTED" and event["id"] == "I21" and event["frame"]*TICK == first)
                        for event in events), f"{scope['id']}: an extra event interrupts a protected sequence")
        result.append({**scope, **samples_window(first, last), "start_sample": first, "end_sample": last})
    return result


def span(token):
    numbers = []
    for item in token.upper().split(":"):
        found = re.fullmatch(r"(?:S12-)?C(\d{2})", item)
        require(found is not None, "Use cuts like C29 or C06:C19")
        numbers.append(int(found.group(1)))
    require(len(numbers) in (1, 2) and 1 <= numbers[0] <= numbers[-1] <= 50, "Shot range must be in story order")
    return numbers[0], numbers[-1]


def measure(handoff, voices, receipts, output, section, overrides):
    source, shots, lines, _, gates, hashes = plan(handoff)
    windows = motion_windows(shots, overrides)
    prefix = []
    if section is not None:
        first, last = section
        prefix, shots = shots[:first-1], shots[first-1:last]
    ids = [cue for cut in shots for cue in cut["dialogue_ids"]]
    gate_models = [gates[cut["id"]]["model_job_id"] for cut in shots if cut["id"] in gates]
    model_ids = gate_models if section is None else [key for key in gate_models if selected(voices, receipts, key)]
    legacy = existing_audio_editor()
    takes, ledger = read_takes(voices, receipts, ids + model_ids, legacy)
    cuts, placement, proof = schedule(shots, lines, gates, takes, ledger, windows)
    frames = cuts[-1]["end"]
    require(section is not None or frames >= source["minimum_narrative_seconds"]*FPS,
            f"Actual WAV/audio and physical windows yield {frames/FPS:.3f}s. 360s needs verified motion, not padding.")
    events, incomplete, quiet = actual_events(cuts, gates, takes)
    require(section is not None or (len(events), len(incomplete), len(ids), len(model_ids)) == (10, 0, 71, 10),
            "Incomplete production timeline")
    protected = protected_windows(source, cuts, quiet)
    expected_offset = 0
    if prefix:
        preceding = [cue for cut in prefix for cue in cut["dialogue_ids"]]
        if all(selected(voices, receipts, cue) for cue in preceding):
            prior, prior_ledger = read_takes(voices, receipts, preceding, legacy)
            result, _, _ = schedule(prefix, lines, gates, prior, prior_ledger, windows)
            expected_offset = result[-1]["end"]
        else:
            expected_offset = None
    edit = {"contract": "S12_V3_71_50_10", "episode": "S12", "title": source["title"],
            "fps": FPS, "frames": frames, "duration": frames/FPS, "fixture": False, "pilot": None,
            "source_sha256": hashes["story"], "source_fingerprints": hashes, "cuts": cuts, "events": events,
            "incomplete_gates": incomplete, "protected_narrative": protected,
            "story_clock_excludes_examples_and_wait": True, "entry_state": cuts[0]["state"],
            "exit_state": cuts[-1]["state"]}
    if section is not None:
        edit.update(preview_only=True, excerpt={"first_shot": shots[0]["id"], "last_shot": shots[-1]["id"],
                    "source_story_first_frame": expected_offset,
                    "pending_external_models": sorted(set(gate_models)-set(model_ids))})
    dry = legacy["dry_pcm"](frames, placement, takes)
    mix, sound = arrange(edit, dry, quiet, expected_offset)
    report = {"scope": "NATIVE_CONTIGUOUS_EXCERPT" if section else "NATIVE_S12_EDIT",
              "cuts": proof, "takes": ledger, "sound_qa": sound, "frames": frames,
              "fps": FPS, "duration_seconds": frames/FPS, "cut_count": len(cuts),
              "staged_story_lines": len(ids), "staged_external_models": len(model_ids),
              "playable_gates": len(events), "boundary_frames": [ev["frame"] for ev in events],
              "editorial_clipping": "NONE", "human_listening_review": "NOT_RUN_IN_EDITOR",
              "picture_contact_validation": "SEPARATE_PRODUCTION_QA"}
    subtitles = runpy.run_path(str(SCENES / "S03/production/editor/assemble.py"))["write_subtitles"]
    output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".s12-editor-", dir=output) as base:
        stage = Path(base)
        scratch_audio = stage/"audio"
        scratch_audio.mkdir()
        for key, pcm in takes.items():
            legacy["write_wav"](scratch_audio/f"{key}.wav", pcm)
        legacy["write_wav"](stage/"mix.wav", mix)
        subtitles(stage/"subtitles.srt", edit)
        for name, data in (("timeline.json", edit), ("edit_report.json", report), ("edit.json", edit)):
            write(stage/name, data)
        (output/"audio").mkdir(exist_ok=True)
        for path in scratch_audio.iterdir():
            path.replace(output/"audio"/path.name)
        for name in ("mix.wav", "subtitles.srt", "timeline.json", "edit_report.json", "edit.json"):
            (stage/name).replace(output/name)
    return {key: value for key, value in report.items() if key not in ("cuts", "takes")}


def main():
    cli = argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--handoff", type=Path, default=HANDOFF)
    cli.add_argument("--voices", type=Path, default=VOICES)
    cli.add_argument("--receipts", type=Path, default=RECEIPTS)
    cli.add_argument("--motion-windows", type=Path)
    cli.add_argument("--output", type=Path)
    variants = cli.add_mutually_exclusive_group()
    variants.add_argument("--through", metavar="C29")
    variants.add_argument("--range", metavar="C06:C19")
    args = cli.parse_args()
    try:
        section = span(f"C01:{args.through}") if args.through else span(args.range) if args.range else None
        output = args.output or BUILD
        require(section is None or (args.output is not None and not output.resolve().is_relative_to(BUILD.resolve())),
                "A native excerpt requires an isolated --output directory")
        edit = output/"edit.json"
        if edit.is_file():
            previous = read(edit).get("excerpt")
            require((previous is None and section is None) or (previous is not None and section is not None
                    and [previous["first_shot"], previous["last_shot"]] ==
                    [f"S12-C{number:02d}" for number in section]), "Output contains a different cut range")
        report = measure(args.handoff, args.voices, args.receipts, output, section, args.motion_windows)
        print(json.dumps(report, ensure_ascii=False))
    except (OSError, ValueError, KeyError, TypeError, IndexError, EOFError, wave.Error) as error:
        cli.exit(1, f"S12 V3 editor: {error}\n")


if __name__ == "__main__":
    main()
