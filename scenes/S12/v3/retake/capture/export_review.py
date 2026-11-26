#!/usr/bin/env python3
"""Export independently playable main and movement review media from the approved cut."""

from argparse import ArgumentParser
from io import BytesIO
import json
from pathlib import Path
import shutil
import subprocess

from PIL import Image, ImageDraw
from register_character import HERE

ROOT = HERE.parent


def photo(video,frame,width):
    body = subprocess.check_output(['ffmpeg','-v','error','-ss',f'{frame/24:.9f}','-i',str(video),
        '-frames:v','1','-vf',f'scale={width}:-2','-f','image2pipe','-vcodec','mjpeg','-threads','1','-'])
    with Image.open(BytesIO(body)) as image:
        return image.convert('RGB')


def board(video, points, output, columns=5, width=320):
    height=round(width*9/16)
    bands = (len(points)+columns-1)//columns
    sheet = Image.new('RGB',(columns*width,bands*(height+22)),'#27231b')
    pen = ImageDraw.Draw(sheet)
    for n,(caption,frame) in enumerate(points):
        row,col=divmod(n,columns)
        x,y=col*width,row*(height+22)
        sheet.paste(photo(video,frame,width),(x,y))
        pen.text((x+7,y+height+4),caption,fill='#f6ead5')
    sheet.save(output,quality=92,optimize=True)


def main():
    cli=ArgumentParser(description=__doc__)
    cli.add_argument('master',type=Path)
    cli.add_argument('output',type=Path)
    args=cli.parse_args()
    args.output.mkdir(parents=True,exist_ok=True)
    shots=json.loads((ROOT/'edition/edit.json').read_text())['cuts']
    index={row['id'][-3:]:row for row in shots}
    family=ROOT/'core/family-C30-C34-retake.mp4'
    shutil.copyfile(family,args.output/'S12-transformation-and-hug.mp4')
    rest = args.output/'S12-hands-and-school.mp4'
    subprocess.run(['ffmpeg','-v','error','-xerror','-y','-ss',f'{index["C35"]["first"]/24:.9f}',
        '-i',str(args.master),'-map','0:v','-map','0:a','-map','0:s','-c','copy','-movflags','+faststart',str(rest)],check=True)
    master_stills=[(shot['id'][-3:],(shot['first']*2+shot['end'])//3) for shot in shots]
    board(args.master,master_stills,args.output/'S12-50-cuts.jpg')
    phases=[('C30',0),('C30',44),('C30',83),('C30',145),('C31',43),('C32',97),
            ('C33',24),('C33',55),('C33',100),('C34',76),('C36',49),('C38',94),
            ('C40',66),('C42',72),('C49',123),('C50',55)]
    board(args.master,[(f'{cut} +{frame}f',index[cut]['first']+frame) for cut,frame in phases],
          args.output/'S12-key-movements.jpg',columns=4,width=416)
    shutil.copyfile(ROOT/'participation-final.json',args.output/'S12-participation-timeline.json')


if __name__=='__main__':
    main()
