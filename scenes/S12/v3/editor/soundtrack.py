"""Continue approved series sound while reserving clean voice and input windows."""

import hashlib
import json
from pathlib import Path
import runpy
import wave

import numpy as np


SCENES = Path(__file__).resolve().parents[3]
RATE, TICK = 24_000, 1_000


def digest(path):
    with path.open("rb") as file:
        return hashlib.file_digest(file, "sha256").hexdigest()


def previous_ambience(road, fragment, pcm):
    folder = SCENES / "S11/v2/build"
    prior = json.loads((folder / "edit.json").read_text(encoding="utf-8"))
    source = next(cue for cue in prior["sound_cues"] if cue["kind"] == "continued_route_ambience")
    first, last = source["start_sample"], source["end_sample"]
    pickup, compare = last - first, RATE // 10
    if prior["frames"] * TICK != last or any(
        clip["sample_end_exclusive"] > last-compare for cut in prior["cuts"] for clip in cut["audio"]
    ):
        raise ValueError("S11 needs a verified speech-free route tail before S12")
    mix_path = folder / "mix.wav"
    with wave.open(str(mix_path), "rb") as wav:
        if (wav.getnchannels(), wav.getsampwidth(), wav.getframerate(), wav.getnframes()) != (1,2,RATE,last):
            raise ValueError("S11 route seam needs the measured 24 kHz mono S11 mix")
        wav.setpos(last-compare)
        actual = np.frombuffer(wav.readframes(compare), dtype="<i2")
    generated = pcm(fragment(road, pickup-compare, compare)*np.float32(.58))
    if not np.array_equal(generated, actual):
        raise ValueError("S11 actual audio does not match the existing route ambience phase")
    return pickup, compare, digest(mix_path)


def arrange(edit, dry, quiet_gates, excerpt_offset):
    helper = runpy.run_path(str(SCENES / "S05/production/editor/sound.py"))
    prior = runpy.run_path(str(SCENES / "S11/v2/editor/soundtrack.py"))
    outdoor = runpy.run_path(str(SCENES / "S07/production/editor/sound.py"))
    road, fragment = outdoor["road_air"], prior["route_fragment"]
    pickup, matched, mix_hash = previous_ambience(road, fragment, helper["to_pcm"])
    phase = pickup + (excerpt_offset or 0)*TICK
    background = fragment(road, phase, len(dry))*np.float32(.58)
    cuts = {cut["id"]: cut for cut in edit["cuts"]}
    cues = []

    def cue(name, kind, cut_id, start, end, source, **details):
        cues.append({"id": name, "kind": kind, "cut_id": cut_id, "start_sample": start, "end_sample": end,
                     "start": start/RATE, "end": end/RATE, "first_frame": start//TICK, "source": source, **details})

    def place(name, cut_id, start, samples, source, **details):
        end = start+len(samples)
        cut = cuts[cut_id]
        if not cut["first"]*TICK <= start < end <= cut["end"]*TICK:
            raise ValueError(f"{name}: sound outside {cut_id} motion window")
        background[start:end] += samples
        cue(name, "event_sound", cut_id, start, end, source, **details)

    first_cut = edit["cuts"][0]["id"]
    cue("same_air_at_school", "continued_route_ambience", first_cut, 0, len(dry), "S07 via S11 V2",
        source_first_sample=phase, canonical_scene_phase_known=excerpt_offset is not None)
    if "S12-C05" in cuts:
        cut = cuts["S12-C05"]
        start = next(line["sample_end_exclusive"] for line in cut["audio"] if line["id"] == "S12-N007")
        end = cut["end"]*TICK
        count = end-start
        gust = np.sin(np.linspace(0, np.pi, count, dtype=np.float32))**2
        # Increase the same source once after the hat grip. Duck processing
        # keeps the following spoken warning clear even at the gust's peak.
        background[start:end] *= 1 + np.float32(2.0)*gust
        cue("leaf_gust_after_hat_grip", "wind_gust", cut["id"], start, end, "S07 route ambience")
    board = cuts.get("S12-C06", {}).get("action_landmarks", {}).get("board_contact")
    if board is not None:
        impact = runpy.run_path(str(SCENES / "S06/production/editor/sound.py"))["impulse"]
        place("board_meets_existing_support", "S12-C06", board["frame"]*TICK,
              impact(1206, .20, 142) * np.float32(.074), "S06 impulse recipe", picture_mark="board_contact")
    if "S12-C09" in cuts:
        cut = cuts["S12-C09"]
        place("same_school_bell", cut["id"], cut["first"]*TICK,
              outdoor["distant_bell"]()*np.float32(.43), "S07 school bell")
    for cut_id, name in (("S12-C22", "fairy_arrival"), ("S12-C30", "actual_transformation")):
        if cut_id in cuts:
            cut = cuts[cut_id]
            light = runpy.run_path(str(SCENES / "S10/production/editor/sound.py"))["contact_light"]
            duration = min(round(cut["action_windows"]["lead"]["end"]*RATE)-cut["first"]*TICK, 2*RATE)
            if duration <= 0:
                raise ValueError(f"{cut_id}: fairy cue needs actual motion before the first line")
            place(name, cut_id, cut["first"]*TICK, light(duration), "S10 existing fairy contact tone")

    motif_hash = None
    if "S12-C50" in cuts:
        cut = cuts["S12-C50"]
        motif_path = SCENES / "S05/production/drum-flute-motif.wav"
        phrase = prior["read_pcm"](motif_path)
        end_voice = cut["audio"][-1]["sample_end_exclusive"]
        if len(phrase) != 3*RATE:
            raise ValueError("S12 needs the existing three-second closing motif")
        place("final_music_resolution", cut["id"], end_voice,
              phrase.astype(np.float32)/32767*np.float32(.37), "S05 score motif, one phrase")
        motif_hash = digest(motif_path)

    mix, bed = helper["mix_audio"]({**edit, "events": quiet_gates}, dry, background)
    if not np.array_equal(mix.astype(np.int32)-bed, dry):
        raise ValueError("The sound bed altered an accepted voice sample")
    for gate in quiet_gates:
        at = gate["frame"]*TICK
        if np.any(bed[at-round(.115*RATE):at]):
            raise ValueError(f"{gate['id']}: ambience remains under question release")
    ratio = 0.0
    for cut in cuts.values():
        for clip in cut["audio"]:
            start, end = clip["sample_start"], clip["sample_end_exclusive"]
            relative = np.sqrt(np.mean(bed[start:end].astype(float)**2)/np.mean(dry[start:end].astype(float)**2))
            ratio = max(ratio, float(relative))
    if ratio > .181:
        raise ValueError("Sound bed exceeds the inherited dialogue RMS guard")
    edit["sound_cues"] = sorted(cues, key=lambda item: item["start_sample"])
    edit["sound"] = {"prior": "S11_V2", "s11_mixed_tail_samples_reference_match": matched,
                     "s11_mix_sha256": mix_hash, "s11_route_pickup_sample": pickup,
                     "current_route_first_sample": phase, "closing_motif_source_sha256": motif_hash,
                     "wood_contact": "TIMED_TO_PICTURE" if board else "UNAVAILABLE_PICTURE_MARK" if "S12-C06" in cuts else "OUTSIDE_EXCERPT"}
    peak = int(np.max(np.abs(mix.astype(np.int32))))
    return mix, {"s11_mixed_tail_samples_reference_match": matched, "compared_opening_in_full_phase": excerpt_offset == 0,
                 "exact_dialogue_pcm_preserved": True, "gate_release_bed_samples_muted": round(.115*RATE),
                 "gate_check_count": len(quiet_gates), "maximum_effect_to_dialogue_rms": round(ratio, 5),
                 "peak_dbfs": round(float(20*np.log10(peak/32768)), 3)}
