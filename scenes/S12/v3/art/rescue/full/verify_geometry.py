#!/usr/bin/env python3
"""Check the raster restoration seam and the authored side-path/support events."""
import json
from math import dist
from pathlib import Path

import numpy as np
from PIL import Image, ImageChops

from build import (
    CRICKET,
    GEP,
    LEAN,
    LIFT,
    PIN,
    REAR_PIXEL,
    REAR_SUPPORT,
    REST,
    SIDE_EXIT,
    STAGE,
    TRAPPED,
    figure,
    level_data,
    location,
)

PROOF = Path("/workspace/scratch/s12-full/rescue-proof")


def whole(name, index):
    row = level_data(name)["poses"][index]
    original = Image.open(STAGE / row["file"]).convert("RGBA")
    canvas = Image.new("RGBA", (1280, 720))
    canvas.alpha_composite(original, tuple(-coordinate for coordinate in row["anchors"]["stage"]))
    return canvas


def exact(a, b):
    return not ImageChops.difference(a, b).getbbox(alpha_only=False)


seam = {
    "standing_original_sign": exact(whole("S12X-sign-14", -1),
                                      figure("S12R-school-sign", 0, (413, 597), 84)),
    "planted_pin": exact(whole("S12X-pin-action-14", -1),
                         figure("S12R-pin-listen-left", 0, PIN, 236)),
    "geppetto_home": exact(whole("S12X-gep-travel-14", -1),
                           figure("S12R-gep-talk", 0, GEP, 315, True)),
    "cricket_home": exact(whole("S12X-cricket-clear", -1),
                          figure("S12R-cricket-talk", 0, CRICKET, 84, True)),
}
if not all(seam.values()):
    raise ValueError(f"Last rescue frame did not restore the C15 character and board identities: {seam}")
entrance_box = (622, 276, 820, 599)
with Image.open(STAGE/"S12R-school.png") as old, Image.open(STAGE/"S12X-school-recess.png") as new:
    door_unchanged = exact(old.convert("RGBA").crop(entrance_box), new.convert("RGBA").crop(entrance_box))
new_sign = whole("S12X-sign-06",0)
old_sign = figure("S12O-board-gust",10,(413,597),84)
incoming_board = new_sign.getbbox() == old_sign.getbbox()
a,b = (np.asarray(cel,dtype=np.int16) for cel in (new_sign,old_sign))
solid = (a[:,:,3] >= 240) & (b[:,:,3] >= 240)
board_color_difference = float(np.abs(a[:,:,:3]-b[:,:,:3])[solid].mean())
if not (door_unchanged and incoming_board and board_color_difference < .05):
    raise ValueError("The new stonework crossed the actual school door or changed the standing sign.")

lift = level_data("S12X-sign-13")["poses"]
drift = max(dist(location(REAR_PIXEL, row["angle"], row["axis"]), REAR_SUPPORT) for row in lift)
height_range = lift[0]["axis"][1] - lift[-1]["axis"][1]
if drift > .00001 or abs(lift[0]["angle"] - LEAN) > .00001 or abs(lift[-1]["angle"] - LIFT) > .00001:
    raise ValueError("The sign left its support during the lift.")
if height_range < 10:
    raise ValueError("The free sign point did not visibly rise.")

approach = level_data("S12X-cricket-entry")["poses"]
settled = next(row["frame"] for row in approach if row["visible_foot_root"] == list(TRAPPED))
first_tilt = next(row["frame"] for row in level_data("S12X-sign-06")["poses"] if row["angle"] > 0)
escape = level_data("S12X-cricket-escape")["poses"]
first_exit = next(row["frame"] for row in escape if dist(row["visible_foot_root"],TRAPPED) > .01)
arrived = next(row["frame"] for row in escape if row["visible_foot_root"] == list(SIDE_EXIT))
if settled >= first_tilt or not 68 < first_exit < arrived:
    raise ValueError("Cricket moved through the sign's action before clearance.")
if any(row["visible_foot_root"][0] >= 422 and row["visible_foot_root"][1] < 593
       for row in escape if row["walk"]):
    raise ValueError("Cricket's visible foot path crossed the outer stone boundary.")

for number in (12, 13, 14):
    for row in level_data(f"S12X-pin-action-{number:02d}")["poses"]:
        if "contacts" in row and len(row["contacts"]) != 2:
            raise ValueError("Every board manipulation drawing needs two registered contact points.")

output = {"exact_c14_to_c15_body_pixels": seam, "c05_to_c06_upright_sign_bounds_matched":incoming_board,
          "c05_to_c06_solid_sign_mean_rgb_channel_delta":board_color_difference,
          "existing_door_region_pixels_matched":door_unchanged,
          "raster_rear_pivot_drift_pixels": drift, "free_end_lift_pixels": height_range,
          "cricket_entry_pose_frame": settled, "board_first_tilt_pose_frame": first_tilt,
          "open_sign_hold_begins_cut13_frame": 68, "cricket_first_exit_pose_frame": first_exit,
          "cricket_reaches_safe_pose_frame": arrived,
          "proof_limit": "2D registration, authored screen-space bounds and timing; not a volume or force simulation"}
(PROOF / "geometry.json").write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
print(json.dumps(output, ensure_ascii=False))
