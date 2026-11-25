#!/usr/bin/env python3
"""Register the approved teacher's backward yield at the C49 threshold."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import runpy
from tempfile import TemporaryDirectory

from PIL import Image

V3 = Path(__file__).resolve().parents[2]
S11 = V3.parents[1] / 'S11/v2'
SOURCE = S11 / 'build/art'
ART = V3 / 'build/art'
LEVEL = 'S12RL-teacher-yield'
ENTRY = (739, 559)
HEIGHT = 193
FPS = 24
FRONT = (752, 555)
REAR = (710, 565)
PLATE = 'S11L-school-open.png'
DOOR = 'S11L-school-door'
# Reverse the existing forward foot poses. The teacher looks toward the
# passage while she moves back to the front edge of the stone threshold.
POSES = (
    (7, (110, 402), 'front', 13, 'looks at the passage'),
    (0, (110, 398), 'front', 8, 'sets weight on the front foot'),
    (4, (111, 401), 'front', 7, 'left boot withdraws'),
    (3, (125, 397), 'front', 9, 'rear boot reaches the sill'),
    (5, (60, 405), 'rear', 6, 'rear sole takes the weight'),
    (6, (61, 404), 'rear', 53, 'leaves the passage and looks on'),
)


def write_json(path, value):
    pending = path.with_suffix('.json.pending')
    pending.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    pending.replace(path)


def register_teacher():
    registry = SOURCE / 'cels/S11L-teacher/registration.json'
    approved = json.loads(registry.read_text(encoding='utf-8'))
    scale = HEIGHT / approved['reference_height']
    dest = ART / 'cels' / LEVEL
    dest.mkdir(parents=True, exist_ok=True)
    drawings, cues, layers = [], [], []
    first = 0
    for index, (old_index, foot, side, length, intent) in enumerate(POSES):
        pose = approved['poses'][old_index]
        src = SOURCE / pose['file']
        with Image.open(src) as sprite:
            if sprite.mode != 'RGBA' or sprite.getpixel(foot)[3] < 160:
                raise ValueError(f'Teacher {old_index} support point must be inside the planted shoe')
        name = dest / f'{index:02d}.png'
        if not name.is_file():
            name.hardlink_to(src)
        root = FRONT if side == 'front' else REAR
        anchor = 'stage' if index == 0 else 'support'
        if index == 0:
            actual = tuple(e - round(s * scale) + round(f * scale)
                           for e, s, f in zip(ENTRY, pose['anchors']['stage'], foot))
            if actual != FRONT:
                raise ValueError('The first support point must preserve the inherited teacher placement')
            root = ENTRY
        cues.append({'pose': index, 'source_pose': old_index, 'phase': intent, 'range': [first, first + length],
                     'floor_pin': list(FRONT if side == 'front' else REAR), 'support_foot': side})
        drawings.append(pose | {'index': index, 'file': str(name.relative_to(ART)),
                                'anchors': pose['anchors'] | {'support': list(foot)}})
        last = first + length
        layers.append({'track': 'teacher', 'level': LEVEL, 'root': list(root), 'height': HEIGHT, 'anchor': anchor,
                       'first_cel': index, 'last_cel': index, 'motion': 'hold',
                       'during': [f'lead@{first/96:.12f}', f'lead@{last/96:.12f}' if last < 96 else 1]})
        first = last
    write_json(dest/'registration.json', {'reference_height': approved['reference_height'], 'poses': drawings,
                                         'source_registration': 'S11/v2/build/art/cels/S11L-teacher/registration.json'})
    return layers, cues


def package():
    layers, cues = register_teacher()
    door = {'track': 'door', 'level': DOOR, 'root': [0, 0], 'height': 720, 'anchor': 'stage',
            'first_cel': 0, 'last_cel': 0, 'motion': 'hold', 'start': 0, 'end': 1}
    document = {'id': 'S12-C49', 'scope': 'SUPPORT_ONLY_HUMAN_AND_FULL_ENTRY_UNVERIFIED',
                'fps': FPS, 'lead_frames': 96, 'plate': PLATE, 'door': door, 'teacher_layers': layers,
                'floor_pins': cues, 'visible_door_slit': {'approx_stage_x': [760, 779], 'widest_approved_pose': 0}}
    write_json(V3/'build/teacher-support.json', document)
    return document


def photograph(document, folder):
    folder.mkdir(parents=True, exist_ok=True)
    camera = runpy.run_path(str(S11/'art/render.py'))
    seconds = document['lead_frames'] / FPS
    window = {'start': 0, 'end': seconds}
    cut = {'id': document['id'], 'first': 0, 'end': document['lead_frames'], 'audio': [],
           'action_windows': {'lead': window, 'story': window, 'tail': {'start': seconds, 'end': seconds}, 'between': []}}
    edit = {'fps': FPS, 'frames': document['lead_frames'], 'duration': seconds, 'cuts': [cut], 'events': []}
    layers = [camera['timed_layer'](cut, row) for row in document['teacher_layers']]
    layout = [{'id': cut['id'], 'plate': document['plate'] + '@526,280,702',
               'layout': [document['door'], *layers]}]
    with TemporaryDirectory(dir=folder) as tmp:
        registered = Path(tmp)
        engine = camera['camera_engine']()
        report = engine['render_shots'](edit, layout, ART, V3/'build/voices', registered, silent=True)
        camera['CAMERA']['encode'](report, edit, registered, folder/'S12-C49-teacher-only.mp4')
    write_json(folder/'C49-teacher-camera.json', report)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--proof-dir', type=Path)
    args = parser.parse_args()
    document = package()
    if args.proof_dir:
        photograph(document, args.proof_dir)


if __name__ == '__main__':
    main()
