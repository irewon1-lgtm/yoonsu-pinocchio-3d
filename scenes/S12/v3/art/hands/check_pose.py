#!/usr/bin/env python3
"""Sample the physical actions through the existing S11 art placement and timing."""
from __future__ import annotations

from argparse import ArgumentParser
import json
from pathlib import Path
import runpy
from PIL import Image, ImageDraw

HERE=Path(__file__).resolve().parent
V3=HERE.parents[1]
BASE=V3/'build'
RUNTIME=runpy.run_path(str(V3/'art/render.py'))
ENGINE=RUNTIME['ENGINE']['camera_engine']()

def read(path):
    return json.loads(path.read_text(encoding='utf-8'))

def check(edit,output):
    relevant={cut['id']:cut for cut in edit['cuts'] if 35<=int(cut['id'][-2:])<=42}
    sections={cut['id']:cut for cut in read(BASE/'layout-hands.json')}
    assert sections.keys()==relevant.keys()
    sample=RUNTIME['resolve_layout']({'cuts':list(relevant.values())},sections)
    art=ENGINE['render_shots'].__globals__['Artwork'](BASE/'art')
    checks=[
        (35,0,'first lowered hands'),(35,14,'own hands up, unfurled'),
        (35,-9,'adult palms demonstrated'),(36,53,'child presents both hands'),
        (37,44,'adult curls, child waits'),(38,47,'one deliberate bend'),
        (38,105,'child feels palm'),(39,-8,'palm offered, contact absent'),
        (40,59,'supported child hand'),(40,-18,'after speech, releasing'),
        (41,38,'adult indicates tilted hat'),(42,43,'wrists at same hat'),
        (42,67,'straightened and released'),(42,-4,'both hands down'),
    ]
    width,height=560,315
    montage=Image.new('RGB',(4*width,4*(height+28)),(240,228,216))
    receipt=[]
    for i,(number,n,name) in enumerate(checks):
        sid=f'S12-C{number}'
        cut,reel=relevant[sid],sample[sid]
        registers=[ENGINE['BodyTrack'](cut,RUNTIME['ENGINE']['timed_layer'](cut,layer),idx,art)
                   for idx,layer in enumerate(reel['layout'])]
        frame=cut['first']+n if n>=0 else cut['end']+n
        modes=[track.state(frame) for track in registers if track.lo<=frame<track.hi]
        photo=art.photograph(reel['plate'],modes).resize((width,height),Image.Resampling.LANCZOS)
        x,y=i%4*width,i//4*(height+28)
        montage.paste(photo,(x,y+27))
        ImageDraw.Draw(montage).text((x+11,y+7),f'{sid[-3:]}  {name} / +{frame-cut["first"]}f',fill=(42,24,20))
        receipt.append({'cut':sid,'cut_frame':frame-cut['first'],'native_frame':frame,'visible_levels':modes})
    output.mkdir(parents=True,exist_ok=True)
    montage.save(output/'hand-contact-stage.jpg',quality=92,optimize=True)
    (output/'hand-contact-stage.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(output/'hand-contact-stage.jpg')

if __name__=='__main__':
    parser=ArgumentParser(description=__doc__)
    parser.add_argument('--edit',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    check(read(args.edit),args.out)
