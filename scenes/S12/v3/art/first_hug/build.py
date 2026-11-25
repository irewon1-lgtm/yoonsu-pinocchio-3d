"""Photograph S12 C31–C34 with registered native whole cels and the measured dialogue clock."""

from functools import lru_cache
from hashlib import file_digest
import json
from math import radians
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageOps
import numpy as np
from scipy.ndimage import map_coordinates

HERE = Path(__file__).resolve().parent
V3 = HERE.parents[1]
BUILD = V3 / "build"
ART = BUILD / "art"
HUMAN = HERE.parent / "human/source"
STAGE = (1280, 720)
HERO_ROOT, ADULT_ROOT, CRICKET_ROOT = (561, 643), (667, 629), (510, 649)
CRICKET_LANDED = (492, 649)
HERO_HEIGHT, ADULT_HEIGHT, CRICKET_HEIGHT = 236, 315, 84
FPS = 24
MODES = ("small", "wide", "round", "pressed", "teeth")
SPEAKERS = {"hero": "피노키오", "adult": "제페토", "cricket": "귀뚜라미"}
MOTION = {
    "S12-C31": {"lead_frames": 7, "tail_frames": 6},
    "S12-C32": {"lead_frames": 12, "tail_frames": 12},
    "S12-C33": {"lead_frames": 108, "tail_frames": 12,
                "marks": {"hug_hand_contact": 70, "hug_joint_settle": 98}},
    "S12-C34": {"lead_frames": 24, "tail_frames": 84,
                "marks": {"cricket_landed": 28, "hug_release_complete": 135}},
}


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path):
    with path.open("rb") as handle:
        return file_digest(handle, "sha256").hexdigest()


def write(path, value):
    temporary = path.with_suffix(".pending")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temporary.replace(path)


def stage():
    return Image.new("RGBA", STAGE)


@lru_cache(maxsize=None)
def source_pose(level, index):
    registry = read(ART / "cels" / level / "registration.json")
    pose = registry["poses"][index]
    with Image.open(ART / pose["file"]) as source:
        return source.convert("RGBA"), pose, registry


def placed(image, root, height, reference, anchor, flip=False):
    scale = height / reference
    draw = image.resize(tuple(round(side * scale) for side in image.size), Image.Resampling.LANCZOS)
    x, y = (round(number * scale) for number in anchor)
    if flip:
        draw = ImageOps.mirror(draw)
        x = draw.width - 1 - x
    left, top = round(root[0] - x), round(root[1] - y)
    result = stage()
    result.alpha_composite(draw, (left, top))
    return result, (left, top, scale)


def rect_stage(rect, frame):
    x, y, ratio = frame
    left, top, right, bottom = rect
    return tuple(round(base + position * ratio) for base, position in
                 zip((x, y, x, y), (left, top, right, bottom), strict=True))


class Level:
    """Bake transparent whole pose/viseme cels in shared stage coordinates."""

    def __init__(self, slug, origin):
        self.name = "S12G-" + slug
        self.directory = ART / "cels" / self.name
        self.directory.mkdir(parents=True, exist_ok=True)
        self.origin = origin
        self.poses = []

    def save(self, image, index, suffix="", mouth=None):
        box = image.getchannel("A").getbbox()
        if box is None:
            raise ValueError(f"Empty pose {self.name}/{index}")
        left, top, right, bottom = box
        left, top, right, bottom = left - 3, top - 3, right + 3, bottom + 3
        cel = image.crop((left, top, right, bottom))
        path = self.directory / f"{index:03d}{suffix}.png"
        cel.save(path, compress_level=4)
        record = {"file": path.relative_to(ART).as_posix(), "size": list(cel.size),
                  "anchors": {"stage": [-left, -top]}, "sole": [-left, -top],
                  "stage_bounds": list(box), "sha256": digest(path)}
        if mouth:
            x0, y0, x1, y1 = mouth
            record["mouth_box"] = [x0-left, y0-top, x1-left, y1-top]
        return record

    def add(self, image, action, *, variants=None, mouth=None, **details):
        index = len(self.poses)
        pose = self.save(image, index, mouth=mouth)
        if variants:
            pose["viseme_cels"] = {mode: self.save(drawing, index, "-" + mode, mouth)
                                   for mode, drawing in variants.items()}
        pose.update(index=index, action=action, **details)
        self.poses.append(pose)
        return index

    def finish(self):
        write(self.directory / "registration.json",
              {"level": self.name, "reference_height": 720, "source": self.origin, "poses": self.poses})
        return self.name


def smooth(x):
    clipped = np.clip(x, 0, 1)
    return clipped*clipped*(3-2*clipped)


def warp_rgba(image, dx, dy):
    """Transport painted pigment and alpha together while moving actual joints."""
    raw = np.asarray(image, dtype=np.float32)/255
    yy, xx = np.indices(raw.shape[:2], dtype=np.float32)
    opacity = raw[..., 3]
    coordinates = (yy - dy, xx - dx)
    alpha = map_coordinates(opacity, coordinates, order=1, mode="constant", prefilter=False)
    denominator = np.maximum(alpha, 1e-5)
    channels = [map_coordinates(raw[..., index]*opacity, coordinates, order=1, mode="constant",
                                prefilter=False) / denominator for index in range(3)]
    return Image.fromarray(np.rint(255 * np.stack((*channels, alpha),axis=2).clip(0, 1)).astype(np.uint8))


def oral_pose(image, centre, figure, mode, fit=1.0):
    """Paint the oral interior on the motion drawing without moving face or silhouette."""
    x, y = centre
    if figure == "hero":
        rx, ry, cavity, lip, tooth, tongue = 12, 8, "#4e2420", "#a65239", "#ffe0b8", "#b55d48"
    elif figure == "adult":
        rx, ry, cavity, lip, tooth, tongue = 13, 7, "#482a21", "#a06a4f", "#e6cba8", "#a26455"
    else:
        rx, ry, cavity, lip, tooth, tongue = 13, 7, "#4e3718", "#92792d", "#e4d18a", "#a68a38"
    # Replace only the oral interior in whole cels. Existing painted cheek and moustache remain attached.
    patterns = {"small": (.65, .50), "wide": (1, .90), "round": (.49, 1.0),
                "pressed": (.58, .20), "teeth": (.95, .55)}
    sx, sy = patterns[mode]
    rx, ry = rx*fit, ry*fit
    w, h = rx*sx, ry*sy
    scale = 4
    area = (round(x-rx-3), round(y-ry-3), round(x+rx+4), round(y+ry+4))
    stroke = Image.new("RGBA", ((area[2]-area[0])*scale, (area[3]-area[1])*scale))
    draw = ImageDraw.Draw(stroke)
    tx, ty = (x-area[0])*scale, (y-area[1])*scale
    def box(xs, ys, xe, ye):
        return tuple(round(value) for value in (tx+xs*scale,ty+ys*scale,tx+xe*scale,ty+ye*scale))
    if mode == "pressed":
        draw.arc(box(-w,-1.5,w,1.5), 15, 165, fill=lip, width=4)
    else:
        draw.ellipse(box(-w,-h,w,h),fill=lip)
        draw.ellipse(box(-w+.8,-h+.35,w-.8,h-.7),fill=cavity)
        if mode in ("wide","teeth"):
            draw.rounded_rectangle(box(-.71*w,-.67*h,.60*w,-.24*h), radius=scale, fill=tooth)
        if mode in ("wide","round") and figure != "cricket":
            draw.ellipse(box(-.44*w,.33*h,.52*w,.82*h),fill=tongue)
    stroke = stroke.resize((area[2]-area[0],area[3]-area[1]),Image.Resampling.LANCZOS)
    result = image.copy()
    result.alpha_composite(stroke, area[:2])
    return result, area


def human_pose(base, anchors, amount, nod):
    """Shift the lower arms and turn the head over an entirely grounded pelvis."""
    yy, xx = np.indices((base.height, base.width), dtype=np.float32)
    near_hand = anchors["near_wrist"]
    far_hand = anchors["far_wrist"]
    near = np.exp(-(((xx-near_hand[0])/35)**2 + ((yy-near_hand[1])/70)**2))
    far = np.exp(-(((xx-far_hand[0])/55)**2 + ((yy-far_hand[1])/62)**2))
    below_cuff = smooth((yy-353)/84)
    above_hips = smooth((504-yy)/36)
    near_quad = near*below_cuff*above_hips
    far_quad = far*below_cuff*above_hips
    neck_x, neck_y = anchors["neck"]
    cap = smooth((321-yy)/34)
    rot = radians(nod)
    dx = amount*(-18*near_quad+20*far_quad) - rot*(yy-neck_y)*cap
    dy = amount*(-24*near_quad-38*far_quad) + rot*(xx-neck_x)*cap
    drawing = warp_rgba(base,dx,dy) if amount or nod else base.copy()
    mouth_x,mouth_y = anchors["mouth"]
    mouth = (mouth_x - rot*(mouth_y-neck_y), mouth_y+rot*(mouth_x-neck_x))
    return drawing,mouth


def human_bases():
    model = read(HUMAN / "registration.json")
    if not (HUMAN / "open.png").is_file():
        raise FileNotFoundError("Waiting for exact human eye-open source.")
    with Image.open(HUMAN / model["closed"]) as closed, Image.open(HUMAN / "open.png") as opened:
        assert opened.size == closed.size
        return model, closed.convert("RGBA"), opened.convert("RGBA")


def revelation(model, closed, opened):
    level = Level("first-revelation", {"human": model["closed_sha256"], "open": digest(HUMAN / "open.png")})
    painted = {}
    for mode in ("small", "wide"):
        with Image.open(HUMAN / f"speech-{mode}.png") as original:
            painted[mode] = original.convert("RGBA")
    frames = (
        (2, 0.00,  0.0, 0.00, "inherited pupils closed"),
        (2, 0.00,  2.0, 0.52, "eyelids lift towards chest"),
        (3, 0.00,  4.7, 1.00, "recognizes the new body"),
        (3, 0.05,  3.1, 1.00, "turns attention first to Grandpa"),
        (4, 0.15,  1.0, 1.00, "raises the face"),
        (6, 0.37, -1.2, 1.00, "Grandpa call lifts shoulders"),
        (8, 0.60, -2.6, 1.00, "opens the two forearms"),
        (10,0.75, -3.5, 1.00, "elbows and wrists present the new body"),
        (13,0.91, -4.0, 1.00, "Look at me expression"),
        (12,0.95, -3.4, 1.00, "holds Grandpa's eyeline"),
        (9, 0.86, -2.3, 1.00, "joy settles into amazement"),
        (10,0.77, -0.8, 1.00, "brief return glance"),
        (8, 0.90, -1.9, 1.00, "real boy realization"),
        (15,1.00, -3.7, 1.00, "renewed delighted presentation"),
        (12,0.79, -2.5, 1.00, "arms ease from the widest point"),
        (12,0.62, -1.7, 1.00, "invites Grandpa's answer"),
        (11,0.55, -1.4, 1.00, "quiet attentive pose"),
    )
    for _, raised, nod, pupils_open, action in frames:
        base = opened if pupils_open == 1 else closed if pupils_open == 0 else Image.blend(closed,opened,pupils_open)
        drawing,mouth_at = human_pose(base, model["anchors"], raised, nod)
        picture, placement = placed(drawing,HERO_ROOT,HERO_HEIGHT,model["reference_height"],model["anchors"]["stage"])
        variants, mouth = {}, None
        if pupils_open == 1:
            for mode in MODES:
                alternate, area = oral_pose(drawing,mouth_at,"hero",mode)
                if mode in painted:
                    alternate, _ = human_pose(painted[mode], model["anchors"], raised, nod)
                variants[mode] = placed(alternate,HERO_ROOT,HERO_HEIGHT,model["reference_height"],model["anchors"]["stage"])[0]
                mouth = rect_stage(area,placement)
        level.add(picture,action,variants=variants,mouth=mouth, soles=[model["anchors"]["left_heel"],model["anchors"]["right_heel"]])
    return level.finish(), [frame[0] for frame in frames]


def invitation_adjust(image, pose):
    """Open the forearm on the low plane, leaving the younger child's face clear."""
    if pose<4:
        return image
    yy,xx=np.indices((image.height,image.width),dtype=np.float32)
    position=smooth((169-xx)/45)*np.exp(-((yy-232)/65)**2)
    position*=smooth((yy-155)/35)*smooth((339-yy)/47)
    weight={4:.11,5:.48,6:.82,7:1}[pose]
    return warp_rgba(image,13*weight*position,64*weight*position)


def response():
    original = "S12H-gep-surprise-open"
    level = Level("grandpa-recognition", {"whole_drawings": original})
    # The painted jaw in each native response source has its own placement.
    centres = ((181,137), (180,136), (183,136), (179,136),
               (181,135), (182,136), (178,136), (184,137))
    phases = [("listens with quiet joy",0),("eyes widen",1),("forearm rises",2),("hand beside mouth",3),
              ("opens his voice to the child",4),("one palm invites",5),("admires with open hands",6),
              ("stable opening for child's step",7)]
    for action, index in phases:
        image, pose, registry = source_pose(original,index)
        image=invitation_adjust(image,index)
        drawing, placement = placed(image,ADULT_ROOT,ADULT_HEIGHT,registry["reference_height"],pose["anchors"]["stage"])
        variants, box = {}, None
        for mode in MODES:
            alternate, rect = oral_pose(image,centres[index],"adult",mode)
            variants[mode] = placed(alternate,ADULT_ROOT,ADULT_HEIGHT,registry["reference_height"],pose["anchors"]["stage"])[0]
            box = rect_stage(rect,placement)
        level.add(drawing,action,mouth=box,variants=variants)
    # Anticipation starts before U031; invitation opens during U032.
    return level.finish(), [4,4,7,18,47,33,31,15]


def local_mouth(reference, drawing):
    """Locate the already-painted mouth on a moving cricket cel."""
    expected = (101, 271, 149, 304)
    raw = np.asarray(reference.convert("L"),dtype=np.float32)
    target = np.asarray(drawing.convert("L"),dtype=np.float32)
    x0,y0,x1,y1 = expected
    sample = raw[y0:y1,x0:x1]
    sample = sample-sample.mean()
    best = (None,x0,y0)
    for dy in range(-5,35,2):
        for dx in range(-35,21,2):
            candidate=target[y0+dy:y1+dy,x0+dx:x1+dx]
            candidate=candidate-candidate.mean()
            cost = -float(np.sum(candidate*sample))/(float(np.linalg.norm(candidate))+1e-6)
            if best[0] is None or cost<best[0]:
                best=(cost,x0+dx,y0+dy)
    return best[1]+23,best[2]+17


def celebratory_jump():
    original = "S12H-cricket-celebration"
    level = Level("cricket-jump", {"whole_drawings": original})
    reference, _, registry = source_pose(original,0)
    exposure=[]
    for index, row in enumerate(registry["poses"]):
        image, _, _ = source_pose(original,index)
        root=tuple(a+b for a,b in zip(CRICKET_ROOT,row["stage_offset"],strict=True))
        art, placement = placed(image,root,CRICKET_HEIGHT,registry["reference_height"],row["anchors"]["stage"],True)
        centre=local_mouth(reference,image)
        variants, box = {}, None
        for mode in MODES:
            speak, area = oral_pose(image,centre,"cricket",mode)
            variants[mode] = placed(speak,root,CRICKET_HEIGHT,registry["reference_height"],row["anchors"]["stage"],True)[0]
            box = rect_stage((image.width-area[2],area[1],image.width-area[0],area[3]),placement)
        level.add(art,row["phase"], mouth=box,variants=variants,pivot=list(root))
        exposure.append(row["phase_ticks"])
    return level.finish(), exposure


# Landmarks share anatomical names across six authored key drawings, with locally annotated
# heel, eye, wrist and shoulder points for reliable inbetweens instead of two visible silhouettes.
RIG = ("hero_plume", "hero_eye", "hero_mouth", "hero_neck", "hero_bag", "hero_near_palm",
       "hero_far_palm", "hero_pelvis", "hero_first_sole", "hero_second_sole", "adult_hair",
       "adult_eye", "adult_mouth", "adult_neck", "adult_near_palm", "adult_far_palm",
       "adult_pelvis", "adult_first_sole", "adult_second_sole")

DRAWING_POINTS = (
    ((42,108),(173,185),(188,207),(158,235),(94,279),(194,316),(246,267),(141,326),(90,467),(227,438),
     (367,27),(370,95),(366,123),(380,157),(475,212),(250,198),(399,309),(337,461),(426,467)),
    ((79,113),(217,182),(236,205),(203,233),(148,278),(260,284),(229,258),(192,342),(163,470),(217,468),
     (319,54),(303,121),(297,150),(323,180),(205,268),(237,239),(353,338),(280,462),(374,469)),
    ((100,121),(246,182),(264,202),(232,235),(207,289),(319,307),(285,315),(231,348),(206,469),(247,469),
     (314,53),(302,122),(303,154),(327,175),(241,247),(210,254),(343,350),(284,468),(365,472)),
    ((93,115),(240,175),(260,190),(235,221),(192,279),(324,301),(281,308),(217,351),(196,467),(247,466),
     (283,44),(290,115),(287,145),(319,171),(232,247),(190,240),(327,348),(283,462),(356,468)),
    ((65,112),(207,175),(228,196),(198,235),(151,294),(259,306),(266,274),(183,357),(152,469),(218,466),
     (312,34),(302,108),(301,133),(324,162),(304,265),(242,229),(352,335),(296,464),(365,470)),
    ((24,109),(160,178),(180,200),(151,232),(99,294),(119,343),(209,333),(142,353),(109,467),(166,468),
     (357,26),(337,99),(336,122),(357,155),(379,269),(225,236),(374,338),(317,469),(401,469)),
)


def split_drawing(tile, person):
    """Extract the separated participants from the opening or recovery pose."""
    from scipy.ndimage import binary_dilation, label
    raw = np.asarray(tile).copy()
    alpha = raw[:, :, 3]
    ids, _ = label(alpha > 25)
    count = np.bincount(ids.ravel())
    count[0] = 0
    indices = np.argsort(count)[-2:]
    left, right = sorted(indices, key=lambda element: np.where(ids == element)[1].mean())
    chosen = left if person == "hero" else right
    boundary = binary_dilation(ids == chosen, iterations=2)
    raw[..., 3] = np.where(boundary, alpha, 0)
    raw[raw[...,3] == 0] = 0
    return Image.fromarray(raw)


def clean_alpha(panel):
    raw = np.asarray(panel).copy()
    source = raw[...,3].astype(np.int32)
    raw[...,3] = np.clip((source - 5)*255//245, 0, 255)
    raw[raw[...,3] == 0] = 0
    return Image.fromarray(raw)


def register_key(tile, number):
    keys = DRAWING_POINTS[number]
    if number in (0, 4, 5):
        settings = {
            0: (((90,467),(532,641),372,236), ((395,469),ADULT_ROOT,450,315)),
            4: (((185,470),(573,643),376,236), ((329,470),ADULT_ROOT,448,284)),
            5: (((146,471),(558,643),379,236), ((359,470),ADULT_ROOT,458,315)),
        }[number]
        drawing = stage()
        actor_markers = []
        for actor, (anchor, root, size, height), points in zip(
                ("hero","adult"),settings,(keys[:10],keys[10:]),strict=True):
            source = split_drawing(tile,actor)
            sprite, (x,y,ratio) = placed(source,root,height,size,anchor)
            drawing.alpha_composite(sprite)
            actor_markers.extend((x+a*ratio,y+b*ratio) for a,b in points)
        return drawing,np.array(actor_markers)
    anchor, size = {1:((328,471),370),2:((345,473),365),3:((339,472),372)}[number]
    drawing,(x,y,ratio)=placed(tile,ADULT_ROOT,236,size,anchor)
    marks=np.array([(x+a*ratio,y+b*ratio) for a,b in keys],dtype=float)
    # Near-side child soles meet the perspective ground, where the camera has
    # always placed Pinocchio. Grandpa's depth, physical shoe size and feet stay fixed.
    ys,xs=np.indices((280,380),dtype=float)
    ys+=400
    xs+=450
    rise=14*smooth((646-xs)/44)*smooth((ys-555)/82)
    cropped=drawing.crop((450,400,830,680))
    corrected=warp_rgba(cropped,np.zeros_like(rise),rise)
    drawing.paste(corrected,(450,400))
    marks[:,1]+=14*smooth((646-marks[:,0])/44)*smooth((marks[:,1]-555)/82)
    return drawing,marks


def upper_shape(base, tilt):
    """Tilt only the worn hat and feather around their crown contact."""
    yy,xx=np.indices((base.height,base.width),dtype=np.float32)
    angle=radians(tilt)
    pivot=(241,168)
    support=smooth((223-yy)/52)
    return warp_rgba(base,-angle*(yy-pivot[1])*support,angle*(xx-pivot[0])*support)


def establish(model, opened, aftermath=False):
    child = upper_shape(opened,-3.2) if aftermath else human_pose(opened,model["anchors"],.55,-1.4)[0]
    hero,(hx,hy,hs)=placed(child,HERO_ROOT,HERO_HEIGHT,model["reference_height"],model["anchors"]["stage"])
    positions = model["anchors"]
    h_points=(positions["hat"], positions["near_eye"], positions["mouth"], positions["neck"],positions["bag"],
              positions["near_palm"],positions["far_palm"],positions["near_hip"],positions["left_heel"],positions["right_toe"])
    adult_name, adult_index = ("S12H-gep-palms-demo",0) if aftermath else ("S12H-gep-surprise-open",7)
    adult_src,adult_pose,adult_reg=source_pose(adult_name,adult_index)
    if not aftermath:
        adult_src=invitation_adjust(adult_src,adult_index)
    adult,(gx,gy,gs)=placed(adult_src,ADULT_ROOT,ADULT_HEIGHT,adult_reg["reference_height"],adult_pose["anchors"]["stage"])
    a_p=( (202,44),(192,105),(184,137),(213,170),
          (244,309) if aftermath else (309,234), (138,290) if aftermath else (48,205),
          (214,312),(156,461),(242,463))
    points=[(hx+x*hs,hy+y*hs) for x,y in h_points]+[(gx+x*gs,gy+y*gs) for x,y in a_p]
    adult.alpha_composite(hero)
    return adult,np.array(points,dtype=float)


def warp_landmarks(drawing, mesh, coordinates, box):
    """Warp one written pose into the shared inbetween shape on its original ground."""
    from scipy.interpolate import LinearNDInterpolator
    left,top,right,bottom=box
    sample_y,sample_x=np.mgrid[top:bottom,left:right]
    pointmap=LinearNDInterpolator(mesh,coordinates)(sample_x,sample_y)
    rgba=np.asarray(drawing.crop(box),dtype=np.float32)/255
    alpha=rgba[...,3].copy()
    inverse=np.array([np.nan_to_num(pointmap[...,1]-top,nan=-20),
                      np.nan_to_num(pointmap[...,0]-left,nan=-20)])
    return np.stack([map_coordinates(rgba[...,channel]*alpha if channel<3 else alpha,
                                     inverse,order=1,mode="constant",prefilter=False)
                     for channel in range(4)],axis=2)


def inbetween(first, later, amount):
    image_a,a = first
    image_b,b = later
    if amount<=0:
        return image_a,a
    if amount>=1:
        return image_b,b
    x0,y0,x1,y1=ImageChops.lighter(image_a.getchannel("A"),image_b.getchannel("A")).getbbox()
    box=(x0-7,y0-7,x1+7,y1+7)
    hull=np.array(((box[0],box[1]),(box[2]-1,box[1]),(box[0],box[3]-1),(box[2]-1,box[3]-1)))
    start=np.concatenate((a,hull))
    stop=np.concatenate((b,hull))
    positions=start+(stop-start)*amount
    # Retain a single crisp pigment drawing at each exposure. The common geometry
    # advances every inbetween without producing a double jaw, hat or planted boot.
    drawing,landmarks=(image_a,start) if amount<.5 else (image_b,stop)
    mixed=warp_landmarks(drawing,positions,landmarks,box)
    opacity=mixed[...,3,None]
    mixed[...,:3]/=np.maximum(opacity,.003)
    mixed=np.rint(255*mixed.clip(0,1)).astype(np.uint8)
    result=stage()
    result.paste(Image.fromarray(mixed),box[:2])
    return result,a+(b-a)*amount


def fixed_soles(pose, wanted):
    """Set planted shoes to the same physical stage points across knee/weight drawings."""
    picture, originals=pose
    x0,y0,x1,y1=picture.getchannel("A").getbbox()
    box=(x0-28,y0-4,x1+28,y1+12)
    hull=np.array(((box[0],box[1]),(box[2]-1,box[1]),(box[0],box[3]-1),(box[2]-1,box[3]-1)))
    positions=originals.copy()
    for index,value in wanted.items():
        positions[index]=value
    premultiplied=warp_landmarks(picture,np.concatenate((positions,hull)),
                                 np.concatenate((originals,hull)),box)
    premultiplied[..., :3]/=np.maximum(premultiplied[...,3,None],.003)
    final=stage()
    final.paste(Image.fromarray(np.rint(255*premultiplied.clip(0,1)).astype("uint8")),box[:2])
    return final,positions


def paint_pair(pose, level, action, speaker=None):
    image, anchors=pose
    mouth=None
    variants=None
    if speaker:
        mouth=anchors[RIG.index(f"{speaker}_mouth")]
        variants={}
        for mode in MODES:
            variants[mode], box=oral_pose(image,mouth,speaker,mode,.77 if speaker=="hero" else .74)
        mouth=box
    level.add(image,action,variants=variants,mouth=mouth,
              anchored_soles={role: [round(float(p),2) for p in anchors[RIG.index(role)]]
                              for role in RIG if role.endswith("_sole")})


def expose_change(level, first, later, length, action, timing, speaker=None, density=5):
    """Expose positive cel durations from the physical phase ledger."""
    count=max(2,round(length/density))
    cuts=[round(length*i/count) for i in range(count+1)]
    for i,(lo,hi) in enumerate(zip(cuts,cuts[1:])):
        amount=float(smooth(i/(count-1)))
        art=inbetween(first,later,amount)
        paint_pair(art,level,action,speaker)
        timing.append(hi-lo)


def pair_scene(model, opened):
    sheet_path=HERE/"paired-keyframes.png"
    with Image.open(sheet_path) as source:
        sheet=source.convert("RGBA")
    if sheet.size != (1536,1024):
        raise ValueError("Six separate 512px key cells require the registered paired atlas")
    physical=[]
    for index in range(6):
        row,column=divmod(index,3)
        box=column*512,row*512,(column+1)*512,(row+1)*512
        physical.append(register_key(clean_alpha(sheet.crop(box)),index))
    original=establish(model,opened)
    departure=establish(model,opened,True)
    provenance={"source":"paired-keyframes.png","sha256":digest(sheet_path),
                "character":model["closed_sha256"],"adult":"S12H-gep-surprise-open",
                "physical_contact": "separate open, initial shoulders, settled reciprocal hands, release, and planted foot return"}

    opening=Level("embrace-approach",provenance)
    timing=[]
    adult_shoes={point:original[1][point] for point in (17,18)}
    hero_rear=original[1][8]
    planted_hero=((568.0,640.0),(610.0,640.0))
    footing={**adult_shoes,8:planted_hero[0],9:planted_hero[1]}
    pose1=fixed_soles(physical[0],{**adult_shoes,8:hero_rear})
    heel_strike=fixed_soles(physical[1],{**footing,8:hero_rear})
    heel_follow=fixed_soles(physical[1],{**footing,8:(550.0,633.0)})
    pose2,pose3,pose4=(fixed_soles(item,footing) for item in physical[1:4])
    pose5=fixed_soles(physical[4],footing)
    pose6=fixed_soles(physical[5],adult_shoes)
    expose_change(opening,original,pose1,29,"one small step with the rear sole planted",timing,density=4)
    expose_change(opening,pose1,heel_strike,15,"lead foot plants while Grandpa lowers both knees",timing,density=4)
    expose_change(opening,heel_strike,heel_follow,7,"weight transfers to planted lead foot",timing,density=3.5)
    expose_change(opening,heel_follow,pose2,7,"rear foot settles beside its new planted partner",timing,density=3.5)
    expose_change(opening,pose2,pose3,19,"Grandpa's palms guide the shoulders, child reciprocates",timing,density=4)
    expose_change(opening,pose3,pose4,31,"both torsos settle into contact before the quiet dialogue",timing)
    start=opening.finish()

    held_adult=Level("embrace-adult-talk",provenance)
    turn1=[]
    expose_change(held_adult,pose4,pose4,3,"held starting posture",turn1,"adult")
    # A fraction of the shoulder motion follows the speech, returning to the same soles.
    def breathing(pose, amount):
        image,marks=pose
        box=(490,324,770,655)
        cut=image.crop(box)
        gy,gx=np.indices((cut.height,cut.width),dtype=np.float32)
        movement=amount*np.exp(-(((gx-160)/123)**2+((gy-125)/73)**2))*smooth((300-gy)/65)
        draw=warp_rgba(cut,-.4*movement,-.88*movement)
        result=image.copy()
        result.paste(draw,box[:2])
        points=marks.copy()
        points[:,0]-=.4*amount*np.exp(-(((points[:,0]-650)/123)**2+((points[:,1]-449)/73)**2))
        points[:,1]-=.88*amount*np.exp(-(((points[:,0]-650)/123)**2+((points[:,1]-449)/73)**2))
        points[[8,9,17,18]]=marks[[8,9,17,18]]
        return result,points
    for amount,count in ((.7,6),(1.55,9),(2.25,11),(1.1,14),(.25,12),(0,13)):
        paint_pair(breathing(pose4,amount),held_adult,"quiet reassurance in a single supported embrace","adult")
        turn1.append(count)
    adult=held_adult.finish()

    held_hero=Level("embrace-child-talk",provenance)
    turn2=[]
    for amount,count in ((0,7),(1.2,9),(2.0,10),(1.25,9),(.4,6),(0,5)):
        paint_pair(breathing(pose4,amount),held_hero,"answering from the same shoulder and hand placement","hero")
        turn2.append(count)
    hero=held_hero.finish()

    release=Level("embrace-release",provenance)
    release_ticks=[]
    expose_change(release,pose4,breathing(pose4,2.4),21,"turns eye-line at the cricket's preparation",release_ticks)
    expose_change(release,breathing(pose4,2.4),pose5,31,"outer hands release while both feet carry weight",release_ticks)
    expose_change(release,pose5,pose6,40,"adult straightens knees and child's return foot lands",release_ticks)
    expose_change(release,pose6,departure,32,"both arms lower, balance returns to the previous shared roots",release_ticks)
    expose_change(release,departure,departure,10,"quiet eye contact with shoe soles already set",release_ticks)
    last=release.finish()
    exit_png=HERE/"post-hug-open.png"
    upper_shape(opened,-3.2).save(exit_png,compress_level=4)
    write(HERE/"exit-state.json",{"hero":{"path":str(exit_png.relative_to(V3)),"stage":list(HERO_ROOT),"height":HERO_HEIGHT,
                                        "anchor":model["anchors"]["stage"],"cap_tilt_degrees":-3.2},
                     "geppetto":{"level":"S12H-gep-palms-demo","cel":0,"stage":list(ADULT_ROOT),"height":315},
                     "cricket":{"level":"S12G-cricket-jump","cel":21,"stage":list(CRICKET_LANDED),"height":84},
                     "fairy":{"level":"S12F-wand","cel":14,"stage":[831,442],"height":122},
                     "last_pair_level":last,"last_pair_cel":len(release.poses)-1})
    return (start,timing),(adult,turn1),(hero,turn2),(last,release_ticks)


def layer(track, visual, *, pos=(0,0), height=720, cel=0, flip=False, speaker=None, period=None,
          motion="story", exposure=None):
    if exposure:
        item = {"track": track,"level":visual,"root":list(pos),"height":height,"anchor":"stage",
                "first_cel":cel,"last_cel":cel+len(exposure)-1,"motion":motion,"flip":flip,
                "exposure_frames":exposure}
    else:
        item = {"track":track,"level":visual,"root":list(pos),"height":height,"anchor":"stage",
                "first_cel":cel,"motion":"hold","flip":flip}
    if period:
        item["span"]=list(period)
    if speaker:
        item["mouth"]={"speaker":SPEAKERS[speaker]}
    return item


def school(cricket=True):
    fixed = [layer("open-door", "S12F-door"),
             layer("teacher","S12F-teacher",pos=(739,559),height=193,cel=7),
             layer("upright-guideboard","S12F-sign",pos=(413,597),height=84)]
    if cricket:
        fixed.append(layer("Cricket","S12F-cricket-acting",pos=CRICKET_ROOT,height=84,cel=2,flip=True))
    fixed.append(layer("Fairy","S12F-wand",pos=(831,442),height=122,cel=14))
    return fixed


def captured(name, crop, layers):
    return {"id":name,"plate":"S11L-school-open.png@"+crop,"layout":layers}


def main():
    model, closed, opened=human_bases()
    boy, boy_ticks = revelation(model,closed,opened)
    grandpa, grandpa_ticks = response()
    cricket, cricket_ticks = celebratory_jump()
    (approach, approach_ticks),(adult_voice, adult_ticks),(child_voice, child_ticks),(release, release_ticks) = pair_scene(model,opened)
    family_rows=[
        captured("S12-C31","454,299,550",[
            *school(),
            layer("Geppetto-fairy-look","S12F-gep-up",pos=ADULT_ROOT,height=315,cel=5,
                  period=("start","lead-point:1.0")),
            layer("Geppetto-to-child","S12H-gep-surprise-open",pos=ADULT_ROOT,height=315,cel=0,
                  period=("lead-point:1.0","end")),
            layer("Pinocchio",boy,exposure=boy_ticks,speaker="hero")]),
        captured("S12-C32","477,292,505",[
            *school(),
            layer("Geppetto",grandpa,exposure=grandpa_ticks,speaker="adult"),
            layer("Pinocchio",boy,cel=len(boy_ticks)-1)]),
        captured("S12-C33","415,272,713",[
            *school(),
            layer("paired-approach",approach,period=("start","before:S12-N020"),motion="lead",exposure=approach_ticks),
            layer("paired-hold-adult-cue",adult_voice,period=("before:S12-N020","before:S12-N021"),exposure=adult_ticks,speaker="adult"),
            layer("paired-hold-child-cue",child_voice,period=("before:S12-N021","end"),exposure=child_ticks,speaker="hero")]),
        captured("S12-C34","383,239,845",[
            *school(False),
            layer("Cricket",cricket,exposure=cricket_ticks,speaker="cricket"),
            layer("paired-release",release,exposure=release_ticks)]),
    ]
    write(BUILD/"layout-hug.json",family_rows)
    write(BUILD/"motion-hug.json",{"cuts":MOTION})
    print("Registered four S12 family shots, 36 additional action frames, staged stable C35 entry.")


if __name__ == "__main__":
    main()
