#!/usr/bin/env python3
"""S02 screenplay structural validation; not actual video validation."""
import json, re, sys
from pathlib import Path
R=Path(__file__).resolve().parents[1]
S=R/'scenes'/'S02'
def ck(cond,label):
    if not cond: raise AssertionError(label)
    print('PASS:', label)
def main():
    data=json.loads((S/'scene_design_v2.json').read_text(encoding='utf-8'))
    events=json.loads((S/'interaction_map_v2.json').read_text(encoding='utf-8'))
    orig=(R/'docs/series_v2/sources/01_STORY_MASTER_V1_1.md').read_text(encoding='utf-8')
    part=orig.split('## 장면 2. 피노키오의 첫 친구',1)[1].split('\n---\n\n# ACT 2.',1)[0]
    speaker=''; expected=[]
    for l in part.splitlines():
        m=re.match(r'^\*\*(피노키오|제페토|내레이션)\*\*',l)
        if m: speaker=m.group(1)
        if l.startswith('"') and l.endswith('"'): expected.append((speaker,l[1:-1]))
    ck(len(expected)==21,'21 source lines')
    beats=data['scenes']; ck(len(beats)==10,'10 scene beats')
    ck(beats[0]['start_seconds']==0 and beats[-1]['end_seconds']==443,'443s target timeline')
    ck(data['duration_target_seconds']>=360 and data['wait_excluded'] is True,'planned >=360 seconds excluding wait')
    ck(all(a['end_seconds']==b['start_seconds'] for a,b in zip(beats,beats[1:])),'continuous timeline')
    ck(all(sum(x['end_seconds']-x['start_seconds'] for x in b['shots'])==b['end_seconds']-b['start_seconds'] for b in beats),'shot sum per beat')
    shots=[x for b in beats for x in b['shots']]; ck(len(shots)==50,'50 shots')
    dialog=[x for b in beats for x in b['dialogue']]
    original=[(x['speaker'],x['text']) for x in dialog if x['kind']=='ORIGINAL']
    ck(original==expected,'original wording/speaker/order unchanged')
    new=[x for x in dialog if x['kind']=='NEW']; ck(len(new)==81,'81 new dialogue lines')
    ids=[x['id'] for x in dialog if x['kind']=='INTERACTION']
    valid=['S02-P%02d'%i for i in range(1,10)]+['I02']
    ck(ids==valid,'9 new interactions + original I02')
    ck(events['count']==10 and [x['id'] for x in events['events']]==valid,'interaction map matches script')
    ck(data['stage']=='G1_DESIGN_COMPLETE_REVIEW_REQUIRED','approval not misrepresented')
    screenplay=(S/'script_v2_draft.md').read_text(encoding='utf-8')
    ck(all(('“'+text+'”') in screenplay for _,text in expected),'all source lines appear in screenplay')
    print('Design validation PASS; actual video and human approval NOT_RUN')
if __name__=='__main__':
    try: main()
    except (AssertionError,KeyError,ValueError,OSError,IndexError) as e:
        print('FAIL:',e,file=sys.stderr); sys.exit(1)
