# 캐릭터 목소리·대사 연기 기준 V2.1

**적용:** 3·4·5화의 모든 대사와 예시 음성. 12장면 전체의 7개 발화 캐릭터 음색 기준도 함께 정의한다. 1·2화 완료본은 수정·재합성하지 않는다.

## 1. 가장 중요한 구분

**같은 캐릭터는 같은 성우를 유지한다. 감정과 말하는 목적은 문장마다 바뀐다.** 피노키오 A·제페토 A·내레이션 A·파란 요정 C는 기존 승인 MP3를 그대로 기준으로 쓴다. 귀뚜라미·마라·핍은 아래 연기 설계가 완성됐지만 승인 음색 참조는 아직 없다. 다른 캐릭터의 목소리로 채우지 않는다.

현재 3·4화의 이전 합성 호출은 대사와 참조 음원만 전달했다. 이 문서와 줄별 지시를 엔진의 실제 지원 기능으로 전달하고 청취 확인해야 한다. 문서 작성만으로 새 음성이 감정적으로 바뀌었다고 표시하지 않는다.

## 2. 전체 캐스트

|캐릭터|고정 ID|목소리와 관계|음색 상태|
|---|---|---|---|
|피노키오|`PINOCCHIO_A`|기존 승인 A. 밝은 어린 남자아이 인상. 순수함과 호기심이 먼저 들리는 목소리.|USER_APPROVED_REFERENCE_LOCKED|
|제페토|`GEPPETTO_A`|기존 승인 A. 80대 할아버지처럼 들리는 연령감, 낮고 따뜻한 울림, 손자를 오래 바라보는 여유.|USER_APPROVED_REFERENCE_LOCKED|
|내레이션|`NARRATOR_A`|기존 승인 A. 따뜻하고 안정적인 성인 이야기꾼. 제페토보다 연령감이 적고 문장 윤곽이 분명하다.|USER_APPROVED_REFERENCE_LOCKED|
|파란 요정|`BLUE_FAIRY_C`|기존 승인 C. 맑고 차분한 성인 여성의 신비로움과 따뜻함.|USER_APPROVED_REFERENCE_LOCKED|
|귀뚜라미|`CRICKET_DESIGN_V1`|신규 음색 설계. 작고 민첩한 동행자, 또렷한 중음~중고음의 친근한 형 같은 인상. 승인 참조는 아직 없음.|PROFILE_AUTHORED_REFERENCE_PENDING|
|마라|`MARA_DESIGN_V1`|신규 음색 설계. 객석을 편하게 맞이하는 성인 공연 진행자. 넓게 전달되는 중음의 따뜻한 공명. 승인 참조는 아직 없음.|PROFILE_AUTHORED_REFERENCE_PENDING|
|핍|`PIP_DESIGN_V1`|신규 음색 설계. 공연하는 작은 인형의 밝고 탄력 있는 목소리. 피노키오보다 리듬감과 무대 자신감이 있으나 별개의 화자. 승인 참조는 아직 없음.|PROFILE_AUTHORED_REFERENCE_PENDING|

## 3. 모든 대사에 적용하는 연기 규칙

- 대사는 상대에게 목적을 가지고 말한다. 직전의 말과 눈앞의 행동에 반응한 뒤 말하며 모든 줄을 같은 높낮이로 읽지 않는다.
- voice_direction은 연기 지시이고 text/spoken_text만 실제 발화한다. 한국어 지시, 영어 연기 프롬프트, 인물 이름, ID, 감정 태그, context는 읽지 않는다.
- 원본 대사 글자·문장부호·화자·순서를 보존한다. 원문에 없는 Oh/Ha-ha/이름/설명을 임의 삽입하지 않는다.
- 참조 음원은 화자 정체성 기준이다. 평평한 한 줄의 억양을 전체 대사에 복제하지 않는다. 목소리·나이·억양이 다른 캐릭터로 바뀌면 실패다.
- 속도와 쉼은 계획 목표다. 실제 WAV를 측정해 컷을 조정하며 음성을 빠르게 늘이거나 의미 없는 침묵으로 영상 분량을 채우지 않는다.
- 질문과 첫 모델 예시가 끝난 뒤에만 마이크를 켠다. 예시는 본편 시간 밖에서 별도 파일로 만든다.
- 감정 지시를 메타데이터에 적기만 하고 엔진에 전달하지 않은 실행은 연기 적용 PASS가 아니다.
- 실제 청취로 화자 일치·대화성·감정전환·명료도·문구 보존을 확인한다. 자동 파형/길이 검사만으로 연기를 통과시키지 않는다.

## 4. 피노키오 — PINOCCHIO_A

기존 승인 A. 밝은 어린 남자아이 인상. 순수함과 호기심이 먼저 들리는 목소리.

- **음역·질감:** 승인 음원의 소년 음색·공명·발음 습관을 유지한다. 억지 고음·아기 말투·성인 남성 낭독 금지.
- **연령 인상:** 약 8세 소년의 인상이며 실제 화자 나이를 뜻하지 않음
- **관계:** 제페토에게는 믿고 기대는 손자, 귀뚜라미에게는 궁금한 것을 바로 묻는 친구, 윤수에게는 함께 해결하자고 청하는 친구.
- **말 빠르기 계획 범위:** 95~120단어/분. 실제 음성 측정값이 아니다.
- **현재 상태:** REFERENCE_READY_ACTING_NOT_YET_GENERATED

### 상황에 따라 달라지는 연기

- **curiosity:** 먼저 보고 놀란 뒤 궁금한 단어만 살짝 올린다. 모든 문장 끝을 올리지 않는다.
- **discovery:** 짧은 숨과 반 박자 뒤 눈앞에 새로 보인 대상에 소리가 밝아진다. 처음부터 끝까지 같은 들뜬 소리 금지.
- **difficulty:** 잠깐 망설이고 상대를 찾는다. 긴 투정·징징거림·울음으로 바꾸지 않는다.
- **promise:** 놀이하던 속도를 잠깐 낮추고 제페토의 눈을 보며 진심으로 받는다. 어른처럼 엄숙한 선언 금지.
- **temptation:** 학교 약속을 알고도 공연에 마음이 가는 작은 들뜸과 머뭇거림. 버릇없게 비웃거나 악동처럼 연기하지 않는다.
- **후반 고백·도움:** 자신의 선택을 인정하는 진심, 친구를 돕는 집중을 표현한다. S12 인간 모습으로 바뀌어도 피노키오 A의 같은 목소리와 이름을 유지한다.

### 피해야 할 연기

- 피노키오·핍·귀뚜라미를 같은 목소리로 처리
- 모든 느낌표를 고함으로 처리
- 매 문장 같은 웃음과 같은 상승조
- 캐릭터 나이를 낮추려고 음원을 일괄 피치업

### 합성 도구에 전달할 기본 영어 연기 지시

> Keep the exact approved Pinocchio A voice identity: a bright young boy. Play a child responding to something happening in front of him, with genuine curiosity, brief thought changes and a warm connection to his partner. Never read like an adult narrator; never make him a squeaky baby.

이 문장은 발화 텍스트가 아니다. 각 줄의 `direction_en`과 함께 연기 입력으로만 사용한다.

### 비교할 짧은 연기 예시

|실제 대사|연기 방향|
|---|---|
|“School?”|방금 처음 들은 단어를 이해하려는 짧은 되물음. 놀람에서 기대감으로.|
|“I will, Grandpa!”|장난을 잠깐 멈추고 약속을 받아들이는 진심. Grandpa는 따뜻하게.|
|“I'll only watch for a minute.”|학교를 떠올린 뒤 스스로를 설득하는 작은 핑계. minute를 가볍게 강조하되 비웃지 않음.|

**고정 참조:** `assets/voice_refs/v6/pinocchio_V6_APPROVED.mp3`  
**SHA-256:** `a32569705a717ac92c8ecbe1c515b9e31e389f508164458ed22a06adcbba0b3d`

## 5. 제페토 — GEPPETTO_A

기존 승인 A. 80대 할아버지처럼 들리는 연령감, 낮고 따뜻한 울림, 손자를 오래 바라보는 여유.

- **음역·질감:** 노년의 중저음과 부드러운 숨결. 나이의 결을 주되 거친 가래 소리나 끊임없는 떨림으로 명료도를 잃지 않는다.
- **연령 인상:** 승인 참조의 82세 할아버지 의도 유지; 젊은 아빠처럼 들리지 않게 연기
- **관계:** 가르치는 교과서 화자가 아니라 손자를 직접 돌보는 할아버지. 윤수에게도 따뜻하게 도움을 청한다.
- **말 빠르기 계획 범위:** 85~105단어/분. 실제 음성 측정값이 아니다.
- **현재 상태:** REFERENCE_READY_ACTING_NOT_YET_GENERATED

### 상황에 따라 달라지는 연기

- **delight:** 입가의 작은 미소와 낮은 웃음기만 담는다. 문장마다 실제 웃음 소리를 추가하지 않는다.
- **guidance:** 아이의 시선을 확인한 뒤 한 생각씩 짧게 말한다. 훈계·아나운서 전달조 금지.
- **searching:** 자신도 잠깐 생각하고 손을 멈춘다. 답을 이미 아는 시험 선생님처럼 묻지 않는다.
- **reassurance:** 음량보다 속도와 말끝의 안정으로 안심시킨다. 실패를 놀리는 소리 금지.
- **promise:** Listen carefully에서 시선을 맞추고, school과before supper에 따뜻한 무게를 둔다. 엄한 명령보다 걱정과 신뢰가 들려야 한다.
- **후반 기다림·화해:** 문 쪽 소리에 귀를 기울이는 낮은 걱정, 거짓말을 알았을 때의 작은 멈춤과 상처, 고백 뒤 천천히 돌아오는 따뜻함을 구분한다. 화난 추궁·불길한 독백으로 만들지 않는다.

### 피해야 할 연기

- 젊은 남성 내레이터 같은 깨끗하고 빠른 전달
- 나이를 표현하려고 모든 음절을 떨거나 기침 추가
- 약속 장면을 화내는 훈계로 변환
- 문장마다 끝을 같은 깊이로 떨어뜨림

### 합성 도구에 전달할 기본 영어 연기 지시

> Keep the approved Geppetto A voice identity, with a convincingly elderly grandfather presence. Use a warm low-middle resonance, a little age in the breath and patient thought-sized phrases. Speak to his grandson, not to a microphone. Be clear and affectionate, never a young father, a flat narrator, or a caricatured croak.

이 문장은 발화 텍스트가 아니다. 각 줄의 `direction_en`과 함께 연기 입력으로만 사용한다.

### 비교할 짧은 연기 예시

|실제 대사|연기 방향|
|---|---|
|“Today is your first day at school!”|손자의 새 출발을 자랑스러워하는 미소. 큰 발표가 아니라 가까이 건네는 기쁜 소식.|
|“You're still learning.”|모자를 어려워하는 손자를 보고 안심시킴. still은 부드럽게, learning에서 안정되게 마침.|
|“Go to school and come home before supper.”|학교에 대한 기대와 안전한 귀가에 대한 걱정을 한 생각씩. before supper 앞에 작은 쉼.|

**고정 참조:** `assets/voice_refs/v6/geppetto_V6_APPROVED.mp3`  
**SHA-256:** `80237e647e1e480987a3cf0a6ac1dc33a3d6b3a40dc62d577f4a0290e338af55`

## 6. 내레이션 — NARRATOR_A

기존 승인 A. 따뜻하고 안정적인 성인 이야기꾼. 제페토보다 연령감이 적고 문장 윤곽이 분명하다.

- **음역·질감:** 중저음 중심의 편안한 공명. 보이는 사건을 함께 지켜보며 말한다. 모든 인물의 음성을 흉내 내지 않는다.
- **연령 인상:** 성인; 노년 캐릭터 연기는 제페토에게만
- **관계:** 윤수에게 이야기를 곁에서 건네는 안내자. 화면에서 이미 보이는 사건에 감정의 방향과 전환을 보탠다.
- **말 빠르기 계획 범위:** 100~120단어/분. 실제 음성 측정값이 아니다.
- **현재 상태:** REFERENCE_READY_ACTING_NOT_YET_GENERATED

### 상황에 따라 달라지는 연기

- **warm_start:** 첫 생각은 여유 있게 시작하고 다음 행동으로 자연스럽게 흐른다. 동화책 제목을 낭독하는 조 금지.
- **movement:** 걸음과 시선의 진행에 맞춰 문장이 앞으로 간다. 단어마다 동일 간격 금지.
- **surprise:** 새 사건 직전 살짝 속도를 줄이고 사건 단어에서만 색을 바꾼다. 과도한 서스펜스 금지.
- **foreshadow:** 미래의 결과를 조용히 암시한다. 무서운 예고편 음성으로 바꾸지 않는다.
- **joy:** 따뜻한 미소가 들리되 피노키오의 흥분과 경쟁하지 않는다.

### 피해야 할 연기

- 모든 문장 시작·끝의 동일한 선율
- 문장 사이 같은 길이의 긴 무음
- 피노키오·제페토를 흉내 내는 과장
- 마지막 교훈을 무서운 경고로 말함

### 합성 도구에 전달할 기본 영어 연기 지시

> Keep the approved narrator A identity. Tell the story warmly to one child while watching the action unfold. Shape each sentence around a new thought and the visual event. Use gentle variation and meaningful pauses, not metronomic audiobook cadence or the voices of the characters.

이 문장은 발화 텍스트가 아니다. 각 줄의 `direction_en`과 함께 연기 입력으로만 사용한다.

### 비교할 짧은 연기 예시

|실제 대사|연기 방향|
|---|---|
|“Pinocchio followed the little road.”|발걸음을 따라 따뜻하게 앞으로 흘러감.|
|“But then, he heard a strange and wonderful sound.”|But then 뒤 작은 전환. strange에 궁금함, wonderful에 부드러운 밝음.|
|“But sometimes, one little minute can turn into a very long time.”|one little minute와very long time의 차이를 부드럽게 대비. 꾸짖거나 겁주지 않음.|

**고정 참조:** `assets/voice_refs/v6/narrator_V6_APPROVED.mp3`  
**SHA-256:** `ec7234237b687246af302db312994c6b9ddc46411c82085a5b1f3884bcfcbddf`

## 7. 파란 요정 — BLUE_FAIRY_C

기존 승인 C. 맑고 차분한 성인 여성의 신비로움과 따뜻함.

- **음역·질감:** 깨끗한 중고음, 또렷한 자음과 부드러운 연결. 숨소리·속삭임·잔향으로 대사를 가리지 않는다.
- **연령 인상:** 차분한 성인; 어린 소녀나 내레이터와 혼용하지 않음
- **관계:** 피노키오와 제페토를 존중하는 조력자. 친절과 진실을 말할 때도 판결자가 되지 않는다.
- **말 빠르기 계획 범위:** 90~105단어/분. 실제 음성 측정값이 아니다.
- **현재 상태:** REFERENCE_READY_ACTING_NOT_YET_GENERATED

### 상황에 따라 달라지는 연기

- **arrival:** 친절하게 먼저 눈을 맞추는 미소. 위압적인 신의 음성 금지.
- **magic:** 확신과 조용한 기쁨. 단어를 지나치게 길게 늘이지 않음.
- **guidance:** 작은 쉼으로 생각할 자리를 주고 부드럽게 핵심을 짚음.
- **forgiveness:** 잘못보다 솔직해진 용기를 먼저 알아주는 온기.
- **transformation:** 기쁨을 차분하게 키우되 피노키오의 감정을 덮지 않음.

### 피해야 할 연기

- 모든 음절의 과도한 속삭임
- 웅장한 잔향으로 명료도 손상
- 내레이션 A 또는 피노키오 A 대체
- 교훈을 차갑게 훈계

### 합성 도구에 전달할 기본 영어 연기 지시

> Keep the exact approved Blue Fairy C identity. Use a clear, graceful adult feminine tone, gentle assurance and warm attention to the listener. Magical means poised and kind, not breathy, echo-heavy, hypnotic or emotionally distant.

이 문장은 발화 텍스트가 아니다. 각 줄의 `direction_en`과 함께 연기 입력으로만 사용한다.

### 비교할 짧은 연기 예시

|실제 대사|연기 방향|
|---|---|
|“Good evening, Geppetto.”|가까이서 안심시키며 인사. Geppetto에 부드럽게 시선이 닿음.|
|“Let me give him a little magic.”|선물을 건네듯 작은 기쁨. 과장된 마법 주문처럼 끊지 않음.|

**고정 참조:** `assets/voice_refs/v6/blue_fairy_V6_APPROVED.mp3`  
**SHA-256:** `c65e44b9c4d221c1fe9052ff201a3d3a0f5bc867c29460130fe2944f59c5965b`

## 8. 귀뚜라미 — CRICKET_DESIGN_V1

신규 음색 설계. 작고 민첩한 동행자, 또렷한 중음~중고음의 친근한 형 같은 인상. 승인 참조는 아직 없음.

- **음역·질감:** 말의 출발은 가볍고 자음은 선명하게. 피노키오보다 침착하고 판단이 빠르다. 작다고 헬륨 음성·곤충 버징·피치업을 쓰지 않는다.
- **연령 인상:** 소년 주인공과 구별되는 젊은 성인 또는 차분한 청년 인상; 성별의 최종 음색은 샘플에서 고정
- **관계:** 길을 아는 친구이자 안전을 살피는 동행자. 윤수에게 도움을 청하고 피노키오의 선택을 대신하지 않는다.
- **말 빠르기 계획 범위:** 105~125단어/분. 실제 음성 측정값이 아니다.
- **현재 상태:** BLOCKED_RESOURCE

### 상황에 따라 달라지는 연기

- **greeting:** 착지한 뒤 자신감 있는 짧은 미소. 처음부터 모든 것을 가르치려 들지 않음.
- **guidance:** 관찰한 것을 구체적으로 짚는다. 안내 방송처럼 낭독하지 않음.
- **encouragement:** 성공 순간에만 밝아지고 곧 편안한 동행 톤으로 돌아옴.
- **concern:** 약속을 상기할 때 음량을 키우지 않고 말의 속도를 낮춘다. 잔소리·꾸지람 금지.
- **help:** 짧고 명확한 제안. 당황한 상대보다 침착하게 말함.

### 피해야 할 연기

- 피노키오 A를 피치만 바꿔 대체
- 삐걱대는 곤충 효과를 대사에 합성
- 항상 높은 텐션·항상 잔소리
- 위험을 과장해 공포감 유발

### 합성 도구에 전달할 기본 영어 연기 지시

> Create a distinct, clear companion voice with a light middle register and alert, friendly older-brother presence. Be quicker in thought but calmer than Pinocchio. Give practical help and warm reminders, never a squeaky insect, a pitch-shifted child, a schoolmaster, or another approved character voice.

이 문장은 발화 텍스트가 아니다. 각 줄의 `direction_en`과 함께 연기 입력으로만 사용한다.

### 비교할 짧은 연기 예시

|실제 대사|연기 방향|
|---|---|
|“Good morning, Pinocchio!”|가볍게 착지한 뒤 자신감 있고 친근한 첫 인사.|
|“Listen carefully.”|먼 소리를 함께 듣자는 가까운 초대. 명령조 금지.|
|“Pinocchio, remember your promise.”|이름에서 시선을 잡고 작은 쉼. promise에 다정한 걱정. 혼내지 않음.|

**참조 음원:** 미확보. 위 지시는 신규 음색의 제작 목표이며 승인된 성우라고 표시하지 않는다.

## 9. 마라 — MARA_DESIGN_V1

신규 음색 설계. 객석을 편하게 맞이하는 성인 공연 진행자. 넓게 전달되는 중음의 따뜻한 공명. 승인 참조는 아직 없음.

- **음역·질감:** 멀리 전달되지만 목을 조이지 않는 열린 소리. 성별·구체적 캐스팅은 원본에 고정되지 않았으므로 샘플에서 고정하며 기본 연기 목표는 동일.
- **연령 인상:** 성인 진행자, 제페토의 노년감·요정의 고요함과 분리
- **관계:** 관객에게는 환영하는 진행자, 문제가 생기면 아이들에게 솔직하게 도움을 청하는 어른.
- **말 빠르기 계획 범위:** 105~125단어/분. 실제 음성 측정값이 아니다.
- **현재 상태:** BLOCKED_RESOURCE

### 상황에 따라 달라지는 연기

- **welcome:** 한 객석을 바라보며 밝고 크게 환영. 광고 성우의 과잉 미소 금지.
- **problem:** 커튼 문제를 확인하며 짧게 놀라고 곧 해결 방법을 찾음.
- **request:** 아이 눈높이로 음량을 낮추고 구체적으로 도움을 요청.
- **danger:** 핍을 걱정하는 즉각적인 주의 환기. 겁주는 비명 금지.
- **relief:** 안전이 확인된 뒤 밝은 숨으로 감사하고 공연 분위기로 복귀.

### 피해야 할 연기

- 내레이터 문장을 읽는 듯한 진행
- 문제 상황에도 축제 톤 유지
- 성우를 다른 캐릭터로 임시 대체
- 매 문장의 과장된 강세

### 합성 도구에 전달할 기본 영어 연기 지시

> Use a distinct adult host voice with warm open resonance and effortless projection to a small audience. Shift naturally from welcoming showmanship to honest concern and gentle requests for help. Do not shout every line, imitate an advertisement, or reuse Geppetto or the Fairy.

이 문장은 발화 텍스트가 아니다. 각 줄의 `direction_en`과 함께 연기 입력으로만 사용한다.

### 비교할 짧은 연기 예시

|실제 대사|연기 방향|
|---|---|
|“Welcome, everyone!”|객석을 둘러보며 활짝 맞이함. everyone 끝은 편하게 열어 둠.|
|“The curtain is stuck!”|문제를 직접 확인한 짧은 놀람. 아직 공포나 분노 아님.|
|“Pinocchio! Pip needs help!”|이름으로 즉시 주의를 끌고 도움 필요를 명확히 전달. 소리지르며 찢어지지 않음.|

**참조 음원:** 미확보. 위 지시는 신규 음색의 제작 목표이며 승인된 성우라고 표시하지 않는다.

## 10. 핍 — PIP_DESIGN_V1

신규 음색 설계. 공연하는 작은 인형의 밝고 탄력 있는 목소리. 피노키오보다 리듬감과 무대 자신감이 있으나 별개의 화자. 승인 참조는 아직 없음.

- **음역·질감:** 가벼운 중고음에 둥근 공명과 짧은 탄력. 피노키오 A의 복제·속도변환·로봇 필터 금지.
- **연령 인상:** 어린 공연자 같은 생기; 피노키오와 구별되는 공명·발음 리듬을 샘플로 고정
- **관계:** 관객 앞에서는 신나는 공연자, 위험할 때는 솔직하게 도움을 청하는 친구.
- **말 빠르기 계획 범위:** 105~125단어/분. 실제 음성 측정값이 아니다.
- **현재 상태:** BLOCKED_RESOURCE

### 상황에 따라 달라지는 연기

- **stuck:** 안쪽에서 상황을 알리는 다급하지 않은 답답함.
- **introduction:** 자신의 이름을 소개하는 작은 자랑.
- **dance:** 움직임에 맞는 경쾌함. 한 단어씩 통통 튀는 기계 리듬 금지.
- **fear:** 발이 미끄러진 순간 짧게 숨이 멎고 도움 요청이 선명해짐. 웃음 금지.
- **thanks:** 구조된 뒤 숨을 고르고 안도와 고마움이 섞여야 함.

### 피해야 할 연기

- 피노키오와 같은 참조·같은 화자 임시 사용
- 인형이라는 이유로 로봇 보코더
- 낙상 위험에서도 웃는 소리
- 매 줄에 강제 웃음·애드리브 추가

### 합성 도구에 전달할 기본 영어 연기 지시

> Use a separate bright puppet performer voice with rounded light resonance and playful rhythmic confidence, clearly different from Pinocchio. Let genuine alarm interrupt the performance when he slips, then let relief soften the thank-you. Never keep a cheerful stage voice during danger.

이 문장은 발화 텍스트가 아니다. 각 줄의 `direction_en`과 함께 연기 입력으로만 사용한다.

### 비교할 짧은 연기 예시

|실제 대사|연기 방향|
|---|---|
|“My name is Pip!”|무대 첫 인사의 작고 당당한 자랑. Pip에 밝은 마침.|
|“I'm falling!”|방금 발이 미끄러진 실제 놀람. 짧고 선명하며 비명으로 늘이지 않음.|
|“Thank you, Pinocchio!”|구조 직후 숨을 되찾고 진심으로 고마워함. 이전의 공연 톤보다 부드러움.|

**참조 음원:** 미확보. 위 지시는 신규 음색의 제작 목표이며 승인된 성우라고 표시하지 않는다.

## 11. 문장별 제작표 사용법

1. 각 화의 `script_v2_draft.md`에서 문장 아래 **음성 연기**를 읽는다.
2. `voice_direction_plan.json` 또는 `voice_direction_sheet.csv`의 동일한 대사 ID를 사용한다.
3. `spoken_text`만 실제로 읽고, `instruct_prompt_en`·`voice_direction`·전후 대사는 별도 문맥으로 전달한다.
4. 질문 예시는 본편과 별도 WAV로 만든다. 첫 실행에서 예시를 한 번 들려준 다음 입력을 받는다.
5. 대표 문장으로 화자와 감정 차이를 확인한 뒤 같은 설정으로 나머지 문장을 만든다. 승인 참조가 없는 캐릭터는 누락 대신 BLOCKED_RESOURCE로 남긴다.

[Codex 음성 제작 지시서](CODEX_VOICE_ACTING_HANDOFF.md) · [기계 판독 음색 기준](VOICE_PERFORMANCE_BIBLE_V2_1.json)

**이 문서의 완료 범위는 음성 연기 설계다. 실제 합성·청취·립싱크 검증은 NOT_RUN이다.**
