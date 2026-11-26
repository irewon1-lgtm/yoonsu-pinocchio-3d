#!/usr/bin/env python3
"""Rephotograph the school rescue with the original school and character paintings."""
from __future__ import annotations

from functools import lru_cache
from hashlib import file_digest
import json
from math import cos, radians, sin
from pathlib import Path
import runpy

from PIL import Image, ImageChops, ImageDraw, ImageFilter

OUTPUT = Path(__file__).resolve().parent
PROJECT = Path("/workspace/yoonsu-pinocchio-3d")
V3 = PROJECT / "scenes/S12/v3"
SOURCE_ART = V3 / "build/art"
SOURCE = runpy.run_path(str(V3 / "art/rescue/full/build.py"))
BODY = SOURCE["BODY"]
SIZE = SOURCE["SIZE"]
PIN, BESIDE, TRAPPED = (SOURCE[key] for key in ("PIN", "BESIDE", "TRAPPED"))
REST, LEAN = SOURCE["REST"], SOURCE["LEAN"]
SIDE_EXIT = (350, 670)
REAR = (342.0, 532.0)
CONTACTS = ((382.0, 540.0), (411.0, 547.0))
ORIGINAL_CROPS = dict(SOURCE["CROPS"])
ORIGINAL_CROPS.update({6: (283, 272, 708), 12: (273, 297, 664), 13: (265, 382, 550),
                       14: (254, 274, 788)})
progress, blend = SOURCE["progress"], SOURCE["blend"]
sample_frames, exposure = SOURCE["sample_frames"], SOURCE["exposure"]
PREFIX = "S12Q-"
STAGE = OUTPUT / "art"
class RescueDrawings(SOURCE["Drawings"]):
    def __init__(self, name):
        self.folder = STAGE / "cels" / (PREFIX + name)
        self.folder.mkdir(parents=True, exist_ok=True)
        self.rows = []

    def save(self, image, filename):
        bounds = image.getchannel("A").getbbox()
        x, y, right, bottom = bounds
        drawing = image.crop((x - 4, y - 4, right + 4, bottom + 4))
        path = self.folder / (filename + ".png")
        drawing.save(path, compress_level=4)
        with path.open("rb") as stream:
            digest = file_digest(stream, "sha256").hexdigest()
        return {"file": str(path.relative_to(STAGE)), "size": list(drawing.size),
                "anchors": {"stage": [4 - x, 4 - y]}, "world_bounds": bounds, "sha256": digest}


def empty(size=SIZE):
    return Image.new("RGBA", size)


def rot(point, degrees):
    x, y = (point[0] - REAR[0], point[1] - REAR[1])
    a = radians(degrees)
    return (REAR[0] + cos(a) * x - sin(a) * y, REAR[1] + sin(a) * x + cos(a) * y)


def leaning_source(point):
    """Recover the sign painting coordinate for the screen-space finger anchor."""
    x, y = SOURCE["location"]((0, 0), LEAN, REST)
    a, d = SOURCE["location"]((1, 0), LEAN, REST)
    b, e = SOURCE["location"]((0, 1), LEAN, REST)
    a, b, d, e = a - x, b - x, d - y, e - y
    rx, ry = point[0] - x, point[1] - y
    den = a * e - b * d
    return ((e * rx - b * ry) / den, (-d * rx + a * ry) / den)


def sign_pose(cut, frame):
    angle = 0
    phase = LEAN
    if cut == 13:
        angle = -15 * progress(frame, 12, 71)
    if cut == 14:
        angle = -15 * (1 - progress(frame, 15, 69))
        phase = LEAN * (1 - progress(frame, 71, 115))
    contact = tuple(rot(SOURCE["location"](leaning_source(p), phase, REST), angle) for p in CONTACTS)
    return phase, angle, contact


@lru_cache(maxsize=85)
def sign_image(phase, angle):
    if phase == 0 and angle == 0:
        return SOURCE["sign_board"](0, REST)
    mast, pedestal = SOURCE["sign_parts"]()
    x, y = rot(SOURCE["location"]((0, 0), phase, REST), angle)
    a, d = rot(SOURCE["location"]((1, 0), phase, REST), angle)
    b, e = rot(SOURCE["location"]((0, 1), phase, REST), angle)
    a, b, d, e = a - x, b - x, d - y, e - y
    det = a * e - b * d
    a, b, d, e = e / det, -b / det, -d / det, a / det
    left, top, right, bottom = (310, 485, 478, 612)
    width, height = right - left, bottom - top
    scale = 4
    sampled = mast.transform(
        (width * scale, height * scale),
        Image.Transform.AFFINE,
        (a / scale, b / scale, a * (left - x) + b * (top - y),
         d / scale, e / scale, d * (left - x) + e * (top - y)),
        Image.Resampling.BICUBIC,
    )
    result = SOURCE["transform_sign"](pedestal, 0, REST)
    result.alpha_composite(sampled.resize((width, height), Image.Resampling.LANCZOS), (left, top))
    return result


@lru_cache(maxsize=None)
def borrow(level, f):
    data = SOURCE["level_data"](level, SOURCE_ART)
    poses = data["poses"]
    pose = next((row for row in poses if row.get("frame", 0) == f), None)
    if pose is None:
        pose = max((row for row in poses if row["frame"] < f), key=lambda row: row["frame"])
    image = SOURCE["source_png"](SOURCE_ART / pose["file"])
    art = empty()
    art.alpha_composite(image, tuple(-x for x in pose["anchors"]["stage"]))
    return art


# The knee-rest painting supplies the two natural arms, textured clothing and boots.
DONOR, DONOR_ANCHOR, _ = SOURCE["source_pose"]("S12R-pin-low-palm", 3, art=SOURCE_ART)
MARGIN = 64
FAR_SHOULDER = (51, 125)
FAR_ELBOW = (43, 136)
FAR_WRIST = (31, 144)
FAR_TIP = (21, 152)
NEAR_SHOULDER = (95, 119)
NEAR_ELBOW = (94, 136)
NEAR_WRIST = (76, 147)
NEAR_TIP = (60, 151)


def pad(point):
    return tuple(coordinate + MARGIN for coordinate in point)


def select(image, points, radius=.45):
    return BODY["isolated"](image, [pad(p) for p in points], radius)


def mapped(image, first, last, start, end, cross=1):
    return BODY["deform"](image, pad(first), pad(last), pad(start), pad(end), cross)


def apply_knee_texture(canvas, sample, area):
    # This texture is the character's existing lower leg. The feathered bottom
    # meets the unchanged painted calf and the top overlaps the cutaway denim.
    x, y, right, bottom = area
    size = (right - x, bottom - y)
    donor = DONOR.crop(sample).resize(size, Image.Resampling.BICUBIC)
    alpha = Image.new("L", size)
    outline = ImageDraw.Draw(alpha)
    outline.rounded_rectangle((0, 0, size[0]-1, size[1]-1), radius=10, fill=255)
    opacity = alpha.filter(ImageFilter.GaussianBlur(.7))
    donor.putalpha(ImageChops.multiply(donor.getchannel("A"), opacity))
    canvas.alpha_composite(donor, pad((x, y)))


@lru_cache(maxsize=1)
def kid_painting():
    sheet = empty((DONOR.width + 2 * MARGIN, DONOR.height + 2 * MARGIN))
    sheet.alpha_composite(DONOR, (MARGIN, MARGIN))
    far = [(39, 123), (58, 124), (58, 131), (55, 137), (49, 142),
           (46, 147), (44, 154), (32, 162), (10, 160), (10, 137), (29, 131), (34, 123)]
    near = [(86, 118), (102, 114), (107, 124), (107, 134), (102, 140),
            (91, 146), (83, 150), (78, 153), (72, 157), (68, 160),
            (57, 158), (54, 154), (55, 147), (60, 142), (66, 140),
            (76, 139), (83, 135), (88, 130)]
    bare = BODY["erase"](sheet, [pad(p) for p in far], .40)
    bare = BODY["erase"](bare, [pad(p) for p in near], .40)

    # Recover the covered denim and knees with pixels from the same approved cel.
    denim = select(sheet, [(58,129),(73,130),(80,133),(73,139),(62,141),
                           (57,146),(53,146),(52,142),(54,134)], 1.0)
    bare.alpha_composite(mapped(denim, (56, 137), (75, 138), (57, 148), (93, 141), 1.08))
    denim_edge = select(sheet, [(86,150),(106,143),(107,150),(105,159),
                                (97,164),(86,166),(80,164),(81,157)], .8)
    bare.alpha_composite(mapped(denim_edge, (85,157), (106,148), (81,149), (105,136), 1.02))
    kneecaps = empty(sheet.size)
    apply_knee_texture(kneecaps, (28, 163, 42, 178), (17, 146, 47, 172))
    apply_knee_texture(kneecaps, (62, 161, 77, 177), (55, 146, 85, 173))
    kneecaps.alpha_composite(bare)
    bare = kneecaps

    # The two sleeves hide the underside of the shoulder seams.
    cuff_far = select(sheet, [(43,108),(51,107),(55,112),(58,118),(57,126),
                              (50,125),(40,121)], .6)
    cuff_near = select(sheet, [(86,104),(96,101),(103,104),(108,111),(107,117),
                               (98,116),(91,118),(83,124),(81,120)], .6)
    upper_far = select(sheet, [(43,121),(56,123),(57,132),(52,138),(45,139),
                               (39,141),(36,137),(39,131)], .65)
    lower_far = select(sheet, [(42,129),(53,132),(50,138),(43,141),(42,147),
                               (39,152),(33,149),(27,147),(26,142),(32,137)], .75)
    hand_far = select(sheet, [(28,138),(38,138),(42,142),(41,151),(36,152),(33,150),
                              (31,153),(25,157),(18,158),(16,154),(17,147),(21,141)], .46)
    upper_near = select(sheet, [(88,116),(101,114),(106,122),(106,132),(103,136),
                                (95,142),(89,143),(83,137),(88,129)], .65)
    lower_near = select(sheet, [(94,130),(105,132),(101,140),(96,143),(88,148),
                                (79,153),(73,152),(70,143),(80,138),(86,135)], .7)
    hand_near = select(sheet, [(75,140),(82,142),(83,147),(77,153),(70,159),
                               (64,159),(58,157),(55,154),(56,148),(61,144),(67,141)], .50)
    return bare, (upper_far, lower_far, hand_far, cuff_far), (upper_near, lower_near, hand_near, cuff_near)


def manipulating_child(handles, effort):
    if effort == 0:
        result = empty()
        result.alpha_composite(DONOR, child_origin())
        return result
    bare, far, near = kid_painting()
    body = bare.copy()
    origin = child_origin()
    for index, (donor, shoulder, elbow, wrist, tip, elbow_offset, wrist_offset) in enumerate((
            (far, FAR_SHOULDER, FAR_ELBOW, FAR_WRIST, FAR_TIP, (25, 7), (8, 2)),
            (near, NEAR_SHOULDER, NEAR_ELBOW, NEAR_WRIST, NEAR_TIP, (39, 12), (11, 3)))):
        target = tuple(p - q for p, q in zip(handles[index], origin))
        elbow_target = tuple(a + b for a, b in zip(target, elbow_offset))
        wrist_target = tuple(a + b for a, b in zip(target, wrist_offset))
        if index == 1:
            elbow_target = (min(92, elbow_target[0]), min(143, elbow_target[1]))
        bend = blend(elbow, elbow_target, effort)
        hinge = blend(wrist, wrist_target, effort)
        touch = blend(tip, target, effort)
        upper, lower, fingers, cuff = donor
        body.alpha_composite(mapped(upper, shoulder, elbow, shoulder, bend, .96))
        body.alpha_composite(mapped(lower, elbow, wrist, bend, hinge, .94))
        body.alpha_composite(mapped(fingers, wrist, tip, hinge, touch, .98))
        body.alpha_composite(cuff)

    result = empty()
    result.alpha_composite(body, (origin[0] - MARGIN, origin[1] - MARGIN))
    return result


def child_origin():
    return tuple(-coordinate + goal - original for coordinate, goal, original
                 in zip(DONOR_ANCHOR, BESIDE, PIN))


@lru_cache(maxsize=9)
def contact_shadow(opacity):
    marks = empty()
    paint = ImageDraw.Draw(marks)
    paint.ellipse((384, 620, 426, 631), fill=(109, 62, 28, opacity))
    paint.ellipse((424, 620, 473, 632), fill=(109, 62, 28, opacity))
    return marks.filter(ImageFilter.GaussianBlur(3.3))


def cricket_at(point, height, frame=0, moving=False, right=False):
    if not moving:
        return SOURCE["figure"]("S12R-cricket-talk", 0, point, height, right, art=SOURCE_ART)
    poses = SOURCE["level_data"]("S12R-cricket-walk", SOURCE_ART)
    pose = poses["poses"][frame % len(poses["poses"])]
    image = SOURCE["source_png"](SOURCE_ART / pose["file"])
    return BODY["blit"](image, SOURCE["rounded"](point), round(height), poses["reference_height"],
                        pose["anchors"]["motion_base"], right)


def cricket_path(cut, frame):
    if cut == 13:
        if frame <= 84:
            return TRAPPED, 72, False, True
        knots = ((84, TRAPPED), (105, (356, 583)), (126, (352, 617)),
                 (148, (322, 644)), (165, (330, 660)), (191, SIDE_EXIT), (192, SIDE_EXIT))
        height = 72 + 2 * progress(frame, 148, 192)
        facing_right = frame >= 148
    else:
        knots = ((0, SIDE_EXIT), (21, (379, 676)), (45, (431, 675)), (71, (476, 668)),
                 (105, SOURCE["CRICKET"]), (216, SOURCE["CRICKET"]))
        height = 74 + 10 * progress(frame, 25, 105)
        facing_right = True
    for (a, first), (b, end) in zip(knots, knots[1:]):
        if frame < b:
            # Linear through the waypoints keeps her stride moving around the jamb.
            pace = (frame - a) / (b - a)
            return blend(first, end, pace), height, first != end, facing_right
    return knots[-1][1], height, False, facing_right


def make_poses(cut, level, render, markers=()):
    total = {12: 192, 13: 192, 14: 216}[cut]
    frames = sample_frames(total, markers)
    drawings = RescueDrawings(level)
    saved = {}
    for frame in frames:
        artwork, metadata = render(frame)
        thumbnail = artwork.crop(artwork.getchannel("A").getbbox())
        key = (artwork.getchannel("A").getbbox(), thumbnail.tobytes())
        if key in saved:
            drawings.rows.append(saved[key] | {"index": len(drawings.rows), "frame": frame} | metadata)
        else:
            index = drawings.add(artwork, frame=frame, **metadata)
            saved[key] = drawings.rows[index]
    drawings.finish()
    return frames, total


def pin_drawing(cut, frame):
    if (cut == 12 and frame < 118) or (cut == 14 and frame >= 147):
        return borrow(f"S12X-pin-action-{cut:02}", frame), {}
    if cut == 12:
        effort = progress(frame, 128, 164)
    elif cut == 14:
        effort = 1 - progress(frame, 123, 143)
    else:
        effort = 1
    _, _, handles = sign_pose(cut, frame)
    return manipulating_child(handles, effort), {
        "grip": effort,
        "handles": list(handles),
        "sole_contacts": [[405, 622], [447, 623]],
    }


def grip_shadow(cut, frame):
    if cut == 12:
        amount = .15 + .85 * progress(frame, 78, 97)
    elif cut == 14:
        amount = 1 - .85 * progress(frame, 143, 154)
    else:
        amount = 1
    return contact_shadow(round(67 * amount)), {}


def board_drawing(cut, frame):
    phase, angle, handles = sign_pose(cut, frame)
    return sign_image(phase, angle), {"lean": phase, "lift_rotation": angle,
                                     "handles": list(handles), "left_pivot": REAR}


def insect_drawing(cut, frame):
    point, height, moving, right = cricket_path(cut, frame)
    return cricket_at(point, height, frame // 5, moving, right), {
        "visible_foot_root": list(point), "moving": moving, "right": right
    }


def layer(track, name, timing, first=0, end=None):
    frames, length = timing
    last = length if end is None else end
    start, stop = frames.index(first), len(frames) if last == length else frames.index(last)
    return {"track": track, "level": PREFIX + name, "root": [0, 0], "height": 720,
            "anchor": "stage", "first_cel": start, "last_cel": stop - 1, "motion": "story",
            "flip": False, "exposure_frames": exposure(frames, length)[start:stop],
            "start": first / length, "end": last / length}


def sign_incident():
    source = SOURCE["level_data"]("S12X-sign-06", SOURCE_ART)
    drawings = RescueDrawings("sign-06")
    for row in source["poses"]:
        frame = row["frame"]
        phase, _ = SOURCE["hold_angle"](6, frame)
        drawings.add(sign_image(phase, 0), frame=frame, lean=phase)
    drawings.finish()
    settled = RescueDrawings("sign-settled")
    settled.add(sign_image(LEAN, 0), lean=LEAN)
    settled.finish()


def main():
    base_layout = json.loads((V3 / "build/layout-rescue-full.json").read_text())
    sign_incident()
    for number, shot in zip(range(6, 15), base_layout, strict=True):
        original = shot["layout"]
        for item in original:
            if item["level"] in ("S12X-sign-06", "S12X-sign-settled"):
                item["level"] = item["level"].replace("S12X-", PREFIX, 1)
        crop = ",".join(map(str, ORIGINAL_CROPS[number]))
        shot["plate"] = f"S12X-school-recess.png@{crop}"
        if number == 6:
            leaf = next(item for item in original if item["track"] == "gust")
            k = original.index(leaf)
            original.insert(k + 1, leaf | {"track": "gust-second", "root": [535, 575],
                           "height": 9, "start": .095, "end": .39, "drift_x": -211, "drift_y": -22})
        if number < 12:
            continue
        pin = make_poses(number, f"pin-{number}", lambda f: pin_drawing(number, f),
                         (118, 128, 164) if number == 12 else ((12, 71) if number == 13 else (69, 71, 115, 123, 143, 146, 147)))
        shadow = make_poses(number, f"paving-{number}", lambda f: grip_shadow(number, f))
        replacement = []
        is_shadow_added = False
        for item in original:
            if item["track"] == "pin":
                replacement.append(layer("shadow", f"paving-{number}", shadow))
                is_shadow_added = True
                replacement.append(layer("pin", f"pin-{number}", pin))
            elif item["track"] == "sign" and number >= 13:
                timing = make_poses(number, f"sign-{number}", lambda f: board_drawing(number, f),
                                    (12, 71) if number == 13 else (15, 69, 71, 115))
                replacement.append(layer("sign", f"sign-{number}", timing))
            elif item["track"] == "cricket" and number == 13 and item["start"] == 0:
                insect = make_poses(13, "cricket-13", lambda f: insect_drawing(13, f), (84, 105, 114, 126, 148, 165))
                replacement.append(layer("cricket", "cricket-13", insect, 0, 114))
            elif item["track"] == "cricket" and number == 13:
                replacement.append(layer("cricket", "cricket-13", insect, 114))
            elif item["track"] == "cricket" and number == 14:
                insect = make_poses(14, "cricket-14", lambda f: insect_drawing(14, f), (21, 45, 71, 105))
                replacement.append(layer("cricket", "cricket-14", insect))
            else:
                replacement.append(item)
        assert is_shadow_added
        shot["layout"] = replacement
    (OUTPUT / "layout-rescue-full.json").write_text(json.dumps(base_layout, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
