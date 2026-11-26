#!/usr/bin/env python3
"""Join the finished sections through native registered cels and the measured episode clock."""

from pathlib import Path
from argparse import ArgumentParser
import runpy

from register_character import ART, BASELINE, HERE, write

ROOT = HERE.parent
OLD = BASELINE/'build'
RENDER = runpy.run_path(str(BASELINE/'art/render.py'))
PUBLISHED = Path('/workspace/shared/downloads')


def overlay(build, candidates):
    levels = {}
    plates = {}
    for source in candidates:
        for path in (source/'art').glob('*.png'):
            plates[path.name] = path
        for path in (source/'art/cels').iterdir():
            # Core keeps references to stock; an actual drawing directory always wins.
            if path.name not in levels or not path.is_symlink():
                levels[path.name] = path
    (build/'art/cels').mkdir(parents=True,exist_ok=True)
    for name,path in levels.items():
        slot = build/'art/cels'/name
        if name == 'S12K-human-acting':
            slot.mkdir(exist_ok=True)
            stock = OLD/'art/cels'/name
            files = {p.name:p for p in stock.iterdir()} | {p.name:p for p in path.iterdir()}
            for file, source in files.items():
                if not (slot/file).exists():
                    (slot/file).symlink_to(source)
            continue
        if not slot.exists():
            slot.symlink_to(path, target_is_directory=True)
        elif slot.resolve() != path.resolve():
            raise ValueError(f'Staged level differs from approved input: {name}')
    for name,path in plates.items():
        slot = build/'art'/name
        if not slot.exists():
            slot.symlink_to(path)


def main():
    cli = ArgumentParser(description=__doc__)
    cli.add_argument('--target', type=Path, default=PUBLISHED/'S12-final/S12-friend-final.mp4')
    args = cli.parse_args()
    build = ROOT/'master-build'
    opening = ROOT/'opening'
    rescue = ROOT/'rescue'
    hands = ROOT/'hands/retake'
    ending = ROOT/'ending/overlay-final'
    farewell = ROOT/'farewell/overlay'
    source = ROOT/'edition'
    overlay(build,[OLD,opening/'build',rescue,HERE/'build',hands,farewell,ending])
    inputs = {name:OLD/name for name in RENDER['LAYOUTS']}
    inputs.update({'layout-opening.json':opening/'build/layout-opening.json',
                   'layout-rescue-full.json':rescue/'layout-rescue-full.json',
                   'layout-transform.json':HERE/'build/layout-transform.json',
                   'layout-hug.json':HERE/'build/layout-hug.json',
                   'layout-hands.json':hands/'layout-hands.json',
                   'layout-ending.json':ending/'layout-ending.json'})
    for name,path in inputs.items():
        write(build/name,RENDER['read'](path))
    edit = RENDER['read'](source/'edit.json')
    farewell_edition = ROOT/'farewell/selected-edition'
    farewell_edition.mkdir(exist_ok=True)
    if not (farewell_edition/'audio').exists():
        (farewell_edition/'audio').symlink_to(source/'audio',target_is_directory=True)
    farewell_clock,_ = RENDER['ENGINE']['select'](edit,[f'S12-C{n:02}' for n in range(43,49)])
    write(farewell_edition/'edit.json',farewell_clock)
    available = [
        (opening/'S12-C01-C05-corrected.mp4', Path('/workspace/scratch/s12-v3/editor-opening/edit.json')),
        (rescue/'rescue-C06-C14.mp4',rescue/'measured-edit-6-14.json'),
        (PUBLISHED/'S12-V3-C15-C29.mp4',Path('/workspace/scratch/s12-v3/editor-post-rescue/edit.json')),
        (HERE/'family-C30-C34-retake.mp4',HERE/'family-C30-C34-edition/edit.json'),
    ]
    for media, ledger in ((ROOT/'hands/C35-C42-retake.mp4',Path('/workspace/scratch/s12-full/hand-pcm/edit.json')),
                          (ROOT/'farewell/S12-C43-C48-farewell.mp4',farewell_edition/'edit.json'),
                          (ROOT/'ending/C49-C50-integrated.mp4',Path('/workspace/scratch/s12-full/ending-door-pcm/edit.json'))):
        if media.is_file() and media.with_suffix('.json').is_file() and ledger.is_file():
            available.append((media,ledger))
    render = args.target
    RENDER['photograph'](edit,['S12-C01','S12-C50'],build,source/'audio',render,
                         source/'mix.wav', source/'subtitles.srt',prior_pictures=available)


if __name__=='__main__':
    main()
