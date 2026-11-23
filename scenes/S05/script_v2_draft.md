# S05 상세 대본 — 수정본·문장별 음성 연기 V2.1

**본편 계획:** 472초 / 50컷 / 참여10회. 입력 대기·모델 예시는 별도 시간이다. 실제 영상·음성 길이 NOT_RUN.
**수정 범위:** 사용자 요청에 따른 검토 지적 수정과 모든 발화의 연기 지시. 1·2화 완료본과 승인 성우 참조는 유지한다.
**성우 기준:** [전체 캐릭터 음색·연기 기준](../../docs/series_v2/VOICE_PERFORMANCE_BIBLE_V2_1.md). 영어 대사만 읽고 연기 지시는 발화하지 않는다.
**기계용 제작표:** [voice_direction_plan.json](voice_direction_plan.json) · [voice_direction_sheet.csv](voice_direction_sheet.csv)

## 비트 시간표

|비트|내용|본편 구간|참여|
|---|---|---|---|
|B01|소리 쪽으로 기울어지는 귀|00:00–00:42|S05-P01|
|B02|작은 북과 피리 소리|00:42–01:29|I08|
|B03|알고 있는 학교 길|01:29–02:12|S05-P02|
|B04|낮은 가지 아래로|02:12–02:57|S05-P03|
|B05|얼굴에 닿는 잎을 살며시|02:57–03:41|S05-P04|
|B06|나무 뒤의 빨간 천막|03:41–04:34|I09|
|B07|손끝에 남아 있는 약속|04:34–05:20|S05-P05|
|B08|작은 관객이 지나갈 자리|05:20–06:12|S05-P06|
|B09|책가방도 함께 자리를 잡기|06:12–07:02|S05-P07|
|B10|한 발 뒤에서 시작을 기다리다|07:02–07:52|S05-P08|

## B01. 소리 쪽으로 기울어지는 귀

**목적:** 4화의 미확인 소리를 같은 자리에서 받아, 걸음 소리를 멈추고 듣는 몸짓을 익힌다. 음악의 근원은 아직 가려 둔다.

**연속성:** S04 B10-C05와 동일한 아침·길·진행 방향. 모자 착용, 책이 든 가방, 마른 신발, 정상 길이 코. 귀뚜라미는 피노키오 옆 땅. 먼 학교 지붕은 배경에 남긴다.

### B01-C01 · 00:00–00:07 · NARRATIVE

**카메라:** WS 35mm · S04 마지막 프레임에서 연속

**자율 행동·연출:** S04의 귀 기울이던 움직임을 이어 피노키오의 들린 발이 땅에 닿고 가방이 한 번 가라앉는다. 카메라는 같은 축을 유지한다. 미확인 소리만 이어 받고 전화 내레이션을 반복하지 않는다.

**시간 배정:** 발화 전 행동 0.6초 / 발화 뒤 행동 0.8초. 대사·쉼·지정 행동 계획 합계 5.69초. 실제 합성 길이는 별도 확인.

**[S05-U001 · ORIGINAL #1] 피노키오:** “Cricket, what's that sound?”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 바로 곁 친구에게 처음 들린 소리를 묻는다 / 감정: 놀람에서 조용한 호기심으로  
**말하는 방식:** 걸음이 멎는 순간 가까운 친구를 부르고 sound에서만 호기심을 올린다. 멀리 소리치는 호출이 아니다.  
**속도·쉼 계획:** 108단어/분, 에너지 3/5, 앞 120ms / 뒤 260ms. 강조: Cricket · sound. Cricket, 뒤 120ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Ask the companion beside you as the foot settles. Lift the question on sound with fresh curiosity, without calling across a distance.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 놀라 비명을 지르거나 이미 음악임을 아는 확신

**[S05-U002 · ORIGINAL #2] 귀뚜라미:** “Listen carefully.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 서둘러 답하지 않고 귀를 기울이게 돕는다 / 감정: 차분한 집중  
**말하는 방식:** 비밀을 들려주는 친구처럼 음량을 조금 낮추고 carefully를 부드럽게 길게 한다. 꾸짖는 명령으로 누르지 않는다.  
**속도·쉼 계획:** 110단어/분, 에너지 2/5, 앞 140ms / 뒤 340ms. 강조: carefully. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Lower the volume slightly as a friend helping him notice something. Give carefully patient attention rather than a stern command.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 교사의 훈계조 또는 과장된 속삭임

### B01-C02 · 00:07–00:15 · NARRATIVE

**카메라:** MS 50mm · 발에서 얼굴로 틸트

**자율 행동·연출:** 피노키오가 자신의 나무 신발을 내려다보며 S05-N001을 말한다. 귀뚜라미의 S05-N002 안내를 받은 뒤 두 발을 가지런히 멈춘다. 귀뚜라미도 두 걸음 다가와 고개를 기울인다. 눈·호흡·가방의 잔운동은 자율 연기이며 대기 루프가 아니다.

**시간 배정:** 발화 전 행동 0.5초 / 발화 뒤 행동 1.4초. 대사·쉼·지정 행동 계획 합계 7.05초. 실제 합성 길이는 별도 확인.

**[S05-N001 · NEW] 피노키오:** “My feet are noisy.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 자신의 발소리가 작은 소리를 가렸음을 알아챈다 / 감정: 뜻밖의 깨달음과 작은 머쓱함  
**말하는 방식:** 신발을 보며 feet를 짚고 noisy 끝에 작게 웃음기만 담는다. 웃음소리나 새 감탄사는 덧붙이지 않는다.  
**속도·쉼 계획:** 110단어/분, 에너지 3/5, 앞 120ms / 뒤 260ms. 강조: feet · noisy. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Notice your own shoes with a small, sheepish smile in the voice. Land noisy as a discovery; add no laugh or extra interjection.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 스스로를 혼내는 죄책감 또는 발을 의인화한 다른 목소리

**[S05-N002 · NEW] 귀뚜라미:** “Then let them rest.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 발을 잠깐 멈추면 들을 수 있다는 쉬운 방법을 제안한다 / 감정: 온화한 재치  
**말하는 방식:** Then은 앞말을 바로 받으며 가볍게, rest는 안심시키듯 둔다. 발이 멈춘 뒤 훈계하는 말처럼 늦추지 않는다.  
**속도·쉼 계획:** 112단어/분, 에너지 2/5, 앞 130ms / 뒤 320ms. 강조: rest. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Pick up his observation lightly on Then and offer rest as a simple, reassuring solution. Keep the gentle wit conversational.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 수면을 유도하는 나른한 톤 또는 단호한 제지

### B01-C03 · 00:15–00:24 · PROMPT

**카메라:** CU 65mm · 손과 귀, 질문

**자율 행동·연출:** 피노키오가 한 손을 귀 옆까지 올렸다 방향을 확인한다. 귀뚜라미의 앞다리 시범을 보고 반대 손도 준비한다. 마지막 질문 오디오가 끝나는 C03 종료 경계에서만 외부 참여 대기로 전환한다.

**시간 배정:** 발화 전 행동 1.0초 / 발화 뒤 행동 0초. 대사·쉼·지정 행동 계획 합계 8.62초. 실제 합성 길이는 별도 확인.

**[S05-N003 · NEW] 귀뚜라미:** “Bring your hands up.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 양손을 귀 쪽으로 준비하도록 안내한다 / 감정: 또렷한 도움  
**말하는 방식:** 귀뚜라미의 앞다리 시범에 맞춰 hands와 up을 이어 붙여 말한다. 단어마다 끊어 읽지 않는다.  
**속도·쉼 계획:** 114단어/분, 에너지 2/5, 앞 100ms / 뒤 230ms. 강조: hands · up. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Guide the small upward movement shown by your forelegs. Connect hands up smoothly instead of spelling out separate commands.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 훈련 구령처럼 hands와 up을 따로 외치기

**[S05-N004 · NEW] 피노키오:** “Like this?”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 자기가 준비한 손 위치가 맞는지 확인한다 / 감정: 열린 기대  
**말하는 방식:** 손을 든 채 상대 눈을 살피는 짧은 진짜 질문이다. this를 살짝 올리고 답을 강요하는 불안은 넣지 않는다.  
**속도·쉼 계획:** 106단어/분, 에너지 2/5, 앞 100ms / 뒤 230ms. 강조: this. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Look to the companion for confirmation while holding the hands ready. Give this a small, genuine questioning lift.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 관객에게 정답을 묻는 진행자 말투

**[S05-N005 · NEW] 피노키오:** “Yoonsu, how can I listen better?”

**음성 연기:** PINOCCHIO_A → 윤수 / 의도: 더 잘 들을 몸짓을 함께 시도하자고 청한다 / 감정: 친근한 부탁  
**말하는 방식:** 윤수를 한 번 다정히 부른 뒤 listen better를 한 덩어리로 묻는다. 이미 답을 아는 시험 질문처럼 또박또박 쪼개지 않는다.  
**속도·쉼 계획:** 105단어/분, 에너지 3/5, 앞 150ms / 뒤 0ms. 강조: listen better. Yoonsu, 뒤 140ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Invite Yoonsu to help you listen better, addressing a friend rather than testing a pupil. Keep the final question open and natural.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 답을 재촉하는 상승조 또는 목표 문장을 본편에 추가 발화

**윤수 참여 1/10 · S05-P01 · 본편 밖 입력 대기**

- 질문 종료 시점: 24초. 본편 시계를 멈춘다.
- 첫 모델 예시: **“Cup your ears!”** — 피노키오의 같은 고정 목소리.
- 모델 예시를 한 번 들려준 뒤 마이크를 켠다. 정확한 단어·발음 채점은 하지 않는다.
- 보호자 터치는 예시를 생략하고 반응으로 진행할 수 있다. 무응답5초 뒤 다시 듣기/터치를 제시한다.
- 시범: 피노키오가 양손을 귀 옆까지 올리는 준비를 보이고 귀뚜라미가 앞다리로 귀 기울이는 방향을 시범. 소리의 근원은 화면 밖.
- 대기 상태: 양손은 귀에 닿기 직전. 숲이 아니라 기존 학교 길가, 천막 전면 미공개.
- 입력 뒤 한 번 실행: 손바닥을 귀 뒤로 모음→상체를 소리 쪽으로 조금 기울임→발소리가 사라진 틈에서 눈을 움직여 듣기.
- 첫 재개: S05-N006 “Now I can hear better.”

**예시 음성 연기:**

**음성 연기:** PINOCCHIO_A → 윤수(본편 밖 따라 말하기 예시) / 의도: 손을 귀 뒤로 모으라는 세 단어를 처음 들려준다 / 감정: 호기심을 돕는 다정함  
**말하는 방식:** Cup을 손 모양과 연결해 부드럽게 시작하고 your ears를 이어 말한다. 세 단어를 따로 시험하듯 읽지 않는다.  
**속도·쉼 계획:** 82단어/분, 에너지 2/5, 앞 120ms / 뒤 360ms. 강조: Cup · ears. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Offer Cup your ears as one gentle, connected phrase tied to the visible hands. Model an easy invitation, not three separate test words.  
**피할 연기:** 세 단어를 낱말 시험처럼 끊거나 큰 소리로 채점하기; 본편 인물의 지식·입모양·발견 반응을 먼저 바꾸기

### B01-C04 · 00:24–00:35 · REACT

**카메라:** CU→MS 50mm · 손 모으기 반응

**자율 행동·연출:** 응답 또는 터치 후 양손을 귀 뒤에 모으고, 팔꿈치·어깨를 자연스럽게 내리면서 상체를 아주 조금 기울인다. 눈동자는 잎 사이를 찾되 소리의 정체는 단정하지 않는다.

**시간 배정:** 발화 전 행동 2.8초 / 발화 뒤 행동 1.0초. 대사·쉼·지정 행동 계획 합계 10.48초. 실제 합성 길이는 별도 확인.

**[S05-N006 · NEW] 피노키오:** “Now I can hear better.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미와 윤수 / 의도: 손을 모은 뒤 실제로 소리가 또렷해진 결과를 말한다 / 감정: 조용한 기쁨  
**말하는 방식:** 귀에 손을 모은 반응이 끝난 뒤 작은 미소로 Now를 시작한다. better에 가벼운 만족을 담고 소리보다 크게 외치지 않는다.  
**속도·쉼 계획:** 108단어/분, 에너지 3/5, 앞 130ms / 뒤 280ms. 강조: hear better. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** After the cupping action finishes, let Now carry a quiet discovery. Smile gently on better and stay softer than a celebratory shout.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 문제 정답을 맞힌 것처럼 환호하기

**[S05-N007 · NEW] 귀뚜라미:** “Keep your eyes on the path.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 듣는 중에도 걷는 길을 살피게 한다 / 감정: 다정한 주의  
**말하는 방식:** eyes에서 시선을 길로 돌릴 계기를 주고 path를 차분하게 닫는다. 호기심 자체를 금지하는 어조는 쓰지 않는다.  
**속도·쉼 계획:** 116단어/분, 에너지 2/5, 앞 130ms / 뒤 260ms. 강조: eyes · path. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Give eyes a clear cue to look down the path, ending calmly. Protect his attention to the route without scolding his curiosity.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 음악을 듣지 말라는 금지처럼 들리는 날카로움

### B01-C05 · 00:35–00:42 · NARRATIVE

**카메라:** OTS 40mm · 잎 너머의 빛

**자율 행동·연출:** 피노키오의 시선이 잎에 걸린 작은 천 조각을 따라간다. 가려진 붉은 색의 단편만 허용하며, 악기·무대·인형은 보이지 않는다. 다음 비트에 쓸 북과 피리 모티프가 바람 너머로 들린다.

**시간 배정:** 발화 전 행동 0.8초 / 발화 뒤 행동 2.0초. 대사·쉼·지정 행동 계획 합계 5.53초. 실제 합성 길이는 별도 확인.

**[S05-N008 · NEW] 피노키오:** “It's beyond those leaves.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 잎 너머에서 소리가 나는 것 같다고 가늠한다 / 감정: 아직 확신 없는 관찰  
**말하는 방식:** beyond를 살짝 늘이며 잎 너머를 살핀다. leaves에서 확정 발표하지 말고 찾는 마음을 남긴다.  
**속도·쉼 계획:** 107단어/분, 에너지 2/5, 앞 170ms / 뒤 320ms. 강조: beyond · leaves. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Trace the sound beyond the leaves with a tentative, attentive voice. Leave a little searching uncertainty rather than announcing the source.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 천막이나 인형극을 이미 발견한 흥분

## B02. 작은 북과 피리 소리

**목적:** 원본 I08을 보존해 막연한 소리를 음악으로 알아듣는 순간을 만든다. 듣기 결과가 다음 선택의 원인이 된다.

**연속성:** B01 위치 그대로. I08 전까지 천막 전체·무대·악기 연주자는 미공개. 음악은 학교 종소리와 확실히 다른 음색이고, 완주 시간과 무관하게 동일한 짧은 모티프만 사용.

### B02-C01 · 00:42–00:49 · NARRATIVE

**카메라:** MS 50mm · 청각에 대한 얼굴 반응

**자율 행동·연출:** 낮은 북 한 번에 피노키오 눈썹이 들리고 높은 피리 한 구절에 시선이 옆으로 움직인다. 손과 고개가 다른 박자로 과장되게 흔들리지 않도록 실제 듣는 반응을 준다.

**시간 배정:** 발화 전 행동 0.6초 / 발화 뒤 행동 1.0초. 대사·쉼·지정 행동 계획 합계 6.34초. 실제 합성 길이는 별도 확인.

**[S05-N009 · NEW] 피노키오:** “A tiny tap... and a high sound.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 낮은 두드림과 높은 소리를 구별해 묘사한다 / 감정: 집중하는 신기함  
**말하는 방식:** tiny tap은 작게 짚고 실제 소리를 듣는 짧은 틈 뒤 high sound를 조금 밝게 올린다. 의성어를 추가하지 않는다.  
**속도·쉼 계획:** 104단어/분, 에너지 2/5, 앞 160ms / 뒤 280ms. 강조: tiny tap · high sound. tap... 뒤 260ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Place tiny tap lightly, pause to notice the sound, then brighten high sound. Describe what you hear without adding drum noises or extra words.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 음높이를 노래로 부르거나 새로운 악기 이름을 말하기

### B02-C02 · 00:49–00:59 · NARRATIVE

**카메라:** TWO SHOT 40mm · 대사 뒤 짧은 음악 구간

**자율 행동·연출:** 귀뚜라미가 먼저 S05-N010으로 짧게 안내한다. 피노키오가 눈을 잠깐 감아 듣다가 같은 소리를 잡아 S05-N011을 말하고 눈을 뜬다. 두 발화 뒤에는 북·피리만 들리는 3초의 한 번뿐인 음악 구간을 둔다. 이 구간을 반복해 길이를 늘리지 않는다.

**시간 배정:** 발화 전 행동 0.3초 / 발화 뒤 행동 3.0초. 대사·쉼·지정 행동 계획 합계 9.59초. 실제 합성 길이는 별도 확인.

**[S05-N010 · NEW] 귀뚜라미:** “Close your eyes for a moment.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 잠깐 눈을 감아 청각에 집중하도록 권한다 / 감정: 차분한 안내  
**말하는 방식:** Close your eyes는 이어서 부드럽게, for a moment는 부담을 덜어 주듯 짧게 둔다. 잠재우는 속삭임은 피한다.  
**속도·쉼 계획:** 108단어/분, 에너지 2/5, 앞 130ms / 뒤 260ms. 강조: eyes · a moment. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Offer a brief listening exercise gently, connecting Close your eyes and making for a moment reassuringly small. Stay alert, not sleepy.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 최면이나 잠자리 안내처럼 늘어지는 말투

**[S05-N011 · NEW] 피노키오:** “There it is again.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 같은 소리가 다시 난 것을 즉시 알아본다 / 감정: 작은 반가움  
**말하는 방식:** 눈을 감고 듣다 다시 포착한 느낌으로 There를 가볍게 꺼낸다. again만 살짝 강조하고 새 발견의 과한 환호는 없다.  
**속도·쉼 계획:** 108단어/분, 에너지 3/5, 앞 110ms / 뒤 230ms. 강조: again. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Catch the returning sound with an immediate little lift on There. Touch again lightly, as recognition of the same motif.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 음악의 정체를 이미 설명하는 확신

### B02-C03 · 00:59–01:09 · PROMPT

**카메라:** MS 50mm · 귀뚜라미 질문

**자율 행동·연출:** 귀뚜라미가 윤수 쪽으로 몸을 돌린 후 소리 쪽을 다시 본다. 피노키오는 입을 다물고 듣는다. 원본 U003, U004를 순서대로 발화하고 U004 종료 시점에서 외부 대기.

**시간 배정:** 발화 전 행동 2.2초 / 발화 뒤 행동 0초. 대사·쉼·지정 행동 계획 합계 8.36초. 실제 합성 길이는 별도 확인.

**[S05-U003 · ORIGINAL #3] 귀뚜라미:** “Yoonsu, can you hear it too?”

**음성 연기:** CRICKET_DESIGN_V1 → 윤수 / 의도: 화면 밖 친구도 같은 소리를 들었는지 함께 확인한다 / 감정: 포함시키는 따뜻함  
**말하는 방식:** Yoonsu 뒤 짧게 공간을 주고 too를 다정히 올린다. 다음 질문을 위한 연결이므로 큰 결론처럼 닫지 않는다.  
**속도·쉼 계획:** 110단어/분, 에너지 3/5, 앞 130ms / 뒤 260ms. 강조: hear · too. Yoonsu, 뒤 100ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Include Yoonsu in the shared listening. Give too a warm lift and leave the exchange open for the following short question.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 청력 시험을 진행하는 검사자 말투

**[S05-U004 · ORIGINAL #4] 귀뚜라미:** “What do you hear?”

**음성 연기:** CRICKET_DESIGN_V1 → 윤수 / 의도: 들은 것을 편하게 표현할 차례를 건넨다 / 감정: 기다릴 준비가 된 호기심  
**말하는 방식:** What을 세게 치지 말고 hear에 부드러운 질문의 중심을 둔다. 문장 끝나면 즉시 본편 밖 예시로 넘어갈 수 있게 불필요한 후렴을 넣지 않는다.  
**속도·쉼 계획:** 108단어/분, 에너지 2/5, 앞 180ms / 뒤 0ms. 강조: hear. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Offer an open turn, centering hear rather than punching What. Finish cleanly for the external model example, with no added prompt or echo.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 정답을 요구하는 시험관 억양

**윤수 참여 2/10 · I08 · 본편 밖 입력 대기**

- 질문 종료 시점: 69초. 본편 시계를 멈춘다.
- 첫 모델 예시: **“I hear music!”** — 귀뚜라미의 같은 고정 목소리.
- 모델 예시를 한 번 들려준 뒤 마이크를 켠다. 정확한 단어·발음 채점은 하지 않는다.
- 보호자 터치는 예시를 생략하고 반응으로 진행할 수 있다. 무응답5초 뒤 다시 듣기/터치를 제시한다.
- 시범: 귀뚜라미가 몸을 세우고 소리를 듣는 몸짓, 피노키오의 손은 귀 근처. 북의 낮은 소리와 피리의 높은 소리를 짧게 번갈아 들려주되 근원은 공개하지 않는다.
- 대기 상태: 음악만 들리는 상태, 천막 전면은 큰 나무 뒤. 질문 종료 뒤에만 VAD 시작.
- 입력 뒤 한 번 실행: 귀뚜라미 귀 기울이기→피노키오 고개 돌리기→나뭇잎 움직이기. 같은 음악이 조금 또렷해진다.
- 첫 재개: S05-U005 “It's coming from the village square.”

**예시 음성 연기:**

**음성 연기:** CRICKET_DESIGN_V1 → 윤수(본편 밖 따라 말하기 예시) / 의도: 들은 소리를 음악이라고 말하는 짧은 예시를 준다 / 감정: 조용한 발견의 기쁨  
**말하는 방식:** I hear는 편하게 이어서 music에 작은 미소를 둔다. 화면 속 귀뚜라미가 먼저 정답을 알아낸 연기는 하지 않는다.  
**속도·쉼 계획:** 84단어/분, 에너지 2/5, 앞 120ms / 뒤 360ms. 강조: hear · music. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Model a relaxed I hear, smiling slightly on music. This is extra-story guidance, not Cricket announcing a discovery inside the scene.  
**피할 연기:** 세 단어를 낱말 시험처럼 끊거나 큰 소리로 채점하기; 본편 인물의 지식·입모양·발견 반응을 먼저 바꾸기

### B02-C04 · 01:09–01:21 · REACT

**카메라:** REACT 50mm · 귀뚜라미→피노키오→잎

**자율 행동·연출:** 정해진 순서로 귀뚜라미가 먼저 귀를 기울이고, 피노키오가 고개를 돌리고, 길가 잎이 움직인다. 근원이 같은 모티프의 믹스만 또렷해진다. 반응 직후 첫 발화는 원본 U005이며 U006이 뒤따른다.

**시간 배정:** 발화 전 행동 3.5초 / 발화 뒤 행동 0.6초. 대사·쉼·지정 행동 계획 합계 10.46초. 실제 합성 길이는 별도 확인.

**[S05-U005 · ORIGINAL #5] 귀뚜라미:** “It's coming from the village square.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 소리가 오는 광장 쪽 방향을 알려 준다 / 감정: 차분한 확신  
**말하는 방식:** I08 반응이 끝난 다음 coming from으로 방향을 잡고 village square를 명료하게 말한다. 새로운 장소 소개 내레이션처럼 거창하게 읽지 않는다.  
**속도·쉼 계획:** 112단어/분, 에너지 3/5, 앞 130ms / 뒤 300ms. 강조: village square. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** After the listening reaction, locate the sound through coming from and clearly name the village square. Speak as a companion giving a direction.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 인형극까지 발견했다고 암시하는 공연 안내 톤

**[S05-U006 · ORIGINAL #6] 피노키오:** “Music! I love music!”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 음악임을 알아채고 좋아하는 마음이 솟는다 / 감정: 발견에서 들뜬 즐거움으로  
**말하는 방식:** 첫 Music은 새로 알아챈 밝은 탄성, 짧은 숨 뒤 I love music은 자기 취향을 말하는 행복으로 바꾼다. 두 문장을 같은 크기로 외치지 않는다.  
**속도·쉼 계획:** 114단어/분, 에너지 4/5, 앞 100ms / 뒤 300ms. 강조: Music · love. Music! 뒤 210ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Let the first Music be a bright recognition; after a tiny breath, make I love music a personal, happy confession. Vary the two phrases instead of shouting both.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 아기처럼 날카로운 고음이나 성인 뮤지컬 진행자 발성

### B02-C05 · 01:21–01:29 · NARRATIVE

**카메라:** LOW MS 40mm · 들썩이는 발과 학교 방향

**자율 행동·연출:** 피노키오가 발끝으로 박자를 한 번 짚었다가 체중을 다시 두 발에 싣는다. 귀뚜라미가 음악 방향과 별개인 학교 길 쪽으로 시선을 준다. 첫 충동과 아직 남은 목적을 한 화면에 둔다.

**시간 배정:** 발화 전 행동 1.0초 / 발화 뒤 행동 1.6초. 대사·쉼·지정 행동 계획 합계 6.81초. 실제 합성 길이는 별도 확인.

**[S05-N012 · NEW] 피노키오:** “I can feel it in my feet.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 발끝이 박자를 따라가는 감각을 발견한다 / 감정: 몸으로 느끼는 장난스러운 즐거움  
**말하는 방식:** feel it은 몸에서 나온 깨달음처럼 가볍고 feet에서 발을 내려다보는 미소가 들리게 한다. 노래나 박자 낭송으로 만들지 않는다.  
**속도·쉼 계획:** 112단어/분, 에너지 3/5, 앞 140ms / 뒤 320ms. 강조: feel · feet. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Enjoy the rhythm arriving in your feet, with a smile that follows the downward glance. Keep it spontaneous speech, not a sung or chanted line.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 영어 문장을 박자에 맞춰 기계적으로 끊기

## B03. 알고 있는 학교 길

**목적:** 학교가 목적지라는 사실을 다시 눈에 보이게 한 뒤 피노키오 스스로 잠깐 보겠다고 결정한다. 윤수에게 잘못된 길을 고르게 하지 않는다.

**연속성:** 학교 지붕과 종탑은 S04에서 본 같은 위치. 가방 속 책은 S03에서 제페토와 그림을 본 뒤 제페토가 넣은 같은 책이며 그 뒤 꺼내지 않았다. 음악의 근원은 아직 가려져 있고 돌아갈 길도 열려 있다.

### B03-C01 · 01:29–01:37 · NARRATIVE

**카메라:** TWO SHOT 40mm · 귀뚜라미의 제동

**자율 행동·연출:** 귀뚜라미가 학교 쪽으로 한 걸음 내딛고 원본 U007을 말한다. 피노키오가 그의 시선을 따라 먼 지붕을 찾는다. 음악은 작아져 대사가 또렷하다.

**시간 배정:** 발화 전 행동 0.6초 / 발화 뒤 행동 0.8초. 대사·쉼·지정 행동 계획 합계 7.76초. 실제 합성 길이는 별도 확인.

**[S05-U007 · ORIGINAL #7] 귀뚜라미:** “But school is waiting.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 음악에 끌리는 친구에게 학교 목적을 다시 붙든다 / 감정: 온화하지만 분명한 염려  
**말하는 방식:** But은 목소리를 세우지 않고 방향을 바꾸는 작은 접속으로, school에 무게를 준다. waiting을 비난처럼 늘이지 않는다.  
**속도·쉼 계획:** 110단어/분, 에너지 2/5, 앞 180ms / 뒤 330ms. 강조: school. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Redirect him gently on But, placing the weight on school. Keep the concern clear without turning waiting into an accusation.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 화를 내거나 음악을 나쁜 것으로 단정하는 훈계

**[S05-N013 · NEW] 피노키오:** “I can still see the roof.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 학교가 아직 시야에 있음을 확인해 안심시킨다 / 감정: 자신 있는 확인  
**말하는 방식:** still을 가볍게 짚어 목적지를 잊지 않았다는 마음을 보인다. roof는 손에 잡히는 관찰처럼 또렷하게 끝낸다.  
**속도·쉼 계획:** 110단어/분, 에너지 3/5, 앞 140ms / 뒤 260ms. 강조: still · roof. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Reassure the companion with a light emphasis on still, showing you have not lost the destination. Name the roof as something you actually see.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 다시 처음 학교를 발견한 것 같은 큰 놀람

### B03-C02 · 01:37–01:46 · NARRATIVE

**카메라:** MS 55mm · 가방과 먼 지붕

**자율 행동·연출:** 귀뚜라미가 가방을 가리키자 피노키오가 끈 위에 손을 얹는다. S03 기억을 별도 회상 화면으로 반복하지 않고 현재의 소품 접촉으로 연결한다.

**시간 배정:** 발화 전 행동 1.0초 / 발화 뒤 행동 1.2초. 대사·쉼·지정 행동 계획 합계 8.66초. 실제 합성 길이는 별도 확인.

**[S05-N014 · NEW] 귀뚜라미:** “Your book is for that school.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 가방 속 책과 보이는 학교의 관계를 연결한다 / 감정: 구체적인 상기  
**말하는 방식:** Your book에서 가방으로, that school에서 먼 지붕으로 시선이 옮겨 가는 간격을 목소리에 담는다. 설교 대신 두 대상을 연결한다.  
**속도·쉼 계획:** 112단어/분, 에너지 2/5, 앞 150ms / 뒤 300ms. 강조: book · that school. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Connect the book at his side with that school in the distance. Let the voice follow those two visible objects rather than deliver a lecture.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 책의 소유권을 검사하듯 딱딱하게 말하기

**[S05-N015 · NEW] 피노키오:** “Grandpa put it here.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 제페토가 책을 넣어 준 일을 현재 가방과 연결한다 / 감정: 가족을 떠올리는 따뜻함  
**말하는 방식:** Grandpa를 부드럽게 말하고 here에서 끈을 잡은 손 쪽으로 작게 내려앉는다. 회상 내레이터 말투로 바꾸지 않는다.  
**속도·쉼 계획:** 104단어/분, 에너지 2/5, 앞 170ms / 뒤 320ms. 강조: Grandpa · here. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Warm the name Grandpa, then settle here toward the hand on the strap. Recall his care from the present moment, not as a narrated flashback.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 늙은 목소리로 제페토를 흉내 내기

### B03-C03 · 01:46–01:54 · PROMPT

**카메라:** OTS 45mm · 학교를 가리킬 준비

**자율 행동·연출:** 학교 건물이 같은 지평선에 있는 구도. 귀뚜라미의 가리키는 몸짓을 보고 피노키오가 팔꿈치를 들지만 아직 손끝을 정렬하지 않는다. 질문 종료 시점에서 외부 대기.

**시간 배정:** 발화 전 행동 2.6초 / 발화 뒤 행동 0초. 대사·쉼·지정 행동 계획 합계 5.60초. 실제 합성 길이는 별도 확인.

**[S05-N016 · NEW] 귀뚜라미:** “Yoonsu, where is our school?”

**음성 연기:** CRICKET_DESIGN_V1 → 윤수 / 의도: 학교 방향을 함께 가리키도록 초대한다 / 감정: 또렷하고 친근한 확인  
**말하는 방식:** our school을 함께 가는 목표로 묻는다. 학교와 공연 중 선택시키는 긴박함 없이 보이는 방향에 관심을 모은다.  
**속도·쉼 계획:** 110단어/분, 에너지 3/5, 앞 150ms / 뒤 0ms. 강조: our school. Yoonsu, 뒤 120ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Invite a shared point toward our school. Ask with clear friendliness, not as a forced choice between school and the show.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 정답 선택을 압박하거나 우회를 부추기는 톤

**윤수 참여 3/10 · S05-P02 · 본편 밖 입력 대기**

- 질문 종료 시점: 114초. 본편 시계를 멈춘다.
- 첫 모델 예시: **“Point to school!”** — 귀뚜라미의 같은 고정 목소리.
- 모델 예시를 한 번 들려준 뒤 마이크를 켠다. 정확한 단어·발음 채점은 하지 않는다.
- 보호자 터치는 예시를 생략하고 반응으로 진행할 수 있다. 무응답5초 뒤 다시 듣기/터치를 제시한다.
- 시범: 귀뚜라미가 먼 학교 지붕과 종탑을 앞다리로 가리키는 동작을 보여준다. 피노키오의 팔은 반쯤 든 준비 상태.
- 대기 상태: 학교 지붕과 열려 있는 길이 함께 보임. 아이에게 학교와 공연 중 선택하라고 묻지 않는다.
- 입력 뒤 한 번 실행: 피노키오가 학교 쪽으로 팔과 눈을 맞춰 가리킴→몸도 잠깐 학교 쪽을 향함→책가방 끈을 가볍게 잡음.
- 첫 재개: S05-N017 “There! Beside the bell tower.”

**예시 음성 연기:**

**음성 연기:** CRICKET_DESIGN_V1 → 윤수(본편 밖 따라 말하기 예시) / 의도: 학교 방향을 가리키라는 표현을 들려준다 / 감정: 차분한 도움  
**말하는 방식:** Point to를 부드럽게 연결하고 school을 분명히 말한다. 보이는 목적지를 함께 짚는 부탁이며 길 선택 시험은 아니다.  
**속도·쉼 계획:** 82단어/분, 에너지 2/5, 앞 120ms / 뒤 360ms. 강조: Point · school. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Connect Point to smoothly and name school clearly. Make it a shared pointing invitation, not a test of which route to choose.  
**피할 연기:** 세 단어를 낱말 시험처럼 끊거나 큰 소리로 채점하기; 본편 인물의 지식·입모양·발견 반응을 먼저 바꾸기

### B03-C04 · 01:54–02:04 · REACT

**카메라:** MS 50mm · 방향 재확인

**자율 행동·연출:** 피노키오가 손끝→눈→몸을 같은 학교 방향으로 맞춘다. 카메라가 학교를 새로 생성하지 않고 기존 지붕을 함께 담아 공간 관계를 유지한다.

**시간 배정:** 발화 전 행동 3.2초 / 발화 뒤 행동 0.6초. 대사·쉼·지정 행동 계획 합계 9.15초. 실제 합성 길이는 별도 확인.

**[S05-N017 · NEW] 피노키오:** “There! Beside the bell tower.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미와 윤수 / 의도: 학교와 종탑의 위치를 짚어 확인한다 / 감정: 찾아 맞춘 산뜻함  
**말하는 방식:** There는 짧게 반짝이고 잠깐 시선을 따라간 뒤 bell tower를 한 대상 이름으로 붙여 말한다. 종 소리를 흉내 내지 않는다.  
**속도·쉼 계획:** 110단어/분, 에너지 3/5, 앞 110ms / 뒤 300ms. 강조: There · bell tower. There! 뒤 160ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Make There a brief, bright point, then connect bell tower as one landmark after the glance. Do not imitate a ringing bell.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; tall bell이라는 이전 문구를 다시 말하거나 종탑을 새 장소처럼 소개

**[S05-N018 · NEW] 귀뚜라미:** “That's our way.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 방금 가리킨 학교 방향이 원래 가야 할 길임을 확인한다 / 감정: 안심과 단단한 목적  
**말하는 방식:** That's를 짧게 받아 주고 our way에 차분한 확신을 둔다. 다음 우회에 동의하는 기쁜 고개 끄덕임의 소리는 아니다.  
**속도·쉼 계획:** 112단어/분, 에너지 2/5, 앞 150ms / 뒤 300ms. 강조: our way. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Confirm the original direction calmly, grounding our way. Do not let this sound like approval of the detour that comes next.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 공연 쪽으로 가자는 신나는 동의

### B03-C05 · 02:04–02:12 · NARRATIVE

**카메라:** PROFILE 40mm · 자율적인 작은 우회

**자율 행동·연출:** 학교를 가리키던 손을 내린 피노키오가 다시 음악 쪽으로 고개를 돌리고 U008을 말한다. 귀뚜라미의 걱정스러운 눈을 본 뒤 스스로 길가 나무 쪽 첫발을 내딛는다. 윤수의 참여가 우회를 명령하지 않는다.

**시간 배정:** 발화 전 행동 0.5초 / 발화 뒤 행동 1.2초. 대사·쉼·지정 행동 계획 합계 7.08초. 실제 합성 길이는 별도 확인.

**[S05-U008 · ORIGINAL #8] 피노키오:** “Just one little look!”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 호기심을 잠깐의 구경으로 작게 포장해 부탁한다 / 감정: 장난스러운 간청과 자기 합리화  
**말하는 방식:** Just와 little은 가볍고 look에 미련을 남긴다. 이미 허락받았다는 승리감 없이 상대 눈치를 한 번 살핀다.  
**속도·쉼 계획:** 108단어/분, 에너지 3/5, 앞 180ms / 뒤 300ms. 강조: Just · little look. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Make the request small on Just and little, lingering with desire on look. Keep a hint of checking the companion, not victory or permission already granted.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 거짓말을 꾸미는 악역 어조 또는 윤수에게 우회를 명령

**[S05-N019 · NEW] 귀뚜라미:** “We must not stay.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 잠깐 보는 선택과 오래 머무는 일을 구별해 경계한다 / 감정: 친근하지만 흔들리지 않는 염려  
**말하는 방식:** We로 동행감을 두고 not stay를 또렷하게 짚는다. 소리 높이지 않고도 시간을 넘기지 말자는 한계를 남긴다.  
**속도·쉼 계획:** 110단어/분, 에너지 2/5, 앞 160ms / 뒤 340ms. 강조: not stay. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Keep companionship in We and a clear boundary in not stay. Be firm through clarity, without raising the volume.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 체류를 허락하는 가벼운 농담 또는 벌을 예고하는 위협

## B04. 낮은 가지 아래로

**목적:** 음악을 향한 작은 우회가 실제 몸의 이동으로 보이게 한다. 낮은 가지 아래를 지나며 모자와 책가방을 스스로 지킨다.

**연속성:** B03에서 내딛은 발을 이어 기존 길가 나무로 이동. 학교 길에서 숲으로 장소가 갑자기 바뀌지 않는다. 귀뚜라미는 같은 옆길로 동행하며 우회를 권하지 않는다.

### B04-C01 · 02:12–02:20 · NARRATIVE

**카메라:** TRACK 35mm · 발과 길의 연결

**자율 행동·연출:** 원본 U009에 맞춰 피노키오가 기존 길의 가장자리를 따라 나무에 접근한다. 귀뚜라미가 낮은 가지를 발견해 가리키고 피노키오가 앞발을 줄인다.

**시간 배정:** 발화 전 행동 0.6초 / 발화 뒤 행동 1.0초. 대사·쉼·지정 행동 계획 합계 7.31초. 실제 합성 길이는 별도 확인.

**[S05-U009 · ORIGINAL #9] 내레이션:** “Pinocchio followed the sound.”

**음성 연기:** NARRATOR_A → 시청자 / 의도: 음악 쪽으로 스스로 내딛는 선택을 관찰한다 / 감정: 따뜻한 관찰 속 작은 염려  
**말하는 방식:** followed the sound를 움직임과 함께 담담하게 잇는다. 벌이 시작된다는 예고가 아니라 지금 일어난 행동을 짚는다.  
**속도·쉼 계획:** 110단어/분, 에너지 2/5, 앞 160ms / 뒤 340ms. 강조: followed the sound. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Observe him choosing to follow the sound, with gentle attention to the movement. Do not announce doom or moral judgment.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 사건을 과장해 예고하는 트레일러 목소리

**[S05-N020 · NEW] 귀뚜라미:** “Careful, that branch is low.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 모자가 낮은 가지에 닿기 전에 주의를 준다 / 감정: 즉각적이지만 안정된 주의  
**말하는 방식:** Careful은 빠르게 눈길을 잡되 날카롭게 외치지 않는다. branch is low는 눈앞 높이를 설명하며 낮고 고르게 말한다.  
**속도·쉼 계획:** 116단어/분, 에너지 3/5, 앞 80ms / 뒤 260ms. 강조: Careful · low. Careful, 뒤 100ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Catch his attention promptly on Careful without shouting, then explain the branch height in an even, reassuring tone.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 위험한 추락이 임박한 듯한 공포 연기

### B04-C02 · 02:20–02:28 · NARRATIVE

**카메라:** MS 50mm · 모자와 가지의 거리

**자율 행동·연출:** 피노키오가 모자 챙을 올려다보고 손을 가볍게 댄다. 귀뚜라미는 몸을 낮춘 채 앞을 살핀다. 접촉 직전 멈추는 동작이므로 가지 관통과 모자 순간이동은 없다.

**시간 배정:** 발화 전 행동 1.2초 / 발화 뒤 행동 2.0초. 대사·쉼·지정 행동 계획 합계 6.48초. 실제 합성 길이는 별도 확인.

**[S05-N021 · NEW] 피노키오:** “It almost brushed my hat.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 모자에 거의 닿을 뻔한 간격을 알아챈다 / 감정: 살짝 놀란 확인  
**말하는 방식:** almost를 짚고 hat에서 모자를 살피며 작은 안도의 기색을 준다. 아직 가지 아래를 통과한 성공 대사는 아니다.  
**속도·쉼 계획:** 106단어/분, 에너지 2/5, 앞 150ms / 뒤 300ms. 강조: almost · hat. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Notice how close the branch came, emphasizing almost and checking the hat. Keep this before the successful duck, not as its celebration.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 모자가 떨어졌거나 이미 통과했다고 들리는 과장

### B04-C03 · 02:28–02:36 · PROMPT

**카메라:** THREE QUARTER 45mm · 무릎 시범과 질문

**자율 행동·연출:** 귀뚜라미의 몸 낮추기와 피노키오 무릎 준비를 같은 화면에 둔다. 질문이 끝나는 C03 종료 경계에서 외부 대기한다. 이 8초는 시범과 발화 분량이다.

**시간 배정:** 발화 전 행동 1.0초 / 발화 뒤 행동 0초. 대사·쉼·지정 행동 계획 합계 7.71초. 실제 합성 길이는 별도 확인.

**[S05-N022 · NEW] 귀뚜라미:** “Bend your knees like this.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 몸을 낮출 수 있는 무릎 동작을 시범과 연결한다 / 감정: 차분한 코칭  
**말하는 방식:** Bend your knees를 부드럽게 이어 말하고 like this에서 귀뚜라미 자신의 낮추기를 보여 준다. 구령 박자로 자르지 않는다.  
**속도·쉼 계획:** 112단어/분, 에너지 2/5, 앞 120ms / 뒤 260ms. 강조: knees · like this. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Connect Bend your knees smoothly with your own small demonstration on like this. Coach rather than issue a drill command.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 군대식 구령 또는 윤수의 정확한 동작을 평가하는 말투

**[S05-N023 · NEW] 피노키오:** “Yoonsu, how can I go under?”

**음성 연기:** PINOCCHIO_A → 윤수 / 의도: 가지 아래로 지나갈 방법을 함께 시도하자고 청한다 / 감정: 필요가 분명한 호기심  
**말하는 방식:** under에서 가지 아래 빈 공간을 보며 질문을 올린다. 도움을 간절히 외치는 위험 상황으로 키우지 않는다.  
**속도·쉼 계획:** 106단어/분, 에너지 3/5, 앞 140ms / 뒤 0ms. 강조: go under. Yoonsu, 뒤 120ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Ask while looking at the space under the branch. Lift under with practical curiosity, not panic or helpless distress.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 우회 장소를 고르게 하는 길 찾기 질문처럼 말하기

**윤수 참여 4/10 · S05-P03 · 본편 밖 입력 대기**

- 질문 종료 시점: 156초. 본편 시계를 멈춘다.
- 첫 모델 예시: **“Duck your head!”** — 피노키오의 같은 고정 목소리.
- 모델 예시를 한 번 들려준 뒤 마이크를 켠다. 정확한 단어·발음 채점은 하지 않는다.
- 보호자 터치는 예시를 생략하고 반응으로 진행할 수 있다. 무응답5초 뒤 다시 듣기/터치를 제시한다.
- 시범: 귀뚜라미가 낮은 가지 아래에서 몸을 낮추는 짧은 시범. 피노키오가 무릎과 목을 굽힐 준비를 하되 아직 통과하지 않는다.
- 대기 상태: 모자 앞끝이 가지에 닿기 전, 두 발은 길 위. 가지를 잡아 꺾거나 모자가 떨어지는 새 사고는 없다.
- 입력 뒤 한 번 실행: 무릎 굽힘→고개와 상체 낮춤→한 발씩 가지 아래 통과→천천히 다시 섬.
- 첫 재개: S05-N024 “My hat stayed on!”

**예시 음성 연기:**

**음성 연기:** PINOCCHIO_A → 윤수(본편 밖 따라 말하기 예시) / 의도: 가지 아래에서 머리를 숙이는 표현을 들려준다 / 감정: 안전한 움직임을 돕는 친근함  
**말하는 방식:** Duck your를 급히 외치지 않고 head로 자연스럽게 연결한다. 위협을 피하는 비상 구령처럼 높이지 않는다.  
**속도·쉼 계획:** 80단어/분, 에너지 2/5, 앞 120ms / 뒤 360ms. 강조: Duck · head. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Keep Duck your head warm and connected, linked to the shown lowering movement. Avoid the urgency of an emergency duck command.  
**피할 연기:** 세 단어를 낱말 시험처럼 끊거나 큰 소리로 채점하기; 본편 인물의 지식·입모양·발견 반응을 먼저 바꾸기

### B04-C04 · 02:36–02:48 · REACT

**카메라:** SIDE MS 40mm · 체중 이동과 통과

**자율 행동·연출:** 두 발이 동시에 미끄러지지 않도록 한 발 지지→반대 발 이동을 지킨다. 무릎·골반·등이 함께 낮아지고 모자는 머리에 붙어 이동한다. 가방이 가지를 지나간 뒤 일어선다.

**시간 배정:** 발화 전 행동 5.5초 / 발화 뒤 행동 0.6초. 대사·쉼·지정 행동 계획 합계 11.74초. 실제 합성 길이는 별도 확인.

**[S05-N024 · NEW] 피노키오:** “My hat stayed on!”

**음성 연기:** PINOCCHIO_A → 귀뚜라미와 윤수 / 의도: 통과한 뒤 모자가 그대로 있음을 기뻐한다 / 감정: 작은 성취와 안도  
**말하는 방식:** 모든 발걸음과 일어서기가 끝난 뒤 hat에 손을 느끼며 stayed on을 밝게 말한다. 경기 승리 같은 함성은 피한다.  
**속도·쉼 계획:** 112단어/분, 에너지 3/5, 앞 100ms / 뒤 300ms. 강조: hat · stayed on. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** After the pass and rise finish, enjoy that the hat stayed on. Let the relief be small and personal rather than a winning cheer.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 가지에 닿기도 전 성공을 말하는 성급한 발화

**[S05-N025 · NEW] 귀뚜라미:** “You kept your hat safe.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 친구가 모자를 조심히 지킨 행동을 알아봐 준다 / 감정: 따뜻한 인정  
**말하는 방식:** You kept는 실제 행동을 인정하고 safe는 편안히 닫는다. 정답 점수나 착한 아이 평가처럼 과장하지 않는다.  
**속도·쉼 계획:** 114단어/분, 에너지 2/5, 앞 150ms / 뒤 320ms. 강조: kept · safe. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Recognize the care he actually took in You kept, settling safe warmly. Acknowledge the action without grading the child.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 점수 채점처럼 과한 칭찬 구호

### B04-C05 · 02:48–02:57 · NARRATIVE

**카메라:** WIDE 35mm · 큰 나무와 붉은 조각

**자율 행동·연출:** 피노키오가 서며 큰 줄기 뒤 붉은 천의 모서리를 발견한다. 원본 U010이 천막을 설명해도 전면·무대·인형은 아직 가린다. 낮은 가지는 뒤에 남아 실제 이동을 증명한다.

**시간 배정:** 발화 전 행동 0.8초 / 발화 뒤 행동 1.2초. 대사·쉼·지정 행동 계획 합계 8.21초. 실제 합성 길이는 별도 확인.

**[S05-U010 · ORIGINAL #10] 내레이션:** “A bright red tent was hiding behind a big tree.”

**음성 연기:** NARRATOR_A → 시청자 / 의도: 큰 나무 뒤 천막 모서리라는 새 시각 단서를 소개한다 / 감정: 은근한 발견의 기대  
**말하는 방식:** bright red tent에는 색이 보이는 선명함을, hiding behind에는 가려진 공간의 호기심을 둔다. 무대 전모를 보여 준 듯 말하지 않는다.  
**속도·쉼 계획:** 108단어/분, 에너지 2/5, 앞 170ms / 뒤 340ms. 강조: bright red tent · big tree. tent 뒤 140ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Give bright red tent visual color, then let hiding behind preserve the curiosity of the obstruction. Do not imply a full stage reveal yet.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 천막을 악당의 은신처처럼 불길하게 묘사

## B05. 얼굴에 닿는 잎을 살며시

**목적:** 세게 잡아당기지 않고 얼굴 옆 잎을 옮겨 지나갈 작은 공간을 만든다. 천막을 가린 주된 장애물은 큰 나무 줄기로 계속 남긴다.

**연속성:** 같은 나무의 통로 옆 잎만 피노키오가 접촉한다. 지면의 귀뚜라미는 자기 앞다리가 닿는 별도의 낮은 잎으로 시범하고, 피노키오 얼굴 옆 잎은 S05-P04 반응까지 그대로 둔다. 큰 줄기와 천막의 가림 관계는 I09 전까지 유지. 잎과 가지를 떼어 가져가지 않는다.

### B05-C01 · 02:57–03:05 · NARRATIVE

**카메라:** CU 65mm · 눈앞의 잎

**자율 행동·연출:** 피노키오가 얼굴에 닿은 잎 때문에 한 번 눈을 깜박이고 손가락을 오므리려 한다. 귀뚜라미가 손을 펴는 몸짓으로 급한 잡아당김을 멈추게 한다.

**시간 배정:** 발화 전 행동 0.6초 / 발화 뒤 행동 0.8초. 대사·쉼·지정 행동 계획 합계 7.09초. 실제 합성 길이는 별도 확인.

**[S05-N026 · NEW] 피노키오:** “These leaves brush my face.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 얼굴에 닿는 잎의 감촉을 말한다 / 감정: 가벼운 불편과 신기함  
**말하는 방식:** brush를 스치는 느낌으로 가볍게 내고 face에서 눈을 한 번 깜박이는 작은 반응을 담는다. 아픈 비명은 넣지 않는다.  
**속도·쉼 계획:** 106단어/분, 에너지 2/5, 앞 130ms / 뒤 280ms. 강조: brush · face. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Let brush feel like a light touch, with a small blink in the voice on face. Show mild inconvenience without pain or a cry.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 상처를 입은 듯한 고통 연기

**[S05-N027 · NEW] 귀뚜라미:** “Don't pull them off.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 잎을 떼려는 손가락에 더 부드러운 방법을 알려 준다 / 감정: 즉각적이고 다정한 제지  
**말하는 방식:** Don't는 짧고 선명하지만 세게 때리지 않고 pull them off를 한 호흡으로 설명한다. 나무를 다치게 하지 말자는 관심을 담는다.  
**속도·쉼 계획:** 116단어/분, 에너지 2/5, 앞 100ms / 뒤 280ms. 강조: pull them off. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Make Don't clear but gentle, connecting pull them off in one phrase. Protect the leaves without shaming or startling him.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 나쁜 행동을 잡아낸 교사의 꾸지람

### B05-C02 · 03:05–03:13 · NARRATIVE

**카메라:** INSERT 60mm · 펴진 손바닥

**자율 행동·연출:** 피노키오가 손가락을 하나씩 펴며 얼굴 옆 잎을 살핀다. 귀뚜라미는 두 발을 지면에 둔 채 자기 앞다리가 편하게 닿는 높이, 즉 귀뚜라미 몸높이 이하의 별도 낮은 잎 아래를 받쳐 작은 옆 움직임을 시범한다. 얼굴 높이 잎에는 닿지 않는다. S05-N029는 이 낮은 잎을 가볍게 받치는 순간에 말한다.

**시간 배정:** 발화 전 행동 1.0초 / 발화 뒤 행동 1.0초. 대사·쉼·지정 행동 계획 합계 7.43초. 실제 합성 길이는 별도 확인.

**[S05-N028 · NEW] 피노키오:** “I'll use an open hand.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 잡아당기지 않고 손바닥을 쓰겠다고 스스로 정한다 / 감정: 생각해 낸 자신감  
**말하는 방식:** I'll use에서 선택이 생기고 open hand에서 손가락을 펴는 감각이 들리게 한다. 책 읽듯 해결 방법을 설명하지 않는다.  
**속도·쉼 계획:** 108단어/분, 에너지 3/5, 앞 130ms / 뒤 280ms. 강조: open hand. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Let I'll use sound like a decision you have just made, opening the fingers through open hand. Speak from the action rather than reciting a solution.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 성인 시범 강사의 완성된 설명조

**[S05-N029 · NEW] 귀뚜라미:** “Gently, like this.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 낮은 별도 잎에서 부드럽게 받치는 시범을 보인다 / 감정: 섬세한 도움  
**말하는 방식:** Gently를 공기처럼 약하게 흘리지 말고 들릴 만큼 부드럽게, like this를 낮은 잎을 받치는 동작과 이어 준다.  
**속도·쉼 계획:** 108단어/분, 에너지 2/5, 앞 140ms / 뒤 320ms. 강조: Gently. Gently, 뒤 120ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Keep Gently soft but audible, connecting like this with the separate low leaf you can reach. Demonstrate light touch, not a whispered secret.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 작은 캐릭터를 흉내 낸 알아듣기 힘든 고음

### B05-C03 · 03:13–03:21 · PROMPT

**카메라:** MS 50mm · 접촉 직전 질문

**자율 행동·연출:** 귀뚜라미가 별도의 낮은 잎을 천천히 놓아 원위치로 돌아가게 한다. 피노키오는 그 시범을 보고 편 손바닥을 얼굴 옆 잎 가까이에 준비하되 아직 밀지 않는다. 큰 줄기는 천막 전면을 계속 가린다. 마지막 질문 S05-N030의 실제 음성이 끝나는 C03 종료 경계에서만 외부 대기로 전환한다.

**시간 배정:** 발화 전 행동 2.2초 / 발화 뒤 행동 0초. 대사·쉼·지정 행동 계획 합계 6.47초. 실제 합성 길이는 별도 확인.

**[S05-N030 · NEW] 피노키오:** “Yoonsu, can you help with these leaves?”

**음성 연기:** PINOCCHIO_A → 윤수 / 의도: 얼굴 옆 잎을 조심히 비켜 갈 도움을 청한다 / 감정: 협력하는 부탁  
**말하는 방식:** these leaves에서 지금 얼굴 옆의 잎을 가리키는 마음을 담는다. 긴 질문을 단어별로 끊지 않고 끝을 편안히 연다.  
**속도·쉼 계획:** 105단어/분, 에너지 3/5, 앞 150ms / 뒤 0ms. 강조: these leaves. Yoonsu, 뒤 120ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Invite help with these visible leaves, keeping the longer question connected. End with an easy invitation instead of urgency or a quiz cadence.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 잎을 떼어 내라고 명령하는 강한 말투

**윤수 참여 5/10 · S05-P04 · 본편 밖 입력 대기**

- 질문 종료 시점: 201초. 본편 시계를 멈춘다.
- 첫 모델 예시: **“Move the leaves!”** — 피노키오의 같은 고정 목소리.
- 모델 예시를 한 번 들려준 뒤 마이크를 켠다. 정확한 단어·발음 채점은 하지 않는다.
- 보호자 터치는 예시를 생략하고 반응으로 진행할 수 있다. 무응답5초 뒤 다시 듣기/터치를 제시한다.
- 시범: 지면의 귀뚜라미가 자기 몸높이 이하의 별도 낮은 잎을 앞다리로 살짝 받쳐 옆으로 옮겼다가 놓는 시범(B05-C02→C03). 피노키오는 얼굴 높이의 다른 잎 옆에 손바닥만 준비한다. 두 잎을 혼동하거나 귀뚜라미를 공중에 띄우지 않는다.
- 대기 상태: 잎은 아직 얼굴 옆, 손바닥이 닿기 직전. 큰 줄기가 무대 전면을 계속 가린다.
- 입력 뒤 한 번 실행: 손바닥으로 잎을 옆에 받침→얼굴과 가방이 잎을 지나감→손을 천천히 떼어 가지가 원래 위치로 돌아감.
- 첫 재개: S05-N031 “Now my face is clear.”

**예시 음성 연기:**

**음성 연기:** PINOCCHIO_A → 윤수(본편 밖 따라 말하기 예시) / 의도: 잎을 옆으로 옮기는 표현을 한번 들려준다 / 감정: 부드러운 배려  
**말하는 방식:** Move는 힘을 빼고 the leaves로 이어 손바닥으로 받치는 느낌을 준다. 잎을 꺾거나 잡아당기는 강한 힘은 없다.  
**속도·쉼 계획:** 82단어/분, 에너지 2/5, 앞 120ms / 뒤 360ms. 강조: Move · leaves. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Soften Move and carry it into the leaves with the sense of a supporting palm. Model gentle repositioning, never tugging or snapping.  
**피할 연기:** 세 단어를 낱말 시험처럼 끊거나 큰 소리로 채점하기; 본편 인물의 지식·입모양·발견 반응을 먼저 바꾸기

### B05-C04 · 03:21–03:33 · REACT

**카메라:** SIDE MS 45mm · 조심스러운 접촉

**자율 행동·연출:** 손바닥 접촉점에 맞춰 잎이 옆으로 움직이고 피노키오가 한 걸음 통과한다. 손이 먼저 관통하지 않도록 손→잎→몸 이동 순서를 보인다. 몸이 지난 뒤 천천히 놓는다.

**시간 배정:** 발화 전 행동 5.0초 / 발화 뒤 행동 0.7초. 대사·쉼·지정 행동 계획 합계 11.53초. 실제 합성 길이는 별도 확인.

**[S05-N031 · NEW] 피노키오:** “Now my face is clear.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미와 윤수 / 의도: 잎을 지나온 뒤 얼굴 앞 공간이 트였음을 확인한다 / 감정: 작고 편안한 안도  
**말하는 방식:** Now에서 숨이 편해지는 느낌을 주고 face is clear를 자연스럽게 잇는다. 잎이 놓인 뒤 실제 결과를 보고 말한다.  
**속도·쉼 계획:** 107단어/분, 에너지 2/5, 앞 130ms / 뒤 280ms. 강조: Now · clear. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** After passing and releasing the leaf, let Now carry the relief of an unobstructed face. Connect the phrase as a simple, present observation.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 청결 제품을 소개하는 듯한 강조 또는 과도한 승리감

**[S05-N032 · NEW] 귀뚜라미:** “The leaves are safe.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 잎도 손상 없이 돌아온 결과를 함께 알아본다 / 감정: 돌봄의 만족  
**말하는 방식:** leaves를 살짝 짚어 사람뿐 아니라 잎도 괜찮음을 보여 준다. safe는 작게 안심시키고 평가 점수처럼 높이지 않는다.  
**속도·쉼 계획:** 112단어/분, 에너지 2/5, 앞 170ms / 뒤 300ms. 강조: leaves · safe. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Notice that the leaves are unharmed too, gently emphasizing leaves. Settle safe with care rather than a reward announcement.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 자연 보호 교훈을 길게 설교하는 어조

### B05-C05 · 03:33–03:41 · NARRATIVE

**카메라:** OTS 40mm · 여전히 가려진 전면

**자율 행동·연출:** 돌아간 잎 너머로 붉은 모서리만 보인다. 피노키오가 큰 줄기의 왼쪽과 오른쪽을 번갈아 보지만 카메라는 무대 전면을 공개하지 않는다. I09의 공간 발견을 남긴다.

**시간 배정:** 발화 전 행동 1.0초 / 발화 뒤 행동 1.8초. 대사·쉼·지정 행동 계획 합계 7.26초. 실제 합성 길이는 별도 확인.

**[S05-N033 · NEW] 피노키오:** “That big trunk still blocks my view.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 잎은 지났지만 큰 줄기가 여전히 시야를 가린다고 말한다 / 감정: 새 문제를 살피는 호기심  
**말하는 방식:** still을 작게 짚고 big trunk를 눈으로 따라 말한다. 짜증이 아니라 다음에 어디를 볼지 궁리하는 마음으로 끝낸다.  
**속도·쉼 계획:** 106단어/분, 에너지 2/5, 앞 170ms / 뒤 330ms. 강조: big trunk · still. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Follow the big trunk with your eyes and lightly mark still. Keep the blocked view a fresh puzzle, not annoyance or defeat.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 앞선 도움을 무용하다고 탓하는 실망

## B06. 나무 뒤의 빨간 천막

**목적:** 원본 I09로 소리의 근원을 최초로 공개한다. 인형극에 끌리는 이유는 자신과 닮은 나무 인형의 움직임이다.

**연속성:** I09 직전까지 큰 나무가 전면을 가린다. 반응 후에는 천막 앞과 동물 관객, 닫힌 본무대 커튼이 보인다. 이름 없는 맛보기 인형 둘은 오른쪽 앞턱의 노출된 측면 대기자리로만 옮겨 S06-U003까지 보이며 핍은 소개하지 않는다.

### B06-C01 · 03:41–03:53 · NARRATIVE

**카메라:** MS 50mm · 보이지만 찾지 못하는 얼굴

**자율 행동·연출:** 피노키오가 나무 양쪽을 번갈아 보다 U011을 말한다. 붉은 천 한 귀퉁이와 음악만 단서로 남긴다. 가방과 신발의 이전 상태는 그대로 이어진다.

**시간 배정:** 발화 전 행동 0.6초 / 발화 뒤 행동 0.7초. 대사·쉼·지정 행동 계획 합계 11.83초. 실제 합성 길이는 별도 확인.

**[S05-U011 · ORIGINAL #11] 피노키오:** “I can hear the music, but where is it coming from?”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 소리를 듣지만 정확히 어디서 나는지 찾지 못한다 / 감정: 확신과 궁금함이 교차  
**말하는 방식:** 앞 절은 이미 듣고 있다는 확인, but 뒤는 탐색으로 바꾼다. music 뒤 짧게 생각하고 where로 눈길을 옮기며 긴 문장을 한 번에 급히 밀지 않는다.  
**속도·쉼 계획:** 107단어/분, 에너지 3/5, 앞 160ms / 뒤 320ms. 강조: hear · where. music, 뒤 220ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** State the hearing with certainty, then turn into a searching question after but. Allow a small thought after music and let where guide the eyeline.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 앞 장면의 정보를 잊은 듯 놀라거나 모든 단어를 같은 세기로 읽기

**[S05-N034 · NEW] 피노키오:** “I can see a red corner.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 붉은 모서리 하나를 단서로 보고한다 / 감정: 찾아낸 작은 기대  
**말하는 방식:** red corner를 작지만 반가운 단서처럼 밝힌다. 아직 천막 전체나 무대를 본 듯 크게 놀라지 않는다.  
**속도·쉼 계획:** 110단어/분, 에너지 3/5, 앞 130ms / 뒤 260ms. 강조: red corner. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Brighten the small clue in red corner, as something useful you have just spotted. Keep the excitement short of seeing the whole tent or stage.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 발견 게이트를 앞당기는 환호

### B06-C02 · 03:53–04:02 · NARRATIVE

**카메라:** TWO SHOT 45mm · 관객의 시야 설명

**자율 행동·연출:** 귀뚜라미가 윤수 쪽을 보고 원본 U012를 말한 뒤 나무 옆으로 몸을 낮춰 방향만 가리킨다. 카메라는 시범을 보여줘도 가림을 넘지 않는다.

**시간 배정:** 발화 전 행동 0.8초 / 발화 뒤 행동 1.0초. 대사·쉼·지정 행동 계획 합계 8.47초. 실제 합성 길이는 별도 확인.

**[S05-U012 · ORIGINAL #12] 귀뚜라미:** “Yoonsu can see the square.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 윤수의 시점이 방향 찾기에 도움이 된다고 설명한다 / 감정: 친근한 연결  
**말하는 방식:** Yoonsu는 곁의 친구를 떠올리듯 자연스럽게 말하고 square로 시선을 넓힌다. 인형극 전면을 이미 보여 줬다는 강조는 넣지 않는다.  
**속도·쉼 계획:** 112단어/분, 에너지 2/5, 앞 150ms / 뒤 280ms. 강조: Yoonsu · square. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Refer naturally to Yoonsu as a friend who can help, widening the sense of space on square. Do not imply that the stage front has already been revealed.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 전지적 내레이터처럼 시청자의 지식을 선언

**[S05-N035 · NEW] 귀뚜라미:** “You can look around this side.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 나무 옆으로 보면 되는 방향을 시범으로 알려 준다 / 감정: 실용적인 도움  
**말하는 방식:** around this side를 가리키는 앞다리와 한 덩어리로 말한다. 먼저 몸을 돌리라는 급한 구령이 아니라 볼 방향을 안내한다.  
**속도·쉼 계획:** 114단어/분, 에너지 2/5, 앞 130ms / 뒤 270ms. 강조: around this side. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Connect around this side with the indicating foreleg. Offer the direction to look without a hurried command to move before the event.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 윤수 입력 전에 카메라가 이미 돌아간 듯한 완료조

### B06-C03 · 04:02–04:11 · PROMPT

**카메라:** MS 50mm · 마지막 가려진 시야

**자율 행동·연출:** 피노키오는 아직 줄기를 보고 있고 귀뚜라미는 나무 옆을 가리킨다. 원본 U013이 마지막 발화. C03 종료 경계에서 외부 대기로 전환한다.

**시간 배정:** 발화 전 행동 2.2초 / 발화 뒤 행동 0초. 대사·쉼·지정 행동 계획 합계 5.21초. 실제 합성 길이는 별도 확인.

**[S05-U013 · ORIGINAL #13] 귀뚜라미:** “Yoonsu, where should Pinocchio look?”

**음성 연기:** CRICKET_DESIGN_V1 → 윤수 / 의도: 나무 옆을 가리켜 줄 차례를 넘긴다 / 감정: 밝고 열린 부탁  
**말하는 방식:** Yoonsu를 한 번 부른 뒤 where와 look 사이를 자연스러운 질문으로 잇는다. 장난스럽게 정답을 숨기는 진행자 톤은 피한다.  
**속도·쉼 계획:** 110단어/분, 에너지 3/5, 앞 160ms / 뒤 0ms. 강조: where · look. Yoonsu, 뒤 120ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Hand the pointing turn to Yoonsu with an open question. Keep where and look connected, without teasing a hidden quiz answer.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 답을 맞힐 때까지 재촉하는 끝 올림

**윤수 참여 6/10 · I09 · 본편 밖 입력 대기**

- 질문 종료 시점: 251초. 본편 시계를 멈춘다.
- 첫 모델 예시: **“Look over there!”** — 귀뚜라미의 같은 고정 목소리.
- 모델 예시를 한 번 들려준 뒤 마이크를 켠다. 정확한 단어·발음 채점은 하지 않는다.
- 보호자 터치는 예시를 생략하고 반응으로 진행할 수 있다. 무응답5초 뒤 다시 듣기/터치를 제시한다.
- 시범: 귀뚜라미가 나무 옆 빈 시야를 가리키되 피노키오와 카메라는 아직 돌아가지 않는다. 화면 행동과 방향을 먼저 제시한다.
- 대기 상태: 천막 전면은 큰 줄기 뒤, 본무대 커튼 상태도 아직 관객에게 보이지 않음. U013 종료 뒤에만 대기.
- 입력 뒤 한 번 실행: 카메라 팬→천막 등장→피노키오가 두 눈을 크게 뜸. 천막 전면과 움직이는 무대 인형 둘이 보이지만 본무대 커튼은 닫혀 있다.
- 첫 재개: S05-U014 “Wow! A puppet show!”

**예시 음성 연기:**

**음성 연기:** CRICKET_DESIGN_V1 → 윤수(본편 밖 따라 말하기 예시) / 의도: 나무 옆 방향을 가리키는 예시를 준다 / 감정: 작은 기대를 담은 안내  
**말하는 방식:** Look over를 연결하고 there에 가리킴만 살짝 얹는다. 천막을 이미 본 큰 감탄이나 화면 속 발견 반응을 대신하지 않는다.  
**속도·쉼 계획:** 84단어/분, 에너지 2/5, 앞 120ms / 뒤 360ms. 강조: Look · there. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Connect Look over and give there a light pointing lift. Preserve anticipation without performing the tent reveal or an in-story exclamation.  
**피할 연기:** 세 단어를 낱말 시험처럼 끊거나 큰 소리로 채점하기; 본편 인물의 지식·입모양·발견 반응을 먼저 바꾸기

### B06-C04 · 04:11–04:23 · REACT

**카메라:** PAN RIGHT 35mm · 첫 전면 공개

**자율 행동·연출:** 응답 후 카메라가 먼저 오른쪽으로 팬하고 큰 나무가 화면 옆으로 빠지며 빨간 천막이 나타난다. 이어 피노키오 두 눈이 커진다. 닫힌 본무대 커튼 앞턱에서 이름 없는 작은 인형 둘이 팔과 몸을 두어 번 흔든다. 원본 U014가 첫 재개 발화.

**시간 배정:** 발화 전 행동 4.5초 / 발화 뒤 행동 0.8초. 대사·쉼·지정 행동 계획 합계 10.09초. 실제 합성 길이는 별도 확인.

**[S05-U014 · ORIGINAL #14] 피노키오:** “Wow! A puppet show!”

**음성 연기:** PINOCCHIO_A → 귀뚜라미와 윤수 / 의도: 처음 드러난 인형 무대를 보고 놀란다 / 감정: 즉각적인 감탄  
**말하는 방식:** 천막과 인형을 보고 눈이 커진 뒤 Wow를 꺼낸다. 짧은 숨 뒤 puppet show를 알아본 기쁨으로 말하되 유아 비명으로 치솟지 않는다.  
**속도·쉼 계획:** 112단어/분, 에너지 4/5, 앞 100ms / 뒤 310ms. 강조: Wow · puppet show. Wow! 뒤 190ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Let Wow arrive only after the reveal and widened eyes, then recognize a puppet show with delighted clarity. Keep the bright boy voice, without a squeal.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 카메라 팬이 끝나기 전 감탄하거나 날카로운 고음으로 소리 지르기

**[S05-N036 · NEW] 피노키오:** “Little wooden dancers!”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 무대 위 작은 나무 인형들의 움직임에 끌린다 / 감정: 애정 어린 신기함  
**말하는 방식:** Little은 작고 귀엽다는 미소, wooden은 자신과 닮았다는 관심, dancers는 실제 움직임을 따라 가볍게 살린다.  
**속도·쉼 계획:** 112단어/분, 에너지 3/5, 앞 140ms / 뒤 300ms. 강조: wooden · dancers. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Smile at Little, notice the shared wooden quality, and let dancers follow their small movement. Admire them without sounding like a show announcer.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 본공연이 이미 시작됐다고 떠드는 공연 진행자 발성

### B06-C05 · 04:23–04:34 · NARRATIVE

**카메라:** OVER SHOULDER 45mm · 닮은 팔과 책가방

**자율 행동·연출:** 피노키오가 자기 팔꿈치를 한 번 굽혀 인형 팔과 비교하고 웃는다. 귀뚜라미는 그의 가방을 보며 학교책을 상기한다. 맛보기 인형 둘은 앞턱 중앙에서 관객 시점 오른쪽 앞턱의 노출된 측면 대기자리로 짧게 걸어가 멈춘다. 옆 가림판 뒤나 닫힌 본커튼 안으로 들어가지 않으며 두 인형의 전신은 객석에서 계속 보인다. 이 위치를 S06-U003까지 유지한다. 핍 이름·얼굴, 커튼 고장·개방, 본공연은 아직 없다.

**시간 배정:** 발화 전 행동 1.0초 / 발화 뒤 행동 2.5초. 대사·쉼·지정 행동 계획 합계 10.71초. 실제 합성 길이는 별도 확인.

**[S05-N037 · NEW] 피노키오:** “Their arms move like mine.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 자신의 팔꿈치와 인형 팔이 닮았음을 비교한다 / 감정: 새로운 친밀감  
**말하는 방식:** arms에서 자기 팔을 보다가 like mine에서 반가운 미소가 자란다. 자랑하는 힘센 영웅 톤은 쓰지 않는다.  
**속도·쉼 계획:** 105단어/분, 에너지 3/5, 앞 180ms / 뒤 320ms. 강조: arms · like mine. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Look from their arms to your own, letting like mine grow into a pleased sense of kinship. Keep the discovery tender rather than boastful.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 나도 공연에 참가하겠다는 선언처럼 들리기

**[S05-N038 · NEW] 귀뚜라미:** “And yours can carry a schoolbook.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 팔의 닮음에서 학교책이라는 현재 책임을 다시 연결한다 / 감정: 조용한 걱정  
**말하는 방식:** And yours는 앞말을 받아 주고 schoolbook에만 낮은 무게를 둔다. 비꼬거나 즐거움을 꺾는 차가운 훈계로 바꾸지 않는다.  
**속도·쉼 계획:** 109단어/분, 에너지 2/5, 앞 190ms / 뒤 360ms. 강조: schoolbook. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Accept his comparison on And yours, then place a quiet weight on schoolbook. Remind without sarcasm or flattening his delight.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 인형과 닮았다는 기쁨을 조롱하는 냉소

## B07. 손끝에 남아 있는 약속

**목적:** 원본 약속 경고를 추상적인 말로만 두지 않고 가방 속 책의 감촉과 연결한다. 피노키오는 목적을 몰라서가 아니라 알고도 망설인다.

**연속성:** 학교와 약속, 제페토와 함께 본 책은 S03에서 이어온 정보. S03에서 가방에 넣은 뒤 꺼내지 않은 같은 책을 천 위로만 느낀다. 가방을 열거나 책을 꺼내지 않는다. 아직 본공연 시작 전이고 학교로 돌아갈 통로는 열려 있다.

### B07-C01 · 04:34–04:42 · NARRATIVE

**카메라:** MS 50mm · 경고와 시선 이동

**자율 행동·연출:** 귀뚜라미가 피노키오 가까이 와 U015를 말한다. 피노키오의 웃음이 작아지고 무대에서 가방으로 시선이 내려간다. 비난하거나 무섭게 몰아붙이지 않는다.

**시간 배정:** 발화 전 행동 0.5초 / 발화 뒤 행동 0.9초. 대사·쉼·지정 행동 계획 합계 7.20초. 실제 합성 길이는 별도 확인.

**[S05-U015 · ORIGINAL #15] 귀뚜라미:** “Pinocchio, remember your promise.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 약속을 아는 친구의 주의를 다시 붙잡는다 / 감정: 가까운 친구의 진지한 염려  
**말하는 방식:** Pinocchio를 부드럽게 불러 눈을 만나고 remember는 느슨하게 흘리지 않는다. promise는 조용히 무게를 남기되 심판하지 않는다.  
**속도·쉼 계획:** 108단어/분, 에너지 2/5, 앞 210ms / 뒤 360ms. 강조: remember · promise. Pinocchio, 뒤 150ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Call his name softly to meet his eyes, then make remember clear and promise quietly weighty. Speak as a concerned companion, not a judge.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 부모를 흉내 낸 호통이나 벌을 암시하는 저음

**[S05-N039 · NEW] 피노키오:** “Grandpa packed my book.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 가방 속 책에 담긴 할아버지의 손길을 떠올린다 / 감정: 따뜻함에 섞인 작은 망설임  
**말하는 방식:** Grandpa에서 한층 부드러워지고 packed my book은 방금 가방을 내려다본 확인으로 말한다. 아직 후회의 결말을 선행하지 않는다.  
**속도·쉼 계획:** 103단어/분, 에너지 2/5, 앞 190ms / 뒤 340ms. 강조: Grandpa · my book. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Soften on Grandpa and speak packed my book as a present reminder of his care. Allow a little hesitation without jumping ahead to full remorse.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 이미 학교를 놓친 것처럼 울먹이는 죄책감

### B07-C02 · 04:42–04:52 · NARRATIVE

**카메라:** INSERT 60mm · 책이 있는 가방

**자율 행동·연출:** 가방 천에 비치는 네모난 책 윤곽을 보여준다. 피노키오가 손가락으로 공중에서 네모를 짚어보고, 귀뚜라미가 손을 댈 위치를 시범한다.

**시간 배정:** 발화 전 행동 1.4초 / 발화 뒤 행동 1.2초. 대사·쉼·지정 행동 계획 합계 9.04초. 실제 합성 길이는 별도 확인.

**[S05-N040 · NEW] 귀뚜라미:** “Feel it through your bag.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 가방을 열지 않고 책의 윤곽을 느낄 방법을 준다 / 감정: 조용하고 구체적인 도움  
**말하는 방식:** Feel을 손끝 감각처럼 부드럽게, through your bag을 붙여 말해 열지 않고 만지는 행동을 안내한다.  
**속도·쉼 계획:** 110단어/분, 에너지 2/5, 앞 150ms / 뒤 300ms. 강조: Feel · through your bag. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Make Feel tactile and gentle, connecting through your bag so the action is clearly felt through the fabric without opening it.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 가방을 열거나 책을 꺼내라는 지시처럼 끊기

**[S05-N041 · NEW] 피노키오:** “I can see its corners.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 천 위로 보이는 책 모서리를 알아본다 / 감정: 집중한 확인  
**말하는 방식:** 닫힌 가방 천 위로 보이는 책 모서리 윤곽에 시선만 모은다. 손끝은 닿지 않은 준비 상태로 두고, corners는 익숙한 책을 눈으로 알아본 작은 확신으로 말한다.  
**속도·쉼 계획:** 106단어/분, 에너지 2/5, 앞 150ms / 뒤 280ms. 강조: corners. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Focus on the visible outline of the book corners in the closed bag; keep fingertips poised without contact. Recognize the familiar book rather than sound surprised by a new object.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 가방 안을 투시하는 마법 같은 신비 톤

### B07-C03 · 04:52–05:01 · PROMPT

**카메라:** TWO SHOT 50mm · 기억을 돕는 질문

**자율 행동·연출:** 피노키오 손이 가방 옆에서 준비되고 귀뚜라미가 윤수 쪽으로 몸을 돌린다. 마지막 질문 종료 시점에서 외부 대기. 가방에 손이 닿는 본반응은 다음 컷.

**시간 배정:** 발화 전 행동 3.8초 / 발화 뒤 행동 0초. 대사·쉼·지정 행동 계획 합계 7.44초. 실제 합성 길이는 별도 확인.

**[S05-N042 · NEW] 귀뚜라미:** “Yoonsu, can you help him remember?”

**음성 연기:** CRICKET_DESIGN_V1 → 윤수 / 의도: 촉각과 시선으로 약속을 떠올리도록 도움을 청한다 / 감정: 낮고 따뜻한 초대  
**말하는 방식:** help him remember를 한 호흡으로 이어 윤수를 도우미로 맞는다. 약속 내용을 시험하거나 암송시키는 말투는 피한다.  
**속도·쉼 계획:** 108단어/분, 에너지 2/5, 앞 170ms / 뒤 0ms. 강조: help · remember. Yoonsu, 뒤 140ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Invite Yoonsu to help him remember through the visible action. Keep the request warm and connected, never a memory test or a demand to recite.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 윤수에게 책임이나 죄책감을 전가하는 진지함

**윤수 참여 7/10 · S05-P05 · 본편 밖 입력 대기**

- 질문 종료 시점: 301초. 본편 시계를 멈춘다.
- 첫 모델 예시: **“Touch your bag!”** — 귀뚜라미의 같은 고정 목소리.
- 모델 예시를 한 번 들려준 뒤 마이크를 켠다. 정확한 단어·발음 채점은 하지 않는다.
- 보호자 터치는 예시를 생략하고 반응으로 진행할 수 있다. 무응답5초 뒤 다시 듣기/터치를 제시한다.
- 시범: 귀뚜라미가 가방 속 책의 모서리 윤곽을 가리킨다. 피노키오가 손을 가방 옆에 두어 그 위치를 보여준다.
- 대기 상태: 손은 가방에 닿기 직전, 책은 가방 안, 끈은 어깨. 약속을 기억하는 질문이며 정답 채점은 없다.
- 입력 뒤 한 번 실행: 가방 천 위에 손바닥을 얹음→책의 모서리를 손끝으로 느껴봄→학교 방향으로 눈길을 돌리고 잠깐 망설임.
- 첫 재개: S05-N043 “My book is still here.”

**예시 음성 연기:**

**음성 연기:** CRICKET_DESIGN_V1 → 윤수(본편 밖 따라 말하기 예시) / 의도: 가방을 만져 약속을 떠올리는 짧은 말을 들려준다 / 감정: 안심시키는 도움  
**말하는 방식:** Touch를 손바닥이 닿는 부드러움으로 시작해 your bag을 붙여 말한다. 아이에게 자기 가방 준비를 요구하는 시험이 아니다.  
**속도·쉼 계획:** 80단어/분, 에너지 2/5, 앞 120ms / 뒤 360ms. 강조: Touch · bag. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Begin Touch with a soft tactile quality, connecting your bag. Model the story instruction without requiring the listener to own or fetch a bag.  
**피할 연기:** 세 단어를 낱말 시험처럼 끊거나 큰 소리로 채점하기; 본편 인물의 지식·입모양·발견 반응을 먼저 바꾸기

### B07-C04 · 05:01–05:12 · REACT

**카메라:** CU→MS 55mm · 소품과 마음

**자율 행동·연출:** 손바닥이 가방에 닿고 손끝이 책 모서리를 짚는다. 피노키오 눈이 학교 방향을 향하며 어깨가 조금 내려간다. 물체 접촉과 표정 변화가 동시에 읽히게 한다.

**시간 배정:** 발화 전 행동 4.0초 / 발화 뒤 행동 0.6초. 대사·쉼·지정 행동 계획 합계 10.85초. 실제 합성 길이는 별도 확인.

**[S05-N043 · NEW] 피노키오:** “My book is still here.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 가방 안에 같은 책이 있음을 만져 확인한다 / 감정: 안심에서 생각에 잠김으로  
**말하는 방식:** My book은 손끝으로 확인한 친숙함, still here는 안심 뒤 잠깐 생각이 남는 끝맺음으로 말한다.  
**속도·쉼 계획:** 104단어/분, 에너지 2/5, 앞 170ms / 뒤 350ms. 강조: My book · still here. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Begin with the familiarity of My book under your fingertips, then let still here settle from reassurance into a small reflective thought.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 책을 잃었다가 찾은 사건처럼 큰 안도

**[S05-N044 · NEW] 귀뚜라미:** “So is your promise.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 책과 함께 약속도 여전히 유효함을 짚는다 / 감정: 부드럽고 단단한 상기  
**말하는 방식:** So is는 바로 앞 말을 조용히 이어 받고 promise만 낮게 짚는다. 재치 있는 승리나 도덕 문제의 정답 발표가 아니다.  
**속도·쉼 계획:** 106단어/분, 에너지 2/5, 앞 200ms / 뒤 380ms. 강조: promise. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Join directly to his observation on So is, placing a quiet emphasis on promise. Stay caring and grounded, without a clever gotcha or moral verdict.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 상대를 궁지에 몰아넣는 따지는 어조

### B07-C05 · 05:12–05:20 · NARRATIVE

**카메라:** PROFILE 45mm · 기억하지만 머무는 얼굴

**자율 행동·연출:** 피노키오가 U016을 말하고 다시 닫힌 무대 커튼을 본다. 무대가 아직 시작 전이라는 사실을 머물 이유로 삼는 표정. 귀뚜라미는 가방과 피노키오를 조용히 번갈아 본다.

**시간 배정:** 발화 전 행동 0.4초 / 발화 뒤 행동 1.0초. 대사·쉼·지정 행동 계획 합계 7.59초. 실제 합성 길이는 별도 확인.

**[S05-U016 · ORIGINAL #16] 피노키오:** “I know, I know.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 약속을 안다고 말하며 자기 망설임을 얼른 덮는다 / 감정: 조금 방어적인 자기 안심  
**말하는 방식:** 첫 I know는 빠른 인정, 짧은 틈 뒤 두 번째는 음량을 조금 내려 스스로를 달랜다. 무례한 십대의 짜증으로 만들지 않는다.  
**속도·쉼 계획:** 106단어/분, 에너지 2/5, 앞 160ms / 뒤 300ms. 강조: know. I know, 뒤 180ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Make the first I know a quick acknowledgment, then soften the second into self-reassurance after a tiny gap. Avoid adolescent irritation.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 상대 말을 비웃거나 버럭 화내는 반항

**[S05-N045 · NEW] 피노키오:** “The show hasn't started yet.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 공연이 아직 시작 전이라는 이유로 머무름을 정당화한다 / 감정: 미련과 조심스러운 합리화  
**말하는 방식:** hasn't started yet을 변명처럼 과장하지 않고 자기가 납득하려는 작고 빠른 생각으로 말한다. 귀뚜라미에게 허락받았다는 자신감은 없다.  
**속도·쉼 계획:** 108단어/분, 에너지 2/5, 앞 180ms / 뒤 330ms. 강조: hasn't started yet. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Offer hasn't started yet as a small argument you are trying to believe yourself. Keep the wish to stay audible without sounding already permitted.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 서술자가 올바른 판단을 설명하는 확신

## B08. 작은 관객이 지나갈 자리

**목적:** 광장 관객에게 접근하는 동선을 실제로 보여 주고, 자신의 발이 통로를 막고 있음을 알아차려 자리를 양보한다.

**연속성:** 천막 발견 위치에서 관객 뒤쪽 진입점으로 이동하고, 작은 관객을 먼저 통과시킨 다음 오른쪽 바깥 통로를 따라 앞모서리까지 걷는다. 동물은 원본 S06의 무언 관객 일부이며 새 이름·대사 없음. 학교 길은 뒤로 이어진다.

### B08-C01 · 05:20–05:29 · NARRATIVE

**카메라:** WIDE 35mm · 관객 뒤 접근

**자율 행동·연출:** 피노키오와 귀뚜라미가 큰 나무 옆 발견 위치에서 관객 뒤쪽 진입점까지 몇 걸음 걸어온다. 중앙 통로로 들어서려는 작은 동물 관객 둘을 보고 속도를 줄인다. 무대는 정면 앞, 학교길은 뒤라는 공간축을 함께 보여 주며 귀뚜라미는 발과 통로 사이를 살핀다.

**시간 배정:** 발화 전 행동 1.8초 / 발화 뒤 행동 0.6초. 대사·쉼·지정 행동 계획 합계 8.17초. 실제 합성 길이는 별도 확인.

**[S05-N046 · NEW] 피노키오:** “Oh! More little visitors.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 다가오는 작은 동물 관객들을 알아본다 / 감정: 새 만남의 반가움  
**말하는 방식:** Oh는 짧은 발견, little visitors는 귀엽다고 내려다보는 미소로 말한다. 새 등장인물을 소개하는 진행자처럼 길게 열지 않는다.  
**속도·쉼 계획:** 111단어/분, 에너지 3/5, 앞 110ms / 뒤 280ms. 강조: little visitors. Oh! 뒤 120ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Let Oh be a brief notice, then smile at the little visitors approaching. Keep it a child's observation, not a formal introduction of a cast.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 작은 관객을 아기 취급하는 과장된 유아어

**[S05-N047 · NEW] 귀뚜라미:** “They're trying to get past.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 관객들이 지나가려는 필요를 알아차리게 한다 / 감정: 친절한 주의 환기  
**말하는 방식:** trying to get past를 가는 방향과 연결해 또렷하게 말한다. 피노키오의 잘못을 들추기보다 상대의 필요를 알려 준다.  
**속도·쉼 계획:** 113단어/분, 에너지 2/5, 앞 150ms / 뒤 290ms. 강조: get past. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Explain their need through trying to get past, following their intended path. Draw attention to the visitors, not blame toward Pinocchio.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 길을 막았다고 꾸짖는 불쾌감

### B08-C02 · 05:29–05:38 · NARRATIVE

**카메라:** LOW MS 45mm · 발과 통로

**자율 행동·연출:** 피노키오가 자기 발이 빈 통로에 놓인 것을 보고 발끝을 안으로 돌린다. 귀뚜라미가 한쪽으로 몸을 비켜 빈 공간을 시범한다. 동물들은 자연스럽게 발을 멈춘다.

**시간 배정:** 발화 전 행동 0.6초 / 발화 뒤 행동 1.0초. 대사·쉼·지정 행동 계획 합계 8.48초. 실제 합성 길이는 별도 확인.

**[S05-N048 · NEW] 피노키오:** “My feet are in their way.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 자신의 발이 통로를 막는 것을 스스로 깨닫는다 / 감정: 작은 머쓱함과 해결 의지  
**말하는 방식:** My feet에서 자기 발을 보며 웃음기만 살짝, in their way에서는 바로 고칠 수 있다는 이해를 담는다.  
**속도·쉼 계획:** 108단어/분, 에너지 2/5, 앞 140ms / 뒤 300ms. 강조: My feet · in their way. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Look down at your feet with a tiny sheepish smile, then recognize in their way as something you can easily fix.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 자기 잘못을 크게 비난하거나 사과를 추가 발화

**[S05-N049 · NEW] 귀뚜라미:** “Leave them a little path.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 작은 통로를 남겨 주는 쉬운 행동을 제안한다 / 감정: 구체적인 배려  
**말하는 방식:** little path를 좁은 틈에 맞춰 부드럽게 붙여 말한다. 크게 비키라고 몰아붙이는 말이 아니라 한 걸음의 방법이다.  
**속도·쉼 계획:** 113단어/분, 에너지 2/5, 앞 150ms / 뒤 300ms. 강조: little path. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Offer little path as a small, practical space he can make. Keep the instruction kind and proportionate to one easy step.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 사람들을 통제하는 교통 지휘관 구령

### B08-C03 · 05:38–05:47 · PROMPT

**카메라:** MS 50mm · 자리를 양보할 준비

**자율 행동·연출:** 피노키오가 지나갈 방향을 보고 한쪽 발을 가볍게 뗄 준비를 한다. 마지막 질문 종료 시점에서만 외부 대기한다.

**시간 배정:** 발화 전 행동 3.0초 / 발화 뒤 행동 0초. 대사·쉼·지정 행동 계획 합계 6.63초. 실제 합성 길이는 별도 확인.

**[S05-N050 · NEW] 피노키오:** “Yoonsu, how can I make room?”

**음성 연기:** PINOCCHIO_A → 윤수 / 의도: 자리를 비켜 주는 도움을 함께 만들자고 청한다 / 감정: 협력하는 의욕  
**말하는 방식:** make room을 한 번에 말하며 윤수를 자신의 도우미로 부른다. 난처한 상황을 해결해야 한다는 부담 대신 쉬운 참여를 준다.  
**속도·쉼 계획:** 107단어/분, 에너지 3/5, 앞 150ms / 뒤 0ms. 강조: make room. Yoonsu, 뒤 120ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Invite Yoonsu into a simple helpful action, connecting make room naturally. Sound ready to cooperate rather than desperate to solve a problem.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 관객이 충돌할 것 같은 다급함

**윤수 참여 8/10 · S05-P06 · 본편 밖 입력 대기**

- 질문 종료 시점: 347초. 본편 시계를 멈춘다.
- 첫 모델 예시: **“Let them through!”** — 피노키오의 같은 고정 목소리.
- 모델 예시를 한 번 들려준 뒤 마이크를 켠다. 정확한 단어·발음 채점은 하지 않는다.
- 보호자 터치는 예시를 생략하고 반응으로 진행할 수 있다. 무응답5초 뒤 다시 듣기/터치를 제시한다.
- 시범: 작은 관객 두 마리가 서로 부딪히지 않게 빈 통로로 지나가려는 행동을 먼저 보인다. 귀뚜라미가 옆의 여유 공간을 가리킨다.
- 대기 상태: 작은 관객은 피노키오 발 앞에서 안전하게 멈춘 상태, 충돌·겁먹는 비명 없음.
- 입력 뒤 한 번 실행: 피노키오가 오른쪽 빈 공간으로 한 걸음 비킴→손으로 중앙 통로 안내→작은 관객 둘이 차례로 완전히 지나감→마지막 관객이 발 앞을 벗어났음을 확인. 이 완료 후에 첫 재개 발화.
- 첫 재개: S05-N051 “There they go.”

**예시 음성 연기:**

**음성 연기:** PINOCCHIO_A → 윤수(본편 밖 따라 말하기 예시) / 의도: 작은 관객을 지나가게 해주는 표현을 들려준다 / 감정: 다정한 협력  
**말하는 방식:** Let them을 한 번에 말하고 through를 길 방향으로 열어 준다. 사람을 재촉하는 호통 없이 자연스럽게 연결한다.  
**속도·쉼 계획:** 82단어/분, 에너지 2/5, 앞 120ms / 뒤 360ms. 강조: through. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Say Let them together and open through toward the clear path. Offer one considerate phrase rather than shout for people to move.  
**피할 연기:** 세 단어를 낱말 시험처럼 끊거나 큰 소리로 채점하기; 본편 인물의 지식·입모양·발견 반응을 먼저 바꾸기

### B08-C04 · 05:47–05:59 · REACT

**카메라:** WIDE 40mm · 실제 통과

**자율 행동·연출:** 반응 시작 뒤 피노키오가 자기 오른쪽 빈 공간으로 한 걸음 비켜 손바닥으로 중앙 통로를 안내한다. 작은 관객 둘이 차례로 피노키오를 지나 앞자리로 향하고, 피노키오가 마지막 관객이 자기 발 앞을 완전히 지났음을 눈으로 확인한다. 이 반응이 끝난 뒤 N051과 결과를 확인하는 N052를 말한다. 다리·꼬리·가방의 동선은 겹치지 않는다.

**시간 배정:** 발화 전 행동 5.5초 / 발화 뒤 행동 0.7초. 대사·쉼·지정 행동 계획 합계 11.43초. 실제 합성 길이는 별도 확인.

**[S05-N051 · NEW] 피노키오:** “There they go.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미와 윤수 / 의도: 통로를 지나 앞자리로 향하는 관객을 눈으로 따라간다 / 감정: 편안한 만족  
**말하는 방식:** There they go를 지나간 뒤에도 이어 걷는 관객의 뒷모습에 가볍게 얹는다. 허락 명령이 아니라 관찰이다.  
**속도·쉼 계획:** 108단어/분, 에너지 2/5, 앞 130ms / 뒤 270ms. 강조: they go. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Place the phrase lightly over the visitors continuing toward their seats after passing you. It is an observation, not permission to begin.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 통과가 시작되기 전 구령처럼 외치기

**[S05-N052 · NEW] 귀뚜라미:** “You made room for them.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 이미 통로를 비워 준 행동의 결과를 알아봐 준다 / 감정: 따뜻하고 구체적인 인정  
**말하는 방식:** made room은 완료된 행동으로 분명히, for them은 방금 지나간 관객을 향한 관심으로 부드럽게 닫는다.  
**속도·쉼 계획:** 112단어/분, 에너지 2/5, 앞 160ms / 뒤 320ms. 강조: made room · for them. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Make made room clearly acknowledge the completed action, then soften for them toward the visitors who have passed. Praise the result without grading.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 아직 통과하지 않은 것처럼 can pass로 되돌아가기

### B08-C05 · 05:59–06:12 · NARRATIVE

**카메라:** TRACK 40mm · 자리 찾은 관객

**자율 행동·연출:** 관객 둘이 앞자리에 멈춘 뒤 피노키오와 귀뚜라미는 관객 오른쪽 바깥 통로를 따라 실제로 몇 걸음 걸어 앞모서리에 도착한다. 카메라가 시작점과 도착점을 한 번의 트랙으로 이어 중앙 통로를 건너뛰지 않았음을 보인다. 발끝은 무대 기단에서 자기 신발 한 개 길이 정도 떨어진 평평한 관객 바닥에 있고 무대에 오르지 않는다. 도착한 뒤 N053과 N054를 말한다. 왼쪽의 북 든 마라, 오른쪽 앞턱의 노출 대기 인형 둘, 뒤로 열린 학교길을 같은 축에 남긴다.

**시간 배정:** 발화 전 행동 5.0초 / 발화 뒤 행동 1.0초. 대사·쉼·지정 행동 계획 합계 12.47초. 실제 합성 길이는 별도 확인.

**[S05-N053 · NEW] 피노키오:** “They found their places.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 앞쪽 자리에 도착한 관객을 확인한다 / 감정: 작은 기쁨  
**말하는 방식:** found their places를 자기 발걸음이 멎은 자리에서 눈으로 확인하며 말한다. 좌석을 배정하는 어른처럼 설명하지 않는다.  
**속도·쉼 계획:** 109단어/분, 에너지 2/5, 앞 140ms / 뒤 290ms. 강조: their places. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Confirm that the visitors have settled as your own walk comes to a stop. Keep found their places a pleased observation, not an usher's announcement.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 갑자기 무대 앞에 생긴 위치를 덮는 빠른 설명

**[S05-N054 · NEW] 귀뚜라미:** “Our road is still behind us.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 학교로 돌아갈 길이 여전히 열려 있음을 상기한다 / 감정: 말없이 선택을 남기는 염려  
**말하는 방식:** still behind us를 뒤쪽 길로 시선을 돌리며 조금 낮게 말한다. 이제 돌아가라고 몰아붙이지도 머물자고 동의하지도 않는다.  
**속도·쉼 계획:** 109단어/분, 에너지 2/5, 앞 180ms / 뒤 360ms. 강조: road · still. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Lower the voice slightly as the eyeline returns to the open road behind. Leave the option present without ordering departure or endorsing staying.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 공연 입장을 축하하는 가벼운 말투

## B09. 책가방도 함께 자리를 잡기

**목적:** 새 공간에 들어왔어도 책을 잃거나 두고 가지 않는 연속성을 보장한다. 옆으로 튀어나온 가방을 몸 앞으로 옮겨 주변 관객을 배려한다.

**연속성:** B08-C05에서 걸어 도착한 관객 오른쪽 앞모서리에 그대로 선다. 끈은 어깨에 걸린 채 가방만 몸 앞으로 회전한다. 책은 S03에서 함께 본 뒤 넣은 같은 책으로 이후 꺼내거나 펼치지 않았다. 관객은 무언 반응만 한다.

### B09-C01 · 06:12–06:21 · NARRATIVE

**카메라:** MS 50mm · 가방과 관객의 간격

**자율 행동·연출:** B08-C05에서 걸어 도착한 오른쪽 앞모서리 그대로, 피노키오가 옆 관객을 돌아보다 가방이 그쪽으로 튀어나오는 것을 보고 즉시 멈춘다. 가까운 작은 관객은 고개만 돌린다. 실제 접촉·부상은 없고 피노키오의 발 위치나 무대까지 거리는 바뀌지 않는다.

**시간 배정:** 발화 전 행동 1.0초 / 발화 뒤 행동 0.7초. 대사·쉼·지정 행동 계획 합계 8.05초. 실제 합성 길이는 별도 확인.

**[S05-N055 · NEW] 피노키오:** “My bag is sticking out.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 가방이 옆 관객 쪽으로 튀어나온 것을 알아챈다 / 감정: 조심스러운 자기 관찰  
**말하는 방식:** bag을 살짝 짚고 sticking out은 몸을 멈추며 확인하는 말로 둔다. 이미 누군가를 친 것처럼 놀라지 않는다.  
**속도·쉼 계획:** 107단어/분, 에너지 2/5, 앞 130ms / 뒤 290ms. 강조: bag · sticking out. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Notice the bag protruding as you stop turning. Place sticking out carefully, without implying that anyone has already been struck.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 관객이 다친 사고처럼 비명을 내기

**[S05-N056 · NEW] 귀뚜라미:** “It needs a safer place.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 옆 사람에게 닿지 않는 위치를 함께 찾자고 한다 / 감정: 실용적이고 침착한 도움  
**말하는 방식:** safer place에 집중하며 몸 앞 빈 공간을 보게 한다. 가방을 혼내거나 새 캐릭터처럼 말을 거는 소리는 아니다.  
**속도·쉼 계획:** 112단어/분, 에너지 2/5, 앞 150ms / 뒤 300ms. 강조: safer place. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Focus on a safer place in the open space in front of him. Keep the practical care calm; do not talk to the bag as another character.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 실제로 위험한 사고가 임박했다는 과한 긴장

### B09-C02 · 06:21–06:29 · NARRATIVE

**카메라:** INSERT 60mm · 끈을 잡을 위치

**자율 행동·연출:** 피노키오가 끈을 눈으로 따라 어깨와 가방의 연결을 확인한다. 귀뚜라미는 몸 앞 빈 공간을 가리키고 피노키오는 양손을 나누어 준비한다.

**시간 배정:** 발화 전 행동 1.0초 / 발화 뒤 행동 0.8초. 대사·쉼·지정 행동 계획 합계 7.47초. 실제 합성 길이는 별도 확인.

**[S05-N057 · NEW] 피노키오:** “I can bring it round.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 가방을 몸 앞으로 돌릴 방법을 스스로 떠올린다 / 감정: 생각해 낸 자신감  
**말하는 방식:** I can을 작지만 확실하게, bring it round를 가방이 갈 경로를 눈으로 따라 자연스럽게 이어 말한다.  
**속도·쉼 계획:** 110단어/분, 에너지 3/5, 앞 140ms / 뒤 280ms. 강조: bring it round. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Let I can carry modest confidence, then connect bring it round while tracing the bag's path with your eyes.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 이미 가방 이동이 끝났다는 완료감

**[S05-N058 · NEW] 귀뚜라미:** “Keep the strap on.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 가방 운반끈을 어깨에 유지하도록 짧게 도와준다 / 감정: 간결한 주의  
**말하는 방식:** Keep은 차분히 시작하고 strap on을 한 묶음으로 말한다. 손과 끈의 관계가 읽힐 만큼 명료하되 딱딱한 구령은 없다.  
**속도·쉼 계획:** 114단어/분, 에너지 2/5, 앞 140ms / 뒤 280ms. 강조: strap on. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Keep the reminder compact and clear, joining strap on as one action condition. Sound like a companion watching the hands, not a drill instructor.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 가방 입구를 새로 묶으라는 지시처럼 말하기

### B09-C03 · 06:29–06:38 · PROMPT

**카메라:** MS 50mm · 이동 직전 질문

**자율 행동·연출:** 어깨 끈은 유지하고 손은 끈과 가방 옆에 준비한다. 마지막 질문 종료 시점에서 외부 대기하며 다음 컷에서만 가방 이동.

**시간 배정:** 발화 전 행동 2.2초 / 발화 뒤 행동 0초. 대사·쉼·지정 행동 계획 합계 6.44초. 실제 합성 길이는 별도 확인.

**[S05-N059 · NEW] 피노키오:** “Yoonsu, can you help me move it?”

**음성 연기:** PINOCCHIO_A → 윤수 / 의도: 가방을 옮기는 안전한 행동을 함께 해보자고 청한다 / 감정: 편안한 부탁  
**말하는 방식:** help me move it에서 도움받는 주체가 자신임을 자연스럽게 드러낸다. 빠르게 끝을 올려 입력을 재촉하지 않는다.  
**속도·쉼 계획:** 106단어/분, 에너지 3/5, 앞 150ms / 뒤 0ms. 강조: move it. Yoonsu, 뒤 130ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Ask for help with your own bag, keeping help me move it connected. Finish with a relaxed invitation rather than a rushed input cue.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 예시를 듣기도 전에 따라 말하라고 재촉하는 톤

**윤수 참여 9/10 · S05-P07 · 본편 밖 입력 대기**

- 질문 종료 시점: 398초. 본편 시계를 멈춘다.
- 첫 모델 예시: **“Move your bag!”** — 피노키오의 같은 고정 목소리.
- 모델 예시를 한 번 들려준 뒤 마이크를 켠다. 정확한 단어·발음 채점은 하지 않는다.
- 보호자 터치는 예시를 생략하고 반응으로 진행할 수 있다. 무응답5초 뒤 다시 듣기/터치를 제시한다.
- 시범: 귀뚜라미가 가방과 가까운 관객 사이의 좁은 틈을 가리키고 자신의 앞쪽을 빈 공간으로 보여준다. 피노키오가 끈을 잡을 준비를 한다.
- 대기 상태: 가방이 관객 옆으로 튀어나왔으나 접촉 전. 어깨 끈과 책의 위치 유지.
- 입력 뒤 한 번 실행: 끈을 한 손으로 고정→다른 손으로 가방을 몸 앞에 돌림→가방을 가슴 아래 안정시킴→옆 관객과의 틈을 확인.
- 첫 재개: S05-N060 “There. Right in front of me.”

**예시 음성 연기:**

**음성 연기:** PINOCCHIO_A → 윤수(본편 밖 따라 말하기 예시) / 의도: 가방을 몸 앞으로 옮기라는 표현을 들려준다 / 감정: 구체적이고 편안한 안내  
**말하는 방식:** Move your bag을 짧지만 끊지 않고 말한다. 가방을 빼앗거나 빨리 치우라는 날카로움을 넣지 않는다.  
**속도·쉼 계획:** 83단어/분, 에너지 2/5, 앞 120ms / 뒤 360ms. 강조: Move · bag. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Keep Move your bag compact but fully connected. Make it practical help, without the edge of ordering someone to clear an obstruction.  
**피할 연기:** 세 단어를 낱말 시험처럼 끊거나 큰 소리로 채점하기; 본편 인물의 지식·입모양·발견 반응을 먼저 바꾸기

### B09-C04 · 06:38–06:52 · REACT

**카메라:** THREE QUARTER 45mm · 가방 이동 반응

**자율 행동·연출:** 한 손은 끈을 고정하고 반대 손은 가방을 몸 앞에 천천히 돌린다. 가방 바닥이 옷을 통과하지 않게 몸과의 간격을 유지하고 손이 닿은 지점에 맞춰 움직인다.

**시간 배정:** 발화 전 행동 5.5초 / 발화 뒤 행동 0.6초. 대사·쉼·지정 행동 계획 합계 13.28초. 실제 합성 길이는 별도 확인.

**[S05-N060 · NEW] 피노키오:** “There. Right in front of me.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미와 윤수 / 의도: 가방이 몸 앞에 안정된 결과를 확인한다 / 감정: 손에 느껴지는 안도  
**말하는 방식:** There는 손이 가방을 놓아도 안정된 순간의 짧은 확인이다. 작은 틈 뒤 Right in front of me를 만족스럽게 말한다.  
**속도·쉼 계획:** 106단어/분, 에너지 2/5, 앞 130ms / 뒤 300ms. 강조: Right in front of me. There. 뒤 180ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Let There mark the moment the bag settles securely. After a small gap, enjoy Right in front of me as a tactile confirmation.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 가방이 아직 움직이는데 완료를 먼저 선언

**[S05-N061 · NEW] 귀뚜라미:** “And your book stays inside.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 가방을 옮겨도 같은 책은 안에 남아 있음을 상기한다 / 감정: 부드러운 확인  
**말하는 방식:** book과 inside를 가볍게 연결한다. 책을 새로 넣거나 열어 확인한 것처럼 새 사건의 발견을 만들지 않는다.  
**속도·쉼 계획:** 111단어/분, 에너지 2/5, 앞 160ms / 뒤 310ms. 강조: book · inside. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Gently connect book and inside, confirming the same book remains enclosed. Do not sound as if it was just inserted or opened.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 책의 미개봉 이력을 새로 단정하는 강한 설명

### B09-C05 · 06:52–07:02 · NARRATIVE

**카메라:** TWO SHOT 45mm · 여유와 선택

**자율 행동·연출:** 같은 앞모서리에서 피노키오가 옆 관객과의 틈을 확인한다. 귀뚜라미는 뒤로 이어진 학교길 쪽으로 몸을 반쯤 돌리고, 피노키오도 떠날 수 있도록 몸과 체중만 그쪽으로 옮긴다. N063 뒤 같은 북소리가 다시 들리자 시선이 무대로 돌아온다. 전진이나 새 자리 이동은 하지 않아 B10의 출발 위치가 그대로 보인다.

**시간 배정:** 발화 전 행동 0.7초 / 발화 뒤 행동 2.0초. 대사·쉼·지정 행동 계획 합계 9.30초. 실제 합성 길이는 별도 확인.

**[S05-N062 · NEW] 피노키오:** “Everyone has room now.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 옆 관객에게 닿지 않게 된 공간을 확인한다 / 감정: 작은 만족  
**말하는 방식:** Everyone에서 주변을 보고 room now는 편히 숨을 놓듯 말한다. 무대 전체를 관리하는 어른의 보고가 아니다.  
**속도·쉼 계획:** 109단어/분, 에너지 2/5, 앞 150ms / 뒤 300ms. 강조: room now. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Look around at the nearby visitors and let room now settle with a small release of ease. Speak as a considerate child, not the organizer.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 약속 문제까지 모두 해결됐다는 완결감

**[S05-N063 · NEW] 귀뚜라미:** “You still have time to leave.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 정리가 끝났으니 지금 떠날 선택도 가능함을 알려 준다 / 감정: 염려를 숨기지 않는 부드러움  
**말하는 방식:** still은 가능성이 남아 있음을, leave는 학교 길을 바라보며 조금 낮게 둔다. 따라가자고 강제하는 구령으로 바꾸지 않는다.  
**속도·쉼 계획:** 108단어/분, 에너지 2/5, 앞 210ms / 뒤 400ms. 강조: still · leave. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Let still keep the possibility open, then lower leave toward the school road. Make the concern clear without taking the decision away from him.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 잠깐 더 있어도 된다는 허락처럼 들리는 낙관

## B10. 한 발 뒤에서 시작을 기다리다

**목적:** 피노키오의 잠깐 보겠다는 원본 결정을 끝에 고정한다. 학교 약속을 아는 채 머무는 선택이 6화의 오래 머무름으로 이어지게 한다.

**연속성:** B08-C05부터 이어지는 관객 오른쪽 앞모서리의 평평한 바닥. B09에서 위치를 바꾸지 않았고 무대 위에 올라가지 않는다. 책이 든 가방은 몸 앞에서 끈 유지, 모자 착용·정상 코·마른 신발. 귀뚜라미는 바로 옆 땅. 마라는 왼쪽에서 북만 치고, 이름 없는 인형 둘은 오른쪽 앞턱의 노출 대기자리에 계속 보인다.

### B10-C01 · 07:02–07:13 · NARRATIVE

**카메라:** MS 50mm · 스스로 정한 한 분

**자율 행동·연출:** B09와 같은 오른쪽 앞모서리에서 피노키오가 막힘없는 학교 쪽 통로를 돌아본 뒤, 떠나려던 발을 멈추고 U017로 스스로 머무는 결정을 말한다. 귀뚜라미는 동의하는 끄덕임 없이 무대와의 간격 및 뒤쪽 빈자리를 가리킨다. 피노키오는 이미 평평한 관객 바닥에 있고 무대에 오르거나 공연 참여를 약속하지 않는다.

**시간 배정:** 발화 전 행동 0.8초 / 발화 뒤 행동 0.7초. 대사·쉼·지정 행동 계획 합계 10.05초. 실제 합성 길이는 별도 확인.

**[S05-U017 · ORIGINAL #17] 피노키오:** “I'll only watch for a minute.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 떠날 수 있음을 알지만 잠깐 보겠다고 스스로 정한다 / 감정: 미련이 담긴 자기 설득  
**말하는 방식:** only와 a minute를 작게 만들어 스스로 시간을 축소하는 마음을 담는다. 원본을 거짓말 고백이나 악의적인 속임수로 연기하지 않는다.  
**속도·쉼 계획:** 104단어/분, 에너지 2/5, 앞 240ms / 뒤 380ms. 강조: only · a minute. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Make only and a minute small as he persuades himself the delay is tiny. Keep the choice his own; do not play a calculated lie.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 학교를 버리겠다는 반항적 선언 또는 윤수 탓하기

**[S05-N064 · NEW] 귀뚜라미:** “The stage is close. Keep some space.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 머물겠다는 선택과 별개로 무대 앞 거리를 확보하게 한다 / 감정: 주의 깊은 동행  
**말하는 방식:** 첫 문장은 현재 거리를 관찰하고 짧게 쉬어 Keep some space를 친절히 안내한다. 공연을 보자고 맞장구치는 밝음은 넣지 않는다.  
**속도·쉼 계획:** 110단어/분, 에너지 2/5, 앞 170ms / 뒤 320ms. 강조: close · space. close. 뒤 160ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Observe the stage distance first, then offer Keep some space as practical care. Stay watchful without sounding pleased that he chose to stay.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 공연 참여를 권하거나 무대에 오르라는 열광

### B10-C02 · 07:13–07:22 · NARRATIVE

**카메라:** LOW MS 40mm · 무대 앞 거리

**자율 행동·연출:** 피노키오가 같은 자리에서 발끝과 무대 기단 사이의 간격을 내려다보며 N065를 말한다. 그 말 동안 귀뚜라미가 뒤쪽 빈자리로 한 걸음 물러나고, 자기 위치를 가리키며 N066을 말한다. 피노키오는 아직 뒤로 이동하지 않는다. 평평한 바닥이며 낭떠러지나 새 장애물은 만들지 않는다.

**시간 배정:** 발화 전 행동 0.8초 / 발화 뒤 행동 1.0초. 대사·쉼·지정 행동 계획 합계 8.77초. 실제 합성 길이는 별도 확인.

**[S05-N065 · NEW] 피노키오:** “My toes are near the edge.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미 / 의도: 발끝과 무대 기단 사이의 짧은 간격을 알아본다 / 감정: 집중한 확인  
**말하는 방식:** toes와 edge를 눈으로 재는 느낌으로 차분하게 말한다. 평평한 관객 바닥에 서 있으므로 낭떠러지 공포를 만들지 않는다.  
**속도·쉼 계획:** 106단어/분, 에너지 2/5, 앞 150ms / 뒤 300ms. 강조: toes · edge. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Measure the visible gap with the words toes and edge, staying calm on the flat audience floor. No fear of a cliff or fall.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 추락 직전의 떨림이나 비명

**[S05-N066 · NEW] 귀뚜라미:** “This spot is far enough.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 자기가 뒤로 옮겨 선 자리를 거리의 기준으로 보여 준다 / 감정: 안심시키는 시범  
**말하는 방식:** This spot은 귀뚜라미 자신의 새 위치를 가리킨다. far enough에 적당한 거리라는 확신을 주되 피노키오도 이미 이동했다고 말하지 않는다.  
**속도·쉼 계획:** 112단어/분, 에너지 2/5, 앞 150ms / 뒤 300ms. 강조: This spot · far enough. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Indicate your own stepped-back position on This spot, making far enough reassuringly clear. Do not imply Pinocchio has already moved.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 아직 앞에 선 피노키오의 완료를 칭찬

### B10-C03 · 07:22–07:30 · PROMPT

**카메라:** TWO SHOT 45mm · 마지막 질문

**자율 행동·연출:** 귀뚜라미가 뒤쪽 빈자리를 가리키고 피노키오는 옮길 발에 체중을 준비한다. 질문 종료 시점에서 외부 대기. 화면의 기다림은 계획 본편 시간에 넣지 않는다.

**시간 배정:** 발화 전 행동 3.2초 / 발화 뒤 행동 0초. 대사·쉼·지정 행동 계획 합계 7.38초. 실제 합성 길이는 별도 확인.

**[S05-N067 · NEW] 귀뚜라미:** “Yoonsu, can you help him step back?”

**음성 연기:** CRICKET_DESIGN_V1 → 윤수 / 의도: 보여 준 빈자리로 한 걸음 물러나도록 도움을 청한다 / 감정: 차분한 협력  
**말하는 방식:** step back을 연결해 부드럽게 안내한다. 마지막 참여라는 이유로 더 크거나 빠른 진행자 목소리를 내지 않는다.  
**속도·쉼 계획:** 108단어/분, 에너지 2/5, 앞 170ms / 뒤 0ms. 강조: step back. Yoonsu, 뒤 120ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Connect step back as one gentle movement and invite cooperation. Do not become louder or more performative because this is the last interaction.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 마지막 문제를 외치는 수업 진행자 톤

**윤수 참여 10/10 · S05-P08 · 본편 밖 입력 대기**

- 질문 종료 시점: 450초. 본편 시계를 멈춘다.
- 첫 모델 예시: **“Step back, please!”** — 귀뚜라미의 같은 고정 목소리.
- 모델 예시를 한 번 들려준 뒤 마이크를 켠다. 정확한 단어·발음 채점은 하지 않는다.
- 보호자 터치는 예시를 생략하고 반응으로 진행할 수 있다. 무응답5초 뒤 다시 듣기/터치를 제시한다.
- 시범: 귀뚜라미가 무대 앞 가장자리와 피노키오 발 사이 거리를 보여주고 자신의 몸을 한 걸음 뒤로 옮기는 시범.
- 대기 상태: 피노키오는 B08-C05부터 같은 오른쪽 앞모서리의 평평한 관객 바닥에 서 있다. 발끝이 무대 기단 가까우나 무대 위가 아니며 뒤쪽 빈자리와 중앙 통로가 함께 보인다.
- 입력 뒤 한 번 실행: 관객 오른쪽 바깥 통로의 빈자리로 한 발씩 뒤로 물러남→두 발 접지→무대와 거리 확인→몸 앞 가방 안정→귀뚜라미가 같은 쪽 옆에 자리함. 중앙 통로는 막지 않음.
- 첫 재개: S05-N068 “Now there is room.”

**예시 음성 연기:**

**음성 연기:** CRICKET_DESIGN_V1 → 윤수(본편 밖 따라 말하기 예시) / 의도: 한 발 물러나는 공손한 표현을 들려준다 / 감정: 차분한 배려  
**말하는 방식:** Step back을 이어서 말하고 please에 부드럽게 힘을 뺀다. 마지막 단어를 상벌의 조건처럼 강조하지 않는다.  
**속도·쉼 계획:** 81단어/분, 에너지 2/5, 앞 120ms / 뒤 360ms. 강조: Step back · please. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Connect Step back, then soften into please. Offer a polite, easy movement without treating the final word as a rule to be tested.  
**피할 연기:** 세 단어를 낱말 시험처럼 끊거나 큰 소리로 채점하기; 본편 인물의 지식·입모양·발견 반응을 먼저 바꾸기

### B10-C04 · 07:30–07:42 · REACT

**카메라:** WIDE 40mm · 최종 자리 맞춤

**자율 행동·연출:** 응답 뒤 피노키오가 관객 오른쪽 바깥 통로의 빈자리 쪽으로 두 발을 순서대로 한 걸음씩 뒤로 옮긴다. 두 발 접지와 몸 앞 가방 안정이 끝난 다음 귀뚜라미가 같은 쪽 옆에 자리한다. N068과 N069는 이 완료 뒤에 재개한다. 중앙 관객 통로와 학교길은 계속 열려 있고 무대에 오르지 않는다.

**시간 배정:** 발화 전 행동 4.5초 / 발화 뒤 행동 1.2초. 대사·쉼·지정 행동 계획 합계 11.28초. 실제 합성 길이는 별도 확인.

**[S05-N068 · NEW] 피노키오:** “Now there is room.”

**음성 연기:** PINOCCHIO_A → 귀뚜라미와 윤수 / 의도: 뒤로 물러난 뒤 확보된 공간을 몸으로 확인한다 / 감정: 편안해진 안도  
**말하는 방식:** 두 발이 닿고 가방이 멎은 뒤 Now를 시작한다. room은 여유가 생긴 느낌으로 넓고 부드럽게 끝낸다.  
**속도·쉼 계획:** 105단어/분, 에너지 2/5, 앞 150ms / 뒤 300ms. 강조: Now · room. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Begin Now only after both feet and the bag settle. Let room open gently into the comfort of the space gained.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 무대 위에 올라간 듯한 환호나 승리감

**[S05-N069 · NEW] 귀뚜라미:** “I'm staying beside you.”

**음성 연기:** CRICKET_DESIGN_V1 → 피노키오 / 의도: 친구 곁을 지키겠다고 조용히 약속한다 / 감정: 다정함 속 남아 있는 걱정  
**말하는 방식:** beside you는 가까이 있는 친구에게 낮게 말한다. 함께 공연을 즐기겠다는 신난 동의 대신 걱정하며 지켜보는 동행을 남긴다.  
**속도·쉼 계획:** 107단어/분, 에너지 2/5, 앞 220ms / 뒤 380ms. 강조: beside you. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Offer beside you quietly to the friend at your side. Keep a trace of concern: companionship and care, not eager agreement to watch the show.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 머무르기로 한 선택을 축하하는 들뜬 말투

### B10-C05 · 07:42–07:52 · NARRATIVE

**카메라:** WIDE 35mm · S06 첫 구도로 인계

**자율 행동·연출:** 원본 U018만 마지막 음성으로 들린다. 피노키오의 기대와 귀뚜라미의 걱정을 함께 담고, 왼쪽 마라가 같은 북 모티프를 친다. 오른쪽 앞턱의 이름 없는 인형 둘은 가림판 바깥 노출 대기자리에서 S06-U003까지 계속 보인다. 본무대 커튼은 닫혀 있고 조명 점등·밧줄 당기기·핍 소개는 없다. 같은 아침빛과 북소리를 유지해 S06 마라의 첫 인사로 잇는다.

**시간 배정:** 발화 전 행동 0.4초 / 발화 뒤 행동 1.0초. 대사·쉼·지정 행동 계획 합계 9.03초. 실제 합성 길이는 별도 확인.

**[S05-U018 · ORIGINAL #18] 내레이션:** “But sometimes, one little minute can turn into a very long time.”

**음성 연기:** NARRATOR_A → 시청자 / 의도: 작은 미룸이 길어질 수 있음을 다음 장면으로 열어 둔다 / 감정: 따뜻한 예감과 절제된 염려  
**말하는 방식:** one little minute는 아이가 작게 여긴 시간을 이해하듯, very long time은 조금 넓혀 조용히 대비한다. 벌이나 공포를 예고하지 않는다.  
**속도·쉼 계획:** 106단어/분, 에너지 2/5, 앞 220ms / 뒤 380ms. 강조: one little minute · very long time. minute 뒤 240ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Understand the smallness he gives one little minute, then widen very long time with restrained concern. Leave a warm, open consequence hint, never a threat.  
**피할 연기:** 한 줄마다 똑같은 낭독 하강조; 도덕 교훈을 과장하는 낭독 또는 공포 예고 음성

## 실제 제작 상태

위 대사·연기·시간은 설계다. 실제 합성·청취·립싱크·VAD·영상 재생은 NOT_RUN이다. 귀뚜라미의 승인 참조 음색은 BLOCKED_RESOURCE이며 다른 성우로 대체하지 않는다.
