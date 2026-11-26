#!/usr/bin/env python3
"""Photograph a contiguous scene range using the canonical story and its exact mix."""

from argparse import ArgumentParser
from pathlib import Path
import runpy
import wave

from register_character import BASELINE, HERE, write

ORIGINAL = Path('/workspace/scratch/s12-full/final-edit')


def main():
    cli = ArgumentParser(description=__doc__)
    cli.add_argument('first', type=int)
    cli.add_argument('last', type=int)
    cli.add_argument('--build', type=Path, default=HERE/'build')
    cli.add_argument('--out', type=Path, required=True)
    args = cli.parse_args()
    render = runpy.run_path(str(BASELINE/'art/render.py'))
    cuts = [f'S12-C{n:02}' for n in range(args.first,args.last+1)]
    prior = render['read'](ORIGINAL/'edit.json')
    edit = render['ENGINE']['select'](prior,cuts)[0]
    args.out.parent.mkdir(parents=True,exist_ok=True)
    edition = args.out.parent / f'{args.out.stem}-edition'
    edition.mkdir(exist_ok=True)
    write(edition/'edit.json',edit)
    if not (edition/'audio').is_symlink():
        (edition/'audio').symlink_to(ORIGINAL/'audio',target_is_directory=True)
    with wave.open(str(ORIGINAL/'mix.wav'),'rb') as source, wave.open(str(edition/'mix.wav'),'wb') as mix:
        if source.getframerate() != 24_000:
            raise ValueError('The existing edit must use 1,000 samples per photographed frame')
        mix.setparams(source.getparams())
        source.setpos(prior['cuts'][args.first-1]['first']*1000)
        mix.writeframes(source.readframes(edit['frames']*1000))
    scenes = BASELINE.parents[1]
    subtitles = runpy.run_path(str(scenes/'S03/production/editor/assemble.py'))['write_subtitles']
    subtitles(edition/'subtitles.srt',edit)
    render['photograph'](edit,[cuts[0],cuts[-1]],args.build,edition/'audio',args.out,
                         edition/'mix.wav',edition/'subtitles.srt',segmented=True)


if __name__=='__main__':
    main()
