#!/usr/bin/env python3
"""Bind the single re-inked C33 replacement to the normally played full movie."""

from argparse import ArgumentParser
import json
from pathlib import Path
import subprocess
from struct import unpack

from register_character import digest, write


def packets(path, stream):
    return json.loads(subprocess.check_output(['ffprobe','-v','error','-select_streams',stream,
        '-show_packets','-show_data_hash','sha256','-show_entries','packet=pts,dts,duration,flags,data_hash',
        '-of','json',str(path)]))['packets']


def faststart(path):
    kinds = []
    with path.open('rb') as handle:
        while header := handle.read(8):
            size,kind = unpack('>I4s',header)
            if size < 8:
                raise ValueError(f'Unsupported container atom {kind}: {size}')
            kinds.append(kind)
            handle.seek(size-8,1)
    return kinds.index(b'moov') < kinds.index(b'mdat')


def main():
    cli = ArgumentParser(description=__doc__)
    cli.add_argument('played',type=Path)
    cli.add_argument('final',type=Path)
    cli.add_argument('edit',type=Path)
    cli.add_argument('report',type=Path)
    args = cli.parse_args()
    edit = json.loads(args.edit.read_text())
    cut = next(shot for shot in edit['cuts'] if shot['id']=='S12-C33')
    first,end = cut['first'],cut['end']
    old,new = packets(args.played,'v:0'),packets(args.final,'v:0')
    assert len(old)==len(new)==edit['frames']==8820 and faststart(args.final)
    assert old[:first]==new[:first] and old[end:]==new[end:]
    assert [tuple((p['pts'],p['dts'],p['duration'])) for p in old] == \
        [tuple((p['pts'],p['dts'],p['duration'])) for p in new]
    assert packets(args.played,'a:0')==packets(args.final,'a:0')
    assert packets(args.played,'s:0')==packets(args.final,'s:0')
    modified=sum(a['data_hash']!=b['data_hash'] for a,b in zip(old[first:end],new[first:end],strict=True))
    assert modified>0
    write(args.report,{'status':'PASS','normally_played_sha256':digest(args.played),'final_sha256':digest(args.final),
                      'retaken_cut':cut['id'],'changed_encoded_frames':modified,'cut_extent':[first,end],
                      'other_video_packets_identical':len(new)-(end-first),
                      'audio_and_caption_packets_identical':True,'timestamps_identical':True,'faststart':True})
    print(f'Only {modified} pictures in {cut["id"]} differ across the two 8,820-frame cuts.')


if __name__=='__main__':
    main()
