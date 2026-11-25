"""Register the authorized real-boy ink against the last wooden drawing."""
from hashlib import sha256
from pathlib import Path
import json
from shutil import copyfile

import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy.ndimage import label

HERE = Path(__file__).resolve().parent
SOURCE = HERE / 'source'
SIZE = (453, 755)
GROUND = (223, 665)
REFERENCE_HEIGHT = 583
STAGE_ROOT = (561, 643)
ART = HERE.parents[1] / 'build' / 'art'

# The wooden and generated drawings are nearly identical at the scalp and
# floor line. Register the shoes six source pixels left under the same hips.
REGISTRATION = {
    'stage': [223, 665],
    'left_heel': [151, 651], 'left_toe': [220, 653],
    'right_heel': [236, 642], 'right_toe': [344, 651],
    'near_ankle': [168, 587], 'far_ankle': [261, 585],
    'near_knee': [181, 540], 'far_knee': [260, 541],
    'near_hip': [194, 471], 'far_hip': [258, 470],
    'neck': [230, 297], 'hat': [235, 143], 'bag': [165, 365],
    'near_shoulder': [206, 331], 'near_cuff': [181, 356],
    'near_elbow': [153, 397], 'near_wrist': [143, 423], 'near_palm': [137, 438],
    'far_shoulder': [294, 338], 'far_cuff': [311, 360],
    'far_elbow': [335, 389], 'far_wrist': [370, 424], 'far_palm': [386, 438],
    'near_eye': [270, 240], 'far_eye': [312, 230], 'mouth': [300, 267],
}


def clean(img):
    return img.convert('RGBA').point([*range(256)] * 3 + [n if n >= 8 else 0 for n in range(256)])


def normalize(path, bounds=None):
    with Image.open(path) as image:
        figure = clean(image)
    crop = figure.crop(bounds or figure.getchannel('A').getbbox())
    width = round(crop.width * REFERENCE_HEIGHT / crop.height)
    canvas = Image.new('RGBA', SIZE)
    canvas.alpha_composite(crop.resize((width, REFERENCE_HEIGHT), Image.Resampling.LANCZOS), (86, 86))
    mesh = []
    for top, bottom, start, stop in [(0, 480, 0, 0), (480, 580, 0, 6), (580, 755, 6, 6)]:
        mesh.append(((0, top, SIZE[0], bottom),
                     (start, top, stop, bottom, SIZE[0] + stop, bottom, SIZE[0] + start, top)))
    return clean(canvas.transform(SIZE, Image.Transform.MESH, mesh, Image.Resampling.BICUBIC))


def replace_patch(base, incoming, polygons, feather=2.0):
    mask = Image.new('L', base.size)
    brush = ImageDraw.Draw(mask)
    for points in polygons:
        brush.polygon(points, fill=255)
    return Image.composite(incoming, base, mask.filter(ImageFilter.GaussianBlur(feather)))


def normalize_back(path):
    with Image.open(path) as raw:
        figure = clean(raw)
    alpha = np.array(figure.getchannel('A'))
    islands, _ = label(alpha >= 8, structure=np.ones((3, 3), dtype=np.uint8))
    counts = np.bincount(islands.ravel())
    counts[0] = 0
    figure.putalpha(Image.fromarray(np.where(islands == counts.argmax(), alpha, 0)))
    crop = figure.crop(figure.getchannel('A').getbbox())
    width = round(crop.width * REFERENCE_HEIGHT / crop.height)
    canvas = Image.new('RGBA', SIZE)
    canvas.alpha_composite(crop.resize((width, REFERENCE_HEIGHT), Image.Resampling.LANCZOS), (86,86))
    return clean(canvas)


def register_source_cels(meta):
    level = ART / 'cels' / 'S12HN-character'
    level.mkdir(parents=True, exist_ok=True)

    def expose(name, image, anchors, mark_mouth):
        target = level / f'{name}.png'
        copyfile(SOURCE / image, target)
        row = {'file':target.relative_to(ART).as_posix(), 'size':list(SIZE),
               'anchors':anchors, 'sole':list(GROUND),
               'sha256':sha256(target.read_bytes()).hexdigest()}
        if mark_mouth:
            row['mouth_box'] = meta['mouth_box']
        return row

    poses = [expose('00', meta['closed'], meta['anchors'], False)]
    if 'open' in meta:
        awake = expose('01', meta['open'], meta['anchors'], True)
        if set(meta['visemes']) == {'small','wide'}:
            awake['viseme_cels'] = {name:expose('01-'+name,take['file'],meta['anchors'],True)
                                    for name,take in meta['visemes'].items()}
        poses.append(awake)
    if 'back_right' in meta:
        rear = meta['back_right']
        poses.append(expose('02', rear['file'], {'stage':list(GROUND), **rear['anchors']}, False))
    for index, pose in enumerate(poses):
        pose['index'] = index
    (level / 'registration.json').write_text(json.dumps({'reference_height':REFERENCE_HEIGHT,
        'character':meta['character'],'poses':poses}, ensure_ascii=False, indent=2) + '\n')


def write_model():
    raw = SOURCE / 'imagegen-closed.png'
    model = normalize(raw)
    processed = SOURCE / 'closed.png'
    model.save(processed)
    meta = {'character': 'CHAR_YOONSU_HUMAN', 'angle': 'three-quarter right', 'size': list(SIZE),
            'reference_height': REFERENCE_HEIGHT, 'stage': {'root': list(STAGE_ROOT), 'height': 236},
            'anchors': REGISTRATION, 'mouth_box': [281, 248, 314, 279],
            'alpha_bbox': list(model.getchannel('A').getbbox()),
            'closed': processed.name, 'closed_sha256': sha256(processed.read_bytes()).hexdigest(),
            'source': raw.name, 'source_sha256': sha256(raw.read_bytes()).hexdigest()}
    eye_source = SOURCE / 'imagegen-open.png'
    if eye_source.exists():
        open_pose = normalize(eye_source, (164, 178, 881, 1436))
        eyes = [[(250, 209), (283, 208), (300, 223), (290, 246), (255, 253), (248, 243)],
                [(298, 207), (322, 204), (327, 224), (323, 241), (302, 240)]]
        opening = replace_patch(model, open_pose, eyes, 1.7)
        registered = SOURCE / 'open.png'
        opening.save(registered)
        meta.update(open=registered.name, open_sha256=sha256(registered.read_bytes()).hexdigest(),
                    eye_source=eye_source.name, eye_source_sha256=sha256(eye_source.read_bytes()).hexdigest())
        mouths = {}
        mouth_polygon = [[(281,252), (292,248), (310,247), (320,256), (316,278),
                           (301,281), (282,274)]]
        for phoneme, variant in (('ah','wide'), ('oo','small')):
            source = SOURCE / f'imagegen-{phoneme}.png'
            if source.exists():
                replacement = normalize(source, (164, 178, 881, 1436))
                variant_sprite = replace_patch(opening, replacement, mouth_polygon, 1.8)
                path = SOURCE / f'speech-{variant}.png'
                variant_sprite.save(path)
                mouths[variant] = {'file':path.name,'sha256':sha256(path.read_bytes()).hexdigest(),
                                   'source':source.name,'source_sha256':sha256(source.read_bytes()).hexdigest()}
        meta['visemes'] = mouths
    rear_source = SOURCE / 'imagegen-back.png'
    if rear_source.exists():
        back = SOURCE / 'back-right.png'
        normalize_back(rear_source).save(back)
        meta['back_right'] = {'file':back.name,'sha256':sha256(back.read_bytes()).hexdigest(),
            'source':rear_source.name,'source_sha256':sha256(rear_source.read_bytes()).hexdigest(),
            'angle':'three-quarter rear toward viewer right', 'stage':list(GROUND),
            'anchors':{'planted_left':[166,665],'left_heel':[120,648],'left_toe':[205,655],
            'right_heel':[253,631],'right_toe':[337,599],'near_ankle':[150,589],'far_ankle':[270,581],
            'near_knee':[178,545],'far_knee':[251,534],'near_hip':[202,496],'far_hip':[243,485],
            'neck':[227,287],'bag':[184,399],'near_shoulder':[266,324],'far_shoulder':[164,335],
            'near_wrist':[321,446],'far_wrist':[113,456],'near_palm':[328,462],'far_palm':[110,475]}}
    (SOURCE / 'registration.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n')
    register_source_cels(meta)


if __name__ == '__main__':
    write_model()
