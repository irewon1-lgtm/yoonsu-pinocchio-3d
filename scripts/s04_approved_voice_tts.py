#!/usr/bin/env python3
"""Verify S04 approved reference voices; optionally synthesize only already-approved speakers. Cricket remains BLOCKED_RESOURCE."""
from __future__ import annotations
import argparse,hashlib,json,subprocess,sys
from collections import Counter
from pathlib import Path
R=Path(__file__).resolve().parents[1]
REFS=R/'assets/voice_refs/v6/VOICE_REFERENCES.json'
KNOWN={'내레이션':'narrator','피노키오':'pinocchio','제페토':'geppetto','파란 요정':'blue_fairy'}
def main():
    p=argparse.ArgumentParser()
    p.add_argument('--synthesize',action='store_true',help='default checks files and missing Cricket voice only')
    p.add_argument('--limit',type=int,default=2,help='preview only, 1..10 lines')
    p.add_argument('--device',default='cpu',choices=['cpu','cuda','mps'])
    args=p.parse_args()
    refs=json.loads(REFS.read_text(encoding='utf-8'))
    d=json.loads((R/'scenes/S04/scene_design_v2.json').read_text(encoding='utf-8'))
    lines=[(beat['id'],x['speaker'],x['text']) for beat in d['scenes'] for x in beat['dialogue'] if x['kind'] in ('ORIGINAL','NEW')]
    all_speakers=Counter(speaker for _,speaker,_ in lines)
    unknown={s:count for s,count in all_speakers.items() if s not in KNOWN}
    if set(unknown)!={'귀뚜라미'}:
        raise RuntimeError('Unexpected missing approved cast; expected only 귀뚜라미: '+str(unknown))
    for slug,info in refs['voices'].items():
        path=R/info['reference_mp3_path']
        if not path.exists():raise RuntimeError('Missing approved '+slug+' '+str(path))
        if hashlib.sha256(path.read_bytes()).hexdigest()!=info['sha256']:
            raise RuntimeError('Approved reference SHA mismatch: '+slug)
        print('APPROVED_VOICE_REF_PASS',slug,path)
    print('S04_TTS_PREFLIGHT: all dialogue lines',len(lines),'known cast',sum(v for k,v in all_speakers.items() if k in KNOWN))
    print('BLOCKED_RESOURCE: 귀뚜라미 voice reference not approved; lines',unknown['귀뚜라미'])
    print('Do not use any existing approved speaker as a replacement for Cricket.')
    if not args.synthesize:
        print('DRY_RUN_PASS_FOR_REFERENCES_ONLY: no audio synthesized; full S04 voice gate BLOCKED_RESOURCE')
        return
    if not 1<=args.limit<=10:raise RuntimeError('1..10 lines per preview to avoid unnecessary generation')
    allowed=[(beat,who,text) for beat,who,text in lines if who in KNOWN]
    import torchaudio as ta
    from chatterbox.tts_turbo import ChatterboxTurboTTS
    out=R/'scenes/S04/audio/voice_previews'
    cache=R/'scenes/S04/audio/reference_cache'
    out.mkdir(parents=True,exist_ok=True);cache.mkdir(parents=True,exist_ok=True)
    for slug,info in refs['voices'].items():
        wav=cache/(slug+'.wav')
        subprocess.run(['ffmpeg','-y','-v','error','-i',str(R/info['reference_mp3_path']),'-ar','24000','-ac','1','-c:a','pcm_s16le',str(wav)],check=True)
    model=ChatterboxTurboTTS.from_pretrained(device=args.device,nano=True)
    for idx,(beat,who,text) in enumerate(allowed[:args.limit],1):
        slug=KNOWN[who]
        pcm=model.generate(text,audio_prompt_path=str(cache/(slug+'.wav')))
        file=out/f'S04-{idx:03d}_{slug}.wav'
        ta.save(str(file),pcm.cpu(),model.sr)
        print('PREVIEW_NOT_APPROVED',beat,who,text,file)
    print('COMPARE_TOBE_APPROVED with S01 V7; Cricket dialogue remains blocked')
if __name__=='__main__':
    try:main()
    except Exception as exc:
        print('FAIL',type(exc).__name__,str(exc),file=sys.stderr)
        raise
