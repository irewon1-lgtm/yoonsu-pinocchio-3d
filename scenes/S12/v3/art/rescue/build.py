#!/usr/bin/env python3
"""Stage the schoolyard after the rescue through the S11 whole-cel camera."""
from __future__ import annotations

import json
from functools import lru_cache
from hashlib import file_digest
from pathlib import Path
import runpy
import shutil

from PIL import Image, ImageDraw, ImageFilter


V3 = Path(__file__).resolve().parents[2]
SCENES = V3.parents[1]
STAGE = V3 / 'build/art'
SCHOOL = SCENES / 'S11/v2/build/art'
S07 = SCENES / 'S07/production/art'
PLATE = 'S12R-school.png'
SIZE = (1280, 720)
PIN = (541, 630)
GEP = (667, 629)
CRICKET = (479, 636)
LEVEL_PREFIX = 'S12R-'
SPEAKERS = {'pin': '피노키오', 'gep': '제페토', 'cricket': '귀뚜라미'}
SCRIPT = SCENES / 'S10/v2/art/late/make_late_art.py'
BODY = runpy.run_path(str(SCRIPT))


def put_json(path, document):
    pending = path.with_suffix('.json.pending')
    pending.write_text(json.dumps(document, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    pending.replace(path)


@lru_cache(maxsize=None)
def registry(name, art=SCHOOL):
    source = 'S11L-' + name if art == SCHOOL else name
    return json.loads((art / 'cels' / source / 'registration.json').read_text())


def clone(name, art=SCHOOL):
    data = registry(name, art).copy()
    folder = STAGE / 'cels' / (LEVEL_PREFIX + name)
    folder.mkdir(parents=True, exist_ok=True)
    original_poses = data['poses']
    origin = original_poses[0]['anchors']['stage']
    sole_offset = original_poses[0]['sole'][0] - origin[0]
    data['poses'] = []

    def drawing(pose):
        source = art / pose['file']
        target = folder / source.name
        if not target.exists():
            target.hardlink_to(source)
        result = pose | {'file': str(target.relative_to(STAGE))}
        if 'stage' not in result.get('anchors', {}):
            sx, sy = pose['sole']
            result['anchors'] = {**pose.get('anchors', {}), 'stage': [sx - sole_offset, sy]}
        return result

    for pose in original_poses:
        copy = drawing(pose)
        if 'viseme_cels' in pose:
            copy['viseme_cels'] = {mode: drawing(value) for mode, value in pose['viseme_cels'].items()}
        data['poses'].append(copy)
    if data.get('visemes'):
        open_poses = {mode: data['poses'][index].copy() for mode, index in data['visemes'].items() if mode != 'closed'}
        for index in (0, 6):
            if index < len(data['poses']):
                data['poses'][index]['viseme_cels'] = open_poses
    data['source_registration'] = str((art / 'cels' / Path(registry(name, art)['poses'][0]['file']).parent.name /
                                       'registration.json').relative_to(SCENES))
    put_json(folder / 'registration.json', data)


def registered_pose(name, index, root, height, flip=False, mode='closed', art=SCHOOL):
    data = registry(name, art)
    row = data['poses'][index]
    if mode != 'closed':
        if 'viseme_cels' in row:
            row = row['viseme_cels'].get(mode, row['viseme_cels']['small'])
        elif 'visemes' in data:
            row = data['poses'][data['visemes'].get(mode, data['visemes']['small'])]
    with Image.open(art / row['file']) as source:
        return BODY['blit'](source, root, height, data['reference_height'], row['anchors']['stage'], flip)


class WholeCels:
    def __init__(self, name):
        self.folder = STAGE / 'cels' / (LEVEL_PREFIX + name)
        self.folder.mkdir(parents=True, exist_ok=True)
        self.poses = []

    def save(self, image, filename):
        x0, y0, x1, y1 = image.getchannel('A').getbbox()
        left, top, right, bottom = x0 - 4, y0 - 4, x1 + 4, y1 + 4
        image = image.crop((left, top, right, bottom))
        target = self.folder / (filename + '.png')
        image.save(target, compress_level=4)
        with target.open('rb') as stream:
            sha = file_digest(stream, 'sha256').hexdigest()
        return {'file': str(target.relative_to(STAGE)), 'size': list(image.size),
                'anchors': {'stage': [-left, -top]}, 'world_bounds': [x0, y0, x1, y1], 'sha256': sha}

    def add(self, image, note, modes=None):
        index = len(self.poses)
        name = f'{index:03d}'
        pose = self.save(image, name) | {'index': index, 'action': note}
        if modes:
            pose['viseme_cels'] = {mode: self.save(take, f'{name}-{mode}') for mode, take in modes.items()}
        self.poses.append(pose)

    def write(self):
        put_json(self.folder / 'registration.json', {'reference_height': 720, 'poses': self.poses})


def adult_look(image, down, toward_pin):
    """Lower the head and chest over planted shoes without scaling the adult."""
    image = image.crop((560, 294, 771, 638))
    rows = ((0, 0, 0), (8, 0, 0), (54, 1, 1), (118, .94, .86),
            (174, .73, .57), (223, .37, .28), (260, .09, .06), (292, 0, 0), (344, 0, 0))
    mesh = []
    for (first, start_dx, start_dy), (last, end_dx, end_dy) in zip(rows, rows[1:]):
        top, bottom = first - down * start_dy, last - down * end_dy
        left_top = toward_pin * start_dx
        left_bottom = toward_pin * end_dx
        mesh.append(((0, first, image.width, last), (left_top, top, left_bottom, bottom,
                     image.width + left_bottom, bottom, image.width + left_top, top)))
    drawing = Image.new('RGBA', SIZE)
    drawing.alpha_composite(image.transform(image.size, Image.Transform.MESH, mesh, Image.Resampling.BICUBIC), (560, 294))
    return drawing


def adult_drawings():
    level = WholeCels('gep-lower-gaze')
    phases = ((0, 0), (2, 2), (5, 4), (8, 7), (11, 9), (13, 11),
              (14, 13), (16, 16), (17, 15), (14, 9), (12, 7), (10, 6), (7, 4), (4, 2), (2, 1), (0, 0))
    for index, (down, toward) in enumerate(phases):
        portrait = {mode: adult_look(registered_pose('gep-talk', 0, GEP, 315, True, mode), down, toward)
                    for mode in ('closed', 'small', 'wide', 'round', 'teeth', 'pressed')}
        note = ('bend' if index < 7 else 'inspect' if index < 9 else 'rise')
        level.add(portrait.pop('closed'), note, portrait)
    level.write()


def paint_reaching_arm(drawing, contact, fraction):
    """Redraw the arm contour and carry the original wood finish to its new pose."""
    shoulder = BODY['offset']((164, 287))
    elbow = BODY['offset'](BODY['blend']((169, 310), (182, 332), fraction))
    wrist = BODY['offset'](contact)
    hand_tip = (wrist[0] + 34, wrist[1] + 18 - 7 * fraction)
    arm = Image.new('RGBA', drawing.size)
    painter = ImageDraw.Draw(arm)
    for shade, width in [((115, 74, 48, 255), 37), ((175, 119, 77, 255), 35),
                         ((210, 151, 98, 255), 31), ((231, 177, 121, 255), 25), ((238, 191, 142, 255), 7)]:
        path = [shoulder, elbow, wrist]
        if width == 7:
            path = [(x - 5, y - 1) for x, y in path]
        painter.line(path, fill=shade, width=width, joint='curve')
        reach = width / 2
        for x, y in path[1:]:
            painter.ellipse((x - reach, y - reach, x + reach, y + reach), fill=shade)
    arm = arm.filter(ImageFilter.GaussianBlur(1.05))

    if fraction < .4:
        wrist_source = BODY['offset']((191, 329))
        tip_source = BODY['offset']((223, 349))
        fingers = [(182, 327), (195, 323), (212, 322), (225, 327), (235, 335), (241, 348),
                   (239, 360), (231, 366), (221, 367), (207, 360), (196, 358), (188, 353), (183, 339)]
        fingers = BODY['isolated'](drawing, [BODY['offset'](point) for point in fingers], .65)
    else:
        # The five-finger open palm is drawn in the approved S11 farewell art.
        source = Image.new('RGBA', drawing.size)
        with Image.open(SCHOOL / 'cels/S11L-pin-wave-motion/05.png') as image:
            source.alpha_composite(image)
        wrist_source = (149, 197)
        tip_source = (181, 187)
        fingers = [(147, 189), (146, 205), (153, 212), (172, 212), (199, 201), (203, 161), (149, 160)]
        fingers = BODY['isolated'](source, fingers, .65)
    arm.alpha_composite(BODY['deform'](fingers, wrist_source, tip_source, wrist, hand_tip, .98))
    return arm


def low_palm(index, fraction):
    """Articulate the original wooden arm within the planted crouch drawing."""
    data = registry('pin-seat-gesture')
    pose = data['poses'][index]
    with Image.open(SCHOOL / pose['file']) as image:
        drawing = BODY['padded'](image.copy())
    anchor = BODY['offset'](pose['anchors']['stage'])
    # The cuff stays at the painted elbow of the original sleeve. The hand
    # approaches the clear patch by Cricket, away from the standing board.
    if index == 6 and fraction:
        edge = [(145, 289), (156, 280), (172, 276), (177, 281), (181, 291), (188, 294),
                (202, 309), (212, 321), (225, 327), (235, 335), (241, 348), (239, 360),
                (231, 366), (221, 367), (207, 360), (196, 358), (188, 353), (183, 339),
                (181, 329), (170, 328), (158, 322), (153, 312), (148, 302)]
        edge = [BODY['offset'](point) for point in edge]
        contact = BODY['blend']((188, 327), (223, 387), fraction)
        clean = BODY['erase'](drawing, edge, .5)
        knee = [(186, 343), (195, 337), (216, 337), (225, 347), (227, 365), (219, 375), (185, 371)]
        knee = [BODY['offset'](point) for point in knee]
        repaired = Image.new('RGBA', clean.size)
        repaired.alpha_composite(drawing, (0, -30))
        clean.alpha_composite(BODY['isolated'](repaired, knee, 1.3))
        clean.alpha_composite(paint_reaching_arm(drawing, contact, fraction))
        cuff = [(141, 243), (163, 237), (181, 271), (185, 278), (170, 279), (149, 289), (136, 283)]
        clean.alpha_composite(BODY['isolated'](drawing, [BODY['offset'](point) for point in cuff], .7))
        drawing = clean
    return BODY['blit'](drawing, PIN, 222, data['reference_height'], anchor, True)


def child_drawings():
    level = WholeCels('pin-low-palm')
    level.add(registered_pose('pin-listen-left', 0, PIN, 236), 'standing with weight over planted shoes')
    for index, amount, description in (
            (0, 0, 'heels stay planted'), (1, 0, 'knees flex'),
            (6, 0, 'rests arm'), (6, .2, 'opens the hand'), (6, .45, 'wrist approaches'),
            (6, .73, 'hand and gaze lower'), (6, 1, 'hand near ground'),
            (6, .76, 'starts releasing'), (6, .41, 'forearm returns'),
            (6, 0, 'forearm supported'), (1, 0, 'shifts hips onto feet'),
            (0, 0, 'straightens knees')):
        level.add(low_palm(index, amount), description)
    level.add(registered_pose('pin-listen-left', 0, PIN, 236), 'standing with weight over planted shoes')
    level.write()


def row(track, level, root, height, cel=0, *, flip=False, speak=False, start=0, end=1):
    value = {'track': track, 'level': LEVEL_PREFIX + level, 'height': height, 'anchor': 'stage',
             'root': list(root), 'first_cel': cel, 'last_cel': cel, 'motion': 'hold',
             'flip': flip, 'start': start, 'end': end}
    if speak:
        value['mouth'] = {'speaker': SPEAKERS[track]}
    return value


def paced(track, level, root, height, first, last, frames, *, flip=False, speak=False, start=0, end=1,
          motion='story'):
    value = row(track, level, root, height, first, flip=flip, speak=speak, start=start, end=end)
    value.update(last_cel=last, motion=motion, exposure_frames=frames)
    return value


def pin_left(*, cel=0, **kwargs):
    return row('pin', 'pin-listen-left', PIN, 236, cel, **kwargs)


def pin_right(*, cel=0, **kwargs):
    return row('pin', 'pin-back-talk', PIN, 236, cel, **kwargs)


def gep(*, cel=0, **kwargs):
    return row('gep', 'gep-talk', GEP, 315, cel, flip=True, **kwargs)


def cricket(*, cel=0, **kwargs):
    return row('cricket', 'cricket-talk', CRICKET, 84, cel, flip=True, **kwargs)


def loc(track, level, cel, **kwargs):
    return row(track, level, (0, 0), 720, cel, **kwargs)


def framing(number, crop, layers):
    props = [row('door', 'school-door', (0, 0), 720),
             row('sign', 'school-sign', (413, 597), 84),
             row('teacher', 'teacher', (739, 559), 193, 7)]
    # The camera photographs the same world roots through each cut's fixed aperture.
    return {'id': f'S12-C{number:02d}', 'plate': PLATE + '@' + ','.join(map(str, crop)),
            'layout': props + layers}


def compose():
    rows = [framing(15, (368, 309, 717), [
        gep(),
        pin_left(end=.52), pin_left(cel=6, start=.52, end=.553), pin_left(start=.553),
        cricket(speak=True, end=.74), cricket(cel=6, speak=True, start=.74, end=.775), cricket(speak=True, start=.775)
    ]), framing(16, (344, 335, 679), [
        gep(), cricket(end=.63), cricket(cel=6, start=.63, end=.666), cricket(start=.666),
        paced('pin', 'pin-low-palm', (0, 0), 720, 0, 3, [5, 6, 7, 9], motion='lead')
        | {'during': [0, 'lead@1']},
        row('pin', 'pin-seat-talk', PIN, 222, flip=True, speak=True)
        | {'during': ['lead@1', 'tail@0']},
        paced('pin', 'pin-low-palm', (0, 0), 720, 11, 13, [4, 4, 4], motion='tail')
        | {'during': ['tail@0', 1]}
    ]), framing(17, (391, 299, 747), [
        cricket(),
        paced('gep', 'gep-lower-gaze', (0, 0), 720, 0, 6, [4, 4, 5, 5, 5, 5, 6], speak=True),
        pin_right(speak=True, end=.3), pin_right(cel=6, speak=True, start=.3, end=.337),
        pin_right(speak=True, start=.337)
    ]), framing(18, (364, 321, 704), [
        cricket(),
        paced('gep', 'gep-lower-gaze', (0, 0), 720, 6, 15, [8, 12, 11, 12, 6, 5, 5, 5, 5, 5],
              speak=True, motion='lead'),
        pin_left(speak=True)
    ]), framing(19, (363, 291, 750), [
        gep(speak=True),
        cricket() | {'during': [0, 'lead@.45']},
        paced('cricket', 'cricket-walk', CRICKET, 84, 0, 3, [5, 6, 5, 5], flip=True, motion='lead')
        | {'during': ['lead@.45', 'lead@.85']},
        cricket(speak=True) | {'during': ['lead@.85', 1]},
        paced('pin', 'pin-low-palm', (0, 0), 720, 0, 7, [6, 5, 5, 6, 6, 6, 6, 7], motion='lead')
        | {'during': [0, 'lead@1']},
        loc('pin', 'pin-low-palm', 7) | {'during': ['lead@1', .405]},
        paced('pin', 'pin-low-palm', (0, 0), 720, 8, 13, [5, 5, 5, 5, 6, 6], start=.405, end=.56),
        pin_left(start=.56, end=.68), pin_right(start=.68)
    ])]
    return rows


def make():
    STAGE.mkdir(parents=True, exist_ok=True)
    plate = STAGE / PLATE
    if not plate.exists():
        shutil.copyfile(SCHOOL / 'S11L-school-open.png', plate)
    for name in ('school-door', 'school-sign', 'teacher', 'cricket-talk', 'cricket-walk', 'pin-back-talk',
                 'pin-listen-left', 'gep-talk'):
        clone(name)
    clone('pin-seat-talk', S07)
    adult_drawings()
    child_drawings()
    put_json(V3 / 'build/layout-rescue.json', compose())
    put_json(V3 / 'build/motion-rescue.json', {'cuts': {
        'S12-C15': {'lead_frames': 24, 'tail_frames': 12},
        'S12-C16': {'lead_frames': 36, 'tail_frames': 12},
        'S12-C17': {'lead_frames': 36, 'tail_frames': 12},
        'S12-C18': {'lead_frames': 96, 'tail_frames': 0},
        'S12-C19': {'lead_frames': 72, 'tail_frames': 24},
    }})


if __name__ == '__main__':
    make()
