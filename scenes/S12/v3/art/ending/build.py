#!/usr/bin/env python3
"""Register the final eight S12 shots from painted 2D action drawings."""
from copy import deepcopy
from hashlib import file_digest
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from scipy import ndimage

HERE = Path(__file__).resolve().parent
V3 = HERE.parents[1]
BUILD = V3 / "build"
ART = BUILD / "art"
SOURCE = HERE / "source"
HUMAN = HERE.parent / "human/source"
S11 = V3.parents[1] / "S11/v2/build/art"
PLATE = "S11L-school-open.png"
ACTOR = "피노키오"
FAIRY = "파란 요정"
STAGE = (1280, 720)
REST = (561, 643)
GEP = (667, 629)
GEP_SIDE = (872, 628)
CRICKET = (492, 649)
PORTAL = ((667, 311), (781, 309), (782, 551), (666, 553))
LEAF = ((673, 312), (759, 322), (761, 541), (672, 552))
HUMAN_SIZE = (453, 755)
HUMAN_FLOOR = (223, 665)
HUMAN_REF = 583


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write(path, value):
    new = path.with_suffix(".pending")
    new.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    new.replace(path)


def digest(path):
    with path.open("rb") as handle:
        return file_digest(handle, "sha256").hexdigest()


class Drawings:
    def __init__(self, name, height, provenance):
        self.name = name
        self.reference_height = height
        self.folder = ART / "cels" / name
        self.folder.mkdir(parents=True, exist_ok=True)
        self.poses = []
        self.provenance = provenance

    def save(self, image, name, anchors, mouth=None):
        path = self.folder / f"{name}.png"
        image.save(path, compress_level=4)
        row = {"file": str(path.relative_to(ART)), "size": list(image.size),
               "anchors": anchors, "sha256": digest(path)}
        if mouth:
            row["mouth_box"] = list(mouth)
        return row

    def add(self, image, anchors, *, mouths=None, mouth_box=None, action=None):
        i = len(self.poses)
        row = self.save(image, f"{i:02}", anchors, mouth_box)
        row["index"] = i
        if action:
            row["action"] = action
        if mouths:
            row["viseme_cels"] = {name: self.save(drawing, f"{i:02}-{name}", anchors, mouth_box)
                                  for name, drawing in mouths.items()}
        self.poses.append(row)
        return i

    def close(self):
        write(self.folder / "registration.json", {"reference_height": self.reference_height,
              "poses": self.poses, "source": self.provenance})


def painted_cells(file_name):
    palette = Image.open(SOURCE / file_name).convert("RGBA")
    raw = np.array(palette)
    labels, _ = ndimage.label(raw[..., 3] >= 180)
    counts = np.bincount(labels.reshape(-1))
    counts[0] = 0
    extents = ndimage.find_objects(labels)
    components = [extents[i-1] for i in np.argsort(counts)[-8:] if counts[i] >= 20000]
    if len(components) != 8:
        raise ValueError(f"{file_name}: expected eight separate painted cel outlines")
    components.sort(key=lambda item: ((item[0].start + item[0].stop) >= palette.height, item[1].start))
    cells = []
    for rows, cols in components:
        box = (cols.start - 2, rows.start - 2, cols.stop + 2, rows.stop + 2)
        x0,y0,x1,y1 = box
        matte = raw[y0:y1, x0:x1].copy()
        local, number = ndimage.label(matte[...,3]>=180)
        count = np.bincount(local.reshape(-1))
        count[0]=0
        selected = ndimage.binary_dilation(local == np.argmax(count), iterations=1)
        matte[~selected] = 0
        # Remove the disagreeable low-density red/yellow fringe outside the painted cel.
        matte[...,3] = np.where(matte[...,3] >= 70, matte[...,3], 0)
        cells.append((Image.fromarray(matte),box))
    return cells


def aligned_body(image, box, mouth_location):
    silhouette = image.getchannel("A").getbbox()
    scale = HUMAN_REF / (silhouette[3]-silhouette[1])
    width, height = [round(a*scale) for a in image.size]
    art = image.resize((width,height), Image.Resampling.LANCZOS)
    support = np.array(art.getchannel("A"))
    y0 = support.shape[0]-max(9,round(height*.07))
    base_y, base_x = np.nonzero(support[y0:] >= 190)
    root_x = int((np.quantile(base_x,.08)+np.quantile(base_x,.92)) / 2)
    root_y = int(np.quantile(base_y,.97))+y0-3
    dx, dy = HUMAN_FLOOR[0]-root_x,HUMAN_FLOOR[1]-root_y
    whole = Image.new("RGBA",HUMAN_SIZE)
    whole.alpha_composite(art,(dx,dy))
    mouth = (round((mouth_location[0]-box[0])*scale)+dx,
             round((mouth_location[1]-box[1])*scale)+dy)
    return whole,mouth


def speech_variants(body,x,y):
    """Paint the core aperture shapes on whole drawings and keep surrounding lips/cheeks intact."""
    output={}
    region=(x-14,y-5,x+15,y+12)
    # Color is sampled from a clean cheek under the smile. The tiny feathered correction
    # removes the closed crease behind each open drawing.
    fill = body.crop((x-7,y+9,x+13,y+20)).resize((29,17),Image.Resampling.BICUBIC)
    matte=Image.new("L",fill.size)
    ImageDraw.Draw(matte).ellipse((0,1,28,15),fill=242)
    matte=matte.filter(ImageFilter.GaussianBlur(1.7))
    for name,h,w in (("small",5,19),("wide",9,21),("round",9,12),("pressed",3,15)):
        viseme=body.copy()
        stage=Image.new("RGBA",body.size)
        stage.paste(fill,(region[0],region[1]),matte)
        draw=ImageDraw.Draw(stage)
        left=x-w//2
        top=y-1
        draw.ellipse((left,top,left+w,top+h),fill=(91,40,28,255))
        if name=="wide":
            draw.arc((left+1,top+1,left+w-1,top+h-1),195,346,fill=(233,190,151,240),width=2)
            draw.arc((left+3,top+3,left+w-3,top+h),30,150,fill=(179,91,75,230),width=2)
        elif name=="small":
            draw.arc((left+2,top+1,left+w-1,top+h),190,337,fill=(221,160,118,242),width=1)
        stage=stage.filter(ImageFilter.GaussianBlur(.45))
        viseme.alpha_composite(stage)
        output[name]=viseme
    return output,(x-17,y-10,x+18,y+15)


def register_actions():
    level = Drawings("S12K-human-acting",HUMAN_REF,
                     {f: digest(SOURCE/f) for f in ["human-actions-sheet.png"]}|{"approved":digest(HUMAN/"open.png")})
    def stash(im, xy, note):
        vis, bounds = speech_variants(im,*xy)
        level.add(im,{"stage":list(HUMAN_FLOOR)},mouths=vis,mouth_box=bounds,action=note)
    open_pose=Image.open(HUMAN/"open.png").convert("RGBA")
    stash(open_pose,(300,267),"locked neutral continuity from C42")
    mouths=((312,134),(726,128),(1146,136),(1558,130),(297,570),(720,567),(1117,581),(1560,579))
    notes=("lower arms","looks up toward fairy","hand-to-heart bow","begins lifting hand",
           "wave to fairy outward","wave to fairy inward","second wave to Yoonsu","checks bag strap")
    fitted=[]
    for (im,box),mouth,note in zip(painted_cells("human-actions-sheet.png"),mouths,notes,strict=True):
        art,point=aligned_body(im,box,mouth)
        fitted.append((art,point))
        stash(art,point,note)
    front, xy = fitted[6]
    # The child turns to ask the audience while both hands remain down before P09.
    neutral = fitted[0][0].copy()
    head_matte = Image.new("L",HUMAN_SIZE)
    ImageDraw.Draw(head_matte).polygon([(65,0),(440,0),(440,299),(320,319),(198,317),(65,310)],fill=255)
    head_matte=head_matte.filter(ImageFilter.GaussianBlur(2))
    artwork=Image.composite(front,neutral,head_matte)
    stash(artwork,xy,"turns to Yoonsu with arms lowered; no early wave")
    level.close()


def polygon(size, points):
    mask=Image.new("L",size)
    ImageDraw.Draw(mask).polygon(points,fill=255)
    return mask


def redraw_door():
    school=Image.open(ART/PLATE).convert("RGBA")
    lobby=Image.open(SOURCE/"school-interior.png").convert("RGBA")
    crop=(662,306,788,557)
    width,height=crop[2]-crop[0],crop[3]-crop[1]
    offset=lambda points:tuple((x-crop[0],y-crop[1]) for x,y in points)
    corridor=ImageEnhance.Brightness(lobby.resize((width,height),Image.Resampling.LANCZOS)).enhance(.58)
    inside=polygon((width,height),offset(PORTAL))
    old=school.crop(crop)
    leaf=old.copy()
    leaf_mask=polygon((width,height),offset(LEAF))
    leaf.putalpha(leaf_mask)
    level=Drawings("S12K-opening-door",720,
                   {"exterior":digest(ART/PLATE),"painted_interior":digest(SOURCE/"school-interior.png")})
    level.add(Image.composite(old,Image.new("RGBA",(width,height)),inside),
              {"stage":[-crop[0],-crop[1]]},action="exact school door at cut-in")
    # Project the painted exterior face to progressively narrower, hinged facets.
    # The right edge recedes up the classroom sill and the hinge stays in world space.
    src_points=offset(LEAF)
    for n in range(1,13):
        t = n/12
        amount=t*t*(3-2*t)
        top_x = round(759-68*amount)
        end=((673,312),(top_x,round(322+15*amount)),(top_x,round(541-15*amount)),(672,552))
        canvas=Image.composite(corridor,Image.new("RGBA",(width,height)),inside)
        dst_points=offset(end)
        system=[]
        values=[]
        for (u,v),(x,y) in zip(src_points,dst_points,strict=True):
            system.append([x,y,1,0,0,0,-u*x,-u*y]); values.append(u)
            system.append([0,0,0,x,y,1,-v*x,-v*y]); values.append(v)
        coefficients=np.linalg.solve(np.array(system,float),np.array(values,float))
        door=leaf.transform((width,height),Image.Transform.PERSPECTIVE,coefficients,
                            resample=Image.Resampling.BICUBIC)
        canvas.alpha_composite(door)
        canvas.putalpha(inside)
        level.add(canvas,{"stage":[-crop[0],-crop[1]]},
                  action=f"inward swing {n}/12, fixed left hinge")
    level.close()


def approved_level(name,new_name):
    src=read(S11/"cels"/name/"registration.json")
    dst=ART/"cels"/new_name
    dst.mkdir(parents=True,exist_ok=True)
    for i,pose in enumerate(src["poses"]):
        alias=dst/f"{i:02}.png"
        if not alias.exists():
            alias.hardlink_to(S11/pose["file"])
        pose["file"]=str(alias.relative_to(ART))
        pose.pop("viseme_cels",None)
    write(dst/"registration.json",src)
    return src


def project(image,point,world,shown_height,*,portal=False,shade=1):
    picture=image.resize(tuple(round(a*shown_height/HUMAN_REF) for a in image.size),
                         Image.Resampling.LANCZOS)
    if shade<.999:
        picture=ImageEnhance.Brightness(picture).enhance(shade)
    x=round(world[0]-point[0]*shown_height/HUMAN_REF)
    y=round(world[1]-point[1]*shown_height/HUMAN_REF)
    canvas=Image.new("RGBA",STAGE)
    canvas.alpha_composite(picture,(x,y))
    if portal:
        # The jamb and header occlude only a child already behind the stone threshold.
        opening=polygon(STAGE,((692,311),(781,309),(782,551),(688,553)))
        alpha=canvas.getchannel("A")
        canvas.putalpha(Image.fromarray((np.array(alpha,dtype=np.uint16)*np.array(opening)//255).astype(np.uint8)))
    return canvas


def crop_stage(level, canvas, note):
    box=canvas.getchannel("A").getbbox()
    if not box:
        # A completely occluded child no longer needs a stage layer.
        return None
    x0,y0,x1,y1=box
    image=canvas.crop((x0-2,y0-2,x1+2,y1+2))
    return level.add(image,{"stage":[2-x0,2-y0]},action=note)


def register_entry():
    refs=[(266,414),(614,414),(1148,411),(1572,417),
          (286,830),(716,846),(1113,852),(1520,855)]
    sheet=painted_cells("human-gait-sheet.png")
    cells=[]
    for (im, box), (px,py) in zip(sheet,refs,strict=True):
        bbox=im.getchannel("A").getbbox()
        scale=HUMAN_REF/(bbox[3]-bbox[1])
        pix=im.resize((round(im.width*scale),round(im.height*scale)),Image.Resampling.LANCZOS)
        pivot=(round((px-box[0])*scale),round((py-box[1])*scale))
        cells.append((pix,pivot))
    level=Drawings("S12K-walking-child",720,
                   {"sheet":digest(SOURCE/"human-gait-sheet.png"),"current_character":digest(HUMAN/"open.png")})
    beats=[
        (0,(590,637),236,False,1.0,10,"child rocks onto the first supporting foot"),
        (1,(558,637),235,False,1.0,7,"right heel reaches from the rear toe"),
        (2,(606,625),230,False,1.0,8,"right sole receives weight"),
        (3,(606,625),230,False,1.0,8,"left boot passes above the ground"),
        (4,(651,610),222,False,1.0,9,"left heel makes the next contact"),
        (5,(651,610),222,False,1.0,8,"left sole carries weight"),
        (6,(651,610),222,False,1.0,8,"right foot crosses the left support"),
        (7,(651,610),222,False,1.0,8,"right boot reaches toward stone"),
        (4,(693,584),203,False,1.0,8,"the next heel lands on the approach"),
        (5,(693,584),203,False,1.0,8,"weight arrives on that foot"),
        (6,(693,584),203,False,1.0,8,"free leg clears the raised school sill"),
        (7,(693,584),203,False,1.0,8,"knee rises for the actual threshold"),
        (0,(751,556),171,False,.93,8,"forefoot lands on the real top of the sill"),
        (2,(749,551),165,True,.76,8,"weight transfers past the outer jamb"),
        (3,(749,551),162,True,.69,8,"trailing boot clears the school threshold"),
        (4,(754,545),153,True,.65,8,"the first room step lands inside"),
        (5,(754,545),152,True,.61,8,"child looks forward from within the classroom"),
        (6,(754,545),149,True,.58,8,"next boot lifts in the shaded room"),
        (7,(766,538),144,True,.55,8,"last over-the-shoulder view as human enters"),
        (4,(756,532),137,True,.53,9,"opposite sole touches the shaded passage"),
        (5,(756,532),137,True,.52,9,"child's weight settles on that floor tile"),
        (6,(756,532),136,True,.51,10,"rear boot swings down the classroom aisle"),
        (7,(756,532),131,True,.50,10,"next heel reaches farther inside"),
        (4,(754,520),122,True,.48,11,"next interior footfall, shorter in perspective"),
        (5,(754,520),122,True,.47,12,"both eyes toward the classroom"),
        (6,(754,520),120,True,.46,8,"continues the last step from C49"),
        (7,(754,520),118,True,.44,8,"passing boot points to the classroom side passage"),
        (4,(773,513),112,True,.43,8,"next footfall recedes into the doorway shadow"),
        (5,(784,509),109,True,.41,9,"last dark shirt and hat silhouette clears the jamb"),
    ]
    for idx,point,height,behind,shade,length,note in beats:
        im,pivot=cells[idx]
        view=project(im,pivot,point,height,portal=behind,shade=shade)
        if crop_stage(level,view,note) is None:
            raise ValueError("Entry schedule failed: child must remain visible until the last stride")
    level.close()
    return [row[5] for row in beats]


def register_sky_and_end():
    cloud=Image.open(SOURCE/"cloud-paint.png").convert("RGBA")
    cloud=cloud.crop(cloud.getchannel("A").point(lambda a:255 if a>80 else 0).getbbox())
    cloud.thumbnail((190,58), Image.Resampling.LANCZOS)
    alpha=cloud.getchannel("A").point(lambda a:round(a*.55))
    cloud.putalpha(alpha)
    sky=Drawings("S12K-cloud",cloud.height,{"painted_cloud":digest(SOURCE/"cloud-paint.png")})
    # The cloud is a slightly modulated painted cel, with the drift carried by its stage roots.
    for i in range(9):
        drawing=cloud.resize((cloud.width+i//4,cloud.height),Image.Resampling.BICUBIC)
        sky.add(drawing,{"stage":[0,0]},action="wisps crossing clear sky")
    sky.close()
    title=Drawings("S12K-end-title",130,{"text":"The End","position":"after original U044"})
    for opacity in (25,55,90,123,157,195,227,247,255):
        canvas=Image.new("RGBA",(410,130))
        font=ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",57)
        draw=ImageDraw.Draw(canvas)
        draw.text((205,67),"The End",anchor="mm",font=font,fill=(255,230,168,opacity),
                  stroke_width=2,stroke_fill=(89,49,20,round(opacity*.9)))
        title.add(canvas,{"stage":[205,65]},action="short end title fade")
    title.close()


def hold(track,level,root,height,cel=0,**extra):
    return {"track":track,"level":level,"root":list(root),"height":height,"anchor":"stage",
            "first_cel":cel,"motion":"hold",**extra}


def act(track,level,root,height,first,last,exposures,**extra):
    return {"track":track,"level":level,"root":list(root),"height":height,"anchor":"stage",
            "first_cel":first,"last_cel":last,"motion":"story","exposure_frames":exposures,**extra}


def broad(number, layers, crop=None, camera=None):
    shot={"id":f"S12-C{number}","plate":PLATE if not crop else PLATE+"@"+",".join(map(str,crop)),
          "layout":layers}
    if camera:
        shot["camera_cues"]=camera
    return shot


def stretch_cels(level,track,root,height,cels,bounds,*,mouth=False):
    rows=[]
    for index, (start, stop) in zip(cels,zip(bounds[:-1],bounds[1:]),strict=True):
        # S11 camera resolves boundaries against each edited shot.
        option={"during":[start,stop]}
        if mouth:
            option["mouth"]={"speaker":ACTOR}
        rows.append(hold(track,level,root,height,index,**option))
    return rows


def fraction(frame,denominator=1):
    return f"lead@{frame/denominator:.12f}"


def layouts(entry):
    door=hold("door","S12F-door",(0,0),720)
    open_door=hold("door","S12K-opening-door",(0,0),720,12)
    teacher=hold("teacher","S12F-teacher",(739,559),193,7)
    side_teacher=hold("teacher","S12RL-teacher-yield",(710,565),193,5,anchor="support")
    sign=hold("guideboard","S12F-sign",(413,597),84)
    gep=hold("Grandpa","S12F-gep-quiet",GEP,315,2)
    gep_side=hold("Grandpa","S12K-gep-end-wave",GEP_SIDE,315,0)
    cricket=hold("Cricket","S12F-cricket-acting",CRICKET,84,2,flip=True)
    fairy=hold("Fairy","S12FL-talking",(831,442),122,flip=True,mouth={"speaker":FAIRY})
    far_fairy=hold("Fairy","S12FL-talking",(903,143),64,flip=True)
    actor="S12K-human-acting"
    pin=lambda cel,**opts:hold("child",actor,REST,236,cel,**opts)
    base=[door,teacher,sign,gep,cricket]
    shots=[]

    lead43=36
    shot43=[door,teacher,sign,
            hold("Grandpa","S12H-gep-palms-demo",GEP,315,0,during=[0,fraction(10,lead43)]),
            gep|{"during":[fraction(10,lead43),1]},
            hold("Cricket","S12G-cricket-jump",(0,0),720,21,during=[0,fraction(10,lead43)]),
            cricket|{"during":[fraction(10,lead43),1]},
            hold("Fairy","S12F-wand",(831,442),122,14,during=[0,fraction(9,lead43)]),
            fairy|{"during":[fraction(9,lead43),1]},pin(0,during=[0,fraction(11,lead43)]),
            pin(1,during=[fraction(11,lead43),fraction(22,lead43)]),
            pin(2,span=[f"lead-point:{22/lead43}","after:S12-U034"]),
            pin(3,span=["after:S12-U034","before:S12-U035"]),
            pin(2,span=["before:S12-U035","end"],mouth={"speaker":ACTOR})]
    shots.append(broad(43,shot43,[423,277,700]))

    lower=act("Fairy","S12FL-lower",(831,442),122,0,7,[3,4,4,5,5,5,6,7],flip=True)
    final_cel44=9
    shot44=[*base,lower,*stretch_cels(actor,"child",REST,236,[2,1,final_cel44],
                                        [0,fraction(13,60),fraction(31,60),1],mouth=True)]
    shots.append(broad(44,shot44,[434,265,722]))

    fairy_motion=read(HERE.parent/"fairy/late-fairy-support.json")["layers"]["S12-C45"]
    wave=fairy_motion["wave"]
    retreat=fairy_motion["retreat"]
    near_hold=hold("Fairy","S12FL-lower",(831,442),122,7,flip=True,during=[0,fraction(32,168)])
    fairy_wave=act("Fairy",wave["level"],wave["root"],wave["height"],wave["first_cel"],wave["last_cel"],
                   wave["exposure_frames"],flip=True,during=[fraction(32,168),fraction(59,168)])
    fairy_retreat=act("Fairy",retreat["level"],retreat["root"],retreat["height"],retreat["first_cel"],
               retreat["last_cel"],retreat["exposure_frames"],root_offsets=retreat["root_offsets"],
               flight=retreat["flight"],during=[fraction(59,168),fraction(136,168)])
    cast=[9,1,4,5,6,5,6,5,4,1,9,7]
    marks=[0,7,17,27,37,48,60,72,85,98,115,142]
    seq=stretch_cels(actor,"child",REST,236,cast,[*(fraction(x,168) for x in marks),1],mouth=True)
    shots.append(broad(45,[*base,near_hold,fairy_wave,fairy_retreat,
              far_fairy|{"during":[fraction(136,168),1]},*seq]))

    door_move=act("door","S12K-opening-door",(0,0),720,0,12,[7,4,4,4,4,4,4,4,4,4,4,5,6])
    adult_walk=[]
    adult_positions=[(667,629),(683,630),(700,628),(720,629),(741,628),(760,629),
                     (782,627),(801,628),(821,627),(840,628),(857,628),(872,628)]
    step_poses=(0,1,2,3,4,5,6,1,2,3,4,7)
    adult_time=(4,11,17,23,29,35,41,47,53,59,64,69,74)
    for i,(pos,p) in enumerate(zip(adult_positions,step_poses,strict=True)):
        adult_walk.append(hold("Grandpa","S12K-gep-walk",pos,315,p,
                        during=[fraction(adult_time[i],84),fraction(adult_time[i+1],84)]))
    shot46=[door_move,teacher,sign,cricket,far_fairy,gep|{"during":[0,fraction(4,84)]},
        *adult_walk,gep_side|{"during":[fraction(74,84),1]},
        *stretch_cels(actor,"child",REST,236,[7,9,1,2,1],
                      [0,fraction(14,84),fraction(25,84),fraction(44,84),fraction(73,84),1])]
    shots.append(broad(46,shot46,[309,171,927]))

    base_late=[open_door,teacher,sign,gep_side,cricket,far_fairy]
    shot47=[*base_late,*stretch_cels(actor,"child",REST,236,[1,8,8,1],
                     [0,fraction(12,24),fraction(24,24),"story@0.5800000000",1])]
    shots.append(broad(47,shot47,[456,272,750]))

    # Supportive look to the door, one close-up-to-wide cut. No child locomotion before C49.
    late_no_fairy=[open_door,teacher,sign,gep_side,cricket]
    shot48=[*late_no_fairy,far_fairy|{"mouth":{"speaker":FAIRY}},
            *stretch_cels(actor,"child",REST,236,[1,2,1],[0,fraction(11,36),fraction(29,36),1])]
    shots.append(broad(48,shot48,[211,68,1050]))

    yield_spec=read(BUILD/"teacher-support.json")["teacher_layers"]
    yield_layers=[]
    for row in yield_spec:
        row=deepcopy(row)
        final=row["first_cel"]==5
        row["during"]=[f"lead@{float(p.removeprefix('lead@'))*96/148:.12f}" if isinstance(p,str) else p
                       for p in row["during"]]
        if final:
            row["root"]=[710,565]
        yield_layers.append(row)
    # The step sequence is separately exposed and spatially registered in each drawing.
    # Once the child is through the sill the same teacher now draws in front
    # of the corridor silhouette. Before that step he walks in front of her.
    initial_lengths=entry[:13]
    inside_lengths=entry[13:25]
    exposure_start=12
    stride_sum=sum(initial_lengths)
    first_stride=act("child","S12K-walking-child",(0,0),720,0,12,initial_lengths,
                     during=[fraction(exposure_start,148),fraction(exposure_start+stride_sum,148)])
    inside_stride=act("child","S12K-walking-child",(0,0),720,13,24,inside_lengths,
                       during=[fraction(exposure_start+stride_sum,148),1])
    shot49=[open_door,sign,gep_side,cricket,far_fairy,inside_stride,*yield_layers,
        pin(1,during=[0,fraction(exposure_start,148)]),first_stride]
    shots.append(broad(49,shot49,camera=[{"frame":0,"crop":[387,211,830]},
        {"frame":55,"crop":[421,225,815],"interpolate":True},
        {"frame":134,"crop":[438,210,825],"interpolate":True}]))

    gep_goodbye=act("Grandpa","S12K-gep-end-wave",GEP_SIDE,315,0,3,[12,12,14,16],flip=False)
    cloud=act("sky-cloud","S12K-cloud",(465,35),42,0,8,[10,10,10,11,11,11,11,11,12],
              drift_x=36,drift_y=-4,flight=[0,8])
    curtain=act("end-title","S12K-end-title",(640,176),130,0,8,[3,3,3,3,3,3,3,3,3],
                span=["after:S12-U044","end"])
    exit_motion=act("child-inside","S12K-walking-child",(0,0),720,24,28,[4,*entry[25:]],
                    during=[0,"lead@0.770833333333"])
    cricket_at_end=act("Cricket","S12F-cricket-acting",CRICKET,84,2,4,[12,7,10],flip=True)
    shot50=[cloud,open_door,exit_motion,side_teacher,sign,gep_goodbye,cricket_at_end,curtain]
    shots.append(broad(50,shot50,camera=[{"frame":0,"crop":[338,175,918]},
        {"frame":84,"crop":[0,0,1280],"interpolate":True}]))
    return shots


def main():
    register_actions()
    redraw_door()
    approved_level("S11L-gep-walk-right","S12K-gep-walk")
    approved_level("S11L-gep-wave","S12K-gep-end-wave")
    entry=register_entry()
    register_sky_and_end()
    result=layouts(entry)
    write(BUILD/"layout-ending.json",result)
    write(BUILD/"motion-ending.json",{"cuts":{
        "S12-C43":{"lead_frames":36,"tail_frames":12,"between_frames":{"S12-U034":22}},
        "S12-C44":{"lead_frames":60,"tail_frames":0},
        "S12-C45":{"lead_frames":168,"tail_frames":12},
        "S12-C46":{"lead_frames":84,"tail_frames":24},
        "S12-C47":{"lead_frames":24,"tail_frames":12},
        "S12-C48":{"lead_frames":36,"tail_frames":24},
        "S12-C49":{"lead_frames":148,"tail_frames":48},
        "S12-C50":{"lead_frames":48,"tail_frames":120},
    }})
    print("Registered actual hallway, walking, farewell, and closing cels for S12-C43–C50.")


if __name__=="__main__":
    main()
