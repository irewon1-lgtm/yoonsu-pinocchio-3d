"""Register the approved Blue Fairy acting needed by S12 C43–C48."""
from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw

from build_fairy import ART, S10, SCENES, isolated, link, pad, read, sha, write

SOURCE = S10 / "fairy/fairy-s10-poses/registration.json"
FAREWELL_ART = SCENES / "S10/v2/build/art"
FAREWELL = FAREWELL_ART / "resolution/v2-fairy-farewell/registration.json"
HERE = Path(__file__).resolve().parent
NEAR = [831, 442]
DISTANT = [903, 143]
HEIGHT_NEAR = 122
HEIGHT_DISTANT = 64
FRAME = (1280, 720)
CUES = ("S12-U034", "S12-U042")


def copy_level(name, art, source):
    registry = read(source)
    out = ART / "cels" / name
    out.mkdir(parents=True, exist_ok=True)
    for i, row in enumerate(registry["poses"]):
        row["index"] = i
        for drawing in (row, *row.get("viseme_cels", {}).values()):
            original = art / drawing["file"]
            target = out / original.name
            link(original, target)
            drawing["file"] = target.relative_to(ART).as_posix()
        if variants := row.get("viseme_cels"):
            source_picture = load(row).convert("RGB")
            rects = [ImageChops.difference(source_picture, load(part).convert("RGB")).getbbox()
                     for part in variants.values()]
            if not all(rects):
                raise ValueError("Approved mouth drawings must change displayed pixels")
            mouth = [min(r[0] for r in rects),min(r[1] for r in rects),
                     max(r[2] for r in rects),max(r[3] for r in rects)]
            for drawing in (row, *variants.values()):
                drawing["mouth_box"] = mouth
    registry["origin_registry"] = source.relative_to(SCENES).as_posix()
    registry["origin_registry_sha256"] = sha(source)
    write(out / "registration.json", registry)
    return registry


def load(row):
    with Image.open(ART / row["file"]) as drawing:
        return drawing.convert("RGBA")


def cell(out, i, drawing, anchor):
    path = out / f"{i:02}.png"
    drawing.save(path)
    return {"file": path.relative_to(ART).as_posix(), "index": i,
            "anchors": {"stage": anchor}, "size": list(drawing.size), "sha256": sha(path)}


def register(name, source, reference, images):
    out = ART / "cels" / name
    out.mkdir(parents=True, exist_ok=True)
    poses = [cell(out, i, image, anchor) for i, (image,anchor) in enumerate(images)]
    write(out / "registration.json", {"origin_registry": source.relative_to(SCENES).as_posix(),
                                     "origin_registry_sha256": sha(source),
                                     "reference_height": reference, "poses": poses})
    return poses


def reduce_wand(row, degrees_by_cel):
    draw = load(row)
    inset = 45
    pic = pad(draw, inset)
    anchor = [value + inset for value in row["anchors"]["stage"]]
    dx = row["anchors"]["stage"][0] - 107
    dy = row["anchors"]["stage"][1] - 478
    # The painted fist and complete wand are enclosed together, and pivot at the wrist cuff.
    polygon = [(0,76),(29,73),(39,105),(43,138),(52,155),(51,171),
               (42,176),(28,169),(18,147),(16,121),(-3,100)]
    mask_pts = [(x+inset+dx,y+inset+dy) for x,y in polygon]
    part, mask = isolated(pic, mask_pts, .55)
    cuff = (48+inset+dx,161+inset+dy)
    for degrees in degrees_by_cel:
        if degrees == 0:
            yield pic, anchor
            continue
        figure = pic.copy()
        figure.paste((0,0,0,0), mask=mask)
        figure.alpha_composite(part.rotate(degrees, Image.Resampling.BICUBIC, center=cuff))
        yield figure, anchor


def bezier(progress, anchors):
    p = progress
    shares = ((1-p)**3,3*p*(1-p)**2,3*p*p*(1-p),p**3)
    return [round(sum(weight*point[axis] for weight, point in zip(shares,anchors,strict=True))) for axis in (0,1)]


def retreat(registry, still):
    """Expose the existing specific wing/bend drawings on a backward flight path."""
    p0, p3 = NEAR, DISTANT
    control = (p0,[872,418],[938,216],p3)
    wing_poses = [4,4,4,5,5,5,4,4,5,5,5,4,4,5,5,5,4,4,5,5,4,4,4,4,4,4,4,4,4,4,0,0]
    source = {i:load(registry["poses"][i]) for i in (4,5)}
    distant = load(still)
    stock = []
    path = []
    for i, key in enumerate(wing_poses):
        q = i/(len(wing_poses)-1)
        p = q*q*(3-2*q)
        height = round(HEIGHT_NEAR+(HEIGHT_DISTANT-HEIGHT_NEAR)*p)
        path.append(bezier(p,control))
        if key == 0:
            original, pose = distant, still
        else:
            original, pose = source[key], registry["poses"][key]
        scale = height/registry["reference_height"]
        drawing = original.resize(tuple(round(length*scale) for length in original.size),
                                  Image.Resampling.LANCZOS)
        ax, ay = (round(value*scale) for value in pose["anchors"]["stage"])
        drawing = drawing.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        ax = drawing.width-1-ax
        canvas = Image.new("RGBA",(180,164))
        canvas.alpha_composite(drawing,(90-ax,148-ay))
        stock.append((canvas,[90,148]))
    return stock,path


def preview(steps, stock, lower, wave):
    """Record the actual Fairy-only layered drawings over the existing school plate."""
    with Image.open(ART/"S11L-school-open.png") as still:
        plate = still.convert("RGBA")
    indexes = (0,9,18,31)
    sheet = Image.new("RGB",(1024,648),"#222631")
    label = ImageDraw.Draw(sheet)
    for x,i in enumerate(indexes):
        view = plate.copy()
        drawing, anchor = stock[i]
        rx, ry = steps[i]
        view.alpha_composite(drawing,(rx-anchor[0],ry-anchor[1]))
        view = view.crop((666,44,1018,471)).resize((237,288),Image.Resampling.LANCZOS)
        sheet.paste(view,(x*256+9,9))
        label.text((x*256+11,307),f"C45  |  {i+1:02}/32",fill="#ffffff")
    for x, (caption, sprite) in enumerate((("C44  |  wand lowered",lower[-1]),
                                          ("C45  |  hand lifts",wave[1]),
                                          ("C45  |  reciprocal wave",wave[2]),
                                          ("C45  |  return to hold",wave[-1]))):
        drawing, anchor = sprite
        factor = HEIGHT_NEAR / 471
        drawing = drawing.resize(tuple(round(unit*factor) for unit in drawing.size),
                                 Image.Resampling.LANCZOS)
        off_x,off_y = (round(unit*factor) for unit in anchor)
        drawing = drawing.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        view = plate.copy()
        view.alpha_composite(drawing, (NEAR[0] - (drawing.width-1-off_x),NEAR[1]-off_y))
        detail = view.crop((760,307,911,471)).resize((237,258),Image.Resampling.LANCZOS)
        sheet.paste(detail,(x*256+9,346))
        label.text((x*256+11,617),caption,fill="#ffffff")
    sheet.save(HERE/"late-fairy-contact.jpg",quality=93)


def main():
    stills = copy_level("S12FL-talking", S10, SOURCE)
    gestures = copy_level("S12FL-farewell", FAREWELL_ART, FAREWELL)
    lowering = list(reduce_wand(gestures["poses"][0],(0,4,9,15,20,23,25,25)))
    register("S12FL-lower", FAREWELL, gestures["reference_height"], lowering)
    sequence = (0,1,2,3,2,1,0)
    wave = [next(reduce_wand(gestures["poses"][index],(25,))) for index in sequence]
    register("S12FL-wave", FAREWELL, gestures["reference_height"], wave)
    stock, path = retreat(gestures, stills["poses"][0])
    register("S12FL-retreat", FAREWELL, HEIGHT_NEAR, stock)
    preview(path,stock,lowering,wave)
    receipt = {
        "scope":"Fairy actor only. These are support layers and not complete shots.",
        "stage":{"plate":"S11L-school-open.png","width":FRAME[0],"height":FRAME[1],
                 "intended_near_root":NEAR,"far_root":DISTANT},
        "approved_art":[{"path":f.relative_to(SCENES).as_posix(),"sha256":sha(f)} for f in (SOURCE,FAREWELL)],
        "layers":{
            "S12-C43":{"level":"S12FL-talking","root":NEAR,"height":HEIGHT_NEAR,"cel":0,"flip":True,
                       "mouth":{"speaker":"파란 요정"},"cue":CUES[0]},
            "S12-C44":{"level":"S12FL-lower","root":NEAR,"height":HEIGHT_NEAR,"first_cel":0,"last_cel":7,
                       "flip":True,"exposure_frames":[3,4,4,5,5,5,6,7],"then":"Hold cel 7 throughout P09.",
                       "hold_predicate":"No wave or departure while awaiting S12-P09 acceptance."},
            "S12-C45":{
                "predicate":"S12-P09 consumed and child has begun the approved wave.",
                "prelude":{"hold_level":"S12FL-lower","hold_cel":7,
                           "minimum_scene_local_frames_before_fairy_reply":16},
                "wave":{"level":"S12FL-wave","first_cel":0,"last_cel":6,"flip":True,
                        "root":NEAR,"height":HEIGHT_NEAR,"exposure_frames":[2,4,5,5,4,4,3]},
                "retreat":{"level":"S12FL-retreat","root":NEAR,"height":HEIGHT_NEAR,
                           "flip":False,"first_cel":0,"last_cel":31,
                           "root_offsets":[[x-NEAR[0],y-NEAR[1]] for x,y in path],
                           "flight":[0,31],
                           "exposure_frames":[3]*10+[2]*21+[5],
                           "last_root":DISTANT},
                "min_lead_frames_for_fairy_only":120,
                "resume_after":"Retreat and child's independent post-wave action have both completed."
            },
            "S12-C46":{"level":"S12FL-talking","root":DISTANT,"height":HEIGHT_DISTANT,"cel":0,
                       "flip":True,"hidden_only_if_outside_approved_crop":True},
            "S12-C47":{"level":"S12FL-talking","root":DISTANT,"height":HEIGHT_DISTANT,"cel":0,
                       "flip":True,"hidden_only_if_outside_approved_crop":True},
            "S12-C48":{"level":"S12FL-talking","root":DISTANT,"height":HEIGHT_DISTANT,"cel":0,"flip":True,
                       "mouth":{"speaker":"파란 요정"},"cue":CUES[1],"requires_roof_and_door_crop":True}
        },
        "evidence":{"contact_sheet":"late-fairy-contact.jpg",
                    "complete_late_shots":"BLOCKED_RESOURCE","audible_u042_in_finished_cut":"NOT_RUN"}}
    write(HERE/"late-fairy-support.json",receipt)
    print(json.dumps({"levels":5,"flight_cels":len(path),"near":NEAR,"far":DISTANT}))


if __name__ == "__main__":
    main()
