#!/usr/bin/env python3
"""Register the S11 exit and photographable S12 opening action cels."""
from argparse import ArgumentParser
from hashlib import file_digest
from math import hypot, pi, sin, sqrt
from pathlib import Path
import json
import runpy
import shutil

import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFilter

ART = Path(__file__).resolve().parent
SCENES = ART.parents[2]
BUILD = ART.parent / "build"
SOURCE = SCENES / "S11/v2/build/art"
OUTPUT = BUILD / "art"
POSE = runpy.run_path(str(SCENES / "S10/v2/art/late/make_late_art.py"))
STAGE = "S11L-school-open.png"
PIN = "S11L-pin-wave-motion"
GEP = "S11L-gep-wave"
BOARD = "S11L-school-sign"
PIN_ARM = [(56,148),(70,142),(81,151),(88,167),(83,183),(77,192),
           (76,227),(83,246),(83,263),(74,279),(54,279),(43,269),(43,252),
           (48,226),(48,191),(51,176)]
GEP_ARM = [(108,163),(142,167),(157,188),(157,211),(147,238),(144,279),
           (132,302),(108,300),(96,284),(98,257),(107,226),(103,190)]


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path, value):
    pending = path.with_suffix(".pending")
    pending.write_text(json.dumps(value, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    pending.replace(path)


def digest(path):
    with path.open("rb") as stream:
        return file_digest(stream, "sha256").hexdigest()


def source_pose(level, index):
    data = read(SOURCE / "cels" / level / "registration.json")
    pose = data["poses"][index]
    return Image.open(SOURCE / pose["file"]).convert("RGBA"), pose["anchors"]["stage"], data["reference_height"]


def stage_sources():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE / STAGE, OUTPUT / STAGE)
    for name in (PIN,GEP,BOARD,"S11L-school-door","S11L-teacher","S11L-cricket-talk"):
        shutil.copytree(SOURCE / "cels" / name, OUTPUT / "cels" / name, dirs_exist_ok=True)


class Level:
    def __init__(self, name, reference, source):
        self.name = name
        self.reference = reference
        self.source = source
        self.directory = OUTPUT / "cels" / name
        self.directory.mkdir(parents=True, exist_ok=True)
        self.poses = []

    def save(self, art, name, anchor, mouth=None):
        file = self.directory / (name + ".png")
        art.save(file, compress_level=3)
        row = {"file":file.relative_to(OUTPUT).as_posix(), "size":list(art.size),
               "anchors":{"stage":list(anchor)}, "sole":list(anchor), "sha256":digest(file)}
        if mouth:
            row["mouth_box"] = list(mouth)
        return row

    def add(self, art, anchor, variants=(), mouth=None):
        index = len(self.poses)
        record = self.save(art,f"{index:02}",anchor,mouth)
        record["index"] = index
        if variants:
            record["viseme_cels"] = {name:self.save(take,f"{index:02}-{name}",anchor,mouth)
                                      for name,take in variants.items()}
        self.poses.append(record)

    def finish(self):
        write(self.directory/"registration.json",{"level":self.name,"reference_height":self.reference,
              "source":self.source,"poses":self.poses})


def offset(points, distance):
    return [(x+distance,y+distance) for x,y in points]


def lifted_arm(image, boundary, joints, wrist, bias, moving):
    if not moving:
        return POSE["padded"](image)
    raw = POSE["padded"](image)
    margin = POSE["PAD"]
    cut = offset(boundary, margin)
    bare = POSE["erase"](raw, cut, .45)
    return POSE["authored_arm"](bare,raw,*offset(joints,margin),cut,offset([wrist],margin)[0],bias,True)


def reach_for_hat(image, wrist):
    """Draw the visible arm against the brim with a fixed shoulder and preserved segment lengths."""
    resting = (59,242)
    scene = POSE["padded"](image)
    if wrist == resting:
        return scene
    pad = POSE["PAD"]
    shoulder, elbow, old_wrist = offset([(68,160),(59,212),resting],pad)
    target = offset([wrist],pad)[0]
    dx,dy=(b-a for a,b in zip(shoulder,target,strict=True))
    distance=hypot(dx,dy)
    a=hypot(elbow[0]-shoulder[0],elbow[1]-shoulder[1])
    b=hypot(old_wrist[0]-elbow[0],old_wrist[1]-elbow[1])
    distance=min(distance,a+b-.1)
    direction=(dx/hypot(dx,dy),dy/hypot(dx,dy))
    target=tuple(round(p+d*distance) for p,d in zip(shoulder,direction,strict=True))
    forward=(a*a - b*b + distance*distance)/(2*distance)
    bend=sqrt(max(0,a*a-forward*forward))
    side=(direction[1],-direction[0])
    join=tuple(p+f*forward+n*bend for p,f,n in zip(shoulder,direction,side,strict=True))
    cut=offset(PIN_ARM,pad)
    sleeve=POSE["isolated"](scene,cut,.55)
    draw=POSE["erase"](scene,cut,.6)

    def strip(first,last):
        return POSE["isolated"](sleeve,[(0,first),(scene.width,first),(scene.width,last),(0,last)],.65)

    draw.alpha_composite(POSE["deform"](strip(0,elbow[1]+8),shoulder,elbow,shoulder,join))
    draw.alpha_composite(POSE["deform"](strip(elbow[1]-7,old_wrist[1]+6),elbow,old_wrist,join,target))
    hand_axis=(old_wrist[0],old_wrist[1]+24)
    length=hypot(target[0]-join[0],target[1]-join[1])
    held_axis=tuple(w+(w-e)*24/length for w,e in zip(target,join,strict=True))
    draw.alpha_composite(POSE["deform"](strip(old_wrist[1]-3,scene.height),old_wrist,hand_axis,target,held_axis))
    return draw


def shift_top(image, head, vertical=0):
    raw = np.array(image, copy=True)
    height = raw.shape[0]
    out = Image.new("RGBA",image.size)
    for y in range(height):
        # The shift falls to zero above the shins, so both contact soles remain registered.
        amount = max(0, min(1, (359-y)/85))
        amount = amount*amount*(3-2*amount)
        dx = round(head*amount)
        dy = round(vertical*amount)
        out.paste(image.crop((0,y,image.width,y+1)),(dx,y+dy))
    return out


def gaze(image, amount, dip=0):
    # Move the painted iris in each sclera, preserving the painted lashes and brows.
    result = image.copy()
    for bounds in ((97,70,117,94),(128,70,149,92)):
        x0,y0,x1,y1 = bounds
        local = image.crop(bounds)
        pigment = np.array(local)
        dark = (pigment[:,:,:3].mean(axis=2)<103) & (pigment[:,:,3]>180)
        inner = Image.new("L",local.size)
        ImageDraw.Draw(inner).ellipse((3,3,local.width-3,local.height-2),fill=245)
        inner = inner.filter(ImageFilter.GaussianBlur(1))
        dark_mask = Image.fromarray((dark*255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(.62))
        dark_mask = ImageChops.multiply(inner,dark_mask)
        if not dark_mask.getbbox():
            continue
        whites = Image.new("RGBA",local.size,(241,222,180,255))
        local.paste(whites,(0,0),dark_mask)
        pigment_image = image.crop(bounds)
        tinted = Image.new("RGBA",local.size)
        pigment_image.putalpha(dark_mask)
        tinted.alpha_composite(pigment_image,(amount,dip))
        local.alpha_composite(tinted)
        result.paste(local,(x0,y0))
    return result


def mouth(image, raw_centre, is_puppet):
    """Bake the mouth shapes into whole action drawings before photography."""
    x,y=raw_centre
    radius = 15 if is_puppet else 13
    e = Image.new("L",image.size)
    ImageDraw.Draw(e).ellipse((x-radius-3,y-6,x+radius+2,y+9),fill=255)
    e=e.filter(ImageFilter.GaussianBlur(1.12))
    skin = image.crop((x-radius-3,y-20,x+radius+3,y-12)).resize((2*radius+6,20))
    patch = image.copy()
    patch.paste(skin,(x-radius-3,y-10))
    erased = Image.composite(patch,image,e)
    shapes = {"small":(9,3),"wide":(13,5),"round":(5,6),"pressed":(11,2),"teeth":(12,3)}
    variants = {}
    for name,(width,depth) in shapes.items():
        drawing = erased.copy()
        layer = Image.new("RGBA",drawing.size)
        pen = ImageDraw.Draw(layer)
        pen.ellipse((x-width,y-depth,x+width,y+depth),fill=(83,36,24,238 if is_puppet else 223))
        if name in ("wide","teeth"):
            pen.ellipse((x-width+3,y-depth+1,x+width-3,y-depth+3),fill=(245,218,174,235))
        if name == "wide":
            pen.arc((x-width+4,y-1,x+width-4,y+depth),0,167,fill=(178,96,69,245),width=2)
        drawing.alpha_composite(layer.filter(ImageFilter.GaussianBlur(.63)))
        variants[name]=drawing
    return variants, (x-radius-4,y-13,x+radius+4,y+12)


def hat_breeze(image, angle):
    if not angle:
        return image
    cap = [(1,5),(27,3),(54,27),(63,3),(104,1),(141,5),(154,13),(158,24),(143,28),
           (122,32),(103,41),(84,51),(68,67),(58,82),(47,89),(32,77),(30,58),(14,43)]
    selected = POSE["isolated"](image,cap,.7)
    rest = POSE["erase"](image,cap,.5)
    rest.alpha_composite(selected.rotate(angle,resample=Image.Resampling.BICUBIC,center=(86,54)))
    return rest


def pin_opening():
    art,point,reference=source_pose(PIN,7)
    resting=(59,242)
    hand_poses=[
        *([resting]*7), (54,238),(49,232),(45,224),(43,213),(42,202),
        (42,178),(46,152),(54,124),(65,101),(71,89),(73,78),
        (67,98),(53,125),(43,159),(42,191),(47,216),(53,232),resting,
    ]
    level=Level("S12O-pin",reference,PIN)
    margin=POSE["PAD"]
    point=[int(point[0])+margin,int(point[1])+margin]
    for index,wrist in enumerate(hand_poses):
        look=(-2,-1,1,2,2,1,0)[index] if index<7 else (0 if index<18 else -1)
        dip=-1 if 2<=index<=4 else 0
        lean=(0,3,6,9,9,7,4)[index] if index<7 else (2 if index<18 else 0)
        source = gaze(art,look,dip) if look else art
        if 7<=index<=11:
            source=hat_breeze(source,(-.7,-1.5,-2.1,-1.4,-.4)[index-7])
        draw=reach_for_hat(source,wrist)
        draw=shift_top(draw,lean)
        variants,box=mouth(draw,(margin+121+round(lean*.94),margin+108),True)
        level.add(draw,point,variants,box)
    level.finish()


def gep_opening():
    image,point,reference=source_pose(GEP,0)
    margin=POSE["PAD"]
    point=[int(point[0])+margin,int(point[1])+margin]
    resting=(123,275)
    path = [resting,(129,267),(138,253),(153,237),(168,219),(182,207),(191,205),
            (175,216),(158,224),(140,233),(126,247),(123,266),resting,
            (120,267),(116,256),(109,244),(100,231),(89,217),(78,207),(69,202)]
    level=Level("S12O-gep",reference,GEP)
    for index,wrist in enumerate(path):
        bias=-9 if index<7 else (-5 if index<13 else 12)
        draw=lifted_arm(image,GEP_ARM,((129,190),(133,231),resting),wrist,bias,wrist!=resting)
        variants,box=mouth(draw,(margin+58,margin+105),False)
        level.add(draw,point,variants,box)
    level.finish()


def wind_and_sign():
    board,anchor,height=source_pose(BOARD,0)
    level=Level("S12O-board-gust",height,BOARD)
    for angle in (0,-.4,-1.0,-2.3,-1.8,-.65,.45,.86,.65,.28,0):
        level.add(board.rotate(angle,Image.Resampling.BICUBIC,center=tuple(anchor)),anchor)
    level.finish()
    level=Level("S12O-leaf",20,STAGE)
    for index in range(16):
        cel=Image.new("RGBA",(35,29))
        pen=ImageDraw.Draw(cel)
        edge=round(3.4+3*abs(sin(index*pi/5)))
        pen.polygon([(6,14),(11,11-edge),(22,9-edge),(30,12),(22,14+edge),(14,17),(6,14)],fill="#8d9755")
        pen.line((5,15,27,11),fill="#b4ab68",width=1)
        pen.line((3,17,11,13),fill="#7e7751",width=1)
        cel=cel.rotate(-22+index*23,Image.Resampling.BICUBIC,center=(17,14))
        level.add(cel,(17,14))
    level.finish()


def layer(track,level,cel,root,height,last=None,motion="hold",**options):
    return {"track":track,"level":level,"first_cel":cel,"last_cel":cel if last is None else last,
            "root":list(root),"height":height,"anchor":"stage","motion":motion,**options}


def pin(cel,last=None,motion="hold",speech=False,**options):
    if speech:
        options["mouth"]={"speaker":"피노키오"}
    return layer("pin","S12O-pin",cel,(541,630),236,last,motion,**options)


def gep(cel,last=None,motion="hold",speech=False,**options):
    if speech:
        options["mouth"]={"speaker":"제페토"}
    return layer("gep","S12O-gep",cel,(667,629),315,last,motion,**options)


def cricket(speech=False):
    options={"flip":True}
    if speech:
        options["mouth"]={"speaker":"귀뚜라미","level":"S11L-cricket-talk"}
    return layer("cricket","S11L-cricket-talk",0,(479,636),84,**options)


def board():
    return layer("guideboard",BOARD,0,(413,597),84)


def leaf(root,travel,length=16,start=None):
    motion=layer("wind","S12O-leaf",0,root,13,last=15,motion="story",drift_x=travel,
                 root_offsets=[[0,round(-6*sin(pi*i/15)+3*sin(i*1.1))] for i in range(16)],active_frames=length)
    if start:
        motion["span"]=start
    return motion


def layout():
    door=layer("door","S11L-school-door",0,(0,0),720)
    teacher=layer("teacher","S11L-teacher",7,(739,559),193)
    normal_pin=layer("pin",PIN,7,(541,630),236)
    normal_gep=layer("gep",GEP,0,(667,629),315)
    rows=[
        (STAGE,[board(),normal_pin|{"span":["start","lead-point:0.37"]},
                pin(0,2,"story",span=["lead-point:0.37","end"],active_frames=15),normal_gep,cricket()]),
        (STAGE+"@240,270,790",[board(),pin(2,4,"lead",active_frames=16),
                              gep(0,6,"lead",True,active_frames=34),cricket()]),
        (STAGE+"@245,244,830",[board(),pin(0,6,"lead",True,exposure_frames=[5,5,6,8,7,6,5]),
                              gep(7,12,"lead",active_frames=25),cricket(True)]),
        (STAGE+"@250,310,710",[board(),leaf((342,626),255,20,["start","lead-point:0.51"]),
                              pin(7,11,"lead",active_frames=42),gep(12,19,"lead",True,active_frames=29),cricket()]),
        (STAGE+"@219,290,750",[
            board()|{"span":["start","after:S12-N007"]},
            layer("guideboard","S12O-board-gust",0,(413,597),84,last=10,motion="story",
                  span=["after:S12-N007","end"],active_frames=22),
            leaf((310,633),299,24,["after:S12-N007","end"]),
            pin(11,17,"lead",True,span=["start","after:S12-N007"],exposure_frames=[6,5,6,7,6,7,8]),
            pin(18,24,"story",span=["after:S12-N007","end"],active_frames=24),
            gep(7,12,"lead",active_frames=26),cricket()]),
    ]
    write(BUILD/"layout-opening.json", [{"id":f"S12-C{index:02}","plate":plate,
          "layout":[door,teacher,*layers]} for index,(plate,layers) in enumerate(rows,1)])
    write(BUILD/"motion-opening.json",{"cuts":{
        "S12-C01":{"lead_frames":36,"tail_frames":12},
        "S12-C02":{"lead_frames":48},
        "S12-C03":{"lead_frames":48,"tail_frames":12},
        "S12-C04":{"lead_frames":48},
        "S12-C05":{"lead_frames":48,"tail_frames":12,"between_frames":{"S12-N007":24}},
    }})


if __name__=="__main__":
    stages={"source":stage_sources,"pin":pin_opening,"geppetto":gep_opening,
            "wind":wind_and_sign,"layout":layout}
    parser=ArgumentParser(description=__doc__)
    parser.add_argument("--component",choices=stages)
    args=parser.parse_args()
    for name,build in stages.items():
        if args.component in (None,name):
            build()
