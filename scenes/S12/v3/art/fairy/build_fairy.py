"""Photograph S12's schoolyard fairy passage with the existing whole-cel renderer."""
from __future__ import annotations

import argparse
from copy import deepcopy
from hashlib import file_digest
import json
import math
import os
from pathlib import Path
import shutil

from PIL import Image, ImageChops, ImageDraw, ImageFilter

V3 = Path(__file__).resolve().parents[2]
SCENES = V3.parents[1]
BUILD = V3 / "build"
ART = BUILD / "art"
S11 = SCENES / "S11/v2/build/art"
S10 = SCENES / "S10/production/art"
AUTHORITY = Path("/workspace/scratch/s12-v3/intake/S12_FINAL_PRODUCTION_READY_V3/source/episodes/S12")
FPS = 24
PIN = (561, 643)
GEP = (667, 629)
CRICKET = (510, 649)
FAIRY = (831, 442)
PLATE = "S11L-school-open.png"
PIN_SPEAKER = "피노키오"
GEP_SPEAKER = "제페토"
FAIRY_SPEAKER = "파란 요정"


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path, data):
    temp = path.with_suffix(".fairy-pending")
    temp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(path)


def sha(path):
    with path.open("rb") as stream:
        return file_digest(stream, "sha256").hexdigest()


def link(source, target):
    try:
        os.link(source, target)
    except FileExistsError:
        if not source.samefile(target) and sha(source) != sha(target):
            raise ValueError(f"Conflicting approved source for {target}")
    except OSError:
        shutil.copyfile(source, target)


def register_stock(label, art, registry, indices=None):
    """Keep the approved drawing bytes and remap paths into the S04 artwork registry."""
    canon = read(registry)
    level = f"S12F-{label}"
    out = ART / "cels" / level
    out.mkdir(parents=True, exist_ok=True)
    poses = canon["poses"]
    if indices is not None:
        if canon.get("visemes"):
            raise ValueError("Global viseme registrations require their original indices")
        poses = [poses[i] for i in indices]
    takes = []
    for i, pose in enumerate(poses):
        row = deepcopy(pose)
        row["index"] = i
        for variant in (row, *row.get("viseme_cels", {}).values()):
            old = art / variant["file"]
            target = out / old.name
            link(old, target)
            variant["file"] = target.relative_to(ART).as_posix()
        takes.append(row)
    result = canon | {"poses": takes, "origin_registry": str(registry.relative_to(SCENES)),
                      "origin_registry_sha256": sha(registry)}
    write(out / "registration.json", result)
    return result


def pad(source, pixels):
    canvas = Image.new("RGBA", (source.width + 2*pixels, source.height + 2*pixels))
    canvas.alpha_composite(source, (pixels, pixels))
    return canvas


def isolated(image, vertices, spread=0.65):
    mask = Image.new("L", image.size)
    ImageDraw.Draw(mask).polygon(vertices, fill=255)
    mask = mask.filter(ImageFilter.GaussianBlur(spread))
    region = image.copy()
    region.putalpha(ImageChops.multiply(image.getchannel("A"), mask))
    return region, mask


def roll_head(source, boundary, pivot, degrees):
    """A small turn above the neck leaves the clothes, wrists and soles planted."""
    if degrees == 0:
        return source.copy()
    head, mask = isolated(source, boundary)
    body = source.copy()
    body.paste((0, 0, 0, 0), mask=mask)
    head = head.rotate(degrees, Image.Resampling.BICUBIC, center=pivot)
    body.alpha_composite(head)
    return body


def fairy_arm(source, upper, wrist, free=0):
    """Give the Fairy two drawn joint arcs with the original fixed wand and grip."""
    pixels = 96
    source = pad(source, pixels)
    move = lambda p: (p[0]+pixels, p[1]+pixels)
    wrist_pin = move((62, 236))
    shoulder = move((136, 132))
    outline = [(130,115),(146,123),(152,142),(156,166),(155,176),(126,184),
               (119,192),(112,200),(101,208),(89,216),(79,224),(78,232),
               (73,240),(67,248),(55,256),(50,264),(44,272),(39,280),
               (34,288),(32,296),(34,319),(-3,322),(-4,290),(21,278),
               (31,252),(36,227),(48,213),(60,194),(80,183),(88,173),
               (102,158),(103,140),(112,128)]
    if upper or wrist:
        arm, mask = isolated(source, [move(p) for p in outline])
        hand, hand_mask = isolated(arm, [move(p) for p in [(-9,228),(79,224),(80,325),(-9,326)]])
        arm.paste((0,0,0,0), mask=hand_mask)
        arm.alpha_composite(hand.rotate(wrist, Image.Resampling.BICUBIC, center=wrist_pin))
        source.paste((0,0,0,0), mask=mask)
        source.alpha_composite(arm.rotate(upper, Image.Resampling.BICUBIC, center=shoulder))
    if free:
        far_arm, mask = isolated(source, [move(p) for p in [
            (183,117),(217,118),(221,156),(229,178),(236,194),(244,208),
            (253,218),(270,220),(302,221),(303,246),(279,251),(251,250),
            (240,244),(232,225),(215,207),(205,196),(199,185),(193,170),
            (188,154),(180,139)]])
        source.paste((0,0,0,0), mask=mask)
        source.alpha_composite(far_arm.rotate(free, Image.Resampling.BICUBIC, center=move((193,143))))
    return source


def pin_prepare(image, unfold):
    """Open the wooden arms from their existing hinges while preserving the bag and floor pins."""
    pixels = 82
    body = pad(image, pixels)
    if not unfold:
        return body
    move = lambda p: (p[0]+pixels, p[1]+pixels)
    wrist_far = [(201,235),(216,241),(232,265),(240,284),(246,315),(249,343),
                 (256,358),(263,375),(269,395),(261,419),(246,431),(226,431),
                 (212,423),(208,407),(212,395),(213,379),(212,366),(206,351),
                 (209,335),(212,317),(212,299),(206,285),(202,265)]
    wrist_near = [(83,272),(98,273),(111,277),(125,275),(138,262),(164,258),
                  (175,262),(178,280),(175,299),(164,309),(143,316),(117,325),
                  (94,325),(80,318),(75,304),(76,284)]
    near, near_mask = isolated(body, [move(p) for p in wrist_near])
    far, far_mask = isolated(body, [move(p) for p in wrist_far])
    body.paste((0,0,0,0), mask=ImageChops.lighter(near_mask,far_mask))
    restored = Image.new("RGBA",body.size)
    bag = image.crop((41,320,95,345)).resize((107,72),Image.Resampling.BICUBIC)
    restored.alpha_composite(bag,move((73,253)))
    denim = image.crop((120,331,171,375)).resize((86,70),Image.Resampling.BICUBIC)
    restored.alpha_composite(denim,move((108,255)))
    fill = ImageDraw.Draw(restored)
    fill.line([move((88,333)),move((159,254)),move((181,232))],fill=(117,68,31,255),width=15)
    fill.line([move((84,330)),move((159,248)),move((176,232))],fill=(177,113,52,255),width=3)
    repair_edge = near_mask.filter(ImageFilter.GaussianBlur(1.25))
    restored.putalpha(ImageChops.multiply(repair_edge,restored.getchannel("A")))
    body.alpha_composite(restored)
    body.alpha_composite(far.rotate(38*unfold,Image.Resampling.BICUBIC,center=move((209,263))))
    body.alpha_composite(near.rotate(-126*unfold,Image.Resampling.BICUBIC,center=move((87,295))))
    return body


def new_level(label, canon, originals, generators, pixels=0):
    """Create registered complete drawings and propagate each mouth drawing through the same pose."""
    out = ART / "cels" / f"S12F-{label}"
    out.mkdir(parents=True, exist_ok=True)
    tracks = []

    def expose(row, name, maker):
        with Image.open(ART / row["file"]) as handle:
            drawing = maker(handle.convert("RGBA"))
        path = out / (name + ".png")
        drawing.save(path, optimize=False)
        box = row.get("mouth_box")
        anchors = {name: [x+pixels, y+pixels] for name, (x, y) in row.get("anchors", {}).items()}
        registration = {"file": path.relative_to(ART).as_posix(), "size": list(drawing.size),
                        "anchors": anchors, "sha256": sha(path)}
        if "sole" in row:
            registration["sole"] = [v+pixels for v in row["sole"]]
        if box:
            registration["mouth_box"] = [v+pixels for v in box]
        return registration

    for i, (old, maker) in enumerate(zip(originals, generators, strict=True)):
        row = canon["poses"][old]
        output = expose(row, f"{i:02}", maker) | {"index": i}
        if "viseme_cels" in row:
            output["viseme_cels"] = {name: expose(source, f"{i:02}-{name}", maker)
                                     for name, source in row["viseme_cels"].items()}
        tracks.append(output)
    write(out / "registration.json", {"reference_height": canon["reference_height"], "poses": tracks,
                                      "source": canon["origin_registry"],
                                      "source_sha256": canon["origin_registry_sha256"]})


def spark_field():
    """An optical pass, with individually timed ascending particles over approved drawings."""
    out = ART / "cels" / "S12F-sparks"
    out.mkdir(parents=True, exist_ok=True)
    particles = [(0,592,1.6), (.02,565,1.4), (.06,606,2.0), (.11,552,1.2), (.19,580,2.5),
                 (.29,603,1.3), (.36,559,1.7), (.43,595,1.6), (.51,570,2.3), (.56,590,1.2),
                 (.63,608,1.7), (.73,550,1.4), (.80,573,2.0), (.88,602,1.5)]
    w, h = 118, 271
    frames = []
    for i in range(32):
        duration = i / 31
        aura = Image.new("RGBA", (w,h))
        ink = Image.new("RGBA", (w,h))
        blur_pen, pen = ImageDraw.Draw(aura), ImageDraw.Draw(ink)
        for birth, side, size in particles:
            local = (duration - birth * .74) / .63
            if not 0 <= local <= 1:
                continue
            x = side - 516 + 6 * math.sin(local * math.pi * 1.3 + birth*12)
            y = 259 - local * (169 + 36*birth)
            strength = max(.1, min(1, math.sin(math.pi*local)*1.3))
            rr = size*1.5
            blur_pen.ellipse((x-rr*2,y-rr*2,x+rr*2,y+rr*2), fill=(97,157,255,round(88*strength)))
            pen.polygon([(x,y-rr),(x+size*.44,y-size*.40),(x+rr,y),(x+size*.44,y+size*.40),
                         (x,y+rr),(x-size*.44,y+size*.40),(x-rr,y),(x-size*.44,y-size*.40)],
                        fill=(173,218,255,round(198*strength)))
        aura = aura.filter(ImageFilter.GaussianBlur(2.1))
        aura.alpha_composite(ink)
        path = out / f"{i:02}.png"
        aura.save(path, optimize=False)
        frames.append({"index": i, "file": path.relative_to(ART).as_posix(), "size": [w,h],
                       "anchors": {"stage":[0,0]}, "sha256": sha(path)})
    write(out / "registration.json", {"reference_height": h, "poses": frames})


def register_art():
    ART.mkdir(parents=True, exist_ok=True)
    link(S11/PLATE, ART/PLATE)
    primary = {
        "door":"school-door", "sign":"school-sign", "teacher":"teacher",
        "walk":"pin-walk-right", "listen":"pin-listen-right", "pin-talk":"pin-back-talk",
        "cricket":"cricket-talk", "cricket-walk":"cricket-walk", "cricket-acting":"cricket-guide",
        "gep-talk":"gep-talk", "gep-quiet":"gep-gentle",
    }
    stock = {name: register_stock(name,S11,S11/"cels"/f"S11L-{src}"/"registration.json")
             for name,src in primary.items()}
    fairy = register_stock("fairy", S10, S10/"fairy/fairy-s10-poses/registration.json")
    register_stock("reveal", S10, S10/"fairy/fairy-s10-reveal/registration.json", range(1,10))
    register_stock("glow", S10, S10/"props/fairy-arrival-glow/registration.json", range(1,17))
    register_stock("halo", S10, S10/"props/fairy-hug-light/registration.json", range(1,14))
    arc = [(0,0),(-1,-1),(-3,-1),(-5,-2),(-7,-3),(-10,-4),(-14,-5),
           (-17,-7),(-20,-8),(-23,-9),(-25,-10),(-27,-10),(-28,-11),(-29,-11),(-30,-11)]
    new_level("wand", fairy, [4]*len(arc),
              [lambda frame, a=a, b=b: fairy_arm(frame,a,b) for a,b in arc], 96)
    palm = [0, 3, 7, 12, 16, 19, 18, 16]
    new_level("palm", fairy, [4]*len(palm),
              [lambda frame, degree=d: fairy_arm(frame,0,0,degree) for d in palm], 96)
    p = stock["pin-talk"]
    # Closed eye pose 07 is a fully approved distinct body drawing.
    new_level("pin-ready", p, [0,0,0,7,7,7,7,7,7,7],
              [lambda frame, a=a: pin_prepare(frame,a) for a in (0,.08,.18,.28,.38,.55,.72,.88,.97,1)],82)
    boundary = [(0,0),(289,0),(289,199),(184,213),(169,224),(119,219),(84,208),(0,174)]
    def head(degree):
        return lambda frame: roll_head(frame,boundary,(141,205),degree)
    new_level("pin-up", p, [0]*7, [head(d) for d in (0,2,5,8,11,13,12)])
    new_level("pin-nod", p, [0,0,0,7,7,0,0,0,0],
              [head(d) for d in (12,8,4,0,-4,-5,0,7,12)])
    # Align the tail of the previous branch to a full, maintained leg register.
    gep = stock["gep-quiet"]
    ghead = [(0,0),(188,0),(188,143),(133,145),(115,152),(74,146),(0,165)]
    new_level("gep-up", gep, [0]*6,
              [lambda f,d=d: roll_head(f,ghead,(89,147),d) for d in (0,2,5,8,10,11)])
    spark_field()


def frameclock(design, edit):
    plans = {row["id"]: row for row in design["shots"]}
    actual = {row["id"]: row for row in edit["cuts"]} if edit else {}
    for i in range(20, 30):
        cut = f"S12-C{i:02}"
        plan = plans[cut]
        if cut in actual:
            row = actual[cut]
            if row.get("audio") is None:
                raise ValueError(f"Missing edited cues in {cut}")
            yield row
            continue
        # Blocking-only clock. Measured audio is required to produce the final layout.
        budget = plan["timing_budget"]
        lead = budget["action_lead_seconds_planned"]
        tail = budget["action_tail_seconds_planned"]
        start = plan["start_seconds_planned"]
        stop = plan["end_seconds_planned"]
        cues = plan["dialogue_ids"]
        step = (stop-start-lead-tail) / max(1,len(cues))
        yield {"id": cut, "first": round(FPS*start), "end": round(FPS*stop),
               "audio": [{"id": key, "start": start+lead+n*step,
                          "audible_start": start+lead+n*step,
                          "end": start+lead+(n+1)*step,
                          "audible_release": start+lead+(n+1)*step} for n,key in enumerate(cues)],
               "action_windows": {"lead": {"start": start, "end": start+lead},
                                  "tail": {"start": stop-tail, "end": stop}}}


def setup_shot(cut, crop):
    n = cut["end"] - cut["first"]
    audio = {line["id"].removeprefix("S12-"): line for line in cut["audio"]}

    def frame(sec, rounding=round):
        return min(n,max(0,rounding(FPS*sec + (1e-8 if rounding is math.floor else -1e-8 if rounding is math.ceil else 0)) - cut["first"]))

    def timed(window, bound, rounding=round):
        return frame(cut["action_windows"][window][bound], rounding)

    def cue(key, bound="start"):
        line = audio[key]
        if bound == "audible_start":
            return frame(line[bound], math.ceil)
        if bound == "audible_release":
            return frame(line[bound], math.ceil)
        return frame(line[bound], math.ceil if bound == "end" else math.floor)

    layers = []

    def add(track, level, root, height, cel=0, *, span=None, sequence=None,
            moving=None, drift=(0,0), flip=False, mouth=None, fallback=None, flight=None, poses=None):
        lo,hi = span or (0,n)
        if lo == hi:
            return
        if not 0 <= lo < hi <= n:
            raise ValueError(f"{cut['id']} {track}: invalid span {lo}–{hi} of {n}")
        row = {"track": track, "level": f"S12F-{level}", "root": root, "height": height,
               "anchor": "stage", "first_cel": cel, "motion": "hold",
               "start": lo/n, "end": hi/n, "flip": flip}
        if sequence:
            length = len(sequence)
            begin, stop = moving or (lo,hi)
            if stop-begin < sum(sequence):
                raise ValueError(f"{cut['id']} {track}: needs {sum(sequence)} drawings, has {stop-begin} frames")
            row.update(motion="story", last_cel=cel+length-1, motion_start=begin/n, motion_end=stop/n,
                       exposure_frames=sequence, drift_x=drift[0], drift_y=drift[1])
            if flight:
                row["flight"] = flight
            if poses:
                row["root_offsets"] = poses
        if mouth:
            row["mouth"] = {"speaker": mouth}
            if fallback:
                row["mouth"]["level"] = f"S12F-{fallback}"
        layers.append(row)

    def base():
        add("open-door", "door", (0,0), 720)
        add("teacher", "teacher", (739,559), 193, 7)
        add("upright-guideboard", "sign", (413,597), 84)

    def shot():
        return {"id": cut["id"], "plate": PLATE+"@"+",".join(map(str,crop)), "layout": layers}

    return n,timed,cue,add,base,shot


def compose(design, edit):
    output = []
    layouts = {
        20: (280,208,780), 21: (270,206,816), 22: (246,163,895),
        23: (382,263,704), 24: (442,290,656), 25: (392,264,704),
        26: (422,267,704), 27: (418,250,736), 28: (360,244,752), 29: (420,271,694),
    }
    action_marks = {}
    for cut in frameclock(design, edit):
        ix = int(cut["id"][-2:])
        n,window,cue,add,base,shot = setup_shot(cut, layouts[ix])
        base()
        light_root = (683,182)
        if ix == 20:
            add("Geppetto", "gep-talk", GEP,315, flip=True, mouth=GEP_SPEAKER, fallback="gep-talk")
            add("Pinocchio", "pin-talk", (541,630),236, 0)
            add("Cricket", "cricket", (479,636),84,0,flip=True)
        elif ix == 21:
            ready_end = window("lead","end")
            contact_end = min(53,ready_end-8)
            cricket_end = min(71,ready_end-3)
            onset = cue("U017","audible_start")
            add("blue-light", "glow", light_root,190,0,span=(onset,n),
                sequence=[2,2,3,3,3,3], moving=(onset,n))
            add("Geppetto", "gep-quiet", GEP,315,0,flip=True,span=(0,onset+5))
            add("Geppetto", "gep-up", GEP,315,0,span=(onset+5,n),
                sequence=[2,2,2,2,3,3], moving=(onset+5,n))
            add("Pinocchio", "pin-talk", (541,630),236,0,span=(0,6))
            add("Pinocchio", "walk", (541,630),236,0,span=(6,contact_end),
                sequence=[5,4,4,6,5,4,4,5], moving=(6,contact_end),drift=(PIN[0]-541,PIN[1]-630))
            add("Pinocchio", "pin-talk", PIN,236,0,span=(contact_end,onset+2),
                mouth=PIN_SPEAKER,fallback="pin-talk")
            add("Pinocchio", "pin-up", PIN,236,0,span=(onset+2,n),
                sequence=[2,2,2,2,3,3,3], moving=(onset+2,n))
            add("Cricket", "cricket-walk", (479,636),84,0,flip=True,span=(0,cricket_end),
                sequence=[4,3,3,4,4,4,4,4], moving=(28,cricket_end),drift=(CRICKET[0]-479,CRICKET[1]-636))
            add("Cricket", "cricket", CRICKET,84,0,flip=True,span=(cricket_end,onset+8))
            add("Cricket", "cricket-acting", CRICKET,84,0,flip=True,span=(onset+8,n),
                sequence=[3,3,4], moving=(onset+8,n))
            action_marks[cut["id"]] = {"pin_enters_safe_spot_frame":contact_end,
                                      "cricket_at_safe_spot_frame":cricket_end,
                                      "actual_light_local_frame":onset}
        elif ix == 22:
            add("blue-light", "glow",light_root,190,5,span=(0,126),
                sequence=[7,8,9,10,11,12,10,8,8,13,14], moving=(0,126))
            add("Geppetto", "gep-up",GEP,315,5)
            add("Pinocchio", "pin-up",PIN,236,6)
            add("Cricket", "cricket-acting",CRICKET,84,2,flip=True)
            add("Fairy","reveal",(764,336),122,0,span=(17,122),
                sequence=[6,7,8,10,11,12,14,14,16],moving=(17,122),drift=(67,106),flight=(0,8))
            add("Fairy","fairy",FAIRY,122,4,span=(122,n))
        elif ix == 23:
            add("Geppetto","gep-up",GEP,315,5)
            add("Pinocchio","pin-up",PIN,236,6)
            add("Cricket","cricket-acting",CRICKET,84,2,flip=True)
            add("Fairy","fairy",FAIRY,122,4,mouth=FAIRY_SPEAKER)
        elif ix == 24:
            add("Geppetto","gep-up",GEP,315,5)
            add("Pinocchio","pin-nod",PIN,236,0,sequence=[5,4,4,6,5,6,5,6,12],
                moving=(max(0,cue("U020","audible_start")+7),n))
            add("Cricket","cricket-acting",CRICKET,84,2,flip=True)
            add("Fairy","palm",FAIRY,122,0,mouth=FAIRY_SPEAKER,
                sequence=[3,3,4,5,4,5,6,10],moving=(max(0,cue("U020","audible_start")-6),n))
        elif ix == 25:
            answer = cue("U023")
            look = max(0,answer-20)
            add("Geppetto","gep-up",GEP,315,5)
            add("Pinocchio","pin-up",PIN,236,6,span=(0,look))
            add("Pinocchio","listen",PIN,236,0,flip=True,span=(look,answer))
            add("Pinocchio","pin-talk",PIN,236,0,span=(answer,n),mouth=PIN_SPEAKER,fallback="pin-talk")
            add("Cricket","cricket-acting",CRICKET,84,2,flip=True)
            add("Fairy","fairy",FAIRY,122,4,span=(0,answer),mouth=FAIRY_SPEAKER)
            add("Fairy","fairy",FAIRY,122,4,span=(answer,n),mouth=FAIRY_SPEAKER)
        elif ix == 26:
            add("Geppetto","gep-up",GEP,315,5)
            add("Pinocchio","pin-up",PIN,236,6)
            add("Cricket","cricket-acting",CRICKET,84,2,flip=True)
            soften = cue("U025")
            add("Fairy","fairy",FAIRY,122,4,span=(0,soften),mouth=FAIRY_SPEAKER)
            add("Fairy","fairy",FAIRY,122,5,flip=True,span=(soften,n),mouth=FAIRY_SPEAKER)
        elif ix == 27:
            release = cue("U026","audible_release")
            add("Geppetto","gep-up",GEP,315,5)
            add("Pinocchio","pin-up",PIN,236,6)
            add("Cricket","cricket-acting",CRICKET,84,2,flip=True)
            add("Fairy","wand",FAIRY,122,0,mouth=FAIRY_SPEAKER,
                sequence=[2,3,4,4,5,5],moving=(release,n))
            action_marks[cut["id"]] = {"wand_begins_no_earlier_than_audio_release_local_frame":release}
        elif ix == 28:
            add("Geppetto","gep-up",GEP,315,5)
            add("Pinocchio","pin-ready",PIN,236,0,sequence=[5,4,4,6,8,9,11,12,12,17],moving=(15,n))
            add("Cricket","cricket-acting",CRICKET,84,2,flip=True)
            add("Fairy","wand",FAIRY,122,5,
                sequence=[3,3,4,4,5,6,7,7,8,10],moving=(0,n))
            add("shoe-to-shoulder-particles","sparks",(499,378),271,0,span=(5,n),
                sequence=[4]*20+[3]*8,moving=(5,n))
        else:
            add("Geppetto","gep-up",GEP,315,5)
            add("Pinocchio","pin-ready",PIN,236,9)
            add("Cricket","cricket-acting",CRICKET,84,2,flip=True)
            add("Fairy","wand",FAIRY,122,14,mouth=FAIRY_SPEAKER)
            add("blue-reflection","halo",(506,427),97,0,
                sequence=[3,4,5,6,7,9,11,14,9,8,7,5,7],moving=(0,n))
            add("rising-particles","sparks",(499,378),271,27,
                sequence=[6,6,6,6,7],moving=(0,n))
            action_marks[cut["id"]] = {"wooden_until_utterance_release_local_frame":cue("U027","audible_release"),
                                      "wooden_for_entire_local_cut_frames":n}
        output.append(shot())
    return output, action_marks


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--authority", type=Path, default=AUTHORITY)
    parser.add_argument("--edit", type=Path, help="Measured accepted voice edit")
    parser.add_argument("--skip-art", action="store_true", help="Reuse the unchanged registered drawings")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    edit = read(args.edit) if args.edit else None
    if edit and edit["fps"] != FPS:
        raise ValueError("The inherited S04/S08 exposure clock uses 24 fps")
    if not args.skip_art:
        register_art()
    design = read(args.authority / "story/scene_design_v2.json")
    layout, marks = compose(design, edit)
    out = args.output or BUILD / "layout-fairy.json"
    write(out, layout)
    write(out.with_name("fairy-action-marks.json"), {"measured_edit": bool(edit), "cuts": marks})
    write(out.with_name("motion-fairy.json"), {"cuts": {
        "S12-C20":{"lead_frames":48,"tail_frames":0},
        "S12-C21":{"lead_frames":72,"tail_frames":24,"between_frames":{"S12-N014":14}},
        "S12-C22":{"silent_frames":192},
        "S12-C23":{"lead_frames":30,"tail_frames":12},
        "S12-C24":{"lead_frames":24,"tail_frames":18},
        "S12-C25":{"lead_frames":24,"tail_frames":12,"between_frames":{"S12-U022":20}},
        "S12-C26":{"lead_frames":24,"tail_frames":12},
        "S12-C27":{"lead_frames":24,"tail_frames":24},
        "S12-C28":{"silent_frames":144},
        "S12-C29":{"lead_frames":36,"tail_frames":12},
    }})
    print(f"Registered {len(layout)} shots at {out}")


if __name__ == "__main__":
    main()
