#!/usr/bin/env python3
"""Register S12 C43–48 farewell drawings without changing the baseline build."""
from argparse import ArgumentParser
from copy import deepcopy
import json
from pathlib import Path
import runpy
import shutil

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent
V3 = Path("/workspace/yoonsu-pinocchio-3d/scenes/S12/v3")
RUN = ROOT / "run"
BASE = V3 / "build"
OUT = ROOT / "overlay"
ACTOR = "S12K-human-acting"
ENDING = runpy.run_path(str(V3 / "art/ending/build.py"))
SIZE = ENDING["HUMAN_SIZE"]
FLOOR = ENDING["HUMAN_FLOOR"]
HEIGHT = ENDING["HUMAN_REF"]

ACTIONS = {
    "blessing": ("lowers arms from the welcome pose", "raises gaze to the nearby fairy",
                 "brings palm to his chest", "bows his head, hand at his heart",
                 "comes out of the nod and begins releasing his hand",
                 "looks toward the fairy, hand down and smile settling"),
    "invite": ("keeps his arms down and looks toward the fairy", "moves his eyes toward Yoonsu",
               "begins turning his chin toward Yoonsu", "makes eye contact with Yoonsu",
               "holds eye contact to ask Yoonsu", "arms low and eyes ready for the shared farewell"),
    "fairy": ("prepares the wave with a low bent elbow", "raises his open palm to the fairy",
              "tilts his palm outward", "arcs the open hand back in",
              "finishes the outward hand arc", "lowers his hand while still facing the fairy"),
    "audience": ("comes around from the fairy, arms lowered", "looks directly at Yoonsu",
                 "lifts a separate small greeting to Yoonsu", "waves toward Yoonsu",
                 "finishes the small wave", "lowers his hand and starts looking toward the school"),
    "school": ("settles upright toward the doorway", "looks into the hall to his right",
               "brings his hand to the leather strap", "settles his hand against the strap",
               "lowers his hand and looks toward the distant fairy",
               "eyes level into the hall and both boots planted, ready to step"),
}

# Mouth landmarks in the extracted 320x512 cells exposed during the selected dialogue.
MOUTHS = {
    14: (192, 146),
    15: (196, 147),
    21: (165, 162),
    29: (167, 166),
}


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def body_scale(frames):
    return HEIGHT / np.median([image.getchannel("A").getbbox()[3] - image.getchannel("A").getbbox()[1]
                              for image in frames])


def fit(image, scale):
    art = image.resize(tuple(round(dim * scale) for dim in image.size), Image.Resampling.LANCZOS)
    rows, columns = np.nonzero(np.asarray(art.getchannel("A")) >= 180)
    floor_band = rows >= rows.max() - round(art.height * .055)
    support_columns = columns[floor_band]
    root_x = round((np.quantile(support_columns, .08) + np.quantile(support_columns, .92)) / 2)
    root_y = round(np.quantile(rows[floor_band], .97)) - 2
    offset = (FLOOR[0] - root_x, FLOOR[1] - root_y)
    canvas = Image.new("RGBA", SIZE)
    canvas.alpha_composite(art, offset)
    return canvas, offset


def frames_for(state):
    return [Image.open(RUN / "frames" / state / f"frame-{cell}.png").convert("RGBA") for cell in range(6)]


def final_pose():
    frames = frames_for("school")
    art, _ = fit(frames[-1], body_scale(frames))
    path = OUT / "art/cels" / ACTOR / "39.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    art.save(path, compress_level=4)


def save(target, image, name, mouth_box=None):
    path = target / f"{name}.png"
    image.save(path, compress_level=4)
    row = {"file": f"cels/{ACTOR}/{path.name}", "size": list(image.size),
           "anchors": {"stage": list(FLOOR)}, "sha256": ENDING["digest"](path)}
    if mouth_box is not None:
        row["mouth_box"] = list(mouth_box)
    return row


def register_mouths(target, image, index, mouth):
    variants, bounds = ENDING["speech_variants"](image, *mouth)
    return {"mouth_box": list(bounds),
            "viseme_cels": {key: save(target, drawing, f"{index:02}-{key}", bounds)
                            for key, drawing in variants.items()}}


def register():
    target = OUT / "art/cels" / ACTOR
    target.mkdir(parents=True, exist_ok=True)
    original = read(BASE / f"art/cels/{ACTOR}/registration.json")
    assert len(original["poses"]) == 10 and original["reference_height"] == HEIGHT
    assert len(ACTIONS) * 6 == 30
    source = original["source"] | {
        "farewell_shared_style_anchor_sha256": ENDING["digest"](RUN / "base-source.png"),
        "farewell_preparation": "Sprite-gen prepared GPT rows, generated in-session, extracted by components",
    }
    # C42 and C43 photograph the exact same registered open drawing at the seam.
    core = ROOT.parent / "core/human-source"
    continuity_path = core / "open.png"
    continuity = Image.open(continuity_path).convert("RGBA")
    assert continuity.size == SIZE
    shutil.copyfile(continuity_path, target / "00.png")
    original["poses"][0].update(
        sha256=ENDING["digest"](continuity_path),
        action="exact open drawing from the end of C42",
        **register_mouths(target, continuity, 0, read(core / "registration.json")["anchors"]["mouth"]),
    )
    source["farewell_c42_continuity_sha256"] = ENDING["digest"](continuity_path)
    for state, actions in ACTIONS.items():
        frames = frames_for(state)
        scale = body_scale(frames)
        source[f"farewell_{state}_raw_sha256"] = ENDING["digest"](RUN / "raw" / f"{state}.png")
        for cell, (frame, action) in enumerate(zip(frames, actions, strict=True)):
            index = len(original["poses"])
            im, offset = fit(frame, scale)
            row = save(target, im, f"{index:02}")
            row.update(index=index, action=action)
            if point := MOUTHS.get(index):
                mouth = [round(coord * scale) + delta for coord, delta in zip(point, offset, strict=True)]
                row.update(register_mouths(target, im, index, mouth))
            original["poses"].append(row)
    original["source"] = source
    write(target / "registration.json", original)


def lead(frame, total):
    return ENDING["fraction"](frame, total)


def child(index, *, during=None, span=None, speech=False):
    row = ENDING["hold"]("child", ACTOR, ENDING["REST"], 236, index)
    if during is not None:
        row["during"] = during
    if span is not None:
        row["span"] = span
    if speech:
        row["mouth"] = {"speaker": ENDING["ACTOR"]}
    return row


def lead_sequence(indices, boundaries, total, speaking=()):
    markers = [lead(value, total) if isinstance(value, int) else value for value in boundaries]
    return [child(index, during=[start, end], speech=index in speaking)
            for index, (start, end) in zip(indices, zip(markers, markers[1:]), strict=True)]


def layout():
    baseline = read(BASE / "layout-ending.json")
    children = {}
    response = ENDING["act"]("child", ACTOR, ENDING["REST"], 236, 12, 14, [5, 8, 8],
                             span=["after:S12-U034", "before:S12-U035"])
    response.update(motion="between", after_dialogue_id="S12-U034")
    gratitude = ENDING["act"]("child", ACTOR, ENDING["REST"], 236, 14, 15, [18, 35],
                              span=["before:S12-U035", "end"], mouth={"speaker": ENDING["ACTOR"]})
    children[43] = [
        child(0, during=[0, lead(8, 36)]),
        child(10, during=[lead(8, 36), lead(20, 36)]),
        child(11, span=[f"lead-point:{20/36}", "after:S12-U034"]),
        response, gratitude,
    ]
    children[44] = lead_sequence([15, 16, 17, 18, 19, 20, 21],
                                 [0, 10, 19, 27, 35, 46, 57, 1.0], 60, speaking=(21,))
    children[45] = lead_sequence([21, 18, 17, 16, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 29],
                                  [0, 7, 12, 17, 23, 31, 43, 57, 69, 81, 94, 109, 136, 145, 153, 162, 1.0],
                                  168, speaking=(29,))
    children[46] = lead_sequence([29, 33, 34, 35], [0, 10, 24, 46, 1.0], 84)
    children[47] = lead_sequence([35, 14, 37], [0, 12, 24, 1.0], 24)
    children[48] = [
        child(37, during=[0, lead(8, 36)]),
        child(14, during=[lead(8, 36), lead(15, 36)]),
        child(35, span=[f"lead-point:{15/36}", "before:S12-U042"]),
        child(38, span=["before:S12-U042", "after:S12-U042"]),
        child(39, span=["after:S12-U042", "end"]),
    ]

    future = deepcopy(baseline[6:])
    for shot in baseline[:6]:
        cut = int(shot["id"][-2:])
        shot["layout"] = [layer for layer in shot["layout"] if layer["track"] != "child"] + children[cut]
    assert baseline[6:] == future
    write(OUT / "layout-ending.json", baseline)


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--final-pose", action="store_true")
    args = parser.parse_args()
    if args.final_pose:
        final_pose()
    else:
        register()
        layout()


if __name__ == "__main__":
    main()
