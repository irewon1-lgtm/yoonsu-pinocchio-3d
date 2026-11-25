from pathlib import Path
import json,re,csv,hashlib,collections,sys
ROOT=Path(__file__).resolve().parents[1]
S=ROOT/'story'; V=ROOT/'voice'; A=ROOT/'assets'; E=ROOT/'evidence'; O=ROOT/'sources'
def dump(p,x): p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def tc(t):return f'{t//60:02d}:{t%60:02d}'
meta=json.loads((S/'S12_AUTHORING_METADATA_V2.json').read_text(encoding='utf-8'))
source=(O/'01_STORY_MASTER_V1_1.md').read_text()
sec=source.split('## 장면 12. 친구를 구한 진짜 아이',1)[1].split('# 제작 공통 규칙',1)[0]
canon=[]; sp=None
for line in sec.splitlines():
 m=re.match(r'^\*\*(내레이션|귀뚜라미|피노키오|제페토|파란 요정)\*\*',line)
 if m: sp=m[1]
 if line.startswith('"') and line.endswith('"'):
  canon.append({'dialogue_id':f'S12-U{len(canon)+1:03d}','speaker':sp,'text':line[1:-1]})
assert len(canon)==44, len(canon)
canon_map={r['dialogue_id']:r for r in canon}
profiles={
'피노키오':{'id':'PINOCCHIO_S03_USER_LOCKED','lock':'최종 승인 S03 음색·이야기 속 이름 유지. 목각→인간형 변신 후에도 화자 교체 금지.','reference_status':'REQUIRE_APPROVED_REFERENCE_AT_RUNTIME','arc':'등교 기대→친구 걱정→자발적 결심→솔직한 두려움 인정→신기함→폭발적인 기쁨→다정한 작별'},
'제페토':{'id':'GEPPETTO_S03_USER_LOCKED','lock':'최종 사용자 고정 S03. 젊은 대체 프리셋 금지.','reference_status':'REQUIRE_APPROVED_REFERENCE_AT_RUNTIME','arc':'기대→침착한 도움→아이에 대한 자랑→감격→변함없는 사랑'},
'귀뚜라미':{'id':'CRICKET_EXISTING_IDENTITY','lock':'기존 고정 음색. 새로운 고음 희화화 금지.','reference_status':'REQUIRE_APPROVED_REFERENCE_AT_RUNTIME','arc':'동행→놀람과 답답함→안도와 감사→회복→친구의 성장에 대한 기쁨'},
'파란 요정':{'id':'BLUE_FAIRY_EXISTING_C','lock':'기존 승인 C 음색. 마법과 무관하게 캐스트 고정.','reference_status':'REFERENCE_BYTES_AVAILABLE','arc':'따뜻한 인정→경이로운 선물→멀어지는 축복'},
'내레이션':{'id':'NARRATOR_EXISTING_A','lock':'기존 승인 A. 평서문 낭독조 금지.','reference_status':'REQUIRE_APPROVED_REFERENCE_AT_RUNTIME','arc':'기대→갑작스러운 변화→경이로움→따뜻한 미래와 완결'}}
# Reference identity is explicit. Available old reference bytes are not new synthesis.
for speaker,name in [('파란 요정','blue_fairy_V6_APPROVED.mp3'),('내레이션','narrator_V6_APPROVED.mp3')]:
 p=V/'references'/name
 profiles[speaker].update(reference_status='REFERENCE_BYTES_AVAILABLE',reference_path=str(p.relative_to(ROOT)),reference_sha256=sha(p),reference_bytes=p.stat().st_size,synthesis_status='NOT_RUN',listening_status='NOT_RUN')
profiles['파란 요정']['legacy_aliases']=['FAIRY_EXISTING_APPROVED_C']
profiles['파란 요정']['alias_rule']='Resolve legacy S12 alias to BLUE_FAIRY_EXISTING_C and its exact approved C reference bytes; do not choose a fallback voice.'
for speaker in ['피노키오','제페토','귀뚜라미']:
 profiles[speaker].update(reference_status='BLOCKED_REFERENCE',reference_path=None,reference_sha256=None,synthesis_status='NOT_RUN',listening_status='NOT_RUN')
# Emotion values are acting targets, not claims of backend controls.
listeners={
'U001':'윤수와 관객','U002':'윤수와 관객','U003':'피노키오와 제페토','U004':'피노키오와 제페토','U005':'귀뚜라미','U006':'피노키오','U007':'자기 자신과 제페토','U008':'자기 자신과 제페토','U009':'피노키오','U010':'윤수','U011':'피노키오','U012':'피노키오','U013':'귀뚜라미','U014':'귀뚜라미','U015':'피노키오','U016':'피노키오','U017':'윤수와 관객','U018':'피노키오','U019':'피노키오','U020':'피노키오','U021':'피노키오','U022':'피노키오','U023':'파란 요정','U024':'피노키오','U025':'피노키오','U026':'피노키오','U027':'피노키오','U028':'윤수와 관객','U029':'제페토','U030':'제페토','U031':'피노키오','U032':'피노키오','U033':'피노키오','U034':'피노키오','U035':'파란 요정','U036':'윤수','U037':'윤수와 관객','U038':'윤수와 관객','U039':'윤수와 관객','U040':'윤수와 관객','U041':'윤수와 관객','U042':'피노키오와 일행','U043':'윤수와 관객','U044':'윤수와 관객',
'N001':'피노키오','N002':'윤수','N003':'제페토','N004':'피노키오','N005':'피노키오','N006':'윤수','N007':'제페토','N008':'피노키오','N009':'제페토','N010':'피노키오','N011':'윤수','N012':'피노키오','N013':'윤수','N014':'제페토와 귀뚜라미','N015':'자기 자신과 제페토','N016':'윤수','N017':'피노키오','N018':'윤수','N019':'제페토','N020':'피노키오','N021':'제페토','N022':'윤수','N023':'피노키오','N024':'제페토','N025':'윤수','N026':'제페토','N027':'윤수'}
emotions={
'U001':'따뜻한 기대','U002':'기대에서 긴장으로 급전환','U003':'갑작스러운 놀람·다급한 요청','U004':'당황과 답답함','U005':'강한 걱정→다정한 확인','U006':'안심→막힌 답답함','U007':'급한 깨달음','U008':'친구 걱정→결심','U009':'침착한 신뢰','U010':'진심 어린 부탁','U011':'강한 안도와 감사','U012':'기쁜 감사','U013':'다정한 확신','U014':'솔직한 우정','U015':'깊은 자랑스러움','U016':'온화한 인정','U017':'익숙한 경이로움','U018':'애정과 인정','U019':'진실에 대한 존중','U020':'용기 인정','U021':'따뜻한 만족','U022':'오늘의 행동에 대한 자부심','U023':'겸손한 솔직함','U024':'다정한 긍정','U025':'존중→배려','U026':'선물을 앞둔 기대','U027':'깊은 기쁨과 경이로운 약속','U028':'경이로움→감동','U029':'폭발적 기쁨','U030':'믿기 어려운 감격과 환희','U031':'놀라움→벅찬 애정','U032':'감격과 기쁨','U033':'친구의 성장에 대한 축하','U034':'따뜻한 축복','U035':'다짐→감사','U036':'밝고 애틋한 작별','U037':'부드러운 희망','U038':'편안한 인정','U039':'미래에 대한 기대','U040':'솔직함에 대한 확신','U041':'깊은 만족','U042':'먼 곳에서의 따뜻한 희망','U043':'충만한 여운','U044':'따뜻한 완결',
'N001':'따뜻한 환영','N002':'기대 어린 초대','N003':'신기함','N004':'친근한 안심','N005':'가벼운 놀람','N006':'다정한 질문','N007':'밝은 안도','N008':'공감','N009':'솔직한 두려움 인정','N010':'다정한 감사','N011':'배려','N012':'안심→밝은 회복','N013':'안전한 안내','N014':'정착한 만족','N015':'포옹 후 촉감에 대한 세밀한 호기심','N016':'편안한 호기심과 다정한 부탁','N017':'가까이서 살펴보는 애정','N018':'신기함과 기대','N019':'촉감의 경이로움','N020':'변하지 않는 사랑','N021':'안온한 행복','N022':'포옹 이후의 편안한 초대','N023':'따뜻한 발견','N024':'장난스러운 반가움','N025':'다정한 미소','N026':'만족→기대','N027':'애틋한 초대'}
shots=[]; dialogue=[]; t=0
for l in (S/'S12_AUTHORING_SOURCE.txt').read_text().splitlines():
 if not l or l.startswith('#'): continue
 parts=l.split('|'); key=parts[0]
 if key.startswith('C'):
  assert len(parts)==6,(key,len(parts))
  _,dur,orig,cam,action,sound=parts; dur=int(dur); n=int(key[1:]);
  state={'pinocchio_form_start':'WOODEN' if n<=30 else 'CHAR_YOONSU_HUMAN','pinocchio_form_end':'WOODEN' if n<30 else 'CHAR_YOONSU_HUMAN','nose':'NORMAL','hat':'SAME_RED_HAT_ON_HEAD','bag':'SAME_CLOSED_BAG_ON_BODY_CONTAINING_SAME_BOOK','footwear':'SAME_APPROVED_SHOES','geppetto_glasses':'ON_FACE','school_door':'OPEN','school_entry':'OUTSIDE' if n<49 else ('CROSSES_THRESHOLD' if n==49 else 'INSIDE'), 'signboard':'STANDING' if n<=5 else ('FALLS' if n==6 else ('FALLEN_STABLE' if n<=12 else ('LIFTED' if n==13 else ('RETURNED_UPRIGHT_STABLE' if n==14 else 'UPRIGHT_STABLE')))), 'cricket':'SAFE_FREE' if n<=5 else ('BLOCKED_UNINJURED' if n<=12 else ('EXITS_SAFE_SIDE' if n==13 else 'SAFE_FREE')), 'fairy':'ABSENT' if n<=20 else ('BLUE_LIGHT' if n==21 else ('PRESENT' if n<=44 else 'DISTANT'))}
  shot={'id':f'S12-{key}','beat_id':f'B{(n-1)//5+1:02d}','original_shot_ids':[f'S12-C{x}' for x in orig.split(',')], 'start_seconds_planned':t,'end_seconds_planned':t+dur,'duration_seconds_planned':dur,'frame_start_planned':24*t,'frame_end_exclusive_planned':24*(t+dur),'camera':cam,'acting_motion':action,'audio_boundary':sound,'dialogue_ids':[],'state':state,'events':[],'actual_duration_seconds':None,'status':'AUTHORING_ONLY'}
  shots.append(shot);t+=dur
 else:
  if key.startswith('U'):
   assert len(parts)==6,(key,len(parts)); _,speaker,ko,en,stress,pron=parts; record=canon_map['S12-'+key]; assert speaker==record['speaker'],(key,speaker,record['speaker']); words=record['text']; kind='ORIGINAL'
  elif key.startswith('N'):
   assert len(parts)==7,(key,len(parts)); _,speaker,words,ko,en,stress,pron=parts; kind='NEW'
  else: raise ValueError(key)
  vd={'listener':listeners[key],'emotion_target':emotions[key],'delivery_ko':ko,'direction_en':en,'emphasis':stress.split('; '),'pronunciation_note':pron,'performance_contract':'Speak only spoken_text. Follow scene action and listener; do not read directions or add words. No flat read or global pitch/speed substitution. Natural within-line emotional transition, keep fixed identity and consonants.','actual_supported_controls':None,'actual_audio_sha256':None,'listening_status':'NOT_RUN'}
  row={'dialogue_id':'S12-'+key,'job_id':'S12-'+key,'kind':kind,'speaker':speaker,'profile_id':profiles[speaker]['id'],'spoken_text':words,'shot_id':shot['id'],'delivery_mode':'NARRATIVE_ACTING','voice_direction':vd,'actual_audio_path':None,'actual_duration_seconds':None,'status':'NOT_RUN'}
  dialogue.append(row);shot['dialogue_ids'].append(row['dialogue_id'])
D={r['dialogue_id']:r for r in dialogue}; Q={r['id']:r for r in shots}
# Each job carries its real neighboring lines and visible action into the synthesis handoff.
for i,d in enumerate(dialogue):
 d['voice_direction']['context_before']={'dialogue_id':dialogue[i-1]['dialogue_id'],'speaker':dialogue[i-1]['speaker'],'spoken_text':dialogue[i-1]['spoken_text']} if i else None
 d['voice_direction']['context_after']={'dialogue_id':dialogue[i+1]['dialogue_id'],'speaker':dialogue[i+1]['speaker'],'spoken_text':dialogue[i+1]['spoken_text']} if i+1<len(dialogue) else None
 d['voice_direction']['visible_action']=Q[d['shot_id']]['acting_motion']
 d['voice_direction']['reference_sha256']=profiles[d['speaker']]['reference_sha256']
 d['voice_direction']['reference_path']=profiles[d['speaker']]['reference_path']
for s in shots:
 key=s['id'].split('-')[1]; count=sum(len(re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?",D[i]['spoken_text'])) for i in s['dialogue_ids'])
 lead=meta['lead_seconds_planned'].get(key,0); tail=meta['tail_seconds_planned'].get(key,0); gap=max(0,len(s['dialogue_ids'])-1)*meta['turn_gap_seconds_for_budget_only']
 estimate=round(count*60/meta['nominal_words_per_minute_for_budget_only']+gap,3)
 available=round(s['duration_seconds_planned']-lead-tail,3)
 s['timing_budget']={'kind':'AUTHORING_ESTIMATE_NOT_MEASURED','word_count':count,'nominal_wpm_for_budget_only':meta['nominal_words_per_minute_for_budget_only'],'action_lead_seconds_planned':lead,'action_tail_seconds_planned':tail,'estimated_speech_and_turns_seconds':estimate,'available_speech_and_turns_seconds':available,'headroom_seconds':round(available-estimate,3),'actual_speech_seconds':None,'actual_motion_seconds':None,'rule':meta['budget_rule']}
raw_events=[
('S12-P01','Look inside, please.',2,3,3,'N002','N003','제페토','피노키오','열린 문 안쪽을 바라보기','제페토가 문 안쪽을 가리킨다. 아이의 두 발은 문턱 밖.','머리와 상체를 실제로 돌려 안쪽을 살펴보고 제페토를 다시 바라본다. 문턱은 넘지 않는다.','시선 전환 및 안정 자세 완료'),
('S12-P02','Hold your hat.',4,5,5,'N006','N007','제페토','피노키오','바람에 움직이는 모자를 잡기','모자 가장자리가 약하게 들리고 제페토가 가리킨다. 안내판은 아직 서 있다.','손을 테두리에 가져가 실제로 닿아 잡고 모자를 안정시킨다. 말한 뒤 손을 내리고 다음 돌풍으로 이어진다.','손과 모자 접촉 및 모자 안정'),
('I21','Help the cricket!',11,12,14,'U010','U011','제페토','피노키오','막힌 친구를 안전하게 도와주기','친구가 다치지 않은 여유 공간, 낮게 막힌 앞 모서리·몸보다 좁은 옆 틈을 한 와이드에서 보인다. 제페토의 현재 직선 접근은 기존 옆면에 가리고 피노키오의 면은 열려 있다. 실제 승인 배경 부합 전 BLOCKED_LAYOUT.','결심→열린 면으로 이동→감속·굽힘→양손 접촉→다른 받침 접촉을 유지해 가까운 모서리 조금 들기→가까운 측면 틈으로 친구 탈출→전체 복원 경로 밖 안전 지점 확인→같은 기존 받침으로 판 안정→손 해제→안도.','친구 안전·판 안정·두 손 해제·안도 표정까지 완료'),
('S12-P03','Check on Cricket.',18,19,19,'N011','N012','피노키오','피노키오','구조 뒤 친구의 상태 살피기','제페토가 먼저 눈높이를 낮추어 귀뚜라미 얼굴과 두 발을 살피는 시범. 피노키오 자신의 확인 동작은 수용 후. 이미 위험 해소.','눈높이를 낮추고 친구 얼굴과 발을 살핀다. 귀뚜라미는 괜찮다는 몸짓과 두 발 지지를 보여 준다.','눈맞춤·친구의 안정된 두 발 확인'),
('S12-P04','Stand beside Grandpa.',20,21,21,'N013','N014','제페토','피노키오','할아버지 옆 안전한 곳에 서기','제페토가 옆 안전 발 위치를 가리킨다.','발걸음으로 제페토 옆에 합류해 안정되게 멈추고 귀뚜라미가 따라온다. 푸른빛은 이후 U017에서 시작.','셋이 안전한 위치에 정착'),
('S12-P05','Show your hands.',35,36,36,'N016','N017','제페토','피노키오','사람이 된 손을 보여 주기','변신·첫 환희·가족 포옹·귀뚜라미 축하와 포옹 해제 완료. 제페토가 자신의 두 손바닥을 보여 주는 시범을 먼저 한다. 아이는 자기 쪽에서 손을 보고, 제페토에게 펼치는 동작은 수용 후.','양팔을 자연스럽게 펼쳐 두 손을 제페토가 볼 수 있게 보여 준다.','두 손의 자세 안정·제페토 시선 도착'),
('S12-P06','Bend your fingers.',37,38,38,'N018','N019','피노키오','피노키오','손가락을 굽혀 새로운 촉감 느끼기','제페토가 자기 손가락을 굽혔다 펴서 먼저 시범을 보인다. 피노키오는 보고 질문하며 자신의 굽힘 동작은 아직 하지 않는다.','손가락을 실제 관절로 굽혔다 펴고 다른 손으로 손바닥을 가볍게 만진다.','손가락 굽힘·펴짐 및 손바닥 접촉 완료'),
('S12-P07',"Take Grandpa's hand.",39,40,40,'N022','N023','제페토','피노키오','할아버지의 손을 잡기','포옹은 끝났고 제페토가 손을 내민다. 두 손은 미접촉.','아이 손이 제페토 손에 실제 닿고 자연스럽게 감싸서 잡는다. N023~N024 대화 뒤 손을 해제한다.','공유 손 접촉 안정(해제는 N024 이후, P08 이전)'),
('S12-P08','Straighten your hat.',41,42,42,'N025','N026','제페토','피노키오','기울어진 모자 바로 쓰기','C40의 실제 손 해제 완료 뒤 제페토가 같은 기울어진 모자를 가리키고 빈 손바닥을 기운 각도에서 수평으로 바꾸는 시범. 피노키오의 모자 접촉은 수용 후.','양손을 테두리에 대고 모자 방향을 바로잡고 손을 놓는다.','같은 모자 정렬·손 해제 완료'),
('S12-P09','Wave goodbye, please.',44,45,45,'N027','U036','피노키오','피노키오','요정에게 마지막 손인사하기','요정과 아이의 눈이 마주치고 손인사 준비 상태.','피노키오가 요정에게 손을 흔들고 요정이 손인사를 되돌려 주며 물러난다. 아이가 손을 내린 뒤 윤수 쪽을 향한다.','요정과 손인사 완료·요정 거리 확보·윤수로 시선 이동')]
policy=json.load(open(O/'S11_interaction_policy.json'))
policy['learner_causality']='윤수는 화면 속 행동을 돕는다. 친구를 도울 마음은 피노키오 스스로 먼저 표현하며, I21의 도움 행동은 발화 활동 또는 보호자 진행 뒤 시작한다. 인간형 변신·마법·사랑·우정은 영어 정확도나 음량의 보상이 아니다.'
events=[]; models=[]
for idx,(eid,cue,p,r0,r1,question,resume,model_sp,actor,meaning,demo,react,done) in enumerate(raw_events,1):
 prompt=Q[f'S12-C{p:02}']; first=Q[f'S12-C{r0:02}']; last=Q[f'S12-C{r1:02}']; question='S12-'+question; resume='S12-'+resume; mid=f'S12-M{idx:03}'
 e={'id':eid,'order':idx,'legacy':eid=='I21','cue':cue,'model_job_id':mid,'question_dialogue_id':question,'question_speaker':D[question]['speaker'],'prompt_shot_id':prompt['id'],'planned_request_end_seconds':prompt['end_seconds_planned'],'planned_request_end_timecode':tc(prompt['end_seconds_planned']),'reaction_shot_ids':[f'S12-C{x:02}' for x in range(r0,r1+1)],'resume_dialogue_id':resume,'meaning_ko':meaning,'meaning_demo':demo,'actor':actor,'wait_state':prompt['state'],'reaction_description':react,'reaction_complete_condition':done,'external_model_speaker':model_sp,'runtime_trigger':'ACTUAL_QUESTION_AUDIO_ENDED','resume_trigger':'ACTUAL_REACTION_COMPLETE','runtime_status':'NOT_RUN','exact_phrase_matching':False,'pronunciation_scoring':False,'once_only':True,'model_microphone':'OFF','input_microphone':'AUTO_ARM_AFTER_ACTUAL_MODEL_END_WITH_PLATFORM_PERMISSION','actual_timing':None}
 prompt['events'].append({'id':eid,'role':'WAIT','trigger_after_dialogue':question})
 for x in range(r0,r1+1): Q[f'S12-C{x:02}']['events'].append({'id':eid,'role':'REACT','completion_before_dialogue':resume if x==r1 else None})
 preconditions={'S12-P05':['S12-U033_ACTUAL_AUDIO_ENDED','HUG_ACTUAL_RELEASE_COMPLETE','GEP_SHOW_OWN_PALMS_DEMO_COMPLETE'],'S12-P06':['S12-P05_ACTUAL_REACTION_COMPLETE','S12-N017_ACTUAL_AUDIO_ENDED','GEP_BEND_OWN_FINGERS_DEMO_COMPLETE'],'S12-P07':['S12-P06_ACTUAL_REACTION_COMPLETE','S12-N019_ACTUAL_AUDIO_ENDED','GEP_OFFER_HAND_COMPLETE_NO_CONTACT'],'S12-P08':['S12-N024_ACTUAL_AUDIO_ENDED','SHARED_HANDS_ACTUAL_RELEASE_COMPLETE','GEP_HAT_LEVEL_DEMO_COMPLETE'],'S12-P09':['S12-U035_ACTUAL_AUDIO_ENDED','FAIRY_STILL_PRESENT']}
 e['authoring_preconditions']=preconditions.get(eid,['MEANING_DEMO_COMPLETE_BEFORE_QUESTION_END'])
 e['precondition_runtime_status']='NOT_IMPLEMENTED_OR_TESTED_IN_THIS_AUTHORING_PACKAGE'
 events.append(e)
 models.append({'job_id':mid,'kind':'EXTERNAL_MODEL','event_id':eid,'speaker':model_sp,'profile_id':profiles[model_sp]['id'],'spoken_text':cue,'delivery_mode':'EXTERNAL_MODEL_CLEAR_WARM','voice_direction':{'listener':'윤수','emotion_target':'따뜻한 발화 예시','delivery_ko':f'화면의 행동({meaning})과 연결되는 가까운 목소리. 세 단어를 자연스럽게 연결하고 핵심 동사를 또렷하게. 본편의 위기·환호 강도를 그대로 쓰지 않으며 따라 하기 편한 명료한 문장으로 말한다.','direction_en':f'Model only the exact phrase "{cue}" in a warm, clear connected manner for a beginning learner. Make the action word clear and allow time to imitate. No instructions, extra words, or dramatic fear.','performance_contract':'외부 모델 전용. 캐릭터 입모양 없음. 마이크 OFF.','listening_status':'NOT_RUN'},'actual_audio_path':None,'actual_duration_seconds':None,'status':'NOT_RUN'})
beatnames=['열린 학교 문과 작은 바람','갑자기 막힌 친구','친구를 구하기로 결정','두려움을 인정하고 친구를 살피다','익숙한 파란빛과 지난 선택','마지막 마법과 인간형 변신','첫 환희·가족 포옹을 먼저 나누다','손의 감촉을 함께 살피다','약속과 마지막 인사','학교로 들어가는 진짜 아이']
beats=[{'beat_id':f'B{i+1:02}','title':name,'start_seconds_planned':shots[i*5]['start_seconds_planned'],'end_seconds_planned':shots[i*5+4]['end_seconds_planned'],'shot_ids':[s['id'] for s in shots[i*5:i*5+5]]} for i,name in enumerate(beatnames)]
protected=[{'id':'CHOICE','from':'S12-U007','to':'S12-U010','rule':'종→자발적 걱정과 결심→제페토의 질문, I21은 U010 실제 종료 후만 허용. 그 전 별도 참여 없음.'},{'id':'RESCUE_AND_THANKS','from':'I21_ACCEPTED','to':'S12-U014','rule':'구조 시작부터 감사와 우정 대화까지 새 입력·모델 없음. I21 완료 뒤 U011.'},{'id':'RECOGNITION_MAGIC_AND_FAMILY_REUNION','from':'S12-U017','to':'S12-U033','rule':'요정 등장→인정→약속→변신→U029 첫 환희→제페토 첫 응답→N020/N021 포옹과 같은 사랑→귀뚜라미 축하. 이 전체 구간에 질문·모델·입력 없음. U033 실제 종료와 포옹 해제 완료 뒤 C35의 손 탐색·P05.'},{'id':'FAIRY_PROMISE','from':'S12-U034','to':'S12-U035','rule':'마지막 축복과 자발적 답변 연속.'},{'id':'FINAL_CLOSING','from':'S12-U036','to':'S12-U044','rule':'윤수 작별→내레이션→먼 요정 축복→학교 입장→The end. 이후 참여·추가 화 없음.'}]
new=sum(r['kind']=='NEW' for r in dialogue); total=len(dialogue)
entry=json.load(open(O/'S11_EXIT_STATE.json'))
exit_state={'story_day':'D2','location':'INSIDE_SAME_OPEN_SCHOOL_DOOR_THEN_VILLAGE_WIDE','pinocchio_form':'CHAR_YOONSU_HUMAN','story_identity':'PINOCCHIO','voice_profile':'PINOCCHIO_S03_USER_LOCKED','nose':'NORMAL_HUMAN','hat':'SAME_RED_ON_HEAD','bag':'SAME_CLOSED_WITH_SAME_BOOK','footwear':'SAME_APPROVED_SHOES','cricket':'SAFE_FREE_OUTSIDE','signboard':'UPRIGHT_STABLE','teacher':'SAME_S07_SILENT_TEACHER','fairy':'DISTANT','geppetto':'OUTSIDE_WAVING_GLASSES_ON','completion':'AFTER_U044_AUDIO_AND_FINAL_CAMERA_MOTION_AND_ALL_10_EVENTS_ONCE','end_card':True}
scene={'scene':'S12','title':'친구를 구한 진짜 아이','version':meta['version'],'stage':'AUTHORING_REVISED_MEDIA_NOT_RUN','original_dialogue_count':44,'new_dialogue_count':new,'narrative_dialogue_count':total,'external_model_count':len(models),'narrative_seconds_planned':t,'minimum_narrative_seconds':360,'actual_narrative_seconds':None,'beat_count':10,'shot_count':50,'participation_count':10,'target_fps':24,'output_size_target':[1920,1080],'renderer':'REUSE_APPROVED_S02_LINEAGE_2D_ENGINE','entry_state':entry,'exit_state':exit_state,'protected_narrative':protected,'scenes':beats,'shots':shots,'dialogue':dialogue,'authoring_metadata':meta,'approval_scope':'V2 우선순위 수정 반영. 정본 문구·화자·순서 보존. 작성물 검증과 실제 미디어 검증을 구분한다. 신규 음성·원화·영상·앱 품질은 NOT_RUN.'}
dump(S/'S12_CANONICAL_LINES.json',canon);dump(S/'scene_design_v2.json',scene);dump(S/'interaction_map_v2.json',{'scene':'S12','global_policy':policy,'narrative_seconds_planned':t,'events':events,'protected_narrative':protected,'runtime_status':'NOT_RUN'});dump(V/'S12_CHARACTER_VOICE_PROFILES.json',profiles)
dump(V/'reference_registry_v2.json',{'episode':'S12','references':profiles,'claim_limit':'Available reference bytes only. No new audio, listening or actual app playback verified.'})
dump(S/'S12_VOICE_JOBS.json',{'scene':'S12','narrative_jobs':total,'external_model_jobs':10,'status':'NOT_RUN','profiles':profiles,'required_trace':['job_id','exact_spoken_text','approved_reference_sha256','engine_version_and_model_sha256','supported_acting_controls_and_actual_arguments','output_sha256','actual_sample_count','asr_for_word_check_only','blind_listening_result','app_loaded_asset_sha256'],'jobs':dialogue+models})
with (S/'S12_DIALOGUE_AND_ACTING.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.writer(f);w.writerow(['ID','kind','shot/event','speaker','spoken_text','listener','emotion_target','direction_ko','direction_en','emphasis','pronunciation','status'])
 for r in dialogue+models:
  v=r['voice_direction'];w.writerow([r['job_id'],r['kind'],r.get('shot_id',r.get('event_id')),r['speaker'],r['spoken_text'],v['listener'],v['emotion_target'],v['delivery_ko'],v['direction_en'],'; '.join(v.get('emphasis',[])),v.get('pronunciation_note','3단어 연결과 끝 자음 유지'),'NOT_RUN'])
# Reading script, with all per-line directives and event state/clock contracts.
md=[f'# 12화 최종편 — 친구를 구한 진짜 아이\n\n**상세 연기 대본 및 2D 제작 콘티 V2.0 | 2026-11-25 | 우선순위 수정본·실제 미디어 미검증**\n\n기존 승인 정본 44개 대사 그대로 + 신규 연결 대사 {new}개 = 본편 {total}개. 외부 모델 10개. 10비트·50컷. 계획 본편 {t}초({t//60}분 {t%60}초), 24fps {24*t:,}프레임. 모델·발화 대기·반복·메뉴 시간 별도. **실제 음성·원화·영상·앱 실행은 아직 NOT_RUN.**\n\n## 핵심 연출\n\n11화의 같은 아침, 열린 학교 문 바로 바깥에서 시작한다. 나무 피노키오가 친구를 구하고 솔직함과 약속을 인정받아 사람이 된다. 인간형은 반드시 승인된 윤수 캐릭터 `CHAR_YOONSU_HUMAN`; 이야기 속 이름·목소리는 피노키오 그대로다. 모자·가방·책·신발과 공간을 유지한다. 진짜 아이가 되기 전부터 제페토의 사랑과 귀뚜라미의 우정은 변하지 않는다. 변신 직후 첫 환희→제페토 응답→가족 포옹→귀뚜라미 축하를 한 번에 이어 주며, 그 뒤에 손 탐색 참여를 배치한다.\n\n원문 `U001~U044`는 한 글자도 수정하지 않았다. 추가 대사는 `N001~N{new:03}`의 고정 ID로 구분한다. 첫 환희와 포옹을 끊지 않도록 N020·N021을 손 탐색 N015~N019보다 먼저 배치했으며, 모든 문구는 보존했다. 아래 계획 컷 C01~C50은 기존 19개 승인 컷을 확장한 번호이며 각 컷에 원전 대응을 표시한다. 기존 다른 화의 원본을 수정하지 않는다.\n\n## 공통 음성 연기 지시\n\n- 영어 인용문만 실제 발화한다. 연기 지시, 감정 이름, 설명은 읽지 않는다. 원문 밖 감탄사·웃음·비명·한숨·헐떡임·단어 추가 금지.\n- 상대와 상황을 실제 합성 입력에 연결한다. 음색 참조와 감정 제어는 분리하고, 지원이 확인된 제어만 사용한다. 기존 Kokoro 낭독 뒤 속도·높낮이 보정만으로 완료 처리하지 않는다. IndexTTS2 등 감정 제어형 후보는 설치·가중치·참조·실행을 확인한 경우에만 사용한다. 현재 모델 다운로드 403은 이전 작업에서 보고된 장애이며 여기서 해결했다고 주장하지 않는다.\n- 같은 화자 내 걱정→기쁨, 긴급→안도, 감격→다정함을 크게 대비한다. 자막 없이 감정이 구분되어야 한다. 명료한 첫·끝 자음, 자연스러운 의미 단위, 원래 발음을 지킨다.\n- 피노키오·제페토 최종 S03 고정, 귀뚜라미 기존, 파란 요정 기존 C, 내레이션 기존 A. 승인 참조를 열 수 없으면 대체 음색을 만들지 않는다. 변신으로 음색 바뀌지 않음.\n- 실제 출력 후보 청취 전 자동 인식 점수나 파형 차이만으로 PASS 금지. 본편 연기와 외부 모델은 다른 전달 방식.\n\n## 시간 및 참여 계획\n\n|비트|계획 본편|내용|\n|---|---|---|']
for b in beats:md.append(f"|{b['beat_id']}|{tc(b['start_seconds_planned'])}–{tc(b['end_seconds_planned'])}|{b['title']}|")
md.append('\n|순서|계획 질문 끝|목표 발화|실제 반응|\n|---:|---|---|---|')
for e in events:md.append(f"|{e['order']} ({e['id']})|{e['planned_request_end_timecode']}|{e['cue']}|{e['meaning_ko']}|")
md.append('\n질문 실제 종료 → 본편 정지 → 예시 1회(마이크 OFF) → 실제 예시 종료 → 자동 입력 준비(권한 내) → 발화 활동 종료 또는 보호자 진행 → 실제 반응 완료 → 후속 대사. 발화 내용·정확도는 평가하지 않는다. 대기는 실제 시간에서 분리하며, 기존 검증된 감도·VAD 종료 기준을 상속하고 미확인 시간은 0으로 해석하지 않는다.\n\n## 전체 연기 대본')
for b in beats:
 md.append(f"\n## {b['beat_id']} — {b['title']} ({tc(b['start_seconds_planned'])}–{tc(b['end_seconds_planned'])})\n")
 for sid in b['shot_ids']:
  s=Q[sid];md.append(f"\n### {sid} · {tc(s['start_seconds_planned'])}–{tc(s['end_seconds_planned'])} ({s['duration_seconds_planned']}초 계획)\n\n**구도:** {s['camera']}\n\n**화면·동작:** {s['acting_motion']}\n\n**음향·경계:** {s['audio_boundary']}\n\n원전 컷 대응(기존 19컷 번호 체계): {', '.join(s['original_shot_ids'])}.\n")
  for ev in s['events']:
   e=next(e for e in events if e['id']==ev['id'])
   if ev['role']=='REACT':md.append(f"**{e['id']} 반응:** {e['reaction_description']}\n\n**반응 종료 조건:** {e['reaction_complete_condition']}. 후속 대사 `{e['resume_dialogue_id']}`는 조건 완료 뒤에만 시작한다.\n")
  for did in s['dialogue_ids']:
   d=D[did];v=d['voice_direction'];md.append(f"#### {d['speaker']} · {did} [{'원문' if d['kind']=='ORIGINAL' else '신규'}]\n\n> {d['spoken_text']}\n\n**상대·감정:** {v['listener']} / {v['emotion_target']}\n\n**연기:** {v['delivery_ko']}\n\n**합성 지시(영문):** {v['direction_en']}\n\n**강세·발음:** {' / '.join(v['emphasis'])}. {v['pronunciation_note']}\n")
   for e in events:
    if e['question_dialogue_id']==did:
     md.append(f"**🎤 {e['id']} — {e['cue']}**\n\n뜻을 보여 주는 화면: {e['meaning_demo']}\n\n대기: {s['state']['pinocchio_form_end']} / {s['state']['cricket']} / 안내판 {s['state']['signboard']}. 다음 핵심 동작은 수용 전 금지.\n\n외부 모델: {e['external_model_speaker']} `{e['model_job_id']}` 1회. 수용 뒤 {e['reaction_description']}\n\n재개: `{e['resume_dialogue_id']}`. {e['reaction_complete_condition']}을 먼저 확인한다.\n")
md.append('\n## 화면 밖 따라 말하기 모델 10개\n\n이 음성은 캐릭터 본편 입모양이나 본편 길이에 포함하지 않는다. 본편처럼 크게 연기하지 않고 윤수가 알아듣기 쉬운 따뜻한 연결 발음으로 말한다.\n')
for m in models:md.append(f"### {m['job_id']} · {m['speaker']} ({m['event_id']})\n\n> {m['spoken_text']}\n\n{m['voice_direction']['delivery_ko']}\n")
md.append('\n## 마지막 완료 조건\n\n학교 입장이 실제로 끝나고 U044 음성이 종료되며 마지막 카메라 이동까지 끝나면 스토리를 한 번만 완료한다. 10개 참여의 실제 종료 상태를 검증한다. V2 대본·제작 데이터의 수정 내용과 실제 미디어 제작 결과는 구분한다. 실제 음원 청취·원화 정합·영상렌더·앱 재생은 별도 검증 전까지 NOT_RUN이다.\n')
(S/'S12_ACTING_SCRIPT.md').write_text('\n'.join(md),encoding='utf-8')
# Compact cues sheet.
cue_lines=['# S12 윤수 참여 10회','계획 질문 끝은 실제 모델 및 대기 제외 본편 시계. 실제 질문 끝 이벤트로 트리거.','|순번|이벤트|계획 질문 끝|모델|질문 ID|반응 컷|재개 ID|','|---|---|---|---|---|---|---|']
for e in events:cue_lines.append(f"|{e['order']}|{e['id']}|{e['planned_request_end_timecode']}|{e['cue']}|{e['question_dialogue_id']}|{', '.join(e['reaction_shot_ids'])}|{e['resume_dialogue_id']}|")
(S/'S12_YOONSU_CUES.md').write_text('\n'.join(cue_lines)+'\n',encoding='utf-8')
# Independent structural checks (actual media deliberately excluded).
checks=[]
def check(name,ok,detail):checks.append({'test':name,'status':'PASS' if ok else 'FAIL','detail':detail}); assert ok,(name,detail)
actual=[{'dialogue_id':d['dialogue_id'],'speaker':d['speaker'],'text':d['spoken_text']} for d in dialogue if d['kind']=='ORIGINAL']
check('source_original_44_exact_and_ordered',actual==canon,len(actual))
check('new_ids_complete_and_unique',sorted(d['dialogue_id'] for d in dialogue if d['kind']=='NEW')==[f'S12-N{i:03}' for i in range(1,28)],{'count':new,'stable_ids_reordered_for_unbroken_reunion':True})
check('unique_dialogue_ids',len(D)==total,total)
check('50_cuts_10_beats',len(shots)==50 and len(beats)==10 and [s['id'] for s in shots]==[f'S12-C{i:02}' for i in range(1,51)],len(shots))
check('all_19_original_cuts_mapped',set(x for s in shots for x in s['original_shot_ids'])==set(f'S12-C{i:02}' for i in range(1,20)),19)
source_shots={}
for m in re.finditer(r'^\|(S12-C\d{2})\|[^|]+\|S12-U(\d{3})–S12-U(\d{3})\|', (O/'01_STEP2_PRODUCTION_STORYBOARD_SPEC.md').read_text(), re.M):
 for i in range(int(m[2]),int(m[3])+1): source_shots[f'S12-U{i:03}']=m[1]
check('canonical_source_cut_association',len(source_shots)==44 and all(source_shots[d['dialogue_id']] in Q[d['shot_id']]['original_shot_ids'] for d in dialogue if d['kind']=='ORIGINAL'),len(source_shots))
check('contiguous_narrative_clock',shots[0]['start_seconds_planned']==0 and all(a['end_seconds_planned']==b['start_seconds_planned'] for a,b in zip(shots,shots[1:])) and shots[-1]['end_seconds_planned']==t,t)
check('minimum_360_seconds_planned',t>=360,{'planned':t,'actual':None})
check('dialogue_shot_coverage',[d for s in shots for d in s['dialogue_ids']]==[d['dialogue_id'] for d in dialogue],total)
check('10_unique_events_one_legacy_I21',len(events)==10 and len({e['id'] for e in events})==10 and sum(e['legacy'] for e in events)==1,10)
check('10_three_word_models',all(len(re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?",e['cue']))==3 for e in events),[e['cue'] for e in events])
for e in events:
 p=Q[e['prompt_shot_id']]; r=Q[e['reaction_shot_ids'][0]]; re_=Q[e['reaction_shot_ids'][-1]]
 check(e['id']+'_question_react_resume',p['dialogue_ids'][-1]==e['question_dialogue_id'] and p['end_seconds_planned']==r['start_seconds_planned'] and D[e['resume_dialogue_id']]['shot_id'] in [re_['id'],f"S12-C{int(re_['id'][-2:])+1:02}"] and D[e['question_dialogue_id']]['speaker']==e['question_speaker'],{'question':e['question_dialogue_id'],'react':e['reaction_shot_ids'],'resume':e['resume_dialogue_id']})
check('legacy_I21_lock',events[2]['id']=='I21' and events[2]['cue']=='Help the cricket!' and events[2]['question_dialogue_id']=='S12-U010' and events[2]['resume_dialogue_id']=='S12-U011',events[2]['reaction_shot_ids'])
check('magic_after_U027',D['S12-U027']['shot_id']=='S12-C29' and D['S12-U028']['shot_id']=='S12-C30' and all(s['state']['pinocchio_form_end']=='WOODEN' for s in shots[:29]) and all(s['state']['pinocchio_form_end']=='CHAR_YOONSU_HUMAN' for s in shots[29:]),'C30 transition')
check('form_identity_locked',all(d['profile_id']==profiles['피노키오']['id'] for d in dialogue if d['speaker']=='피노키오'),'one profile')
check('rescue_wait_states',events[2]['wait_state']['cricket']=='BLOCKED_UNINJURED' and events[2]['wait_state']['pinocchio_form_end']=='WOODEN' and events[2]['wait_state']['school_door']=='OPEN' and Q['S12-C14']['state']['cricket']=='SAFE_FREE' and Q['S12-C14']['state']['signboard']=='RETURNED_UPRIGHT_STABLE','I21')
check('protected_question_ranges',not any(int(e['prompt_shot_id'][-2:]) in list(range(9,11))+list(range(12,17))+list(range(21,35))+[43]+list(range(45,51)) for e in events),'choice, rescue, unbroken recognition/magic/reunion, blessing, ending')
order=[d['dialogue_id'] for d in dialogue]
check('F01_joy_immediately_after_transformation',order[order.index('S12-U028')+1:order.index('S12-U033')+1]==['S12-U029','S12-U030','S12-U031','S12-U032','S12-N020','S12-N021','S12-U033'] and Q['S12-C30']['end_seconds_planned']==Q['S12-C31']['start_seconds_planned'],'no model or participation inside first family reunion')
check('F01_hand_exploration_after_family_reunion',order.index('S12-U033')<order.index('S12-N015')<order.index('S12-N016') and next(e for e in events if e['id']=='S12-P05')['prompt_shot_id']=='S12-C35','P05 first possible after U033 and actual hug release')
check('F05_fairy_reference_resolved',profiles['파란 요정']['id']=='BLUE_FAIRY_EXISTING_C' and profiles['파란 요정']['reference_sha256']=='c65e44b9c4d221c1fe9052ff201a3d3a0f5bc867c29460130fe2944f59c5965b','same approved C bytes as S10; no synthesis/listening claim')
check('F09_concrete_helper_demonstrations',all('제페토' in next(e for e in events if e['id']==eid)['meaning_demo'] and '시범' in next(e for e in events if e['id']==eid)['meaning_demo'] for eid in ['S12-P03','S12-P05','S12-P06','S12-P08']),'helper demonstrates; Pinocchio result stays after acceptance')
check('F09_hand_release_before_hat_question',D['S12-N024']['shot_id']=='S12-C40' and D['S12-N025']['shot_id']=='S12-C41' and '손 해제 완료' in Q['S12-C40']['audio_boundary'],'separate release and next demonstration/question')
check('planning_speech_budget_positive',all(s['timing_budget']['headroom_seconds']>=0 for s in shots if s['dialogue_ids']),{s['id']:s['timing_budget']['headroom_seconds'] for s in shots if s['dialogue_ids']})
check('question_cut_has_no_forced_post_question_tail',all(Q[e['prompt_shot_id']]['timing_budget']['action_tail_seconds_planned']==0 for e in events),'question audio ended is the boundary, not planned timer')
check('F09_event_preconditions_explicit','HUG_ACTUAL_RELEASE_COMPLETE' in next(e for e in events if e['id']=='S12-P05')['authoring_preconditions'] and 'SHARED_HANDS_ACTUAL_RELEASE_COMPLETE' in next(e for e in events if e['id']=='S12-P08')['authoring_preconditions'],'authoring contract; not runtime test')
layout=json.loads((A/'S12_RESCUE_LAYOUT_V2.json').read_text(encoding='utf-8'))
check('F10_layout_contract_is_conditional',layout['status']=='CONDITIONAL_DESIGN_REQUIRES_APPROVED_ART' and 'BLOCKED_LAYOUT' in Q['S12-C06']['acting_motion'] and '현재' in Q['S12-C10']['acting_motion'] and '측면' in Q['S12-C13']['acting_motion'],'concrete layout is not approved art or rendered motion evidence')
check('honesty_today_addition',D['S12-N009']['spoken_text']=='Yes. I was scared.' and int(D['S12-N009']['shot_id'][-2:])<int(D['S12-U040']['shot_id'][-2:]),'D2 confession')
check('entry_exit_continuity',entry['pinocchio_form']=='WOODEN' and entry['school_signboard']=='SMALL_WOODEN_BOARD_STANDING' and entry['hands_joined']==False and entry['school_door']=='OPEN_BY_EXISTING_S07_SILENT_TEACHER' and exit_state['pinocchio_form']=='CHAR_YOONSU_HUMAN','S11 exact state copied')
check('ending_after_entry',D['S12-U044']['shot_id']=='S12-C50' and Q['S12-C49']['state']['school_entry']=='CROSSES_THRESHOLD' and Q['S12-C50']['state']['school_entry']=='INSIDE' and dialogue[-1]['spoken_text']=='The end.','final entry before last line')
check('voice_direction_all_jobs',all(r['voice_direction']['direction_en'] and r['voice_direction']['delivery_ko'] and r['profile_id'] in [p['id'] for p in profiles.values()] for r in dialogue+models),len(dialogue)+len(models))
check('original_sources_sha256',sha(O/'01_STORY_MASTER_V1_1.md')=='eb5ca04f5e4302d4a71726f1a24b6cead5cec682b96baee600f6eef8ee951d3e' and sha(O/'01_STEP2_PRODUCTION_STORYBOARD_SPEC.md')=='b5ff72a4e6d889006eacc669a7c15c68a739ca1805117b8c79d79d4ab5181610','source bytes copied')
check('no_actual_media_claim',all(r['actual_audio_path'] is None and r['status']=='NOT_RUN' for r in dialogue+models) and scene['actual_narrative_seconds'] is None,'all synthesis/render/runtime NOT_RUN')
dump(E/'AUTHORING_VALIDATION.json',{'scope':'STRUCTURAL_AUTHORING_ONLY','pass_count':len(checks),'fail_count':0,'tests':checks,'media_status':{'voice':'NOT_RUN','listening':'NOT_RUN','approved_human_art':'REQUIRE_RESOURCE_VERIFICATION','sprites':'NOT_RUN','video':'NOT_RUN','app':'NOT_RUN','device':'NOT_RUN'}})
print(json.dumps({'original':44,'new':new,'narrative':total,'models':10,'total_jobs':total+10,'seconds':t,'frames':t*24,'shots':len(shots),'passes':len(checks),'events':[(e['id'],e['planned_request_end_timecode'],e['cue']) for e in events]},ensure_ascii=False,indent=2))
