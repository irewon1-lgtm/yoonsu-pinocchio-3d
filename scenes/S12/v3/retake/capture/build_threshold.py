#!/usr/bin/env python3
"""Register the two final shots' Album-based character art at the school set."""
from argparse import ArgumentParser
from copy import deepcopy
from hashlib import file_digest
import json
from math import ceil, floor, hypot
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter


HERE = Path(__file__).resolve().parent
V3 = Path('/workspace/yoonsu-pinocchio-3d/scenes/S12/v3')
BASE = V3 / 'build'
FAREWELL = HERE.parent / 'farewell/overlay'
READY = FAREWELL / 'art/cels/S12K-human-acting/39.png'
REFERENCE = HERE.parent / 'identity/yoonsu-alpha'
STAGE = (1280, 720)
SILL = (750, 559)
PORTAL = ((692, 311), (780, 309), (781, 550), (689, 554))
START = 12
INTERIOR_START = 123
EXTERIOR_END = 168
ARRIVE = 123
ARRIVE_END = 137
HANDOFF = 252
EXIT_END = 37
HOLD_CAMERA = [405, 176, 869]

# Pelvis and soles of the eight keyed drawings, in extracted cell pixels.
ANCHORS = (
    ((155, 309), (110, 447), (201, 443)),
    ((149, 308), (95, 446), (215, 434)),
    ((161, 312), (95, 448), (197, 446)),
    ((168, 302), (130, 417), (177, 447)),
    ((149, 309), (103, 449), (206, 420)),
    ((157, 302), (102, 447), (192, 439)),
    ((159, 301), (132, 448), (196, 399)),
    ((159, 296), (128, 450), (228, 364)),
    ((223, 460), (165, 668), (285, 666)),
)

# Frames are relative to the C49 opening, with no edit or dialogue changes.
# Each shoe follows its own footprint through the approaches and over the sill.
# The final row continues into C50 on this same clock.
# Frame, drawing, projected height, pelvis, foot A, foot B, grounded feet.
KEYS = (
    (12, 8, 236, (561, 560), (538, 644), (586, 643), 'AB'),
    (18, 0, 235, (569, 561), (538, 644), (586, 643), 'B'),
    (26, 2, 233, (580, 558), (561, 618), (586, 643), 'B'),
    (34, 1, 229, (590, 555), (611, 625), (586, 643), 'B'),
    (40, 2, 227, (600, 553), (613, 625), (586, 643), 'A'),
    (47, 2, 226, (609, 553), (613, 625), (586, 627), 'A'),
    (56, 3, 223, (615, 549), (613, 625), (601, 602), 'A'),
    (64, 4, 219, (625, 542), (613, 625), (650, 603), 'A'),
    (70, 5, 215, (637, 534), (613, 625), (653, 603), 'B'),
    (77, 4, 213, (646, 531), (627, 607), (653, 603), 'B'),
    (86, 3, 210, (653, 528), (642, 580), (653, 603), 'B'),
    (95, 4, 205, (668, 519), (686, 581), (653, 603), 'B'),
    (101, 5, 201, (681, 515), (689, 581), (653, 603), 'A'),
    (108, 3, 198, (690, 511), (689, 581), (676, 558), 'A'),
    (115, 7, 193, (703, 507), (689, 581), (730, 545), 'A'),
    (119, 7, 190, (715, 501), (689, 581), (744, 548), 'A'),
    (123, 4, 185, (722, 500), (689, 581), SILL, 'AB'),
    (130, 5, 181, (731, 497), (689, 581), SILL, 'B'),
    (137, 5, 178, (737, 495), (701, 571), SILL, 'B'),
    (145, 3, 174, (741, 490), (721, 545), SILL, 'B'),
    (153, 6, 169, (747, 490), (760, 538), SILL, 'B'),
    (161, 5, 164, (751, 490), (761, 544), SILL, 'A'),
    (172, 3, 159, (754, 488), (761, 544), (741, 536), 'A'),
    (187, 6, 151, (756, 487), (761, 544), (767, 521), 'A'),
    (199, 5, 148, (761, 486), (761, 544), (772, 535), 'B'),
    (213, 3, 145, (764, 482), (748, 522), (772, 535), 'B'),
    (227, 3, 141, (764, 483), (757, 522), (772, 535), 'B'),
    (240, 5, 138, (767, 481), (755, 535), (772, 535), 'AB'),
    (252, 5, 136, (769, 481), (755, 535), (772, 535), 'AB'),
    (260, 3, 133, (773, 478), (769, 514), (772, 535), 'B'),
    (270, 6, 128, (782, 475), (795, 519), (772, 535), 'B'),
    (278, 5, 125, (792, 474), (798, 527), (772, 535), 'A'),
    (289, 7, 120, (817, 472), (798, 527), (827, 507), 'A'),
)


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def write(path, data):
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def digest(path):
    with path.open('rb') as file:
        return file_digest(file, 'sha256').hexdigest()


def smooth(amount):
    amount = max(0.0, min(1.0, amount))
    return amount * amount * (3.0 - 2.0 * amount)


def lerp(source, target, amount):
    return tuple(a + amount * (b - a) for a, b in zip(source, target, strict=True))


def state(frame):
    for start, stop in zip(KEYS[:-1], KEYS[1:], strict=True):
        if start[0] <= frame < stop[0]:
            break
    else:
        _, pose, height, pelvis, a, b, supports = KEYS[-1]
        return pose, height, pelvis, a, b, supports
    f0, pose0, height0, hip0, a0, b0, support0 = start
    f1, _, height1, hip1, a1, b1, support1 = stop
    t = (frame - f0) / (f1 - f0)
    pose = pose0
    height = height0 + t * (height1 - height0)
    hip = lerp(hip0, hip1, t)
    a, b = lerp(a0, a1, smooth(t)), lerp(b0, b1, smooth(t))
    grounded = ''.join(foot for foot, first, last in (('A', a0, a1), ('B', b0, b1))
                       if foot in support0 and (first == last or t == 0))
    return pose, height, hip, a, b, grounded


def portal_mask():
    result = Image.new('L', STAGE)
    ImageDraw.Draw(result).polygon(PORTAL, fill=255)
    return result


def project(painting, pose, height, hip, feet):
    """Reposition the knees and boots under a rigid shirt, satchel and head."""
    source_hip, *source_feet = ANCHORS[pose]
    scale = height / (583 if pose == 8 else 420)
    left, right = sorted(feet)
    bound_x = floor(hip[0] - 111)
    bound_y = floor(hip[1] - 0.78 * height - 5)
    right_x = ceil(hip[0] + 105)
    bottom_y = ceil(max(a[1] for a in feet) + 20)
    width, height_px = right_x - bound_x, bottom_y - bound_y
    target_feet = (left, right)
    natural_feet = tuple(((x - source_hip[0]) * scale + hip[0],
                          (y - source_hip[1]) * scale + hip[1]) for x, y in source_feet)
    shifts = tuple((a[0] - b[0], a[1] - b[1])
                   for a, b in zip(target_feet, natural_feet, strict=True))
    axis = (right[0] - left[0], right[1] - left[1])
    distance = max(1.0, hypot(*axis))

    def inverse(x, y):
        proj = ((x - left[0]) * axis[0] + (y - left[1]) * axis[1]) / distance**2
        weight = smooth((proj - 0.18) / 0.64)
        weight_x, weight_y = lerp(shifts[0], shifts[1], weight)
        sole = left[1] + weight * axis[1]
        leg = smooth((y - hip[1] - 4) / max(8, sole - hip[1] - 16))
        return ((x - hip[0] - weight_x * leg) / scale + source_hip[0],
                (y - hip[1] - weight_y * leg) / scale + source_hip[1])

    xs = sorted(set((0, width, *range(8, width, 8),
                     *(round(foot[0]) - bound_x for foot in feet))))
    ys = sorted(set((0, height_px, *range(8, height_px, 8),
                     *(round(foot[1]) - bound_y for foot in feet))))
    grid = [[inverse(x + bound_x, y + bound_y) for x in xs] for y in ys]
    mesh = []
    for j, (y0, y1) in enumerate(zip(ys[:-1], ys[1:], strict=True)):
        for i, (x0, x1) in enumerate(zip(xs[:-1], xs[1:], strict=True)):
            source = (*grid[j][i], *grid[j + 1][i], *grid[j + 1][i + 1], *grid[j][i + 1])
            mesh.append(((x0, y0, x1, y1), source))
    drawing = painting.transform((width, height_px), Image.Transform.MESH, mesh,
                                 resample=Image.Resampling.BICUBIC)
    canvas = Image.new('RGBA', STAGE)
    canvas.alpha_composite(drawing, (bound_x, bound_y))
    return canvas


def multiply_alpha(drawing, mask):
    drawing.putalpha(ImageChops.multiply(drawing.getchannel('A'), mask))
    return drawing


def depth(drawing, frame, portal):
    if frame < INTERIOR_START:
        return drawing, None
    amount = smooth((frame - INTERIOR_START) / (EXTERIOR_END - INTERIOR_START))
    light = 1 - 0.43 * amount - 0.11 * smooth((frame - EXTERIOR_END) / 55)
    shaded = ImageEnhance.Brightness(drawing).enhance(light)
    if frame >= EXTERIOR_END:
        return None, multiply_alpha(shaded, portal)
    # Toe and shoulder enter at different times. The body is split at the
    # opening plane so the jamb and teacher occlude only the interior portion.
    top = 814 - 177 * amount
    bottom = 750 - 100 * amount
    lower_edge = 555 + 8 * smooth((frame - 151) / 14)
    ahead = Image.new('L', STAGE)
    ImageDraw.Draw(ahead).polygon(((round(top), 300), (1280, 300),
                                   (1280, round(lower_edge)), (round(bottom), round(lower_edge))), fill=255)
    outside = multiply_alpha(drawing, ImageChops.invert(ahead))
    inside = multiply_alpha(multiply_alpha(shaded, ahead), portal)
    return outside, inside


def source_shadow(height, points, grounded, frame, portal):
    canvas = Image.new('RGBA', STAGE)
    for identity, (x, y) in zip('AB', points, strict=True):
        if identity not in grounded:
            continue
        width = height * 0.069
        draw = ImageDraw.Draw(canvas)
        draw.ellipse((x - width, y - 2, x + width, y + 4), fill=(56, 27, 15, 108))
    canvas = canvas.filter(ImageFilter.GaussianBlur(2.1))
    return multiply_alpha(canvas, portal) if frame >= EXTERIOR_END else canvas


class Registration:
    def __init__(self, art, name, source):
        self.art = art
        self.name = name
        self.folder = art / 'cels' / name
        self.folder.mkdir(parents=True, exist_ok=True)
        self.source = source
        self.poses = []

    def add(self, canvas, label):
        index = len(self.poses)
        box = canvas.getchannel('A').getbbox() if canvas is not None else None
        if box:
            x0, y0, x1, y1 = box
            image = canvas.crop((x0 - 2, y0 - 2, x1 + 2, y1 + 2))
            anchor = [2 - x0, 2 - y0]
        else:
            image = Image.new('RGBA', (4, 4))
            anchor = [0, 0]
        path = self.folder / f'{index:03}.png'
        image.save(path, compress_level=4)
        self.poses.append({'index': index, 'file': str(path.relative_to(self.art)),
                           'anchors': {'stage': anchor}, 'size': list(image.size),
                           'sha256': digest(path), 'action': label})

    def close(self):
        write(self.folder / 'registration.json', {'reference_height': 720, 'poses': self.poses,
              'source': self.source, 'opaque_field': True})


def register(output, anticipation, layout_file):
    pose_images = [Image.open(HERE / 'yoonsu-shapes' / f'cell-{i}.png').convert('RGBA') for i in range(8)]
    pose_images.append(Image.open(anticipation).convert('RGBA'))
    source = {'gait_drawing': digest(HERE / 'yoonsu-school-gait-sheet.png'),
              'anticipation_drawing': digest(anticipation),
              'starlight_album_source': {file.name: digest(file) for file in (
                  REFERENCE / 'Y06_profile_right.png', REFERENCE / 'Y03_back.png',
                  REFERENCE / 'Y10_walk_pose.png')}}
    old_art = BASE / 'art'
    art = output / 'art'
    art.mkdir(exist_ok=True)
    cels = art / 'cels'
    cels.mkdir(exist_ok=True)
    for path in old_art.iterdir():
        if path.name != 'cels' and not (art / path.name).exists():
            (art / path.name).symlink_to(path)
    for path in (old_art / 'cels').iterdir():
        target = cels / path.name
        override = layout_file.parent / 'art' / 'cels' / path.name
        if override.exists() and override.resolve() != path.resolve():
            if target.is_symlink():
                target.unlink()
            target.mkdir(exist_ok=True)
            entries = {entry.name: entry for entry in path.iterdir()}
            entries.update({entry.name: entry for entry in override.iterdir()})
            for filename, source_path in entries.items():
                dest = target / filename
                if dest.is_symlink() and dest.resolve() != source_path.resolve():
                    dest.unlink()
                if not dest.exists():
                    dest.symlink_to(source_path)
        elif not target.exists():
            target.symlink_to(path)
    exterior = Registration(art, 'S12END-yoon-exterior', source)
    interior = Registration(art, 'S12END-yoon-interior', source)
    shadow = Registration(art, 'S12END-yoon-contact', source)
    registration = []
    portal = portal_mask()
    for frame in range(START, HANDOFF + EXIT_END + 1):
        pose, height, hip, a, b, grounded = state(frame)
        canvas = project(pose_images[pose], pose, height, hip, (a, b))
        alpha = canvas.getchannel('A')
        contact_pixels = {}
        for identity, (x, y) in zip('AB', (a, b), strict=True):
            px, py = round(x), round(y)
            contact_pixels[identity] = [alpha.crop((px - 5, j, px + 6, j + 1)).getextrema()[1]
                                        for j in range(py - 4, py + 6)]
        outside, inside = depth(canvas, frame, portal)
        note = f"walk frame {frame}, source pose {pose}, contacts {grounded}"
        exterior.add(outside, note)
        interior.add(inside, note)
        shadow.add(source_shadow(height, (a, b), grounded, frame, portal), note)
        registration.append({'frame': frame, 'cel': frame - START, 'source_pose': pose,
                             'pelvis': hip, 'height': round(height, 3), 'A': a, 'B': b,
                             'contact': grounded, 'sole_alpha': contact_pixels,
                             'exterior_box': outside.getbbox() if outside else None,
                             'interior_box': inside.getbbox() if inside else None})
    for slate in (exterior, interior, shadow):
        slate.close()
    write(output / 'threshold-geometry.json', {'stage': STAGE, 'portal': PORTAL, 'sill': SILL,
          'contact_frames': [ARRIVE, ARRIVE_END], 'handoff': HANDOFF, 'source': source,
          'exterior_end': EXTERIOR_END, 'frames': registration})


def sequence(level, track, first, last, position):
    exposure = [1] * (last - first + 1)
    return {'track': track, 'level': level, 'root': [0, 0], 'height': 720, 'anchor': 'stage',
            'first_cel': first - START, 'last_cel': last - START,
            'motion': 'story', 'exposure_frames': exposure, 'during': position}


def finish_layout(output, edit_file, layout_file):
    rows = read(layout_file)
    cuts = {cut['id']: cut for cut in read(edit_file)['cuts']}
    by_id = {shot['id']: shot for shot in rows}
    c48, c49, c50 = (by_id[f'S12-C{i}'] for i in (48, 49, 50))
    length49 = cuts[c49['id']]['end'] - cuts[c49['id']]['first']
    length50 = cuts[c50['id']]['end'] - cuts[c50['id']]['first']
    if length49 <= HANDOFF or length50 <= 84:
        raise ValueError('Measured edit does not fit the registered entrance and pull away')
    remaining = [layer for layer in c49['layout'] if layer['track'] not in ('child', 'teacher')]
    teacher = [layer for layer in c49['layout'] if layer['track'] == 'teacher']
    child = deepcopy([layer for layer in c48['layout'] if layer['track'] == 'child'][-1])
    if child['motion'] != 'hold':
        raise ValueError('C48 closing cel must be held through the opening of C49')
    for field in ('span', 'start', 'end'):
        child.pop(field, None)
    child['during'] = [0, START / length49]
    window49 = [START / length49, 1]
    c49['layout'] = [*remaining, sequence('S12END-yoon-contact', 'child-contact', START, HANDOFF, window49),
                     sequence('S12END-yoon-interior', 'child-interior', START, HANDOFF, window49),
                     *teacher, child,
                     sequence('S12END-yoon-exterior', 'child-exterior', START, HANDOFF, window49)]
    if c48.get('camera_cues'):
        first_camera = c48['camera_cues'][-1]['crop']
    elif '@' in c48['plate']:
        first_camera = [int(v) for v in c48['plate'].split('@')[1].split(',')]
    else:
        first_camera = [0, 0, 1280]
    c49['camera_cues'] = [
        {'frame': 0, 'crop': first_camera},
        {'frame': 13, 'crop': first_camera},
        {'frame': 63, 'crop': [330, 145, 940], 'interpolate': True},
        {'frame': 111, 'crop': [441, 190, 775], 'interpolate': True},
        {'frame': 170, 'crop': [441, 190, 775]},
        {'frame': 222, 'crop': HOLD_CAMERA, 'interpolate': True},
    ]
    window50 = [0, (EXIT_END + 1) / length50]
    for idx, layer in enumerate(c50['layout']):
        if layer['track'] == 'child-inside':
            c50['layout'][idx:idx + 1] = [
                sequence('S12END-yoon-contact', 'child-contact', HANDOFF, HANDOFF + EXIT_END, window50),
                sequence('S12END-yoon-interior', 'child-interior', HANDOFF, HANDOFF + EXIT_END, window50),
            ]
            break
    c50['camera_cues'][0]['crop'] = HOLD_CAMERA
    write(output / 'layout-ending.json', rows)


def main():
    ap = ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, default=HERE / 'overlay')
    ap.add_argument('--edit', type=Path, default=Path('/workspace/scratch/s12-full/final-edit/edit.json'))
    ap.add_argument('--layout', type=Path, default=FAREWELL / 'layout-ending.json')
    ap.add_argument('--anticipation', type=Path, default=READY)
    ap.add_argument('--layout-only', action='store_true')
    args = ap.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    if not args.layout_only:
        register(args.output, args.anticipation, args.layout)
    finish_layout(args.output, args.edit, args.layout)


if __name__ == '__main__':
    main()
