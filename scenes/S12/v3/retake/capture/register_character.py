#!/usr/bin/env python3
"""Register the new school-costume artwork without moving the two planted soles."""

from hashlib import file_digest
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy.ndimage import binary_dilation, label

HERE = Path(__file__).resolve().parent
BASELINE = Path('/workspace/yoonsu-pinocchio-3d/scenes/S12/v3')
ORIGINAL = BASELINE / 'art/human/source'
SOURCE = HERE / 'human-source'
ART = HERE / 'build/art'
SIZE = (453, 755)
GROUND = (223, 665)
HEIGHT = 583


def digest(path):
    with path.open('rb') as handle:
        return file_digest(handle, 'sha256').hexdigest()


def load(path):
    with Image.open(path) as image:
        return image.convert('RGBA')


def write(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def trim(image):
    """Retain the connected cel and its narrow antialiased border."""
    rgba = np.array(image.convert('RGBA'))
    alpha = rgba[:, :, 3]
    islands, _ = label(alpha >= 144, structure=np.ones((3, 3), dtype=np.uint8))
    counts = np.bincount(islands.ravel())
    counts[0] = 0
    connected = binary_dilation(islands == counts.argmax(), iterations=2)
    rgba[~connected | (alpha < 12)] = 0
    output = Image.fromarray(rgba)
    return output.crop(output.getchannel('A').getbbox())


def shoe_center(figure):
    alpha = np.asarray(figure.getchannel('A'))
    y, x = np.nonzero(alpha >= 185)
    floor = int(y.max())
    toes = x[y >= floor - max(10, round(figure.height*.075))]
    return float(np.mean(np.quantile(toes, [.06, .94]))), floor


def fitted(figure, target_center=241, target_floor=665, target_height=HEIGHT):
    cropped = trim(figure)
    ratio = target_height / cropped.height
    cropped = cropped.resize((round(cropped.width*ratio), target_height), Image.Resampling.LANCZOS)
    x, y = shoe_center(cropped)
    canvas = Image.new('RGBA', SIZE)
    canvas.alpha_composite(cropped, (round(target_center-x), target_floor-y))
    return canvas


def extract_row(state):
    paths = sorted((HERE / state / 'frames' / state).glob('frame-*.png'),
                   key=lambda path: int(path.stem.rsplit('-', 1)[-1]))
    return [fitted(load(path)) for path in paths]


def restore_lids(opened, closed):
    """Register the painted closed eyelids on the final neutral stance."""
    alternate = closed.transform(SIZE, Image.Transform.AFFINE,
                                 (1, 0, -4, 0, 1, 7), Image.Resampling.BICUBIC)
    mask = Image.new('L', SIZE)
    brush = ImageDraw.Draw(mask)
    brush.ellipse((251, 211, 287, 237), fill=255)
    brush.ellipse((290, 206, 315, 228), fill=255)
    return Image.composite(alternate, opened, mask.filter(ImageFilter.GaussianBlur(3)))


def register():
    SOURCE.mkdir(exist_ok=True)
    metadata = json.loads((ORIGINAL/'registration.json').read_text())
    source = HERE/'identity-anchor.png'
    opened = fitted(load(source))
    closed = restore_lids(opened, extract_row('revelation')[0])
    plate = {'closed.png': closed, 'open.png': opened, 'back-right.png': extract_row('direction')[3]}
    metadata['anchors'].update(near_eye=[270, 220], far_eye=[307, 214], mouth=[297, 258])
    metadata.update(source='identity-anchor.png', source_sha256=digest(source), mouth_box=[279, 245, 315, 273],
                    character='CHAR_YOONSU_HUMAN', identity='Starlight Album; see album-art-provenance.json')
    for name, image in plate.items():
        image.save(SOURCE / name)
    metadata['closed_sha256'] = digest(SOURCE/'closed.png')
    metadata['open_sha256'] = digest(SOURCE/'open.png')
    metadata['back_right'].update(sha256=digest(SOURCE/'back-right.png'))
    metadata['visemes'] = {}
    metadata['alpha_bbox'] = list(opened.getchannel('A').getbbox())
    write(SOURCE/'registration.json', metadata)
    return metadata, closed, opened


if __name__ == '__main__':
    register()
