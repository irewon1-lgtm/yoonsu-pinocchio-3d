#!/usr/bin/env python3
"""Register supporting S12 whole cels for the approved human performance."""
from functools import lru_cache
from hashlib import file_digest
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw
from scipy.ndimage import binary_dilation, find_objects, label, map_coordinates

HERE = Path(__file__).resolve().parent
V3 = HERE.parents[1]
SCENES = V3.parents[1]
S11 = SCENES / 'S11/v2/build/art'
OUT = V3 / 'build/art'
PAD = 88
GEP_WORLD = (667, 629)
CRICKET_WORLD = (515, 636)
SURPRISE_SHEET = HERE / 'source-geppetto-surprise-8cels.png'
DEMO_SHEET = HERE / 'source-geppetto-hands-8cels.png'


def sha(path):
    with path.open('rb') as file:
        return file_digest(file, 'sha256').hexdigest()


def write(path, value):
    temp = path.with_suffix(path.suffix + '.pending')
    temp.write_text(json.dumps(value, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    temp.replace(path)


def coord(point):
    return tuple(p + PAD for p in point)


def pad(image):
    result = Image.new('RGBA', (image.width+2*PAD, image.height+2*PAD))
    result.alpha_composite(image, (PAD,PAD))
    return result


@lru_cache(maxsize=None)
def source(name, index):
    registry = S11 / 'cels' / name / 'registration.json'
    data = json.loads(registry.read_text(encoding='utf-8'))
    pose = data['poses'][index]
    path = S11 / pose['file']
    with Image.open(path) as image:
        art = image.convert('RGBA')
    return art, pose['anchors']['stage'], data['reference_height'], {
        'file':path.relative_to(SCENES).as_posix(), 'sha256':sha(path),
        'registry_sha256':sha(registry), 'donor_index':index,
    }


def warp(image, x_shift, y_shift):
    """Sample one textured drawing with alpha-weighted pigment at each new point."""
    xs, ys = np.meshgrid(np.arange(image.width, dtype=np.float32), np.arange(image.height,dtype=np.float32))
    coords = (ys-y_shift, xs-x_shift)
    raw = np.asarray(image, dtype=np.float32)
    opacity = raw[:,:,3] / 255
    alpha = map_coordinates(opacity, coords, order=1, prefilter=False)
    denom = np.maximum(alpha, .003)
    color = np.stack([map_coordinates(raw[:,:,i]*opacity, coords, order=1, prefilter=False)/denom
                      for i in range(3)], axis=2)
    return Image.fromarray(np.concatenate((color, (255*alpha)[:,:,None]), axis=2).clip(0,255).astype(np.uint8))


def opaque_components(path):
    with Image.open(path) as source_sheet:
        sheet = np.asarray(source_sheet.convert('RGBA')).copy()
    alpha_floor = 197 if sheet[0,0,3] > 100 else 6
    component_threshold = 224 if alpha_floor > 100 else 40
    glyph, _ = label(sheet[:,:,3] >= component_threshold)
    components = []
    for index, bounds in enumerate(find_objects(glyph),1):
        y,x = bounds
        owned = glyph[bounds] == index
        if np.count_nonzero(owned) < 40000:
            continue
        region=(slice(max(0,y.start-4),min(sheet.shape[0],y.stop+4)),
                slice(max(0,x.start-4),min(sheet.shape[1],x.stop+4)))
        art = sheet[region].copy()
        connected = binary_dilation(glyph[region] == index, iterations=2)
        alpha = art[:,:,3].astype(np.int32)
        alpha = np.clip((alpha-alpha_floor)*255//(252-alpha_floor), 0, 255)
        art[:,:,3] = np.where(connected, alpha, 0)
        art[art[:,:,3] == 0] = 0
        components.append((y.start//500,x.start,Image.fromarray(art)))
    components.sort(key=lambda entry:entry[:2])
    if len(components) != 8:
        raise ValueError(f'{path.name}: expected eight complete connected full-body cels')
    return [art for _,_,art in components]


def registered_gep(raw):
    # A draw-specific matte trim with opaque-pixel shoe registration, not a bounding-box centre.
    mask=np.asarray(raw)[:,:,3] >= 128
    leaves,columns=np.where(mask)
    foot_y=int(leaves.max())
    sole_columns=columns[leaves>=foot_y-20]
    foot_x=float(np.median(sole_columns))
    scale=427/(foot_y-int(leaves.min()))
    resized=raw.resize(tuple(round(d*scale) for d in raw.size),Image.Resampling.LANCZOS)
    out=Image.new('RGBA',(450,500))
    # The S11 stage point is 12 pixels toward the apron-side boot from the opaque shoe centre.
    x=220-round(foot_x*scale)-12
    y=465-round(foot_y*scale)
    out.alpha_composite(resized,(x,y))
    return out



class Level:
    def __init__(self, label, sources, world, height, reference, anchor):
        self.name = 'S12H-' + label
        self.directory = OUT / 'cels' / self.name
        self.directory.mkdir(parents=True, exist_ok=True)
        self.sources, self.world, self.height = sources, world, height
        self.reference, self.anchor = reference, anchor
        self.poses = []
        self.drawings = []

    def save(self,image,number,viseme=''):
        path=self.directory / f'{number:02d}{viseme}.png'
        image.save(path,compress_level=2)
        return {'file':path.relative_to(OUT).as_posix(), 'size':list(image.size),
                'anchors':{'stage':list(self.anchor)},'sole':list(self.anchor),'sha256':sha(path)}

    def add(self,image,ticks,phase,offset=(0,0),variants=None):
        row=self.save(image,len(self.poses))
        if variants:
            row['viseme_cels']={key:self.save(value,len(self.poses),'-'+key) for key,value in variants.items()}
        row.update(index=len(self.poses),phase_ticks=ticks,phase=phase,stage_offset=list(offset))
        self.poses.append(row)
        self.drawings.append(image)

    def finish(self):
        keep={Path(p['file']).name for p in self.poses}
        keep.update(Path(v['file']).name for p in self.poses for v in p.get('viseme_cels',{}).values())
        for old in self.directory.glob('*.png'):
            if old.name not in keep:
                old.unlink()
        write(self.directory/'registration.json',{'level':self.name,'reference_height':self.reference,
              'sources':self.sources,'stage_anchor':self.world,'display_height':self.height,'poses':self.poses})


def gep_levels():
    references=[source('S11L-gep-wave',i)[3] for i in (0,3)]
    surprise=Level('gep-surprise-open',
        references+[{'file':SURPRISE_SHEET.name,'sha256':sha(SURPRISE_SHEET),
                     'role':'reference-guided whole-cel action drawings'}],GEP_WORLD,315,427,(220,465))
    image=[registered_gep(art) for art in opaque_components(SURPRISE_SHEET)]
    beats=[(4,'listening'),(3,'eyes widen'),(3,'forearm rises'),(5,'hand near mouth'),
           (4,'uncovering face'),(4,'opens arms'),(4,'open invitation'),(7,'holds invitation')]
    for index,(ticks,phase) in enumerate(beats):
        surprise.add(image[index],ticks,phase)
    surprise.finish()
    references=references+[{'file':DEMO_SHEET.name,'sha256':sha(DEMO_SHEET),
                            'role':'reference-guided whole-cel action drawings'}]
    demo=[registered_gep(art) for art in opaque_components(DEMO_SHEET)]
    palms=Level('gep-palms-demo',references,GEP_WORLD,315,427,(220,465))
    for i,(ticks,phase) in enumerate([(5,'rests'),(5,'elbows lead'),(5,'wrists turn'),(11,'shows palms')]):
        palms.add(demo[i],ticks,phase)
    palms.finish()
    flex=Level('gep-flex-demo',references,GEP_WORLD,315,427,(220,465))
    # Initiate the reach in the uncurled palm before the single bend and recovery.
    sequence=[(demo[0],4,'rests'),(image[1],4,'lifts wrist'),(demo[4],7,'shows one open palm'),
              (demo[5],5,'bends fingers'),(demo[6],7,'fingers curled'),(demo[5],5,'releases tension'),
              (demo[7],10,'opens same palm')]
    for drawing,ticks,phase in sequence:
        flex.add(drawing,ticks,phase)
    flex.finish()
    return surprise,palms,flex

def cricket_level():
    still,anchor,ref,donor=source('S11L-cricket-ground',0)
    padded=pad(still)
    x,y=np.meshgrid(np.arange(padded.width)-PAD,np.arange(padded.height)-PAD)
    # All non-flying cels leave every source foot pixel below its shin exactly in place.
    above_ankles=np.clip((386-y)/123,0,1)
    above_ankles=above_ankles*above_ankles*(3-2*above_ankles)
    toward_front=np.clip((205-x)/195,0,1)
    beat=[(0,0,0,0,0,5,'ready'),(5,-4,0,0,0,2,'anticipation'),
          (14,-7,0,0,0,2,'lowers hips'),(28,-11,0,0,0,2,'weight loads'),
          (34,-12,0,0,0,2,'push'),(8,1,0,0,0,1,'toe-off'),
          (-11,2,1,-2,-10,1,'extension'),(-17,7,15,-4,-23,1,'lift'),
          (-11,11,27,-6,-34,1,'tuck'),(-6,9,35,-8,-42,1,'ascent'),
          (-1,4,39,-10,-47,2,'apex'),(4,0,31,-12,-44,1,'descent'),
          (9,-4,16,-14,-35,1,'untucks'),(8,-3,5,-16,-23,1,'reaches for ground'),
          (4,-2,0,-17,-10,1,'approaches landing'),(8,-4,0,-18,0,1,'toe contact'),
          (24,-7,0,-18,0,2,'absorbs weight'),(30,-10,0,-18,0,2,'all feet loaded'),
          (20,-6,0,-18,0,2,'unloads'),(11,-2,0,-18,0,2,'settles'),
          (4,0,0,-18,0,2,'settles'),(0,0,0,-18,0,6,'feet planted')]
    level=Level('cricket-celebration', [donor],CRICKET_WORLD,84,ref,coord(anchor))
    for dip,sway,tuck,travel,lift,ticks,name in beat:
        foreleg=np.clip((y-236)/159,0,1)*toward_front
        hindleg=np.clip((y-254)/145,0,1)*(1-toward_front)
        dx=sway*above_ankles*(.7+.3*toward_front)+tuck*(foreleg*.42-hindleg*.23)
        dy=dip*above_ankles*(.77+.23*toward_front)-tuck*(foreleg*.54+hindleg*.43)
        image=warp(padded,dx,dy) if dip or sway or tuck else padded.copy()
        if lift == 0:
            grounded_strip=PAD+387
            image.paste(padded.crop((0,grounded_strip,padded.width,padded.height)),(0,grounded_strip))
        level.add(image,ticks,name,(travel,lift))
    level.finish()
    return level


def preview(levels):
    for level in levels:
        from PIL import ImageFont
        size=(260,300) if level.name.startswith('S12H-gep') else (220,190)
        count=len(level.poses)
        columns=6
        width,height=size
        board=Image.new('RGB',(columns*width,((count+columns-1)//columns)*height),'#d7c5a8')
        pen=ImageDraw.Draw(board)
        for i,(row,image) in enumerate(zip(level.poses,level.drawings,strict=True)):
            col, line = i%columns,i//columns
            dx,dy = row['stage_offset']
            scale=(height-37)/level.reference
            if not level.name.startswith('S12H-gep'):
                scale*=.72
            size=(round(image.width*scale),round(image.height*scale))
            art=image.resize(size,Image.Resampling.LANCZOS)
            local_anchor=tuple(round(p*scale) for p in level.anchor)
            x=col*width+width//2-local_anchor[0]+round(dx)
            y=line*height+height-24-local_anchor[1]+round(dy)
            ground=line*height+height-23
            pen.line((col*width+8,ground,(col+1)*width-8,ground), fill='#a9916b',width=1)
            board.paste(art,(x,y),art)
            pen.text((col*width+7,line*height+7),f"{i:02d}  {row['phase']}  ({row['phase_ticks']}f)",fill='#241c12')
        board.save(HERE/(level.name+'-contact.jpg'),quality=86,optimize=True)


def state(geps, cricket):
    surprise, palms, flex = geps
    def clip(level):
        return {'level':level.name,'fps':24,'xy':list(level.world),'height':level.height,
                'poses': [{'index':p['index'],'frames':p['phase_ticks'],'stage_offset':p['stage_offset'],
                           'phase':p['phase']} for p in level.poses]}
    write(HERE/'support-state.json',{
        'scope':'SUPPORT_ONLY_HUMAN_COMPOSITE_BLOCKED_RESOURCE',
        'plate':'S11L-school-open.png', 'plate_size':[1280,720],
        'stage':{'geppetto':list(GEP_WORLD),'cricket':list(CRICKET_WORLD),'fairy':[831,442],
                 'teacher':[739,559],'human':None},
        'state':{'geppetto_glasses':'ON_FACE','school_door':'OPEN','signboard':'UPRIGHT_STABLE',
                 'cricket':'SAFE_FREE','fairy':'PRESENT'},
        'cuts':{
            'S12-C32':clip(surprise) | {'sync':'Recognition before U031; open arms into C33 once U032 completes.',
                     'pending':'Human eyeline and reverse frame; align actual U031/U032 readings to mouth variants.'},
            'S12-C34':clip(cricket) | {'sync':'One jump only. U033 requires cricket viseme exposure; final ground stage offset persists in C35 onward.',
                     'end_stage':[497,636], 'pending':'Human/Geppetto hug release, U033 lip shapes, Fairy reaction.'},
            'S12-C35':clip(palms) | {'sync':'N015 then finish both palms, N016 actual end then P05. Hold finale during waiting.',
                     'pending':'Human examines hands; human performs own P05 response in C36.'},
            'S12-C37':clip(flex) | {'sync':'One Geppetto flex only before N018. P06 opens after N018 actual end.',
                     'pending':'Human keeps fingers inert until C38 response.'}},
        'blocked':{'source':'CHAR_YOONSU_HUMAN', 'range':'S12-C30–S12-C50',
                   'C33':'Requires counterweight, torso/arm contact and child’s bag clearance.',
                   'C36':'Requires approved human palms and Geppetto eyeline',
                   'C38':'Requires approved human hand articulation after P06',
                   'C39':'Requires actual hand-in-hand contact after question gate.'}})


if __name__=='__main__':
    geps=gep_levels()
    cricket=cricket_level()
    preview((*geps,cricket))
    state(geps,cricket)
