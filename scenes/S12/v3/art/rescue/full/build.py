#!/usr/bin/env python3
"""Photograph the V3 school rescue as registered S11 whole-figure 2D drawings.

The stonework and every actor have one 1280 x 720 ground registration. The sign
is the original S11 painting on a fixed pedestal. Its two pivots, hand targets
and the lateral escape timing are measured in the same stage coordinates.
"""
from __future__ import annotations

import argparse
import json
import math
import runpy
from functools import lru_cache
from hashlib import file_digest
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter, ImageOps

HERE = Path(__file__).resolve().parent
V3 = HERE.parents[2]
STAGE = V3 / "build/art"
SCENES = V3.parents[1]
SCHOOL = SCENES / "S11/v2/build/art"
OLD = runpy.run_path(str(HERE.parent / "build.py"))
BODY = OLD["BODY"]
SIZE = (1280, 720)
PREFIX = "S12X-"
PLATE = "S12X-school-recess.png"
ARCH = "S12X-recess-foreground"
PIN, GEP, CRICKET = (541, 630), (667, 629), (479, 636)
ASCEND = (509, 625)
BESIDE = (447, 624)
ADULT_EDGE = (533, 574)
TRAPPED = (377, 580)
SIDE_EXIT = (440, 654)
SIGN_STAGE = (413, 597)
SIGN_SCALE = 84 / 911
SIGN_SOCKET = (382, 783)
LEAN, LIFT = 61.0, 81.0
VIEWS = ("closed", "small", "wide", "round", "teeth", "pressed")
SPEAKERS = {"pin": "피노키오", "gep": "제페토", "cricket": "귀뚜라미"}
CROPS = {6: (243, 275, 768), 7: (288, 328, 625), 8: (286, 306, 680),
         9: (285, 253, 790), 10: (238, 260, 800), 11: (255, 284, 768),
         12: (266, 279, 770), 13: (265, 292, 740), 14: (254, 273, 780)}


def json_out(path, value):
    pending = path.with_suffix(".pending")
    pending.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    pending.replace(path)


def blank(size=SIZE):
    return Image.new("RGBA", size)


def smooth(x):
    x = clamp(x)
    return x*x*(3-2*x)


def clamp(x):
    return min(1.0, max(0.0, x))


def progress(frame, first, last):
    return smooth((frame-first)/(last-first))


def blend(a, b, u):
    return tuple(x + (y-x)*u for x,y in zip(a,b,strict=True))


def rounded(point):
    return tuple(round(x) for x in point)


class Drawings:
    def __init__(self, name):
        self.name = PREFIX + name
        self.folder = STAGE/"cels"/self.name
        self.folder.mkdir(parents=True, exist_ok=True)
        self.rows = []

    def save(self, image, filename):
        x, y, u, v = image.getchannel("A").getbbox()
        left, top, right, bottom = x-4, y-4, u+4, v+4
        drawing = image.crop((left, top, right, bottom))
        path = self.folder/(filename+".png")
        drawing.save(path, compress_level=4)
        with path.open("rb") as handle:
            digest = file_digest(handle, "sha256").hexdigest()
        return {"file": str(path.relative_to(STAGE)), "size": list(drawing.size),
                "anchors": {"stage": [-left,-top]}, "world_bounds": [x,y,u,v], "sha256": digest}

    def add(self, image, *, variants=None, **details):
        index = len(self.rows)
        name = f"{index:03d}"
        row = self.save(image,name) | {"index":index} | details
        if variants:
            row["viseme_cels"] = {mode:self.save(variant,f"{name}-{mode}") for mode,variant in variants.items()}
        self.rows.append(row)
        return index

    def finish(self):
        json_out(self.folder/"registration.json",{"reference_height":720,"poses":self.rows})


@lru_cache(maxsize=128)
def level_data(name, art=STAGE):
    return json.loads((art/"cels"/name/"registration.json").read_text())


@lru_cache(maxsize=320)
def source_png(path):
    with Image.open(path) as image:
        return image.convert("RGBA")


def source_pose(name,index,mode="closed",art=STAGE):
    info=level_data(name,art)
    row=info["poses"][index % len(info["poses"])]
    if mode!="closed":
        variants=row.get("viseme_cels")
        if variants:
            row=variants.get(mode,variants["small"])
        elif "visemes" in info:
            row=info["poses"][info["visemes"].get(mode,info["visemes"]["small"])]
        else:
            raise ValueError(f"Native mouth pose missing: {name}/{index}/{mode}")
    return source_png(art/row["file"]),row["anchors"]["stage"],info["reference_height"]


def figure(name,index,root,height,flip=False,mode="closed",art=STAGE):
    source,anchor,reference=source_pose(name,index,mode,art)
    return BODY["blit"](source,rounded(root),round(height),reference,anchor,flip)


def with_scope(value,start,end):
    if isinstance(start,str) or isinstance(end,str):
        return value|{"during":[start,end]}
    return value|{"start":start,"end":end}


def track(name,level,root=(0,0),height=720,first=0,last=None,
          motion="hold",flip=False,speak=False,active=None,exposures=None,visible=(0,1)):
    value={"track":name,"level":level,"root":list(root),"height":height,"anchor":"stage",
           "first_cel":first,"last_cel":first if last is None else last,"motion":motion,"flip":flip}
    if speak:
        value["mouth"]={"speaker":SPEAKERS[name]}
    if active is not None:
        value["active_frames"]=active
    if exposures is not None:
        value["exposure_frames"]=exposures
    return with_scope(value,*visible)


def stage_track(name,lvl,first=0,*args,**kwargs):
    return track(name,PREFIX+lvl,first=first,*args,**kwargs)


def pin_static(root=PIN, facing="left", speak=False, blink=False, visible=(0,1)):
    lv="S12R-pin-back-talk" if facing=="right" else "S12R-pin-listen-left"
    return track("pin",lv,rounded(root),236,6 if blink else 0,speak=speak,visible=visible)


def adult_static(root=GEP,speak=False,visible=(0,1)):
    return track("gep","S12R-gep-talk",rounded(root),315,flip=True,speak=speak,visible=visible)


def cricket_static(root=TRAPPED,height=72,index=0,speak=False,flip=True,visible=(0,1)):
    return track("cricket","S12R-cricket-talk",rounded(root),height,index,flip=flip,speak=speak,visible=visible)


def add_clean_plate(niche):
    """Keep all of the original compositing coordinates and doorway pixels."""
    source=source_png(STAGE/"S12R-school.png")
    prop=source_png(niche)
    bb=prop.getchannel("A").point(lambda a:255 if a>=112 else 0).getbbox()
    if bb is None or prop.getchannel("A").getextrema()[0] != 0:
        raise ValueError("The added stone source must have real alpha")
    # The top ledge meets the sign at the documented rear support. At this
    # scale the feature belongs to the existing foundation beside the planter.
    prop=prop.crop(bb).resize((130,72),Image.Resampling.LANCZOS)
    shadow=blank()
    shade=ImageDraw.Draw(shadow)
    shade.ellipse((312,575,457,596),fill=(103,53,19,80))
    source=Image.alpha_composite(source,shadow.filter(ImageFilter.GaussianBlur(4)))
    source.alpha_composite(prop,(317,516))
    source.save(STAGE/PLATE,compress_level=4)
    return {"source":niche.name,"origin":[317,516],"size":[130,72],"plate":PLATE}


def school_sign():
    info=level_data("S11L-school-sign")
    row=info["poses"][0]
    return source_png(STAGE/row["file"]),row["anchors"]["stage"]


def socket_stage():
    # Position at the cut between the wood and the grounded pedestal.
    _, anchor=school_sign()
    return (SIGN_STAGE[0] + (SIGN_SOCKET[0]-anchor[0])*SIGN_SCALE,
            SIGN_STAGE[1] + (SIGN_SOCKET[1]-anchor[1])*SIGN_SCALE)


def vector(point,theta):
    # A 2D parallelogram cel slants out of the vertical towards the recess.
    # Contacts use exactly the same matrix as the painted sign.
    rad=math.radians(theta)
    sine,cosine=math.sin(rad),math.cos(rad)
    x,y=point
    q=(x-SIGN_SOCKET[0])*SIGN_SCALE
    h=(SIGN_SOCKET[1]-y)*SIGN_SCALE
    return q*(1-.09*sine) - h*.91*sine, q*.17*sine - h*(cosine+.42*sine)


def location(point,theta,base):
    x,y=vector(point,theta)
    return x+base[0],y+base[1]


REST=socket_stage()
REAR_PIXEL=(35,238)
REAR_SUPPORT=location(REAR_PIXEL,LEAN,REST)
RIGHT_HANDLE=(694,385)
LEFT_HANDLE=(340,361)


def locked_base(theta):
    return tuple(s-v for s,v in zip(REAR_SUPPORT,vector(REAR_PIXEL,theta),strict=True))


@lru_cache(maxsize=1)
def sign_parts():
    source,_=school_sign()
    boundary=[(0,0),(source.width,0),(source.width,783),(455,783),(439,801),
              (304,801),(292,783),(0,783)]
    mast=BODY["isolated"](source,boundary,.5)
    pedestal=BODY["erase"](source,boundary,.5)
    return mast,pedestal


def transform_sign(drawing,theta,base):
    """Inverse-map the authored whole cel so there is no texture relighting jump."""
    if theta==0 and base==REST:
        # Match the native renderer's original registration and resampling.
        _,anchor=school_sign()
        return BODY["blit"](drawing,SIGN_STAGE,84,911,anchor)
    ox,oy=location((0,0),theta,base)
    ax,ay=location((1,0),theta,base)
    bx,by=location((0,1),theta,base)
    a,b,d,e=ax-ox,bx-ox,ay-oy,by-oy
    den=a*e-b*d
    A,B,D,E=e/den,-b/den,-d/den,a/den
    inverse=(A,B,-A*ox-B*oy,D,E,-D*ox-E*oy)
    return drawing.transform(SIZE,Image.Transform.AFFINE,inverse,Image.Resampling.BICUBIC)


def sign_board(theta,base):
    if theta==0 and base==REST:
        source,anchor=school_sign()
        return BODY["blit"](source,SIGN_STAGE,84,911,anchor)
    mast,pedestal=sign_parts()
    above=transform_sign(mast,theta,base)
    result=transform_sign(pedestal,0,REST)
    result.alpha_composite(above)
    return result

def hold_angle(cut,frame):
    if cut==6:
        amount=progress(frame,49,83)
        overshoot=0
        if 83 <= frame < 92:
            overshoot=.9*math.sin((frame-83)/9*math.pi)
        return LEAN*amount+overshoot,REST
    if cut==13:
        theta=blend((LEAN,),(LIFT,),progress(frame,9,68))[0]
        return theta,locked_base(theta)
    if cut==14:
        if frame<62:
            theta=LIFT+(LEAN-LIFT)*progress(frame,10,61)
            return theta,locked_base(theta)
        return LEAN*(1-progress(frame,62,115)),REST
    return LEAN,REST


def sample_frames(length, extra=()):
    return sorted(set(range(0,length,4)) | {length-1} | set(extra))


def exposure(frames,length):
    return [b-a for a,b in zip(frames,frames[1:]+[length])]


def sign_levels():
    settled=Drawings("sign-settled")
    settled.add(sign_board(LEAN,REST),pivot=list(REST),rear_support=list(REAR_SUPPORT),angle=LEAN)
    settled.finish()
    for cut,length,markers in ((6,96,(49,83,92)),(13,192,(9,68,95,157)),(14,216,(10,61,62,115))):
        drawings=Drawings(f"sign-{cut:02d}")
        frames=sample_frames(length,markers)
        for frame in frames:
            theta,base=hold_angle(cut,frame)
            drawings.add(sign_board(theta,base),frame=frame,angle=theta,
                         pedestal=list(REST),axis=list(base),
                         near_handle=list(location(RIGHT_HANDLE,theta,base)),
                         far_handle=list(location(LEFT_HANDLE,theta,base)))
        drawings.finish()
        yield cut,frames,length


def packed(track_name,name,drawings,visible=(0,1),motion="story"):
    frames,length=drawings
    return stage_track(track_name,name,0,last=len(frames)-1,motion=motion,
                       exposures=exposure(frames,length),visible=visible)


def walk(source,frame,total,start,end,height,*,art=SCHOOL, stages=14,flip=False):
    # A painted planted/contact/lift sequence with easing at the endpoints.
    angle=clamp(frame/total)
    phase=round(angle*stages)
    pose=phase % len(level_data(source,art)["poses"])
    root=blend(start,end,smooth(angle))
    return figure(source,pose,root,height,flip,art=art)


def cricket_motion():
    drawings=Drawings("cricket-entry")
    start=CRICKET
    mid=(432,604)
    end=TRAPPED
    frames=sample_frames(96,(9,26,46,53))
    for f in frames:
        if f<8:
            drawing=figure("S12R-cricket-talk",0,start,84,True)
            point=start
        elif f<26:
            point=blend(start,mid,progress(f,8,26))
            drawing=figure("S12R-cricket-walk",(f-8)//4,point,
                           84-7*progress(f,8,26),False)
        elif f<46:
            point=blend(mid,end,progress(f,26,46))
            drawing=figure("S12R-cricket-walk",3+(f-26)//4,point,
                           77-5*progress(f,26,46),False)
        else:
            point=end
            drawing=figure("S12R-cricket-talk",6 if 50<=f<=54 else 0,point,72,True)
        drawings.add(drawing,frame=f,visible_foot_root=list(point))
    drawings.finish()
    yield "entry",frames,96
    for name,length,knots in (("escape",192,((82,TRAPPED),(106,(386,599)),(127,(397,618)),
                                            (140,(406,632)),(172,SIDE_EXIT),(192,SIDE_EXIT))),
                              ("clear",216,((0,SIDE_EXIT),(29,(451,655)),(55,(469,647)),
                                            (89,CRICKET),(216,CRICKET)))):
        drawings=Drawings("cricket-"+name)
        frames=sample_frames(length,tuple(min(length-1,f) for f,_ in knots))
        for f in frames:
            point=knots[0][1]
            moving=False
            for (a,p),(b,q) in zip(knots,knots[1:]):
                if f>=b:
                    point=q
                    continue
                if a<=f<b:
                    point=blend(p,q,progress(f,a,b))
                    moving=p!=q
                break
            height=(72+2*progress(f,84,172)) if name=="escape" else (74+10*progress(f,10,89))
            level="S12R-cricket-walk" if moving else "S12R-cricket-talk"
            drawing=figure(level,(f//4)%8 if moving else (6 if name=="clear" and 133<=f<139 else 0),
                           point,height,True)
            drawings.add(drawing,frame=f,visible_foot_root=list(point),walk=moving)
        drawings.finish()
        yield name,frames,length

# Two painted arm donors are taken from the already staged schoolyard crouch.
# Their wrists and bends are retimed independently; the clothing and both
# shoe contacts stay on the original whole-body drawing.
FAR_EDGE=[(53,105),(63,109),(56,122),(50,140),(42,153),(34,169),(28,178),
          (16,180),(6,177),(3,166),(12,158),(25,158),(31,147),(39,133),(45,123),(46,115)]
NEAR_EDGE=[(90,102),(107,107),(113,120),(107,132),(96,141),(85,151),(71,160),
           (61,157),(59,150),(64,144),(77,137),(85,122),(87,112)]


def planted_crouch(root,touch,grip=0):
    source,anchor,_=source_pose("S12R-pin-low-palm",7)
    # Both cuffs and the original pixel alignment stay on the registered cel.
    image=BODY["padded"](source)
    shift=BODY["offset"]((0,0))[0]
    arm=lambda points:[BODY["offset"](p) for p in points]
    offsets=(-anchor[0]+root[0]-PIN[0]-shift,-anchor[1]+root[1]-PIN[1]-shift)
    local=lambda p:(p[0]-offsets[0],p[1]-offsets[1])
    if grip<=0 or touch is None:
        drawing=blank()
        drawing.alpha_composite(image,rounded(offsets))
        return drawing,()
    body=BODY["erase"](BODY["erase"](image,arm(FAR_EDGE),.9),arm(NEAR_EDGE),.9)
    wrists=[]
    for index,(edge,joints,bias) in enumerate(((FAR_EDGE,((55,112),(44,141),(24,166),(9,171)),-8),
                                                (NEAR_EDGE,((97,114),(94,134),(77,146),(64,150)),8))):
        tip=local(touch[index])
        shoulder,joint,wrist,old_tip=arm(joints)
        target=blend(wrist,(tip[0]+(15 if index==0 else 13),tip[1]-3),grip)
        new_tip=blend(old_tip,tip,grip)
        elbows=(shoulder[0]+(target[0]-shoulder[0])*.47+bias,
                shoulder[1]+(target[1]-shoulder[1])*.55+4)
        elbow=blend(joint,elbows,grip)
        skin=BODY["isolated"](image,arm(edge),.6)
        w,h=image.size
        upper=BODY["isolated"](skin,[(0,0),(w,0),(w,joint[1]+6),(0,joint[1]+6)],.6)
        lower=BODY["isolated"](skin,[(0,joint[1]-8),(w,joint[1]-8),(w,wrist[1]+1),
                                     (0,wrist[1]+1)],.6)
        # The fingers have their own transform, with their painted tip as
        # an actual solved contact rather than an elbow-direction estimate.
        if index==0:
            hand_region=[(4,158),(30,156),(32,172),(21,182),(4,181),(2,170)]
        else:
            hand_region=[(59,145),(66,140),(81,141),(86,150),(80,157),(67,161),(59,157)]
        hand=BODY["isolated"](image,arm(hand_region),.7)
        layer=blank(image.size)
        layer.alpha_composite(BODY["deform"](upper,shoulder,joint,shoulder,elbow,.94))
        layer.alpha_composite(BODY["deform"](lower,joint,wrist,elbow,target,.92))
        layer.alpha_composite(BODY["deform"](hand,wrist,old_tip,target,new_tip,.96))
        if index==0:
            layer.alpha_composite(body)
            body=layer
        else:
            body.alpha_composite(layer)
        wrists.append(tuple(a+b for a,b in zip(target,offsets,strict=True)))
    drawing=blank()
    drawing.alpha_composite(body,rounded(offsets))
    return drawing,wrists


def pin_figure(root=PIN,mode="closed",pose=0,facing="left"):
    if facing=="right":
        return figure("S12R-pin-back-talk",pose,root,236,False,mode)
    return figure("S12R-pin-listen-left",pose,root,236,False,mode)


def pin_sit(root=ASCEND,mode="closed",pose=0):
    return figure("S12R-pin-seat-talk",pose,root,222,True,mode)


def gep_figure(root=GEP,mode="closed",pose=0):
    return figure("S12R-gep-talk",pose,root,315,True,mode)


def blink_layers(constructor, intervals, **kwargs):
    rows=[]
    start=0
    for start_blink,end_blink in intervals:
        rows.append(constructor(visible=(start,start_blink),**kwargs))
        rows.append(constructor(visible=(start_blink,end_blink),blink=True,**kwargs))
        start=end_blink
    rows.append(constructor(visible=(start,1),**kwargs))
    return rows


def adult_approach():
    for cut,length,begin,finish in ((8,60,GEP,(596,594)),
                                    (9,48,(596,594),ADULT_EDGE),
                                    (14,216,ADULT_EDGE,GEP)):
        drawings=Drawings(f"gep-travel-{cut:02d}")
        frames=sample_frames(length,(0,length-1))
        for f in frames:
            if cut==14:
                u=progress(f,115,197)
                steps=(f-115)//6
            else:
                u=progress(f,5,length-5)
                steps=(f-5)//5
            root=blend(begin,finish,u)
            moving=0<u<1
            if moving:
                direction="left" if finish[0]<begin[0] else "right"
                name="S11L-gep-walk-"+direction
                drawing=figure(name,steps,root,315,False,art=SCHOOL)
            else:
                drawing=gep_figure(root)
            drawings.add(drawing,frame=f,feet=list(root),moving=moving)
        drawings.finish()
        yield cut,frames,length


def waiting_actor_levels():
    # The first three poses track the fall from the last C05 mark to a fixed
    # listening posture. The sign does not animate again during the I21 cue.
    child_level=Drawings("pin-sees-tilt")
    frames=sample_frames(96,(19,41,47,53,56))
    for f in frames:
        if f<19:
            key=24
            art=figure("S12O-pin",key,PIN,236)
        elif f<45:
            art=pin_figure(pose=6 if 41<=f<=44 else 0)
        else:
            art=pin_figure(pose=0)
        child_level.add(art,frame=f,feet=list(PIN))
    child_level.finish()
    yield "pin-sees-tilt",frames,96
    for cut,length in ((8,60),(9,48),(10,72),(12,192),(13,192),(14,216)):
        drawing=Drawings(f"pin-action-{cut:02d}")
        markers={8:(12,32,52),9:(12,27,42),10:(8,24,42),
                 12:(12,65,90,111,131,157,171),13:(9,68,95,157),14:(10,61,62,115,128,146,170,203)}[cut]
        frames=sample_frames(length,markers)
        for f in frames:
            wrist=()
            contacts=()
            if cut==8:
                root=blend(PIN,ASCEND,progress(f,12,33))
                if f<12:
                    art=pin_figure(root)
                elif f<33:
                    art=figure("S11L-pin-walk-left",(f-12)//4,root,236,False,art=SCHOOL)
                elif f<52:
                    art=figure("S12R-pin-low-palm",min(3,1+(f-33)//6),
                               (root[0]-PIN[0],root[1]-PIN[1]),720)
                else:
                    art=pin_sit(root)
            elif cut==9:
                root=ASCEND
                if f<12:
                    art=pin_sit(root)
                elif f<27:
                    art=figure("S12R-pin-low-palm",12 if f<21 else 13,
                               (root[0]-PIN[0],root[1]-PIN[1]),720)
                elif f<42:
                    art=pin_figure(root,facing="left")
                else:
                    art=pin_figure(root,facing="right")
            elif cut==10:
                root=ASCEND
                art=pin_figure(root,facing="right" if f<15 else "left",pose=6 if 29<=f<33 else 0)
            elif cut==12:
                root=blend(ASCEND,BESIDE,progress(f,13,77))
                if 13<=f<77:
                    art=figure("S11L-pin-walk-left",(f-13)//6,root,236,False,art=SCHOOL)
                elif f<91:
                    art=pin_figure(root)
                elif f<128:
                    bent=min(7,1+(f-91)//6)
                    art=figure("S12R-pin-low-palm",bent,(root[0]-PIN[0],root[1]-PIN[1]),720)
                else:
                    theta,axis=hold_angle(cut,f)
                    contacts=(location(LEFT_HANDLE,theta,axis),location(RIGHT_HANDLE,theta,axis))
                    art,wrist=planted_crouch(root,contacts,progress(f,129,169))
            elif cut==13:
                root=BESIDE
                theta,axis=hold_angle(cut,f)
                contacts=(location(LEFT_HANDLE,theta,axis),location(RIGHT_HANDLE,theta,axis))
                art,wrist=planted_crouch(root,contacts,1)
            elif cut==14:
                theta,axis=hold_angle(cut,f)
                contacts=(location(LEFT_HANDLE,theta,axis),location(RIGHT_HANDLE,theta,axis))
                if f<=133:
                    root=BESIDE
                    art,wrist=planted_crouch(root,contacts,1-progress(f,121,132))
                elif f<154:
                    root=BESIDE
                    art=figure("S12R-pin-low-palm",min(13,10+(f-133)//6),
                               (root[0]-PIN[0],root[1]-PIN[1]),720)
                elif f<206:
                    u=progress(f,154,205)
                    root=blend(BESIDE,PIN,u)
                    art=figure("S11L-pin-walk-right",(f-154)//6,root,236,False,art=SCHOOL)
                else:
                    root=PIN
                    art=pin_figure(root)
            drawing.add(art,frame=f,feet=list(root),
                        **({"contacts":[list(p) for p in contacts],"wrists":[list(p) for p in wrist]} if wrist else {}))
        drawing.finish()
        yield f"pin-action-{cut:02d}",frames,length


def adult_reach():
    level=Drawings("gep-blocked-reach")
    frames=sample_frames(72,(11,27,34,41,59,69))
    for f in frames:
        amount=progress(f,9,31)*(1-progress(f,41,60))
        arm=None
        if amount>.055:
            arm=blend((500,533),(453,551),amount)
            drawing=BODY["gep"](ADULT_EDGE,315,True,arm,bare=False)
        else:
            drawing=gep_figure(ADULT_EDGE)
        level.add(drawing,frame=f,visible_reach=list(arm) if arm else None,
                  intended_stop="near outer jamb" if arm else None)
    level.finish()
    return frames,72


def compose(moves,boards,cricket,adult,adult_draw):
    def base(shot):
        return [track("door","S11L-school-door"),track("teacher","S11L-teacher",(739,559),193,7)]
    def cro(value):
        return ','.join(map(str,CROPS[value]))
    def hold_sign():
        return stage_track("sign","sign-settled")
    def pin_crouch(speak=False,visible=(0,1)):
        return track("pin","S12R-pin-seat-talk",ASCEND,222,0,flip=True,speak=speak,visible=visible)
    def sign_for(c,scope=(0,1),motion="story"):
        return packed("sign",f"sign-{c:02d}",boards[c],visible=scope,motion=motion)
    def pm(c,scope=(0,1),motion="story"):
        name=f"pin-action-{c:02d}"
        return packed("pin",name,moves[name],visible=scope,motion=motion)
    def traveller(c,scope=(0,1),motion="story"):
        return packed("gep",f"gep-travel-{c:02d}",adult[c],visible=scope,motion=motion)
    def alive(scope=(0,1),speak=False):
        return cricket_static(speak=speak,visible=scope)
    def fore():
        return track("jamb",ARCH)
    def cursor_interval(name, start, end):
        frames,length=cricket[name]
        first=frames.index(start)
        last=frames.index(end)-1 if end<length else len(frames)-1
        return stage_track("cricket","cricket-"+name,first,last=last,motion="story",
                           exposures=exposure(frames,length)[first:last+1],
                           visible=(start/length,end/length))
    before=("lead@0","lead@1")
    after=("lead@1",1)
    shots={
        6: [
            adult_static(),
            track("gust","S12O-leaf",(482,596),12,0,15,"story",active=33,
                  visible=(.01,.30)) | {"drift_x": -154, "drift_y": -18},
            packed("cricket","cricket-entry",cricket["entry"],visible=before,motion="lead"),
            alive(after,True),
            sign_for(6,before,"lead"),
            hold_sign()|{"during":list(after)},
            fore(),
            packed("pin","pin-sees-tilt",moves["pin-sees-tilt"],visible=before,motion="lead"),
            pin_static(visible=after),
        ],
        7: [
            adult_static(),alive(speak=True),hold_sign(),fore(),pin_static()
        ],
        8: [
            traveller(8,before,"lead"),adult_static((596,594),visible=after),
            alive(speak=True),hold_sign(),fore(),
            pm(8,before,"lead"),pin_crouch(True,after),
        ],
        9: [
            traveller(9,before,"lead"),adult_static(ADULT_EDGE,visible=after),
            alive(),hold_sign(),fore(),pm(9,before,"lead"),
            pin_static(ASCEND,"right",True,visible=after),
        ],
        10: [
            packed("gep","gep-blocked-reach",adult_draw,visible=before,motion="lead"),
            adult_static(ADULT_EDGE,True,after),alive(),hold_sign(),fore(),
            pm(10,before,"lead"),pin_static(ASCEND,"left",True,visible=after),
        ],
        11: [
            adult_static(ADULT_EDGE,True),alive(),hold_sign(),fore(),
            *blink_layers(pin_static,[(.16,.193)],root=ASCEND),
        ],
        12: [
            adult_static(ADULT_EDGE),alive(),hold_sign(),fore(),pm(12),
        ],
        13: [
            adult_static(ADULT_EDGE),cursor_interval("escape",0,140),
            sign_for(13),fore(),pm(13),cursor_interval("escape",140,192),
        ],
        14: [
            traveller(14),sign_for(14),fore(),pm(14),packed("cricket","cricket-clear",cricket["clear"]),
        ],
    }
    return [{"id":f"S12-C{n:02d}","plate":f"{PLATE}@{cro(n)}","layout":base(n)+shots[n]}
            for n in sorted(shots)]


def plate_assets(niche):
    record=add_clean_plate(niche)
    # The actual front stones are a separate occlusion overlay. This lets
    # Geppetto's hand disappear behind the side while Cricket is in the niche.
    raw=source_png(niche)
    box=raw.getchannel("A").point(lambda a:255 if a>=112 else 0).getbbox()
    art=raw.crop(box).resize(tuple(record["size"]),Image.Resampling.LANCZOS)
    x,y=record["origin"]
    regular=blank()
    left=BODY["isolated"](art,[(0,14),(20,20),(18,71),(0,72)],.7)
    right=BODY["isolated"](art,[(105,22),(130,14),(130,72),(110,71)],.7)
    regular.alpha_composite(left,(x,y));regular.alpha_composite(right,(x,y))
    level=Drawings("recess-foreground")
    level.add(regular,front_wall_origins=[[x,y],[x+105,y+14]])
    level.finish()
    return record


def main():
    cli=argparse.ArgumentParser(description=__doc__)
    cli.add_argument("--niche",type=Path,default=HERE/"school-niche-source.png")
    args=cli.parse_args()
    STAGE.mkdir(parents=True,exist_ok=True)
    scene=plate_assets(args.niche)
    boards={number:(frames,length) for number,frames,length in sign_levels()}
    insect={key:(frames,length) for key,frames,length in cricket_motion()}
    motion={key:(frames,length) for key,frames,length in waiting_actor_levels()}
    adult={key:(frames,length) for key,frames,length in adult_approach()}
    ready=adult_reach()
    json_out(V3/"build/layout-rescue-full.json",compose(motion,boards,insect,adult,ready))
    json_out(V3/"build/motion-rescue-full.json",{"cuts":{
        "S12-C06":{"lead_frames":96,"tail_frames":12,
                   "marks":{"board_contact":83}},
        "S12-C07":{"lead_frames":24,"tail_frames":12},
        "S12-C08":{"lead_frames":60,"tail_frames":12},
        "S12-C09":{"lead_frames":48,"tail_frames":12},
        "S12-C10":{"lead_frames":72,"tail_frames":12},
        "S12-C11":{"lead_frames":36,"tail_frames":0},
        "S12-C12":{"silent_frames":192},"S12-C13":{"silent_frames":192},"S12-C14":{"silent_frames":216},
    }})
    json_out(HERE/"stage-registration.json",scene|{"socket":list(REST),"rear_pivot":list(REAR_SUPPORT),
        "trapped":list(TRAPPED),"side_exit":list(SIDE_EXIT),"safe_goal":list(CRICKET),
        "close_lean_deg":LEAN,"lift_lean_deg":LIFT,"cricket_clear_before_fall_frame":46,
        "fall_first_frame":49,"lift_settled_before_exit_frame":68,
        "lead_per_cut":{"C06":96,"C08":60,"C10":72},"silent_i21_frames":600})
    print("Wrote native whole-figure registrations and 9 S12 school-rescue cuts.")


if __name__=="__main__":
    main()
