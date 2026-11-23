#!/usr/bin/env python3
"""Verify S04 authored screenplay vs immutable V1.1 and S02/S03 data schema; not real video QA."""
from pathlib import Path
import json, re, sys
R = Path(__file__).resolve().parents[1]
D = R/'scenes'/'S04'
def check(condition, label):
    if not condition: raise AssertionError(label)
    print('PASS',label)
def main():
    master=(R/'docs/series_v2/sources/01_STORY_MASTER_V1_1.md').read_text(encoding='utf-8')
    source=master.split('## 장면 4. 학교로 가는 길',1)[1].split('\n---\n\n# ACT 3.',1)[0]
    speaker=None; originals=[]
    for line in source.splitlines():
        m=re.match(r'^\*\*(제페토|피노키오|내레이션|귀뚜라미)\*\*',line)
        if m: speaker=m.group(1)
        if line.startswith('"') and line.endswith('"'): originals.append((speaker,line[1:-1]))
    check(len(originals)==32,'V1.1 S04 32 speech lines present')
    d=json.loads((D/'scene_design_v2.json').read_text(encoding='utf-8'))
    im=json.loads((D/'interaction_map_v2.json').read_text(encoding='utf-8'))
    base=json.loads((R/'scenes/S02/scene_design_v2.json').read_text(encoding='utf-8'))
    prev=json.loads((R/'scenes/S03/scene_design_v2.json').read_text(encoding='utf-8'))
    check(set(base).issubset(set(d)),'S02 JSON schema backward-compatible')
    check(set(prev).issubset(set(d)),'S03 JSON schema backward-compatible')
    check(d['scene']=='S04' and d['base_engine_scene']=='S02','correct S04 / S02 contract')
    beats=d['scenes'];check(len(beats)==10,'10 story beats')
    check(beats[0]['start_seconds']==0 and beats[-1]['end_seconds']==479,'479s target no gaps')
    check(d['duration_target_seconds']==479 and d['wait_excluded'] is True,'wait excluded from planned duration')
    check(all(a['end_seconds']==b['start_seconds'] for a,b in zip(beats,beats[1:])),'beat timeline contiguous')
    shots=[s for b in beats for s in b['shots']]
    check(len(shots)==50 and len({s['id'] for s in shots})==50,'50 unique camera/acting shots')
    check(all(len(b['shots'])==5 and sum(s['end_seconds']-s['start_seconds'] for s in b['shots'])==b['end_seconds']-b['start_seconds'] for b in beats),'5 shots/beat and timings add up')
    check(all(all(s['end_seconds']>s['start_seconds'] for s in b['shots']) for b in beats),'positive shot durations')
    dialog=[x for b in beats for x in b['dialogue']]
    kept=[x for x in dialog if x['kind']=='ORIGINAL']
    check([(x['speaker'],x['text']) for x in kept]==originals,'all 32 original lines speaker/text/order preserved')
    check([x['source_index'] for x in kept]==list(range(1,33)),'source indexing unchanged 1..32')
    check(d['original_dialogue_count']==32,'source count metadata')
    check(sum(x['kind']=='NEW' for x in dialog)==d['new_dialogue_count']==77,'77 new lines metadata')
    ids=[x['id'] for x in dialog if x['kind']=='INTERACTION']
    expected=['S04-P01','I05','S04-P02','S04-P03','S04-P04','I06','S04-P05','S04-P06','I07','S04-P07']
    check(ids==expected and len(set(ids))==10,'exactly 10 events preserving I05/I06/I07')
    check(im['count']==10 and im['legacy_ids']==['I05','I06','I07'] and im['new_count']==7,'three original, seven new')
    check([x['id'] for x in im['events']]==expected,'interaction map matches authored screenplay')
    check(im['rules']['word_recognition'] is False and im['rules']['react_once'] is True and im['rules']['parent_tap_alternative'] is True,'VAD/tap accessible once-only interactions')
    check(d['stage']=='G1_DESIGN_COMPLETE_REVIEW_REQUIRED','no user approval inferred')
    check(d['unapproved_voice_speakers']==['귀뚜라미'],'new Cricket speaker flagged as unapproved')
    txt=(D/'script_v2_draft.md').read_text(encoding='utf-8')
    check(all(('“'+t+'”') in txt for _,t in originals),'all 32 source lines printed in screenplay')
    man=json.loads((R/'docs/series_v2/series_manifest_v2.json').read_text(encoding='utf-8'))
    s=next(s for s in man['scenes'] if s['id']=='S04')
    check(s['design_runtime_target_seconds']==479 and s['design_shot_count']==50 and s['expanded_script_approved'] is False,'S04 manifest matches draft')
    print('DESIGN_ONLY_PASS: actual S04 rendering/voice/child testing NOT_RUN, Cricket voice BLOCKED_RESOURCE')
if __name__=='__main__':
    try: main()
    except (AssertionError,ValueError,KeyError,OSError,IndexError,StopIteration) as exc:
        print('FAIL:',exc,file=sys.stderr)
        sys.exit(1)
