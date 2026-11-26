#!/usr/bin/env python3
"""Register the post-hug hand and hat performance as stable whole cels."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from functools import lru_cache
from hashlib import file_digest
import json
import runpy
from math import atan2, cos, degrees, hypot, radians, sin, sqrt
from pathlib import Path

SPEECH_ONLY = False

import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageOps
from scipy.ndimage import binary_dilation, find_objects, label

HERE = Path(__file__).resolve().parent
V3 = Path('/workspace/yoonsu-pinocchio-3d/scenes/S12/v3')
BUILD = HERE / 'build'
ART = BUILD / 'art'
HUMAN_SOURCE = V3 / 'art/human/source'
HUG_END = V3 / 'art/first_hug/post-hug-open.png'
PIN, GEP = (561, 643), (667, 629)
CRICKET, FAIRY = (492, 649), (831, 442)
BASE_PLATE = 'S11L-school-open.png'
PIN_SPEAKER, GEP_SPEAKER = '피노키오', '제페토'
HAND_TILT = -3.2
HUG_TILT = runpy.run_path(str(V3/"art/first_hug/build.py"))["upper_shape"]

# Replacement cut-outs stop before the fixed backpack strap and overall seams.
PIN_NEAR = ((196,312),(212,320),(214,343),(210,356),(198,370),(184,380),(165,412),
            (158,432),(161,452),(156,478),(105,480),(107,429),(127,388),(142,352),
            (169,330))
PIN_FAR = ((289,318),(311,327),(322,344),(334,363),(349,393),(374,408),
           (427,416),(431,469),(372,471),(355,449),(337,422),(319,409),(301,388),
           (296,368))
# Only Grandpa's nearest offering arm moves. His apron and other hand are retained.
GEP_NEAR = ((153,207),(167,218),(171,234),(161,252),(155,279),(151,305),
            (154,331),(113,334),(110,294),(123,259),(133,228))
CUFFS = {
    (True,'near'):((196,313),(209,316),(220,327),(224,338),(218,352),(208,368),
                   (196,375),(187,367),(175,361),(161,355),(155,347),(168,332),(183,321)),
    (True,'far'):((292,322),(302,326),(313,329),(321,340),(323,350),(320,362),
                  (308,378),(296,374),(292,367),(296,358),(293,344)),
    (False,'near'):((152,203),(161,209),(166,218),(167,222),(163,228),(158,237),
                    (148,240),(139,237),(141,224),(147,210)),
}
CAP = ((77,73),(180,75),(199,109),(246,84),(286,94),(322,103),(330,125),
       (309,143),(284,141),(257,148),(237,155),(222,174),(206,188),(195,200),
       (176,216),(162,236),(165,251),(177,264),(151,269),(138,254),(135,234),
       (141,210),(135,174),(111,157),(79,124))


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def write(path, data):
    temporary = path.with_suffix(path.suffix + '.hands-pending')
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temporary.replace(path)


def sha(path):
    with path.open('rb') as handle:
        return file_digest(handle, 'sha256').hexdigest()


def load(path):
    with Image.open(path) as handle:
        return handle.convert('RGBA')


def region(size, points, blur=.7):
    out = Image.new('L', size)
    ImageDraw.Draw(out).polygon(points, fill=255)
    return out.filter(ImageFilter.GaussianBlur(blur)) if blur else out


def colored_patch(drawing, source, bounds, corners):
    """Expose the original cloth pigment in a previously occluded region."""
    left, top = map(min, zip(*corners))
    right, bottom = map(max, zip(*corners))
    patch = Image.new('RGBA', drawing.size)
    stamp = source.crop(bounds).resize((right-left, bottom-top), Image.Resampling.LANCZOS)
    patch.alpha_composite(stamp, (left, top))
    patch.putalpha(ImageChops.multiply(patch.getchannel('A'), region(drawing.size, corners)))
    return patch


@lru_cache(maxsize=1)
def hands():
    sheet = np.asarray(load(HERE/'painted_hands.png')).copy()
    labels, _ = label(sheet[:,:,3] > 190)
    parts = []
    for n, box in enumerate(find_objects(labels), 1):
        if box is None:
            continue
        yy, xx = box
        mask = labels[box] == n
        if np.count_nonzero(mask) < 20_000:
            continue
        kept = binary_dilation(mask, iterations=2)
        pixels = sheet[box].copy()
        alpha = np.clip((pixels[:,:,3].astype(float)-32) * 255/223,0,255)
        pixels[:,:,3] = np.where(kept, alpha, 0).astype(np.uint8)
        pixels[pixels[:,:,3] == 0] = 0
        y = 0 if yy.start < sheet.shape[0]/2 else 1
        parts.append((y, xx.start, Image.fromarray(pixels)))
    if len(parts) != 6:
        raise ValueError(f'Expected six clean five-finger hand drawings, got {len(parts)}')
    live = ('open','half','curl','back','adult-open','adult-curl')
    return dict(zip(live,(piece for _,_,piece in sorted(parts,key=lambda p:p[:2])),strict=True))


def stamp_hand(size, kind, at, direction, mirror, adult=False):
    art = hands()[kind]
    # All assets have a short wrist below their palm. Lock the actual wrist cross section.
    raw = np.asarray(art)[:,:,3] > 180
    h,w = raw.shape
    wrist_rows = np.where(raw[round(.91*h):round(.96*h)])[1]
    ax = float(np.median(wrist_rows)) if len(wrist_rows) else .53*w
    ay = .88*h
    thickness = max(1, np.quantile(wrist_rows,.91)-np.quantile(wrist_rows,.09)) if len(wrist_rows) else .34*w
    child_height = (14 if kind=='back' else 13) / thickness
    scale = ((16 if kind=='adult-open' else 16.5) / thickness) if adult else child_height
    # Scale is tied to the wrist, so different finger flex stages do not change hand size.
    if mirror:
        art = ImageOps.mirror(art)
        ax = w-1-ax
    scaled = art.resize((round(w*scale),round(h*scale)),Image.Resampling.LANCZOS)
    angle = -direction-90
    # A local transparent canvas retains the desired center throughout rotation.
    side = 2*max(scaled.size)+12
    center = side//2
    base = Image.new('RGBA',(side,side))
    base.alpha_composite(scaled,(round(center-ax*scale),round(center-ay*scale)))
    rotated = base.rotate(angle,Image.Resampling.BICUBIC,center=(center,center))
    result = Image.new('RGBA',size)
    result.alpha_composite(rotated,(round(at[0]-center),round(at[1]-center)))
    return result


def tube(size, nodes, widths, light, shade):
    """Rasterize an inked tapered 2D arm along its actual joint chain."""
    border = max(widths)+4
    x0=max(0,int(min(p[0]for p in nodes)-border))
    y0=max(0,int(min(p[1]for p in nodes)-border))
    x1=min(size[0],int(max(p[0]for p in nodes)+border)+1)
    y1=min(size[1],int(max(p[1]for p in nodes)+border)+1)
    yy,xx=np.meshgrid(np.arange(y0,y1,dtype=float),np.arange(x0,x1,dtype=float),indexing='ij')
    closest=np.full(xx.shape,1e4)
    nearest_radius=np.zeros(xx.shape)
    fraction=np.zeros(xx.shape)
    for start,end,r0,r1 in zip(nodes[:-1],nodes[1:],widths[:-1],widths[1:],strict=True):
        dx,dy=end[0]-start[0],end[1]-start[1]
        length=max(1.,dx*dx+dy*dy)
        t=np.clip(((xx-start[0])*dx+(yy-start[1])*dy)/length,0,1)
        vx,vy=xx-start[0]-t*dx,yy-start[1]-t*dy
        dist=np.hypot(vx,vy)
        radius=r0+(r1-r0)*t
        edge=dist-radius
        replace=edge<closest
        closest=np.where(replace,edge,closest)
        nearest_radius=np.where(replace,radius,nearest_radius)
        fraction=np.where(replace,(vx*.50+vy*.70)/np.maximum(radius,1),fraction)
    fade=np.clip(.8-closest,0,1)
    # Highlights follow the existing upper-left illumination. A fine grain is in pigment, never opacity.
    pigment=np.clip(.52+.60*fraction+.17*(1-np.clip(-closest/np.maximum(nearest_radius,1),0,1)),0,1)
    border_ink=np.clip((closest+1.4)/1.4,0,1)*.17
    grain=1.2*np.sin(xx*1.63+np.sin(yy*1.17)*4.2)+.65*np.cos(yy*2.75-xx*.38)
    rgb=[(a*(1-pigment)+b*pigment)*(1-border_ink)+grain for a,b in zip(light,shade,strict=True)]
    rgba=np.stack([*rgb,fade*255],axis=2).clip(0,255).astype(np.uint8)
    result=Image.new('RGBA',size)
    result.alpha_composite(Image.fromarray(rgba),(x0,y0))
    return result


def cross(a,b):
    return a[0]*b[1]-a[1]*b[0]


def delta(a,b):
    return (a[0]-b[0],a[1]-b[1])


def ik(shoulder, old_elbow, old_wrist, target):
    upper=hypot(*delta(old_elbow,shoulder))
    lower=hypot(*delta(old_wrist,old_elbow))
    dx,dy=delta(target,shoulder)
    distance=max(hypot(dx,dy),.01)
    reach=min(distance,upper+lower-1.2)
    direction=(dx/distance,dy/distance)
    wrist=(shoulder[0]+direction[0]*reach,shoulder[1]+direction[1]*reach)
    along=min(upper-.01,max(-upper+.01,(reach**2+upper**2-lower**2)/max(2*reach,.1)))
    down=sqrt(max(0,upper*upper-along*along))
    side=1 if cross(delta(old_wrist,shoulder),delta(old_elbow,shoulder))>0 else -1
    elbow=(shoulder[0]+direction[0]*along-direction[1]*down*side,
           shoulder[1]+direction[1]*along+direction[0]*down*side)
    return elbow,wrist


@dataclass(frozen=True)
class Wrist:
    x: float
    y: float
    angle: float
    hand: str = 'open'


@dataclass(frozen=True)
class State:
    near: Wrist | None = None
    far: Wrist | None = None
    chin: float = 0
    hat: float = HAND_TILT
    blink: bool = False


def point(a,b,mix):
    return tuple(x+(y-x)*mix for x,y in zip(a,b,strict=True))


def rotate_head(base, chin):
    if not chin:
        return base
    shape=((55,62),(356,58),(365,247),(335,287),(270,296),(247,309),(219,311),(201,303),(144,290),(88,261))
    mask=region(base.size,shape,1.4)
    face=base.copy()
    face.putalpha(ImageChops.multiply(base.getchannel('A'),mask))
    headless=base.copy()
    headless.putalpha(ImageChops.multiply(base.getchannel('A'),ImageChops.invert(mask)))
    headless.alpha_composite(face.rotate(chin,Image.Resampling.BICUBIC,center=(228,299)))
    return headless


def rotate_cap(base, angle):
    """Maintain the actual cap-bearing warp used for the preceding hug."""
    return base if not angle else HUG_TILT(base,angle)


@lru_cache(maxsize=6)
def original_cuff(actor,side):
    source=actor.source.copy()
    matte=region(source.size,CUFFS[(actor.child,side)],.75)
    source.putalpha(ImageChops.multiply(source.getchannel('A'),matte))
    return source


def painted_cuff(actor,side,pivot,old,current):
    x,y=delta(old,pivot)
    xx,yy=delta(current,pivot)
    angle=-degrees(atan2(yy,xx)-atan2(y,x))
    origin,_,_,_=actor.sockets[side]
    sleeve=original_cuff(actor,side).rotate(angle,Image.Resampling.BICUBIC,center=origin)
    adjusted=Image.new('RGBA',sleeve.size)
    adjusted.alpha_composite(sleeve,tuple(round(v) for v in delta(pivot,origin)))
    return adjusted


def native_hand(actor,state,side):
    hand=getattr(state,side)
    target=actor.local((hand.x,hand.y))
    shoulder,cuff,elbow,wrist=actor.shoulder_arc(side,target)
    _,actual=ik(shoulder,elbow,wrist,target)
    layer=stamp_hand(actor.source.size,hand.hand,actual,hand.angle,side=='near'and actor.child,not actor.child)
    output=Image.new('L',(1280,720))
    drawing=layer.getchannel('A').resize(tuple(round(n*actor.scale) for n in layer.size),Image.Resampling.LANCZOS)
    output.paste(drawing,tuple(round(x-a*actor.scale)for x,a in zip(actor.root,actor.ank,strict=True)))
    return np.asarray(output)>123


def describe_contact(kid,gep,offered,held,open_gep,grip_gep):
    from scipy.ndimage import distance_transform_edt
    result={}
    for title,k,g in (('awaiting_input',offered,open_gep),('accepted',held,grip_gep)):
        child,adult=native_hand(kid,k,'far'),native_hand(gep,g,'near')
        distance=distance_transform_edt(~adult)
        result[title]={'min_distance_stage_pixels':float(distance[child].min()),
                       'opaque_overlap_pixels':int((child&adult).sum())}
    return result


def cap_edges(actor, state):
    art=actor.source.copy()
    rgba=np.asarray(art).astype(float)
    red=(rgba[:,:,0]>1.35*rgba[:,:,1]) & (rgba[:,:,0]>1.66*rgba[:,:,2]) & (rgba[:,:,0]>91)
    outer=(np.asarray(region(art.size,CAP,0))>125)&(rgba[:,:,3]>155)
    art.putalpha(Image.fromarray(np.where(red&outer,255,0).astype('uint8')))
    art=rotate_head(rotate_cap(art,state.hat),state.chin)
    canvas=Image.new('L',(1280,720))
    alpha=art.getchannel('A').resize(tuple(round(v*actor.scale)for v in art.size), Image.Resampling.LANCZOS)
    canvas.paste(alpha,tuple(round(x-a*actor.scale)for x,a in zip(actor.root,actor.ank,strict=True)))
    return np.asarray(canvas)>125


def rotate_point(point_xy, pivot, a):
    dx,dy=delta(point_xy,pivot)
    u=radians(a)
    return pivot[0]+dx*cos(u)+dy*sin(u),pivot[1]-dx*sin(u)+dy*cos(u)


class Actor:
    def __init__(self, child, source=None, records=None):
        self.child=child
        if child:
            self.records=read(HUMAN_SOURCE/'registration.json')
            self.path=HUMAN_SOURCE/'open.png'
            self.root,self.height=PIN,236
            self.ank=self.records['anchors']['stage']
            self.ref=self.records['reference_height']
            self.sockets={
               side: tuple(self.records['anchors'][f'{side}_{name}']for name in ('shoulder','cuff','elbow','wrist'))
               for side in ('near','far')}
            self.box=self.records['mouth_box']
        else:
            self.records=records
            self.path=source
            self.root,self.height=GEP,315
            self.ank=records['anchors']['stage']
            self.ref=427
            self.sockets={'near':((151,184),(152,227),(141,247),(136,292))}
            self.box=(162,122,202,148)
        self.scale=self.height/self.ref
        self.source=load(self.path)

    def local(self, world):
        return tuple(ank+(n-root)/self.scale for n,root,ank in zip(world,self.root,self.ank,strict=True))

    def world(self, local):
        return tuple(root+(n-ank)*self.scale for n,root,ank in zip(local,self.root,self.ank,strict=True))

    def actual_rest(self, side, back=None):
        pos = self.world(self.sockets[side][-1])
        return Wrist(*pos, back if back is not None else (110 if self.child and side=='near' else 55), 'back')

    def atlas_source(self, mode, blink=False):
        if self.child:
            if blink:
                return self.child_source('closed.png')
            variants=self.records.get('mouth_variants') or self.records.get('viseme_files') or self.records.get('visemes') or {}
            asset=variants.get(mode)
            if isinstance(asset,dict):
                asset=asset['file']
            defaults={'small':'speech-small.png','wide':'speech-wide.png'}
            named=asset or defaults.get(mode,'open.png' if mode=='closed' else '')
            if named and (HUMAN_SOURCE / named).is_file():
                return self.child_source(named)
        return self.source.copy() if mode=='closed' else shape_lips(self.source,self.box,mode,self.child)

    @lru_cache(maxsize=12)
    def child_source(self, path):
        return load(HUMAN_SOURCE/path)

    @lru_cache(maxsize=12)
    def capped_child(self, voice, blink, hat):
        return rotate_cap(self.atlas_source(voice,blink),hat)

    def shoulder_arc(self, side, target):
        points=self.sockets[side]
        if not self.child:
            return points
        rise=min(23,max(0,(points[0][1]-target[1]-44)*.52))
        if side=='far':
            rise=min(39,max(rise,(points[0][1]-target[1]-44)*.70))
        inward=(4 if side=='near' else -5)*rise/23
        return tuple((x+inward,y-rise) for x,y in points)

    def arm(self, base, side, hand):
        target=self.local((hand.x,hand.y))
        shoulder,cuff0,old_elbow,old_wrist=self.shoulder_arc(side,target)
        elbow,wrist=ik(shoulder,old_elbow,old_wrist,target)
        fraction=hypot(*delta(cuff0,shoulder))/hypot(*delta(old_elbow,shoulder))
        cuff=point(shoulder,elbow,min(.85,fraction))
        sleeve=painted_cuff(self,side,shoulder,cuff0,cuff)
        if self.child:
            skin,lower=(241,179,131),(172,100,68)
            width=(15,13,10.5) if side=='near' else (13,11.5,10)
        else:
            skin,lower=(235,166,114),(166,93,61)
            width=(15.5,13.2,11)
        base.alpha_composite(tube(base.size,(cuff,point(cuff,elbow,.77),elbow,point(elbow,wrist,.30),wrist),
                                  (width[0],width[1],width[1],width[1]-.2,width[2]),skin,lower))
        hand_tex=stamp_hand(base.size,hand.hand,wrist,hand.angle,side=='near' and self.child,not self.child)
        base.alpha_composite(hand_tex)
        base.alpha_composite(sleeve)
        return self.world(wrist)

    def drawing(self, state, voice='closed'):
        if self.child:
            base=self.capped_child(voice,state.blink,state.hat).copy()
            base=rotate_head(base,state.chin)
        else:
            base=self.atlas_source(voice)
        anchors={}
        active=[s for s in ('far','near') if getattr(state,s) is not None]
        if active:
            for side in active:
                poly=(PIN_NEAR if side=='near' else PIN_FAR) if self.child else GEP_NEAR
                arm_matte=region(base.size,poly,.55)
                base.putalpha(ImageChops.multiply(base.getchannel('A'),ImageChops.invert(arm_matte)))
                if self.child and side=='near':
                    bag=colored_patch(base,self.source,(127,378,150,412),[(117,337),(141,334),(179,343),
                        (188,387),(174,413),(153,446),(113,456),(114,403)])
                    bag.putalpha(ImageChops.multiply(bag.getchannel('A'),arm_matte))
                    base.alpha_composite(bag)
                    top=colored_patch(base,self.source,(193,322,213,348),[(171,319),(227,319),(224,350),
                        (205,359),(184,353)])
                    top.putalpha(ImageChops.multiply(top.getchannel('A'),arm_matte))
                    base.alpha_composite(top)
            for side in active:
                anchors[side]=list(self.arm(base,side,getattr(state,side)))
        box=self.box
        if self.child and state.chin:
            x0,y0,x1,y1=self.box
            p,q=zip(*(rotate_point(xy,(228,299),state.chin) for xy in ((x0,y0),(x1,y0),(x0,y1),(x1,y1))))
            box=[int(min(p)),int(min(q)),int(max(p)+1),int(max(q)+1)]
        return base, box, anchors


def shape_lips(base, box, mode, child):
    # Preserve authored mustache, nose, eye and teeth surrounding each approved expression.
    x0,y0,x1,y1=box
    cx=(x0+x1)/2 + (1 if child else -4)
    cy=(y0+y1)/2 + (3 if child else -.3)
    radii={'small':(4,2.5),'wide':(8,4),'round':(3.6,4),'pressed':(6,.75),'teeth':(6,2)}
    rx,ry=radii[mode]
    layer=Image.new('RGBA',base.size)
    pen=ImageDraw.Draw(layer)
    pen.ellipse((cx-rx-.65,cy-ry-.5,cx+rx+.65,cy+ry+1),fill=(151,83,62,215))
    pen.ellipse((cx-rx,cy-ry,cx+rx,cy+ry),fill=(66,33,21,255))
    if mode in ('wide','teeth'):
        pen.rounded_rectangle((cx-rx*.7,cy-ry*.7,cx+rx*.7,cy-ry*.03),radius=1,fill=(249,217,184,253))
    if mode=='wide':
        pen.ellipse((cx-rx*.4,cy+.6,cx+rx*.48,cy+ry*.7),fill=(161,78,61,245))
    out=base.copy()
    out.alpha_composite(layer.filter(ImageFilter.GaussianBlur(.55)))
    return out


class Level:
    def __init__(self,label,actor):
        self.name=f'S12J-{label}'
        self.actor=actor
        self.path=ART/'cels'/self.name
        self.path.mkdir(parents=True,exist_ok=True)
        self.poses=[]

    def store(self, frame, n, mode):
        body,mouth,wrists=frame
        target=self.path/f'{n:02d}{("-"+mode) if mode else ""}.png'
        if mode or not SPEECH_ONLY or not target.is_file() or self.name=='S12J-38-return':
            body.save(target,compress_level=3)
        return {'file':target.relative_to(ART).as_posix(),'size':list(body.size),
                'anchors':{'stage':list(self.actor.ank)},'sole':list(self.actor.ank),
                'mouth_box':list(mouth),'physical_wrist_stage':wrists,'sha256':sha(target)}

    def add(self,state,dialogue=False):
        n=len(self.poses)
        p=self.store(self.actor.drawing(state),n,'')
        if dialogue:
            p['viseme_cels']={name:self.store(self.actor.drawing(state,name),n,name)
                             for name in ('small','wide','round','pressed','teeth')}
        self.poses.append(p|{'index':n,'hand_shapes':{
            side:getattr(state,side).hand for side in ('near','far') if getattr(state,side) is not None}})

    def finish(self):
        source = self.actor.path.relative_to(V3) if self.actor.path.is_relative_to(V3) else self.actor.path.name
        write(self.path/'registration.json',{'reference_height':self.actor.ref,'level':self.name,
              'source':str(source),'source_sha256':sha(self.actor.path),
              'hand_source_sha256':sha(HERE/'painted_hands.png'),'poses':self.poses})
        return self.name


def stock(label,index):
    reg=read(ART/'cels'/label/'registration.json')
    pose=reg['poses'][index]
    return ART / pose['file'], pose


def state_at(body, before, after, ratio, halfway='half'):
    def wrist(x,y,side):
        if x is None and y is None:
            return None
        if ratio<=0:
            return x
        if ratio>=1:
            return y
        x=x or body.actual_rest(side)
        y=y or body.actual_rest(side)
        shape=x.hand if ratio<.27 else y.hand if ratio>.68 else (halfway if x.hand!=y.hand and body.child else y.hand)
        return Wrist(x.x+(y.x-x.x)*ratio,x.y+(y.y-x.y)*ratio,x.angle+(y.angle-x.angle)*ratio,shape)
    return State(wrist(before.near,after.near,'near'),wrist(before.far,after.far,'far'),
                 before.chin+(after.chin-before.chin)*ratio,before.hat+(after.hat-before.hat)*ratio,
                 before.blink if ratio<.40 else after.blink)


def tween(body,before,after,count,halfway='half'):
    def eased(t):
        return t*t*(3-2*t)
    return [state_at(body,before,after,eased(index/max(1,count-1)),halfway) for index in range(count)]


def ctrl(track,level,root,height,first=0,last=None,*,phase='hold',ticks=None,when=None,
         duration=None,mouth=None,flip=False):
    row={'track':track,'level':level,'root':list(root),'height':height,'anchor':'stage',
         'motion':phase,'start':0.,'end':1.,'first_cel':first,'flip':flip}
    if last is not None:
        row['last_cel']=last
    if ticks is not None:
        row['exposure_frames']=ticks
    if duration is not None:
        row['active_frames']=duration
    if when is not None:
        row['span']=[('start' if p==0 else 'end' if p==1 else p) for p in when]
    if mouth is not None:
        row['mouth']={'speaker':mouth}
    return row


def actor_level(label,actor,states,boundary,speaker=None):
    level=Level(label,actor)
    for index,state in enumerate(states):
        level.add(state,index in boundary)
    name=level.finish()
    return lambda **kw:ctrl('Pinocchio' if actor.child else 'Geppetto',name,actor.root,actor.height,
                            mouth=speaker,**kw)


def setup():
    kid=Actor(True)
    stock_pose=stock('S12H-gep-palms-demo',0)
    gep=Actor(False,*stock_pose)
    basic=State()
    neutral=State()
    inspect_back=State(Wrist(548,540,-91,'back'),Wrist(592,527,-103),chin=-3.5)
    inspect_near=State(Wrist(548,535,-121),Wrist(592,527,-112),chin=-5.2)
    inspect=State(Wrist(553,535,-71),Wrist(593,523,-108),chin=-3.5)
    displayed=State(Wrist(567,523,-47),Wrist(618,493,-115),chin=-2)
    relaxed=State(Wrist(554,539,-64,'back'),Wrist(613,513,-96),chin=-1.7)
    flex=State(Wrist(563,527,-66),Wrist(614,502,-116),chin=-3)
    fold=State(Wrist(563,529,-63,'half'),Wrist(614,503,-114,'curl'),chin=-3.8)
    feel=State(Wrist(580,520,6,'back'),Wrist(602,521,-152),chin=-3.9)
    offered=State(Wrist(552,544,36,'back'),Wrist(585,513,-4,'back'),chin=-1.5)
    # Both wrists meet along the same stage coordinator. The upper child's fingers overlap
    # only the lower supporting palm. Fingers stay free throughout the question.
    held=State(Wrist(551,545,60,'back'),Wrist(609,505,-12,'back'),chin=.9)
    open_gep=State(near=Wrist(644,509,-175,'adult-open'))
    grip_gep=State(near=Wrist(644,508,-173,'adult-curl'))
    point_gep=State(near=Wrist(627,470,-159,'adult-open'))
    angle_gep=State(near=Wrist(640,485,-130,'adult-open'))
    level_gep=State(near=Wrist(643,486,-177,'adult-open'))
    hat_grasp=State(Wrist(539,479,-80,'back'),Wrist(575,439,-130,'half'),chin=-7)
    strap=State(Wrist(554,529,-53,'curl'),Wrist(614,533,35,'back'),chin=1.5,hat=0)
    straighten=State(Wrist(541,478,-80,'back'),Wrist(575,439,-130,'half'),chin=-6,hat=0)
    awake=State(hat=0)
    seats={}
    geometry=describe_contact(kid,gep,offered,held,open_gep,grip_gep)
    assert geometry['awaiting_input']['min_distance_stage_pixels']>8
    assert 20 <= geometry['accepted']['opaque_overlap_pixels'] <= 57
    geometry['C42']={}
    cap_contact_states=tween(kid,hat_grasp,straighten,7)
    cap_contact_labels=('tilted_cap_contact',*(f'alignment_{index}' for index in range(1,6)),
                        'straight_cap_contact')
    for kind,state in zip(cap_contact_labels,cap_contact_states,strict=True):
        rim=cap_edges(kid,state)
        hits={side:int((native_hand(kid,state,side)&rim).sum())for side in ('near','far')}
        assert min(hits.values())>0, (kind,hits)
        geometry['C42'][kind]={'hand_opaque_overlap_at_red_cap':hits,'cap_rotation_degrees':state.hat}
    palm_near=native_hand(kid,feel,'near')
    palm_far=native_hand(kid,feel,'far')
    geometry['C38']={'own_hand_overlap_pixels':int((palm_near & palm_far).sum())}
    assert geometry['C38']['own_hand_overlap_pixels']>0, geometry['C38']
    assert kid.drawing(basic)[0].tobytes()==load(HUG_END).tobytes()
    geometry['same_hug_end_cel_at_C35'] = True
    write(BUILD/'contact-geometry.json',geometry)

    def stage(id, crop, actor_tracks, *, detail=None):
        door=ctrl('open-door','S12F-door',(0,0),720)
        teacher=ctrl('teacher','S12F-teacher',(739,559),193,first=7)
        board=ctrl('upright-guideboard','S12F-sign',(413,597),84)
        cricket=ctrl('Cricket','S12G-cricket-jump',(0,0),720,first=21)
        fairy=ctrl('Fairy','S12F-wand',FAIRY,122,first=14)
        shot={'id':f'S12-C{id}','plate':BASE_PLATE+'@'+crop,
              'layout':[door,teacher,board,cricket,fairy,*actor_tracks]}
        if detail:
            view, return_frame = detail
            shot['plate']=BASE_PLATE
            shot['camera_cues']=[{'frame':0,'crop':view},
                                 {'frame':return_frame,'crop':[int(value) for value in crop.split(',')]}]
        seats[shot['id']]=shot

    # C35: examine hands first, then Grandpa demonstrates with his actual paired open palms.
    pin=actor_level('35-inspect',kid,tween(kid,basic,inspect_back,7,halfway='back'),set())
    roll=tween(kid,inspect_back,inspect_near,7,halfway='back')
    roll+=tween(kid,inspect_near,inspect,6,halfway='back')[1:]
    wrist_roll=actor_level('35-wrist-roll',kid,roll,set(range(len(roll))),PIN_SPEAKER)
    gpath,gpose=stock('S12H-gep-palms-demo',3)
    assert gpose['anchors']['stage']==[220,465]
    palm=actor_level('35-palm-hold',Actor(False,gpath,gpose),[State(hat=0)],{0},GEP_SPEAKER)
    stage(35,'390,280,670',[pin(last=6,phase='lead',ticks=[1,2,2,2,2,2,2],when=[0,'before:S12-N015']),
        wrist_roll(last=len(roll)-1,phase='story',ticks=[4,4,4,4,5,5,6,5,5,5,5,6],when=['before:S12-N015',1]),
        ctrl('Geppetto','S12H-gep-palms-demo',GEP,315,last=3,phase='between',ticks=[12,12,16,12],
             duration=52,when=[0,'before:S12-N016'])|{'after_dialogue_id':'S12-N015'},
        palm(when=['before:S12-N016',1])],detail=([460,381,418],68))
    # C36: the child starts the actual show on the response side of P05.
    kid36=actor_level('36-display',kid,tween(kid,inspect,displayed,11,halfway='back'),set())
    g36_hold=actor_level('36-settled-talk',gep,[State()],{0},GEP_SPEAKER)
    stage(36,'440,304,592',[
        ctrl('Geppetto','S12J-36-lower-demo',GEP,315,last=4,phase='lead',ticks=[10,11,13,12,7],
             when=[0,'before:S12-N017']),
        g36_hold(when=['before:S12-N017',1]),
        kid36(last=10,phase='lead',ticks=[4,4,5,6,7,8,9,8,8,10,10])],detail=([474,405,298],75))

    # C37: same grown-up fingers open, flex once, reopen. Child maintains a non-flexed hand.
    kid37=actor_level('37-listen',kid,tween(kid,displayed,relaxed,9,halfway='back'),{8},PIN_SPEAKER)
    stage(37,'415,289,640',[kid37(last=8,phase='lead',ticks=[8,9,10,10,10,9,9,8,7]),
        ctrl('Geppetto','S12H-gep-flex-demo',GEP,315,last=6,phase='lead',ticks=[6,9,12,11,14,11,12])])
    # C38: organic rolling finger flex, tactile touch, release after N019.
    spread=tween(kid,relaxed,flex,6,halfway='back')
    bending=tween(kid,flex,fold,5)[1:]
    opening=tween(kid,fold,flex,5)[1:]
    touch=tween(kid,flex,feel,6,halfway='back')[1:]
    sequence=spread+bending+opening+touch
    kid38=actor_level('38-flex-touch',kid,sequence,{len(sequence)-1},PIN_SPEAKER)
    tail38=actor_level('38-return',kid,tween(kid,feel,neutral,7),set(),PIN_SPEAKER)
    stage(38,'448,302,590',[ctrl('Geppetto','S12J-38-gep-return',GEP,315,last=4,phase='lead',ticks=[8,9,9,9,7]),
        kid38(last=len(sequence)-1,phase='lead',ticks=[5]*6+[6]*4+[6]*4+[5]*4+[10],
              when=[0,'after:S12-N019']),
        tail38(last=6,phase='tail',ticks=[3,4,5,6,6,5,4],when=['after:S12-N019',1])],
        detail=([460,436,364],106))

    # C39: the offered adult palm remains visibly separate from the child's.
    kid39=actor_level('39-prepare',kid,tween(kid,neutral,offered,8),set())
    gep39=actor_level('39-offer',gep,tween(gep,State(),open_gep,11),{10},GEP_SPEAKER)
    stage(39,'425,290,630',[gep39(last=10,phase='lead',ticks=[5,5,6,6,6,7,7,7,7,8,8]),
        kid39(last=7,phase='lead',ticks=[7,7,8,9,9,9,10,12])])
    # C40: once P07 accepts, support, warmth, then both hands safely fall apart.
    kid40=actor_level('40-contact',kid,tween(kid,offered,held,9),{8},PIN_SPEAKER)
    gep40=actor_level('40-support',gep,tween(gep,open_gep,grip_gep,8),{7},GEP_SPEAKER)
    krel=tween(kid,held,offered,6)+tween(kid,offered,neutral,7)[1:]
    grel=tween(gep,grip_gep,open_gep,6)+tween(gep,open_gep,State(),7)[1:]
    krelease=actor_level('40-child-release',kid,krel,set(),PIN_SPEAKER)
    grelease=actor_level('40-parent-release',gep,grel,set(),GEP_SPEAKER)
    stage(40,'450,301,592',[
        gep40(last=7,phase='lead',ticks=[8,8,8,8,7,7,7,7],when=[0,'after:S12-N024']),
        grelease(last=11,phase='tail',ticks=[4,4,4,5,5,5,5,6,6,6,5,5],when=['after:S12-N024',1]),
        kid40(last=8,phase='lead',ticks=[5,5,6,6,7,7,7,8,9],when=[0,'after:S12-N024']),
        krelease(last=11,phase='tail',ticks=[4,4,4,5,5,5,5,6,6,6,5,5],when=['after:S12-N024',1])],
        detail=([475,421,350],59))
    # C41: open hand draws gaze to the hat, followed by a simple leveling demonstration.
    gep41_states=tween(gep,State(),point_gep,8)+tween(gep,point_gep,angle_gep,5)[1:]+tween(gep,angle_gep,level_gep,6)[1:]
    gep41=actor_level('41-show-level',gep,gep41_states,{len(gep41_states)-1},GEP_SPEAKER)
    kid41=actor_level('41-notice-hat',kid,tween(kid,neutral,State(chin=1.9),6),set())
    stage(41,'422,282,644',[gep41(last=len(gep41_states)-1,phase='lead',
                                ticks=[5]*7+[7]+[5]*4+[6]*4+[8]),
        kid41(last=5,phase='lead',ticks=[8,8,9,10,11,12])])

    # C42: touch, rotate the actual same hat, let go, inspect book bag strap and settle.
    aa=tween(kid,State(chin=1.9),hat_grasp,8)
    bb=cap_contact_states[1:]
    cc=tween(kid,straighten,strap,6)[1:]
    dd=tween(kid,strap,awake,6)[1:]
    fix=aa+bb+cc+dd
    kid42=actor_level('42-straighten',kid,fix,{len(fix)-1},PIN_SPEAKER)
    gp42=actor_level('42-observe',gep,tween(gep,level_gep,State(),9),set())
    stage(42,'427,280,654',[gp42(last=8,phase='lead',ticks=[5,5,6,6,7,7,7,8,8]),
        kid42(last=len(fix)-1,phase='lead',ticks=[3,3,3,3,3,3,4,6,4,4,4,4,4,8]+[4]*10)],
        detail=([465,362,354],72))

    # Reverse stock whole-cel order without inventing an additional motion on either hold.
    def repack_stock(name, reference_path, indexes):
        src=read(ART/'cels'/reference_path/'registration.json')
        level=f'S12J-{name}'
        directory=ART/'cels'/level
        directory.mkdir(parents=True,exist_ok=True)
        poses=[]
        for index in indexes:
            info=src['poses'][index].copy()
            file=ART/info['file']
            target=directory/f'{len(poses):02d}.png'
            if not target.exists() or target.stat().st_size!=file.stat().st_size:
                target.write_bytes(file.read_bytes())
            poses.append(info|{'index':len(poses),'file':target.relative_to(ART).as_posix()})
        write(directory/'registration.json',{'reference_height':src['reference_height'],'poses':poses})
    repack_stock('36-lower-demo','S12H-gep-palms-demo',[3,2,2,1,0])
    repack_stock('38-gep-return','S12H-gep-flex-demo',[6,2,1,1,0])
    write(BUILD/'layout-hands.json',list(seats.values()))
    # These windows use movement intervals only. No dead-time extension or models in the master.
    write(BUILD/'motion-hands.json',{'cuts':{
        'S12-C35':{'lead_frames':13,'tail_frames':0,'between_frames':{'S12-N015':72}},
        'S12-C36':{'lead_frames':84,'tail_frames':24},'S12-C37':{'lead_frames':84,'tail_frames':0},
        'S12-C38':{'lead_frames':108,'tail_frames':36},'S12-C39':{'lead_frames':72,'tail_frames':0},
        'S12-C40':{'lead_frames':60,'tail_frames':60},'S12-C41':{'lead_frames':96,'tail_frames':0},
        'S12-C42':{'lead_frames':96,'tail_frames':24}}})
    print(f'Wrote {len(seats)} measured C35–C42 stage layouts and one bounded gesture clock.')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--speech-only',action='store_true',help='Preserve already inspected closed drawings')
    parser.add_argument('--human-source',type=Path,default=HUMAN_SOURCE)
    parser.add_argument('--hug-end',type=Path,default=HUG_END)
    parser.add_argument('--build-dir',type=Path,default=BUILD)
    args=parser.parse_args()
    SPEECH_ONLY=args.speech_only
    HUMAN_SOURCE=args.human_source.resolve()
    HUG_END=args.hug_end.resolve()
    BUILD=args.build_dir.resolve()
    ART=BUILD/'art'
    setup()
