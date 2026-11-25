#!/usr/bin/env python3
"""Expose the C30 foot-to-face transformation as registered 2D drawings."""
from copy import deepcopy
from hashlib import sha256
from itertools import accumulate
from math import cos, pi, sin
from pathlib import Path
import json

import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from normalize import GROUND, REFERENCE_HEIGHT, SIZE, STAGE_ROOT, SOURCE

V3 = Path(__file__).resolve().parents[2]
BUILD = V3 / 'build'
ART = BUILD / 'art'
WOOD = ART / 'cels/S12F-pin-ready/09.png'
EXPOSURES = [2] * 72 + [4] * 23 + [8]
OPTICAL_START = 10
OPTICAL_END = 134
STOCK = (453, 755)
GRID_Y, GRID_X = np.mgrid[:SIZE[1], :SIZE[0]]
C30 = 'S12-C30'


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def stage_json(path, data):
    temporary = path.with_suffix('.transform-pending')
    temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    temporary.replace(path)


def smooth(q):
    q = np.clip(q, 0, 1)
    return q*q*(3-2*q)


def progress(frame, first, last):
    return smooth((frame-first)/(last-first))


def group(y0, y1, radius=5):
    return smooth((GRID_Y-y0+radius)/(2*radius)) * smooth((y1+radius-GRID_Y)/(2*radius))


def ramp_at(frame, first, last, low, high, radius):
    front = (low+radius) + (high-radius - (low+radius))*progress(frame, first, last)
    resolved = smooth((GRID_Y-front+radius)/(2*radius))
    if frame >= last:
        resolved[:] = 1.0
    return resolved


def narrow_nose(wood, progress_value):
    """Shorten a single outer contour first, leaving the scalp and mouth stable."""
    if not progress_value:
        return wood
    crop = (314, 217, 386, 265)
    sculpt = wood.crop(crop)
    squeeze = 1 - .81*progress_value
    warp = []
    for top in range(0, 48, 2):
        mid = crop[1] + top + 1
        width = 1 - (1-squeeze) * smooth((mid-220)/12) * smooth((262-mid)/10)
        warp.append(((0, top, 72, top+2), (0, top, 0, top+2, 72/width, top+2, 72/width, top)))
    sculpt = sculpt.transform(sculpt.size, Image.Transform.MESH, warp, Image.Resampling.BICUBIC)
    out = wood.copy()
    out.paste(sculpt, (crop[0], crop[1]))
    return out


def material_masks(frame):
    far = smooth((GRID_X - (311+np.maximum(0, GRID_Y-354)*-.16))/15)
    near = (1-smooth((GRID_X - (160+np.maximum(0, 416-GRID_Y)*.49))/13))
    wrists = np.maximum(near, far)*group(338, 469, 9)
    hat = 1-smooth((GRID_Y-175)/13)
    lower = group(483, 683, 8)*ramp_at(frame, 3, 49, 672, 480, 16)
    costumes = group(294, 485, 9)*(1-wrists)*ramp_at(frame, 31, 75, 495, 281, 20)
    wrists_window = group(332, 474, 10)*wrists
    arms_front = 322+(489-322)*progress(frame, 59, 99)
    arms = wrists_window*smooth((arms_front-GRID_Y+11)/22)
    if frame >= 99:
        arms = wrists_window
    skin_face = group(168, 332, 11)*ramp_at(frame, 88, 125, 331, 160, 18)
    cap = hat*progress(frame, 113, 131)
    return np.maximum.reduce([lower, costumes, arms, skin_face, cap])


def actor(wood, human, frame):
    if frame <= 3:
        return wood.copy()
    if frame >= 135:
        return breathe(human, frame)
    wood = narrow_nose(wood, progress(frame, 87, 121))
    region = material_masks(frame)
    # Motion remains local to the texture edge: feet stay planted and the cap
    # sits in the same registered coordinate space. The last seamless tail uses
    # the exact generated human original rather than an outlined graphic.
    region = region+(1-region)*progress(frame, 119, 135)
    matte = Image.fromarray(np.rint(region*255).astype('uint8'))
    return Image.composite(human, wood, matte)


def breathe(source, frame):
    if frame <= 145 or frame >= 236:
        return source.copy()
    fraction = (frame-145)/(238-145)
    lift = (sin(pi*fraction)**2) * (2.45-.68*cos(2*pi*fraction))
    bands = [(0,285, lift,lift), (285,384,lift,.94*lift), (384,479,.94*lift,0), (479,755,0,0)]
    mesh = [((0,top,SIZE[0],bottom), (0,top+first,0,bottom+last,SIZE[0],bottom+last,SIZE[0],top+first))
            for top,bottom,first,last in bands]
    return source.transform(SIZE, Image.Transform.MESH, mesh, Image.Resampling.BICUBIC)


def light_pulse(frame):
    """Drifting glints outside the child's silhouette and a thin local rim."""
    size = (231, 300)
    lit = Image.new('RGBA',size)
    points = ImageDraw.Draw(lit)
    duration = 142
    if frame >= duration:
        return lit
    visibility = progress(frame, 4, 22)*(1-progress(frame, 116, duration))
    height = 253-198*progress(frame, 12, 130)
    # Few sparsely placed motes match the preparatory glow. At each body phase
    # the glints are offset so eyes and fingers remain readable.
    for num in range(16):
        phase = (frame / 47 + num * .107)%1
        beat = sin(pi*phase)**2
        x = 43+num*9.4+sin(num*1.72+phase*3.2)*15
        y = height + cos(num*.95)*19 - phase*(15+(num%3)*7)
        radius = (1.15 + (num%4)*.51)*beat
        bright = int((48+num%3*12)*beat*visibility)
        if bright <= 4:
            continue
        colour = (152,204,244,bright) if num%5 else (251,218,153,bright)
        points.ellipse((x-radius,y-radius,x+radius,y+radius),fill=colour)
        if num%4 == 0:
            points.line((x-radius*1.6,y,x+radius*1.6,y),fill=(232,248,255,bright),width=1)
            points.line((x,y-radius*1.8,x,y+radius*1.8),fill=(232,248,255,bright),width=1)
    return lit


def export_level(label, frames, reference_height, ground):
    level = ART / 'cels' / label
    level.mkdir(exist_ok=True)
    rows = []
    for i, frame in enumerate(frames):
        filename = level / f'{i:03}.png'
        frame.save(filename, compress_level=6)
        rows.append({'file':filename.relative_to(ART).as_posix(),'size':list(frame.size),
                     'anchors':{'stage':list(ground)},'sole':list(ground),
                     'sha256':sha256(filename.read_bytes()).hexdigest(),'index':i})
    stage_json(level / 'registration.json', {'level':label,'reference_height':reference_height,
               'poses':rows,'source_wood_sha256':sha256(WOOD.read_bytes()).hexdigest(),
               'source_human_sha256':sha256((SOURCE/'closed.png').read_bytes()).hexdigest()})


def make_art():
    with Image.open(WOOD) as source:
        wood = source.convert('RGBA')
    with Image.open(SOURCE/'closed.png') as source:
        human = source.convert('RGBA')
    if wood.size != STOCK or human.size != STOCK:
        raise ValueError('Transformation artwork changed its original registration')
    starts = [0, *list(accumulate(EXPOSURES))[:-1]]
    export_level('S12T-metamorph', (actor(wood,human,index) for index in starts),
                 REFERENCE_HEIGHT, GROUND)


def make_optics():
    glints = [light_pulse(index) for index in range(OPTICAL_START,OPTICAL_END,2)]
    if any(not frame.getchannel('A').getbbox() for frame in glints):
        raise ValueError('The optical exposure must hold transparent space around visible paint.')
    export_level('S12T-optics', glints,300,(0,0))


def make_layout():
    prior = next(shot for shot in read(BUILD/'layout-fairy.json') if shot['id']=='S12-C29')
    # Keep the two preparatory highlights for the first frames without a flash.
    layers = [deepcopy(row) for row in prior['layout']
              if row['track'] not in ('Pinocchio','blue-reflection','rising-particles')]
    character = {'track':'Pinocchio-transformation','level':'S12T-metamorph',
                 'root':list(STAGE_ROOT),'height':236,'anchor':'stage',
                 'first_cel':0,'last_cel':len(EXPOSURES)-1,'motion':'story','start':0,'end':1,
                 'motion_start':0,'motion_end':1,'exposure_frames':EXPOSURES}
    layers.insert(4, character)
    n = sum(EXPOSURES)
    for row in prior['layout']:
        if row['track'] not in ('blue-reflection','rising-particles'):
            continue
        carry = {name: row[name] for name in ('track','level','root','height','anchor','flip')}
        carry.update(first_cel=row['last_cel'],motion='hold',start=0,end=4/n)
        layers.append(carry)
    layers.append({'track':'staged-magic-motes','level':'S12T-optics','root':[446,377],
                   'height':300,'anchor':'stage','first_cel':0,
                   'last_cel':(OPTICAL_END-OPTICAL_START)//2-1,'motion':'story',
                   'start':OPTICAL_START/n,'end':OPTICAL_END/n,
                   'motion_start':OPTICAL_START/n,'motion_end':OPTICAL_END/n,
                   'exposure_frames':[2]*((OPTICAL_END-OPTICAL_START)//2)})
    stage_json(BUILD/'layout-transform.json',[{'id':C30,'plate':prior['plate'].split('@',1)[0],
        'camera_cues':[{'frame':0,'crop':[420,271,694]},{'frame':63,'crop':[420,271,694]},
                       {'frame':132,'crop':[440,399,297],'interpolate':True}], 'layout':layers}])
    stage_json(BUILD/'motion-transform.json',{'cuts':{C30:{'lead_frames':144,'tail_frames':6}}})


if __name__ == '__main__':
    make_art()
    make_optics()
    make_layout()
