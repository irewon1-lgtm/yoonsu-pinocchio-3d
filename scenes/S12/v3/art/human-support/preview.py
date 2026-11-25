#!/usr/bin/env python3
"""Check native 2D cel registration and photograph a silent action-only review strip."""
from hashlib import file_digest
import json
from pathlib import Path
import runpy
import subprocess

from PIL import Image, ImageDraw, ImageFont

HERE=Path(__file__).resolve().parent
V3=HERE.parents[1]
SCENES=V3.parents[1]
ART=V3/'build/art'
ENGINE=runpy.run_path(str(SCENES/'S04/production/render.py'))
STATE=HERE/'support-state.json'
SIZE=(960,540)
FPS=24


def sha(path):
    with path.open('rb') as file:
        return file_digest(file,'sha256').hexdigest()


def audit_cut(artwork, level):
    registry=artwork.registry(level['level'])[0]
    near_point=None
    records=[]
    for mark, entry in zip(level['poses'],registry,strict=True):
        assert mark['index']==entry['index']
        path=ART/entry['file']
        assert entry['sha256']==sha(path)
        root=[xy+delta for xy,delta in zip(level['xy'],mark['stage_offset'],strict=True)]
        actual={'level':level['level'],'cel':entry['index'],'root':root,'height':level['height'],
                'anchor':'stage','flip':False}
        drawing,offset,_,_=artwork.placement(actual)
        bounds=drawing.getchannel('A').getbbox()
        assert bounds and min(bounds[0],bounds[1])>0 and bounds[2]<drawing.width and bounds[3]<drawing.height
        assert drawing.getchannel('A').getextrema()==(0,255)
        pos=[int(bound+offset[axis%2]) for axis,bound in enumerate(bounds)]
        assert 0<=pos[0]<pos[2]<=1280 and 0<=pos[1]<pos[3]<=720
        records.append((drawing,offset,mark['frames'],pos))
        if level['level']=='S12H-cricket-celebration' and root[1]==level['xy'][1]:
            # Keep the actual soles exactly planted independently of the compression above the shins.
            with Image.open(path) as full:
                foot_strip=full.crop((0,475,full.width,full.height)).tobytes()
            if near_point is not None:
                assert near_point==foot_strip
            near_point=foot_strip
    return records


def photograph(report, cuts):
    output=HERE/'S12H-action-cel-review.mp4'
    args=['ffmpeg','-hide_banner','-loglevel','error','-y','-f','rawvideo','-pixel_format','rgb24',
          '-video_size',f'{SIZE[0]}x{SIZE[1]}','-framerate',str(FPS),'-i','-','-an','-c:v','libx264',
          '-threads','2','-preset','veryfast','-crf','18','-pix_fmt','yuv420p',
          '-movflags','+faststart',str(output)]
    font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',21)
    camera=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',17)
    with subprocess.Popen(args,stdin=subprocess.PIPE) as encoder:
        frame_cursor=0
        for cut,records in cuts.items():
            start=frame_cursor
            for figure,offset,duration,bounds in records:
                world=Image.new('RGBA',(1280,720),(218,197,167,255))
                anchor=(515,636) if cut=='S12-C34' else (667,629)
                ImageDraw.Draw(world).line((0,anchor[1],1280,anchor[1]),fill='#957958',width=1)
                world.alpha_composite(figure,offset)
                window=(350,470,670,650) if cut=='S12-C34' else (295,249,1039,667)
                photo=world.crop(window).resize(SIZE,Image.Resampling.LANCZOS).convert('RGB')
                tags=ImageDraw.Draw(photo)
                tags.rectangle((0,0,960,55),fill='#493a2c')
                tags.text((18,14),'S12 SUPPORTING CELS   '+cut,fill='#fff4e0',font=font)
                tags.text((675,16),'Silent motion reference',fill='#fff4e0',font=camera)
                raster=photo.tobytes()
                for _ in range(duration):
                    encoder.stdin.write(raster)
                frame_cursor+=duration
            report['cuts'][cut]['preview_frames']=[start,frame_cursor]
        encoder.stdin.close()
        if encoder.wait():
            raise RuntimeError('Support motion preview encoded with errors')
    probe=subprocess.run(['ffprobe','-v','error','-count_frames','-select_streams','v:0',
                          '-show_entries','stream=codec_name,width,height,r_frame_rate,nb_read_frames,duration',
                          '-of','json',str(output)],check=True,capture_output=True,text=True)
    media=json.loads(probe.stdout)['streams'][0]
    assert int(media['nb_read_frames'])==frame_cursor and media['r_frame_rate']=='24/1'
    report['preview']=media|{'path':output.name,'sha256':sha(output),'silent':True}


def main():
    artwork=ENGINE['Artwork'](ART)
    state=json.loads(STATE.read_text(encoding='utf-8'))
    records={cut:audit_cut(artwork,level) for cut,level in state['cuts'].items()}
    report={'support_registration':'PASS','full_scene_playback':'BLOCKED_RESOURCE',
            'synchronized_dialogue_and_paired_contact':'NOT_RUN',
            'human_overlay':'BLOCKED_RESOURCE', 'review_basis':'native player renderer placement, matte, anchors, cels and silent exposure sequence',
            'cuts':{cut:{'cel_count':len(entries),'exposure_frames':sum(row[2] for row in entries),
                         'stage_alpha_bounds': [row[3] for row in entries]} for cut,entries in records.items()}}
    photograph(report,records)
    (HERE/'support-qa.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(report['preview'])


if __name__=='__main__':
    main()
