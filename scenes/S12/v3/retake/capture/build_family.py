#!/usr/bin/env python3
"""Register the re-inked transformation and family sequence in the original 2D camera."""

from copy import deepcopy
from argparse import ArgumentParser
import json
from pathlib import Path
import runpy
import shutil
import sys

import numpy as np
from PIL import Image

from register_character import ART, BASELINE, GROUND, HEIGHT, HERE, SIZE, SOURCE
from register_character import digest, extract_row, load, register, write

BUILD = ART.parent
BASE_BUILD = BASELINE / 'build'
HERO_HEIGHT, HERO_ROOT = 236, (561, 643)
ADULT_HEIGHT, ADULT_ROOT = 315, (667, 629)
NEW_ADULT = 'S12N-adult-reaction'


def isolate():
    levels = ART / 'cels'
    levels.mkdir(parents=True, exist_ok=True)
    for path in (BASE_BUILD/'art').iterdir():
        if path.name != 'cels' and not (ART/path.name).exists():
            (ART/path.name).symlink_to(path)
    for path in (BASE_BUILD/'art/cels').iterdir():
        # The builders below write only their own levels. Other layers are read-only.
        if path.name.startswith(('S12G-', 'S12T-metamorph')) or path.name == 'S12HN-character':
            continue
        if not (levels/path.name).exists():
            (levels/path.name).symlink_to(path, target_is_directory=True)


def setup_family():
    module = runpy.run_path(str(BASELINE/'art/first_hug/build.py'))['main'].__globals__
    sources = HERE / 'hug-source'
    sources.mkdir(exist_ok=True)
    shutil.copyfile(HERE/'paired-keyframes.png', sources/'paired-keyframes.png')
    module.update(BUILD=BUILD, ART=ART, HUMAN=SOURCE, HERE=sources, V3=HERE)
    # Record new facial landmarks in the actual newly painted 512px panels.
    child_faces = (((166,186),(190,207)),((219,182),(235,204)),((242,181),(267,196)),
                   ((239,176),(262,196)),((200,181),(218,198)),((157,174),(180,204)))
    artwork = [list(panel) for panel in module['DRAWING_POINTS']]
    for panel, (eye, mouth) in zip(artwork, child_faces, strict=True):
        panel[1:3] = [eye, mouth]
    original_register = module['register_key']
    refined_step = HERE/'pair-step-refined.png'
    if refined_step.is_file():
        # A new whole drawing puts the receiving palm below the child's eyes.
        artwork[0] = [(39,109),(171,187),(188,207),(135,228),(82,275),(184,320),(253,267),
                      (133,340),(94,466),(209,446),(362,66),(333,134),(340,162),(373,190),
                      (450,295),(283,292),(387,346),(334,464),(420,467)]
        drawing = load(refined_step).resize((512,512),Image.Resampling.LANCZOS)

        def corrected_step(art, number):
            return original_register(drawing if number == 0 else art,number)

        module['register_key'] = corrected_step
    module['DRAWING_POINTS'] = tuple(tuple(panel) for panel in artwork)
    return module


def key(draw, eye, nose, mouth, elbow, wrist, support=(168, 665, 290, 661)):
    """Track both sole contacts, the hat, and the landmarks used in the drawn turn."""
    alpha = draw.getchannel('A').getbbox()
    left, top, _, _ = alpha
    return draw, np.array(((left+24, top+13), (237, 132), (223, 299), eye, nose, mouth,
                            (134,347), (257,414), (152,427), elbow, wrist,
                            (204,478),(174,582),(261,586), support[:2], support[2:]))


def between(module, first, last, amount):
    image, points = module['inbetween'](first, last, amount)
    return image.crop((0, 0, *SIZE)), points


def exposures(module, keys, times, end):
    output, ticks, marks = [], [], []
    for first, last, start, stop in zip(keys[:-1], keys[1:], times[:-1], times[1:], strict=True):
        frames = stop-start
        for offset in range(0, frames, 2):
            fraction = float(module['smooth'](offset/frames))
            image, points = between(module, first, last, fraction)
            output.append(image)
            ticks.append(min(frames-offset, 2))
            marks.append(points)
    output.append(keys[-1][0]); ticks.append(end-times[-1]); marks.append(keys[-1][1])
    return output, ticks, marks


def transform(module, final):
    wood = load(BASE_BUILD/'art/cels/S12F-pin-ready/09.png')
    poses = extract_row('metamorph')
    neutral = key(final,(273,220),(306,246),(297,258),(340,383),(377,426))
    frames, ticks, _ = exposures(module, [
        key(wood,(271,239),(364,244),(296,277),(326,386),(378,423)),
        key(poses[0],(258,225),(335,229),(280,251),(282,351),(352,317)),
        key(poses[1],(281,246),(324,263),(283,281),(295,351),(337,300)),
        key(poses[2],(282,254),(303,264),(279,282),(300,346),(337,310)),
        key(poses[3],(290,249),(318,269),(288,291),(303,357),(350,330)),
        key(poses[4],(275,222),(302,244),(295,259),(328,381),(354,436)),
        neutral,
    ], [0, 20, 44, 72, 94, 124, 144], 244)
    sys.path.insert(0, str(BASELINE/'art/human'))
    old = runpy.run_path(str(BASELINE/'art/human/transform.py'))['make_layout'].__globals__
    old.update(ART=ART, BUILD=BUILD, SOURCE=SOURCE)
    old['export_level']('S12T-metamorph', frames, HEIGHT, GROUND)
    spec = json.loads((BASE_BUILD/'layout-transform.json').read_text())[0]
    hero = next(row for row in spec['layout'] if row['track']=='Pinocchio-transformation')
    hero.update(last_cel=len(ticks)-1, exposure_frames=ticks)
    spec['camera_cues'] = [{'frame':0,'crop':[420,271,694]}, {'frame':84,'crop':[420,271,694]},
                           {'frame':136,'crop':[451,297,580], 'interpolate':True}]
    return spec


def add_lips(module, model, opened):
    for mode in ('small', 'wide'):
        drawing, _ = module['oral_pose'](opened, model['anchors']['mouth'], 'hero', mode, .74)
        path = SOURCE / f'speech-{mode}.png'
        drawing.save(path)
        model['visemes'][mode] = {'file':path.name,'sha256':digest(path)}
    write(SOURCE/'registration.json',model)


def revelation(module, final):
    rows = extract_row('revelation')
    level = module['Level']('first-revelation', {'art':'revelation/sprite-sheet-alpha.png',
                                               'atlas_sha256':digest(HERE/'revelation/sprite-sheet-alpha.png')})
    base = key(final,(271,221),(309,245),(297,258),(340,383),(377,426))
    # The first close view continues the previous face before a short downward check.
    order = [base,
             key(rows[1],(274,244),(299,258),(279,272),(305,371),(344,393)),
             key(rows[2],(280,247),(296,264),(279,279),(291,360),(314,327)),
             key(rows[3],(267,245),(289,260),(276,269),(298,363),(313,390)),
             key(rows[4],(268,212),(287,224),(285,240),(341,376),(350,440)),
             key(rows[5],(269,213),(296,230),(287,246),(322,384),(352,446)), base]
    frames, ticks, points = exposures(module, order, [0,5,14,24,39,66,106],145)
    previous_smile = (0, 0)
    for index, (art, marks) in enumerate(zip(frames, points, strict=True)):
        mouth = marks[5]
        position = (mouth[0],mouth[1])
        picture, placement = module['placed'](art,HERO_ROOT,HERO_HEIGHT,HEIGHT,GROUND)
        variants = {}
        for mode in module['MODES']:
            alternate, bounds = module['oral_pose'](art,position,'hero',mode,.66)
            variants[mode] = module['placed'](alternate,HERO_ROOT,HERO_HEIGHT,HEIGHT,GROUND)[0]
        level.add(picture, 'first glance, recognition and joy', variants=variants,
                  mouth=module['rect_stage'](bounds,placement), planted_stage=list(HERO_ROOT))
        previous_smile = position
    if previous_smile != (297,258):
        raise ValueError('Recognition must finish at the registered school costume pose')
    return level.finish(), ticks


def adult_bridge(module):
    sketch = module['Level']('adult-first-response', {'sheet':digest(HERE/'adult/sprite-sheet-alpha.png')})
    def place(source, height, reference, anchor):
        return module['placed'](source, ADULT_ROOT, height, reference, anchor)[0]

    prior, info, registry = module['source_pose']('S12F-gep-up',5)
    initial = place(prior,ADULT_HEIGHT,registry['reference_height'],info['anchors']['stage'])
    sketch.add(initial,'C29 carry: looking at the fairy')
    paths = sorted((HERE/'adult/frames/recognize').glob('frame-*.png'))
    for path in paths[:5]:
        actor = load(path)
        alpha = actor.getchannel('A').getbbox()
        # Keep the two boots on the prior stage baseline; the head and arms do the acting.
        left,top,right,bottom=alpha
        sketch.add(place(actor,ADULT_HEIGHT,bottom-top,(round((left+right)/2),bottom-2)),
                   'Geppetto notices the change, looks across, and reacts before speaking')
    next_pose, info, registry=module['source_pose']('S12H-gep-surprise-open',0)
    final = place(next_pose,ADULT_HEIGHT,registry['reference_height'],info['anchors']['stage'])
    sketch.add(final,'Recognizes the boy at his left, held into the next cut')
    return sketch.finish(), [78, 6, 9, 10, 12, 20, 109]


def main():
    cli = ArgumentParser(description=__doc__)
    cli.add_argument('--pair-only', action='store_true', help='Rephotograph only the updated two-person poses')
    args = cli.parse_args()
    isolate()
    if args.pair_only:
        module = setup_family()
        model, _, opened = module['human_bases']()
        module['pair_scene'](model,opened)
        return
    model, closed, opened = register()
    module = setup_family()
    add_lips(module,model,opened)
    spec = transform(module,opened)
    level, durations = adult_bridge(module)
    adult = next(row for row in spec['layout'] if row['track']=='Geppetto')
    adult.update(level=level,root=[0,0],height=720,first_cel=0,last_cel=len(durations)-1,
                 motion='story',motion_start=0,motion_end=1,exposure_frames=durations)
    write(BUILD/'layout-transform.json',[spec])
    module['revelation'] = lambda _model,_closed,_opened: revelation(module,_opened)
    module['main']()
    hug = json.loads((BUILD/'layout-hug.json').read_text())
    hug[0]['layout'] = [layer for layer in hug[0]['layout'] if layer['track']!='Geppetto-fairy-look']
    adult_carry = next(layer for layer in hug[0]['layout'] if layer['track']=='Geppetto-to-child')
    adult_carry['span']=['start','end']
    write(BUILD/'layout-hug.json',hug)


if __name__=='__main__':
    main()
