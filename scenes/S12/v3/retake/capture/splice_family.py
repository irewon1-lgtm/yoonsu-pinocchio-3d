#!/usr/bin/env python3
"""Replace only the approach shot in the photographed family sequence."""

from pathlib import Path
import runpy
import subprocess
from tempfile import TemporaryDirectory

from register_character import BASELINE, HERE, digest, write


def main():
    render = runpy.run_path(str(BASELINE/'art/render.py'))
    read = render['read']
    base = HERE/'family-C30-C34.mp4'
    corrected = HERE/'hug-C33-corrected.mp4'
    clock = HERE/'family-C30-C34-edition'
    edit = read(clock/'edit.json')
    original = read(base.with_suffix('.json'))
    patch = read(corrected.with_suffix('.json'))
    assert original['output_sha256']==digest(base) and patch['output_sha256']==digest(corrected)
    shot = next(cut for cut in edit['cuts'] if cut['id']=='S12-C33')
    assert patch['frames']==shot['end']-shot['first'] and patch['cuts']==[shot['id']]
    c34 = HERE/'build/photographed-sections/S12-C34-S12-C34.mp4'
    assert read(c34.with_suffix('.json'))['output_sha256']==digest(c34)
    final = HERE/'family-C30-C34-retake.mp4'
    with TemporaryDirectory(prefix='s12-family-mux-',dir=HERE) as directory:
        directory = Path(directory)
        prefix = directory/'earlier-picture.mp4'
        subprocess.run(['ffmpeg','-v','error','-xerror','-i',str(base),'-map','0:v:0','-frames:v',
                        str(shot['first']),'-c','copy','-video_track_timescale','24000',str(prefix)],check=True)
        segments = [(prefix,shot['first']),(corrected,patch['frames']),(c34,edit['frames']-shot['end'])]
        target = directory/'retake.mp4'
        render['merge_picture_streams'](target,segments,edit,clock/'mix.wav',clock/'subtitles.srt')
        target.replace(final)
    original['rows'] = ([r for r in original['rows'] if r['end']<=shot['first']] +
                        [r | {'first':r['first']+shot['first'],'end':r['end']+shot['first']} for r in patch['rows']] +
                        [r for r in original['rows'] if r['first']>=shot['end']])
    original['output_sha256']=digest(final)
    original['retake']={'cut':shot['id'],'first':shot['first'],'end':shot['end'],'source_sha256':digest(corrected)}
    write(final.with_suffix('.json'),original)


if __name__=='__main__':
    main()
