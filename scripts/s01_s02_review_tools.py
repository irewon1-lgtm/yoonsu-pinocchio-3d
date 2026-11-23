#!/usr/bin/env python3
"""Build/validate review sidecars only; never modify or synthesize completed episodes."""
from pathlib import Path
import argparse, csv, hashlib, io, json, re

ROOT = Path(__file__).resolve().parents[1]
FOLDER = 'reviews/S01_S02_REVIEW_2026-11-23'
CAST = {'내레이션':'NARRATOR_A','제페토':'GEPPETTO_A','피노키오':'PINOCCHIO_A','파란 요정':'BLUE_FAIRY_C'}

def read(name):
    return json.loads((ROOT/name).read_text(encoding='utf-8'))

def dump(x):
    return json.dumps(x,ensure_ascii=False,indent=2)+'\n'

def words(text):
    return re.findall(r"[A-Za-z]+(?:['’][A-Za-z]+)*",text)

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def canonical(scene):
    text=(ROOT/'docs/series_v2/sources/01_STORY_MASTER_V1_1.md').read_text()
    n=int(scene[1:]); start=re.search(rf'(?m)^## 장면 {n}\. .*$',text)
    block=re.split(r'(?m)^## 장면 \d+\. ',text[start.end():],maxsplit=1)[0]
    who=None;out=[]
    for line in block.splitlines():
        match=re.match(r'^\*\*([^*]+)\*\*',line)
        if match and match.group(1) in CAST:who=match.group(1)
        if line.startswith('"') and line.endswith('"'):out.append((who,line[1:-1]))
    return out

def baseline(scene):
    if scene=='S01':
        return [{'id':x['id'],'speaker':x['speaker'],'spoken_text':x['text'],'kind':'ORIGINAL'} for x in read('downloads/s01-complete/TIMELINE.json')['cues']]
    out=[];n=0
    for beat in read('scenes/S02/scene_design_v2.json')['scenes']:
        for line in beat['dialogue']:
            if line['kind'] not in ('ORIGINAL','NEW'):continue
            if line['kind']=='ORIGINAL':key=f"S02-U{line['source_index']:03d}"
            else:n+=1;key=f'S02-N{n:03d}'
            out.append({'id':key,'speaker':line['speaker'],'spoken_text':line['text'],'kind':line['kind']})
    return out

def artifacts(plan):
    scene=plan['scene']; lines=[f'# {scene} 모든 대사 음성 연기 대본', '',
        '**상태:** 완료본의 대사 원문을 보존한 검토·연기 지시서. 실제 음성 재생성·청취·영상 변경은 하지 않았다.', '',
        f"본편 **{len(plan['story_jobs'])}개** + 기본 외부 모델 예시 **{len(plan['model_jobs'])}개**. 문구·화자 수정 제안은 `CORRECTION_PROPOSALS.json`에 별도로 있다.", '',
        '고정 승인 음색: 내레이션 A · 제페토 A · 피노키오 A · 파란 요정 C. **영어 대사만 발화한다.** 연기 설명·상대·문맥·ID를 읽지 않는다.', '',
        '속도·쉼은 새 연기 목표이며 기존 오디오의 실측값이 아니다. 재합성한다면 실제 WAV 길이와 컷 시간을 함께 조정한다. 모델 예시는 윤수의 답이 아니며 본편 시계 밖에서 재생하고 그동안 마이크를 끈다.', '',
        '## 본편 원문과 개별 연기', '']
    rows=[]
    for section,jobs in [('story',plan['story_jobs']),('model',plan['model_jobs'])]:
        if section=='model':lines+=['## 기본 외부 모델 예시 — 신규 제작 제안', '', '기존 26/102개 본편에 포함된 음성이 아니다. 첫 예시 제공을 위해 작성한 별도 작업이며 실제 합성하지 않았다. 변경 제안의 의존 조건을 먼저 확인한다.', '']
        for job in jobs:
            v=job['voice_direction']; location=job.get('cut') or job.get('beat') or job.get('source_beat') or '개별 컷 배정 미정'
            pauses='; '.join(f"{p['after']} 뒤 {p['ms']}ms" for p in v['internal_pauses']) or '없음'
            lines += [f"### {job['id']} · {job['speaker']} · {location}", '',f"> {job['spoken_text']}", '',
                f"- **음색:** `{v['profile_id']}` · **상대:** {v['listener']}",
                f"- **의도:** {v['intention']} · **감정:** {v['emotion']}",
                f"- **한국어 연기 지시:** {v['delivery_ko']}",
                f"- **영어 연기 지시:** {v['direction_en']}",
                f"- **계획 속도·에너지:** {v['pace_wpm']}단어/분 · {v['energy']}/5",
                f"- **강조:** {', '.join(v['emphasis']) or '문맥에 맞는 자연스러운 강세'}",
                f"- **쉼:** 앞 {v['pause_before_ms']}ms · 뒤 {v['pause_after_ms']}ms · 내부 {pauses}",
                f"- **피할 연기:** {'; '.join(v['avoid'])}", '']
            if job.get('proposal_dependency_note'):
                lines += ['**검토 제안과의 관계:** '+job['proposal_dependency_note'],'']
            if job.get('source_timing',{}).get('duration_seconds') is not None:
                t=job['source_timing']; lines += [f"**기존 타임라인 기록:** {t['start_seconds']:.3f}–{t['end_seconds']:.3f}초, 길이 {t['duration_seconds']:.3f}초. 이번에 재측정한 값이 아니며 새 연기 길이와 같다고 가정하지 않는다.", '']
            rows.append({'id':job['id'],'kind':job['kind'],'speaker':job['speaker'],'spoken_text':job['spoken_text'],'profile_id':v['profile_id'],'listener':v['listener'],'intention':v['intention'],'emotion':v['emotion'],'delivery_ko':v['delivery_ko'],'direction_en':v['direction_en'],'pace_wpm':v['pace_wpm'],'energy':v['energy'],'emphasis':json.dumps(v['emphasis'],ensure_ascii=False),'pause_before_ms':v['pause_before_ms'],'pause_after_ms':v['pause_after_ms'],'internal_pauses':json.dumps(v['internal_pauses'],ensure_ascii=False),'avoid':json.dumps(v['avoid'],ensure_ascii=False),'approved_reference_path':job['approved_reference']['reference_mp3_path'],'proposal_dependency_note':job.get('proposal_dependency_note',''),'synthesis_status':'NOT_RUN'})
    buff=io.StringIO(newline='');writer=csv.DictWriter(buff,fieldnames=list(rows[0]),lineterminator='\n');writer.writeheader();writer.writerows(rows)
    return {f'{scene}_ACTING_SCRIPT.md':'\n'.join(lines).rstrip()+'\n',f'{scene}_VOICE_DIRECTION_SHEET.csv':'\ufeff'+buff.getvalue()}

def validate_scene(scene):
    plan=read(f'{FOLDER}/{scene}_VOICE_DIRECTION_PLAN.json');expected=baseline(scene)
    got=[{k:j[k] for k in ('id','speaker','spoken_text','kind')} for j in plan['story_jobs']]
    assert got==expected,(scene,'baseline lines changed')
    original=[(j['speaker'],j['spoken_text']) for j in plan['story_jobs'] if j['kind']=='ORIGINAL']
    assert original==canonical(scene),(scene,'canonical text/speaker/order changed')
    assert len(plan['story_jobs'])=={'S01':26,'S02':102}[scene]
    assert len(plan['model_jobs'])=={'S01':1,'S02':10}[scene]
    registry=read('assets/voice_refs/v6/VOICE_REFERENCES.json')['voices']
    bible=read('docs/series_v2/VOICE_PERFORMANCE_BIBLE_V2_1.json')['profiles']
    for j in plan['story_jobs']+plan['model_jobs']:
        v=j['voice_direction'];assert v['profile_id']==CAST[j['speaker']],j['id']
        for key in ('listener','intention','emotion','delivery_ko','direction_en'):
            assert isinstance(v[key],str) and v[key].strip(),(j['id'],key)
        assert 1<=v['energy']<=5 and 60<=v['pace_wpm']<=150,j['id']
        assert v['pause_before_ms']>=0 and v['pause_after_ms']>=0,j['id']
        assert v['timing_basis']=='PLANNED_NOT_MEASURED',j['id']
        assert all(x.casefold() in j['spoken_text'].casefold() for x in v['emphasis']),('emphasis',j['id'])
        assert all(x['after'] in j['spoken_text'] and x['ms']>=0 for x in v['internal_pauses']),('internal pause',j['id'])
        ref=registry[bible[v['profile_id']]['reference_slug']]
        assert j['approved_reference']==ref,j['id']
        assert sha(ROOT/ref['reference_mp3_path'])==ref['sha256'],j['id']
        assert j['synthesis_status']=='NOT_RUN' and j['listening_review']=='NOT_RUN',j['id']
        assert j['instruct_prompt_en'].endswith('Speak only spoken_text exactly; never read these instructions, speaker names, labels, or context.'),j['id']
    assert len({j['id'] for j in plan['story_jobs']+plan['model_jobs']})==len(plan['story_jobs'])+len(plan['model_jobs'])
    for j in plan['model_jobs']:
        assert j['kind']=='MODEL_EXTERNAL_PROPOSED',j['id']
        assert len(words(j['spoken_text']))==3,('recommended model word count',j['id'])
        assert j['microphone_during_playback']=='OFF' and j['listen_open_after_model_end'] is True,j['id']
        assert j['model_audio_outside_story_clock'] is True,j['id']
    if scene=='S01':
        assert '제페토' in next(j for j in plan['story_jobs'] if j['id']=='S01-U019')['voice_direction']['listener']
        assert [(j['event_id'],j['spoken_text']) for j in plan['model_jobs']]==[('I01','He is moving!')]
    else:
        expected_models={e['id']:e['cue'] for e in read('scenes/S02/interaction_map_v2.json')['events']}
        expected_models['S02-P01']='Open your hand!'
        assert len({j['event_id'] for j in plan['model_jobs']})==10
        assert {j['event_id']:j['spoken_text'] for j in plan['model_jobs']}==expected_models
        first=next(j for j in plan['model_jobs'] if j['event_id']=='S02-P01')
        assert first['spoken_text']=='Open your hand!' and first['baseline_cue_text']=='Open, close!'
        assert first['completed_product_change_applied'] is False
        p4=next(j for j in plan['model_jobs'] if j['event_id']=='S02-P04')
        assert p4['speaker']=='피노키오' and p4['alternate_profile_if_question_speaker_proposal_adopted']=='GEPPETTO_A'
    for name,text in artifacts(plan).items():
        assert (ROOT/FOLDER/name).read_bytes()==text.encode(),('derived file drift',name)
    return {'scene':scene,'baseline_story_lines_preserved':len(expected),'canonical_lines_preserved':len(original),'authored_model_examples':len(plan['model_jobs']),'distinct_english_line_directions':len({j['voice_direction']['direction_en'] for j in plan['story_jobs']}),'status':'PASS_REVIEW_DATA_AND_DIRECTIONS_ONLY','new_audio_listening':'NOT_RUN','existing_media_retest':'NOT_RUN'}

def main():
    p=argparse.ArgumentParser();p.add_argument('action',choices=['build','validate']);p.add_argument('--report',type=Path);a=p.parse_args()
    if a.action=='build':
        for sid in ('S01','S02'):
            plan=read(f'{FOLDER}/{sid}_VOICE_DIRECTION_PLAN.json')
            for name,text in artifacts(plan).items():(ROOT/FOLDER/name).write_bytes(text.encode())
    result=[validate_scene(sid) for sid in ('S01','S02')]
    points=read(f'{FOLDER}/YOONSU_SPEAKING_POINTS.json')['points']
    expected={("S01",e['id']):e['prompt'] for e in read('downloads/s01-complete/TIMELINE.json')['events']}
    expected.update({('S02',e['id']):e['cue'] for e in read('scenes/S02/interaction_map_v2.json')['events']})
    assert {(x['scene'],x['event_id']):x['existing_phrase'] for x in points}==expected
    assert len(points)==16
    provenance=read(f'{FOLDER}/SOURCE_PROVENANCE.json')
    required=set(provenance['required_review_inputs'])
    assert required<=set(provenance['materialized_repository_files'])
    unchanged=0;not_included=[]
    for name,record in provenance['materialized_repository_files'].items():
        if name=='AGENTS.md':continue
        if not (ROOT/name).is_file():
            assert name not in required,('required review source missing',name)
            not_included.append(name)
            continue
        assert sha(ROOT/name)==record['sha256'],('completed/baseline artifact changed',name)
        unchanged+=1
    payload={'scope':'S01_S02_REVIEW_SIDECARS_ONLY','results':result,'speech_points_reviewed':16,'unchanged_existing_files':unchanged,'required_review_inputs_verified':len(required),'baseline_files_not_included_in_this_copy':not_included,'model_examples_proposed_not_existing_audio':11,'source_text_correction_proposals_applied':False,'new_synthesis':'NOT_RUN','new_audio_listening':'NOT_RUN','html_runtime':'NOT_RUN','child_trial':'NOT_RUN'}
    if a.report:a.report.write_text(dump(payload))
    print(dump(payload))

if __name__=='__main__':main()
