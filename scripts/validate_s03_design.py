#!/usr/bin/env python3
"""Check S03 against immutable V1.1 and S02 schema. Design validation only."""
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
S=ROOT/'scenes'/'S03'
def check(cond,name):
    if not cond: raise AssertionError(name)
    print('PASS:',name)
def main():
    story=(ROOT/'docs/series_v2/sources/01_STORY_MASTER_V1_1.md').read_text(encoding='utf-8')
    block=story.split('## 장면 3. 빨간 모자는 어디에?',1)[1].split('\n---\n\n## 장면 4.',1)[0]
    who=''; source=[]
    for l in block.splitlines():
        m=re.match(r'^\*\*(피노키오|제페토|내레이션)\*\*',l)
        if m: who=m.group(1)
        if l.startswith('"') and l.endswith('"'): source.append((who,l[1:-1]))
    data=json.loads((S/'scene_design_v2.json').read_text(encoding='utf-8'))
    events=json.loads((S/'interaction_map_v2.json').read_text(encoding='utf-8'))
    base=json.loads((ROOT/'scenes/S02/scene_design_v2.json').read_text(encoding='utf-8'))
    check(len(source)==22,'V1.1 S03 22 original lines')
    check(set(base.keys()).issubset(set(data.keys())),'S02 scene-design schema superset')
    beats=data['scenes'];check(len(beats)==10,'10 story beats')
    check(beats[0]['start_seconds']==0 and beats[-1]['end_seconds']==456,'target 456 seconds')
    check(data['duration_target_seconds']==456 and data['wait_excluded'] is True,'non-wait runtime target >=360s')
    check(all(a['end_seconds']==b['start_seconds'] for a,b in zip(beats,beats[1:])),'no timing gaps')
    shots=[s for b in beats for s in b['shots']]
    check(len(shots)==50,'50 acting/camera shots')
    check(all(sum(s['end_seconds']-s['start_seconds'] for s in b['shots'])==b['end_seconds']-b['start_seconds'] for b in beats),'shot spans add up')
    dialog=[x for b in beats for x in b['dialogue']]
    retained=[(x['speaker'],x['text']) for x in dialog if x['kind']=='ORIGINAL']
    check(retained==source,'original wording, speaker, relative order unchanged')
    check(all(x['source_index']==i+1 for i,x in enumerate([z for z in dialog if z['kind']=='ORIGINAL'])),'source indexes 1..22 preserved')
    check(data['original_dialogue_count']==22,'original metadata consistent')
    check(data['new_dialogue_count']==sum(x['kind']=='NEW' for x in dialog),'added-line count consistent')
    ids=[x['id'] for x in dialog if x['kind']=='INTERACTION']
    expected=['S03-P%02d'%i for i in range(1,6)]+['I03','S03-P06','I04','S03-P07','S03-P08']
    check(ids==expected,'eight new and two legacy interactions in plot order')
    check([e['id'] for e in events['events']]==expected and events['count']==10,'10 consistent WAIT/REACT events')
    check(events['rules']['word_recognition'] is False and events['rules']['react_once'] is True,'child accessibility and once-only reactions')
    check(events['legacy_ids']==['I03','I04'],'original I03/I04 not replaced')
    check(data['stage']=='G1_DESIGN_COMPLETE_REVIEW_REQUIRED','unapproved script not marked production-ready')
    script=(S/'script_v2_draft.md').read_text(encoding='utf-8')
    check(all(('“'+line+'”') in script for _,line in source),'all 22 originals printed in script')
    check(data['base_engine_scene']=='S02','S02 engine contract reference preserved')
    print('DESIGN PASS only; 3D runtime, voice, rendered duration and child use NOT_RUN')
if __name__=='__main__':
    try: main()
    except (AssertionError,KeyError,OSError,ValueError,IndexError) as e:
        print('FAIL:',e,file=sys.stderr);sys.exit(1)
