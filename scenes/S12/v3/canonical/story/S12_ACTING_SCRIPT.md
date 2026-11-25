# 12화 최종편 — 친구를 구한 진짜 아이

**상세 연기 대본 및 2D 제작 콘티 V2.0 | 2026-11-25 | 우선순위 수정본·실제 미디어 미검증**

기존 승인 정본 44개 대사 그대로 + 신규 연결 대사 27개 = 본편 71개. 외부 모델 10개. 10비트·50컷. 계획 본편 468초(7분 48초), 24fps 11,232프레임. 모델·발화 대기·반복·메뉴 시간 별도. **실제 음성·원화·영상·앱 실행은 아직 NOT_RUN.**

## 핵심 연출

11화의 같은 아침, 열린 학교 문 바로 바깥에서 시작한다. 나무 피노키오가 친구를 구하고 솔직함과 약속을 인정받아 사람이 된다. 인간형은 반드시 승인된 윤수 캐릭터 `CHAR_YOONSU_HUMAN`; 이야기 속 이름·목소리는 피노키오 그대로다. 모자·가방·책·신발과 공간을 유지한다. 진짜 아이가 되기 전부터 제페토의 사랑과 귀뚜라미의 우정은 변하지 않는다. 변신 직후 첫 환희→제페토 응답→가족 포옹→귀뚜라미 축하를 한 번에 이어 주며, 그 뒤에 손 탐색 참여를 배치한다.

원문 `U001~U044`는 한 글자도 수정하지 않았다. 추가 대사는 `N001~N027`의 고정 ID로 구분한다. 첫 환희와 포옹을 끊지 않도록 N020·N021을 손 탐색 N015~N019보다 먼저 배치했으며, 모든 문구는 보존했다. 아래 계획 컷 C01~C50은 기존 19개 승인 컷을 확장한 번호이며 각 컷에 원전 대응을 표시한다. 기존 다른 화의 원본을 수정하지 않는다.

## 공통 음성 연기 지시

- 영어 인용문만 실제 발화한다. 연기 지시, 감정 이름, 설명은 읽지 않는다. 원문 밖 감탄사·웃음·비명·한숨·헐떡임·단어 추가 금지.
- 상대와 상황을 실제 합성 입력에 연결한다. 음색 참조와 감정 제어는 분리하고, 지원이 확인된 제어만 사용한다. 기존 Kokoro 낭독 뒤 속도·높낮이 보정만으로 완료 처리하지 않는다. IndexTTS2 등 감정 제어형 후보는 설치·가중치·참조·실행을 확인한 경우에만 사용한다. 현재 모델 다운로드 403은 이전 작업에서 보고된 장애이며 여기서 해결했다고 주장하지 않는다.
- 같은 화자 내 걱정→기쁨, 긴급→안도, 감격→다정함을 크게 대비한다. 자막 없이 감정이 구분되어야 한다. 명료한 첫·끝 자음, 자연스러운 의미 단위, 원래 발음을 지킨다.
- 피노키오·제페토 최종 S03 고정, 귀뚜라미 기존, 파란 요정 기존 C, 내레이션 기존 A. 승인 참조를 열 수 없으면 대체 음색을 만들지 않는다. 변신으로 음색 바뀌지 않음.
- 실제 출력 후보 청취 전 자동 인식 점수나 파형 차이만으로 PASS 금지. 본편 연기와 외부 모델은 다른 전달 방식.

## 시간 및 참여 계획

|비트|계획 본편|내용|
|---|---|---|
|B01|00:00–00:42|열린 학교 문과 작은 바람|
|B02|00:42–01:24|갑자기 막힌 친구|
|B03|01:24–02:05|친구를 구하기로 결정|
|B04|02:05–02:56|두려움을 인정하고 친구를 살피다|
|B05|02:56–03:48|익숙한 파란빛과 지난 선택|
|B06|03:48–04:34|마지막 마법과 인간형 변신|
|B07|04:34–05:22|첫 환희·가족 포옹을 먼저 나누다|
|B08|05:22–06:09|손의 감촉을 함께 살피다|
|B09|06:09–06:56|약속과 마지막 인사|
|B10|06:56–07:48|학교로 들어가는 진짜 아이|

|순서|계획 질문 끝|목표 발화|실제 반응|
|---:|---|---|---|
|1 (S12-P01)|00:18|Look inside, please.|열린 문 안쪽을 바라보기|
|2 (S12-P02)|00:34|Hold your hat.|바람에 움직이는 모자를 잡기|
|3 (I21)|01:32|Help the cricket!|막힌 친구를 안전하게 도와주기|
|4 (S12-P03)|02:34|Check on Cricket.|구조 뒤 친구의 상태 살피기|
|5 (S12-P04)|02:56|Stand beside Grandpa.|할아버지 옆 안전한 곳에 서기|
|6 (S12-P05)|05:22|Show your hands.|사람이 된 손을 보여 주기|
|7 (S12-P06)|05:40|Bend your fingers.|손가락을 굽혀 새로운 촉감 느끼기|
|8 (S12-P07)|05:59|Take Grandpa's hand.|할아버지의 손을 잡기|
|9 (S12-P08)|06:18|Straighten your hat.|기울어진 모자 바로 쓰기|
|10 (S12-P09)|06:46|Wave goodbye, please.|요정에게 마지막 손인사하기|

질문 실제 종료 → 본편 정지 → 예시 1회(마이크 OFF) → 실제 예시 종료 → 자동 입력 준비(권한 내) → 발화 활동 종료 또는 보호자 진행 → 실제 반응 완료 → 후속 대사. 발화 내용·정확도는 평가하지 않는다. 대기는 실제 시간에서 분리하며, 기존 검증된 감도·VAD 종료 기준을 상속하고 미확인 시간은 0으로 해석하지 않는다.

## 전체 연기 대본

## B01 — 열린 학교 문과 작은 바람 (00:00–00:42)


### S12-C01 · 00:00–00:08 (8초 계획)

**구도:** 학교 외부 WS → 낮은 눈높이

**화면·동작:** 11화 마지막 프레임에서 연결. 같은 손인사가 자연스럽게 끝난 뒤 피노키오가 손을 내리고 열린 문으로 시선을 옮긴다. 제페토의 안경, 가방, 모자, 신발, 귀뚜라미와 서 있는 안내판 위치를 그대로 잇는다. 교사는 문 안쪽에서 조용히 기다린다.

**음향·경계:** 기존 아침 환경음 연속. 아직 바람 사건 없음.

원전 컷 대응(기존 19컷 번호 체계): S12-C01.

#### 내레이션 · S12-U001 [원문]

> Pinocchio was almost inside the school.

**상대·감정:** 윤수와 관객 / 따뜻한 기대

**연기:** 관객을 문 앞의 설렘으로 데려간다. almost에서 이제 한 걸음 남았다는 친근한 기대를 주고 school은 아직 안으로 들어가지 않은 여유로 마친다.

**합성 지시(영문):** Bring the audience right to the open doorway. Lift almost with quiet anticipation, then ease into school; he has not crossed the threshold yet.

**강세·발음:** almost / school. almost의 끝과 school의 /l/을 살린다.


### S12-C02 · 00:08–00:18 (10초 계획)

**구도:** 문 안쪽과 피노키오 얼굴을 잇는 OTS

**화면·동작:** 제페토가 열린 문 안쪽을 손바닥으로 가리킨다. 문턱 너머 복도만 보이고 교실이나 친구들을 새로 만들지 않는다. 피노키오는 문 밖에 두 발을 둔 채 눈을 옮긴다. 윤수 쪽으로 얼굴을 돌리는 제페토.

**음향·경계:** P01 질문 끝에만 정지. 문은 계속 열려 있다.

원전 컷 대응(기존 19컷 번호 체계): S12-C01.

#### 제페토 · S12-N001 [신규]

> Look, the door is open.

**상대·감정:** 피노키오 / 따뜻한 환영

**연기:** 따뜻한 안내. Look으로 시선을 문에 데려오고 open에서 환하게 초대한다. 이미 열려 있는 문을 새로 열라는 말투가 아니다.

**합성 지시(영문):** Invite his gaze toward the already open door. Brighten open as a welcoming discovery, not an instruction to open it.

**강세·발음:** Look / open. door와 is를 매끄럽게 연결한다.

#### 제페토 · S12-N002 [신규]

> Yoonsu, can you help him look inside?

**상대·감정:** 윤수 / 기대 어린 초대

**연기:** 윤수에게 미소를 건네고 손짓으로 안쪽을 보여 준다. look inside에 관심을 모아 질문을 열린 채 마친다.

**합성 지시(영문):** Address Yoonsu warmly, then gently invite him to help Pinocchio look inside. Let the last words ask for a response rather than demand one.

**강세·발음:** Yoonsu / look inside. 이름은 기존 승인 발음. inside 끝 /d/ 보존.

**🎤 S12-P01 — Look inside, please.**

뜻을 보여 주는 화면: 제페토가 문 안쪽을 가리킨다. 아이의 두 발은 문턱 밖.

대기: WOODEN / SAFE_FREE / 안내판 STANDING. 다음 핵심 동작은 수용 전 금지.

외부 모델: 제페토 `S12-M001` 1회. 수용 뒤 머리와 상체를 실제로 돌려 안쪽을 살펴보고 제페토를 다시 바라본다. 문턱은 넘지 않는다.

재개: `S12-N003`. 시선 전환 및 안정 자세 완료을 먼저 확인한다.


### S12-C03 · 00:18–00:26 (8초 계획)

**구도:** 피노키오 CU → 문 방향 시점

**화면·동작:** P01 수용 후 머리와 몸통을 작은 범위로 돌려 문 안을 살핀다. 신발은 문턱 밖에 고정. 제페토의 얼굴로 다시 시선을 돌리고 귀뚜라미도 같은 방향을 바라본다.

**음향·경계:** 실제 시선 전환 완료 후 N003. 교사의 발화 없음.

원전 컷 대응(기존 19컷 번호 체계): S12-C01.

**S12-P01 반응:** 머리와 상체를 실제로 돌려 안쪽을 살펴보고 제페토를 다시 바라본다. 문턱은 넘지 않는다.

**반응 종료 조건:** 시선 전환 및 안정 자세 완료. 후속 대사 `S12-N003`는 조건 완료 뒤에만 시작한다.

#### 피노키오 · S12-N003 [신규]

> I can see inside!

**상대·감정:** 제페토 / 신기함

**연기:** 실제로 문 안쪽을 본 뒤 조용히 들뜬다. see에서 발견이 피어나고 inside를 환하게 마쳐 할아버지와 나눈다.

**합성 지시(영문):** Let the little discovery brighten his face as he speaks. Spring gently into see, then open inside with delighted recognition.

**강세·발음:** see / inside. I can을 붙이고 inside를 늘여 다른 단어로 만들지 않는다.

#### 귀뚜라미 · S12-N004 [신규]

> I'm right here.

**상대·감정:** 피노키오 / 친근한 안심

**연기:** 발치에서 든든하게 함께 있음을 알린다. right here를 친한 친구에게 작고 확실하게 보낸다.

**합성 지시(영문):** From his safe place by Pinocchio's feet, reassure him with a small, warm, confident reply.

**강세·발음:** right here. I'm을 정확히 연결한다.


### S12-C04 · 00:26–00:34 (8초 계획)

**구도:** 모자와 얼굴 MS

**화면·동작:** 잎 하나가 바닥을 지나가고 모자 가장자리가 약하게 들린다. 안내판은 아직 완전히 서 있다. 피노키오가 손을 모자 쪽으로 준비하되 닿지는 않는다. 제페토가 모자를 가리킨다.

**음향·경계:** 약한 바람만. P02 질문 종료에서 정지.

원전 컷 대응(기존 19컷 번호 체계): S12-C01.

#### 제페토 · S12-N005 [신규]

> A little breeze!

**상대·감정:** 피노키오 / 가벼운 놀람

**연기:** 작은 바람을 반갑게 알아챈다. little은 가벼운 미소, breeze는 바람결을 따라 부드럽게 흐른다. 위험을 예고하는 공포 연기 금지.

**합성 지시(영문):** Notice a playful little breeze. Keep this pleasantly surprised, not ominous; let breeze flutter lightly.

**강세·발음:** little breeze. breeze의 /z/ 끝 유지.

#### 제페토 · S12-N006 [신규]

> Yoonsu, what should he hold?

**상대·감정:** 윤수 / 다정한 질문

**연기:** 모자 쪽 손짓으로 대상이 무엇인지 먼저 보여 준다. hold에 주의를 모아 윤수에게 간결하게 묻는다.

**합성 지시(영문):** Point toward the hat and invite Yoonsu to help. Make hold the purposeful word; finish with a real question.

**강세·발음:** Yoonsu / hold. should he 연결, hold의 /d/ 보존.

**🎤 S12-P02 — Hold your hat.**

뜻을 보여 주는 화면: 모자 가장자리가 약하게 들리고 제페토가 가리킨다. 안내판은 아직 서 있다.

대기: WOODEN / SAFE_FREE / 안내판 STANDING. 다음 핵심 동작은 수용 전 금지.

외부 모델: 제페토 `S12-M002` 1회. 수용 뒤 손을 테두리에 가져가 실제로 닿아 잡고 모자를 안정시킨다. 말한 뒤 손을 내리고 다음 돌풍으로 이어진다.

재개: `S12-N007`. 손과 모자 접촉 및 모자 안정을 먼저 확인한다.


### S12-C05 · 00:34–00:42 (8초 계획)

**구도:** 정면 MS → 안내판으로 PAN

**화면·동작:** P02 수용 후 피노키오가 모자 테두리에 손을 실제로 대고 바람이 잦을 때까지 잡는다. 모자는 머리 위 그대로. 손을 내린 뒤 돌풍으로 주변 잎이 빨라지고 안내판 쪽으로 시선이 움직인다. 판은 컷 끝까지 서 있는 채 흔들리기만 한다.

**음향·경계:** N007 뒤 바람이 급격히 변함. U002는 실제 변화가 시작된 뒤, 낙하 전.

원전 컷 대응(기존 19컷 번호 체계): S12-C01.

**S12-P02 반응:** 손을 테두리에 가져가 실제로 닿아 잡고 모자를 안정시킨다. 말한 뒤 손을 내리고 다음 돌풍으로 이어진다.

**반응 종료 조건:** 손과 모자 접촉 및 모자 안정. 후속 대사 `S12-N007`는 조건 완료 뒤에만 시작한다.

#### 피노키오 · S12-N007 [신규]

> I've got my hat!

**상대·감정:** 제페토 / 밝은 안도

**연기:** 손으로 모자를 붙잡은 뒤 밝은 안도. got에 손으로 잡았다는 확신, hat은 장난스러운 미소. 모자를 벗지 않는다.

**합성 지시(영문):** Smile with relief once his fingers actually secure the brim. Make got confident and hat playful, not a shouted victory.

**강세·발음:** got / hat. I've와 got의 자음 및 hat의 /t/ 유지.

#### 내레이션 · S12-U002 [원문]

> But something unexpected happened.

**상대·감정:** 윤수와 관객 / 기대에서 긴장으로 급전환

**연기:** 바람결이 달라지는 것을 함께 알아챈다. But에서 기대를 끊고 unexpected에 긴장감을 모으며 happened를 짧게 마쳐 다음 사건의 공간을 준다.

**합성 지시(영문):** Interrupt the pleasant morning with a sudden change of attention. Tighten unexpected, then release the sentence into the visible event without melodramatic horror.

**강세·발음:** But / unexpected / happened. unexpected의 각 음절과 happened의 끝을 또렷하게.


## B02 — 갑자기 막힌 친구 (00:42–01:24)


### S12-C06 · 00:42–00:50 (8초 계획)

**구도:** 안내판과 귀뚜라미가 함께 보이는 낮은 WS

**화면·동작:** 조건부 승인 배경의 기존 문틀·벽·받침이 실제로 이 배치를 허용할 때, 한 와이드 구도에서 같은 작은 판의 밑면 회전과 귀뚜라미의 안전 공간 이동을 함께 보인다. 판이 실제 기존 받침에 걸려 멈추며 귀뚜라미와 충돌하지 않는다. 머리 위 여유와 낮게 막힌 가장자리를 같은 구도에서 보여 준다. 승인 배경에 지지 구조가 없으면 BLOCKED_LAYOUT.

**음향·경계:** 짧은 나무 닿는 소리. 위협적인 충격·비명 효과 금지. U003은 막힌 사실을 알아챈 순간.

원전 컷 대응(기존 19컷 번호 체계): S12-C02.

#### 귀뚜라미 · S12-U003 [원문]

> Oh! Help!

**상대·감정:** 피노키오와 제페토 / 갑작스러운 놀람·다급한 요청

**연기:** 놀람이 Oh에서 저절로 튀어나온다. Help!에는 친구에게 바로 닿으려는 힘을 싣는다. 아프거나 다쳤다는 울음은 없다.

**합성 지시(영문):** React instantly to the exit being blocked. Let Oh burst out in surprise, then throw Help toward his friends with urgent clarity, not pain.

**강세·발음:** Oh / Help. Help의 /h/와 끝 /p/를 남긴다.


### S12-C07 · 00:50–00:57 (7초 계획)

**구도:** 판 너머 귀뚜라미 CU

**화면·동작:** 귀뚜라미는 기존 구조 면과 비스듬한 판이 만드는 안전 여유 공간에 있다. 낮은 앞 모서리와 몸보다 작은 옆 틈이 출구를 막았음을 보인다. 몸을 누르거나 다치게 하지 않으며, 좌우 확인과 작은 자세 변화만으로 도움 필요를 보여 준다. 반복 점프 실패나 공포 루프 없음.

**음향·경계:** U004 뒤 억지 긴 침묵 없이 피노키오에게 컷.

원전 컷 대응(기존 19컷 번호 체계): S12-C02.

#### 귀뚜라미 · S12-U004 [원문]

> I'm stuck!

**상대·감정:** 피노키오와 제페토 / 당황과 답답함

**연기:** I'm은 상황을 깨달은 짧은 시작, stuck은 길이 막힌 답답함으로 단단하게 닫는다. 겁을 주는 고함보다 실제 도움 요청이다.

**합성 지시(영문):** Start with startled recognition, then land stuck with frustrated urgency. Call for help, not a comic scream or an injury cry.

**강세·발음:** stuck. I'm의 /m/, stuck의 /k/를 살린다.


### S12-C08 · 00:57–01:07 (10초 계획)

**구도:** 피노키오와 귀뚜라미 시선 일치 교차 CU

**화면·동작:** 피노키오가 판 쪽으로 몸을 돌리고 눈높이를 낮춰 귀뚜라미를 확인한다. 손은 안내판에 닿지 않는다. 귀뚜라미가 고개를 들어 괜찮다는 표시를 하고 막힌 쪽을 본다.

**음향·경계:** U005 직후 귀뚜라미 응답. 판 위치 고정.

원전 컷 대응(기존 19컷 번호 체계): S12-C03.

#### 피노키오 · S12-U005 [원문]

> Cricket! Are you okay?

**상대·감정:** 귀뚜라미 / 강한 걱정→다정한 확인

**연기:** Cricket!은 친구를 알아챈 순간 걱정이 확 튀어 나오는 호출. Are you okay?에서는 가까이 살피려는 마음으로 소리를 낮추고 okay를 진짜 질문으로 열어 둔다.

**합성 지시(영문):** Call Cricket with an immediate jolt of concern. Then pull the energy inward to check on him; are you okay must sound like a real question awaiting an answer.

**강세·발음:** Cricket / okay. Cricket 이름·okay 발음 유지. 질문 끝을 자르지 않는다.

#### 귀뚜라미 · S12-U006 [원문]

> I'm okay, but I can't get out!

**상대·감정:** 피노키오 / 안심→막힌 답답함

**연기:** I'm okay에서 다치지 않았음을 먼저 안심시킨다. but에서 답답함으로 급격히 돌아서고 can't get out을 붙여 도움의 필요를 분명하게 전달한다.

**합성 지시(영문):** Reassure him sincerely on I'm okay, then pivot sharply at but into the practical frustration of being unable to get out. He is safe but blocked.

**강세·발음:** okay / can't / out. can't의 부정이 can으로 들리지 않게 끝 자음과 모음 유지.


### S12-C09 · 01:07–01:15 (8초 계획)

**구도:** 피노키오·열린 문·판을 한 구도에

**화면·동작:** 두 번째 아침 종이 울린다. 피노키오가 문 쪽으로 고개를 돌렸다가 귀뚜라미 쪽으로 돌아본다. 발은 두 방향 중 어디에도 아직 달리지 않는다. 같은 책 든 가방의 무게를 어깨에 느낀다.

**음향·경계:** 종은 실제 사건음. U007을 덮지 않도록 감쇠. 새로운 참여 없음.

원전 컷 대응(기존 19컷 번호 체계): S12-C04.

#### 피노키오 · S12-U007 [원문]

> School is starting!

**상대·감정:** 자기 자신과 제페토 / 급한 깨달음

**연기:** 종을 듣고 학교 시간이 떠오른 순간 School이 튀어나온다. starting에서 급한 마음을 드러내되 친구를 비난하지 않는다.

**합성 지시(영문):** React to the bell with a sudden reminder of his promise. Sound genuinely rushed on starting, without blaming Cricket.

**강세·발음:** School / starting. school /l/과 starting의 끝 보존.


### S12-C10 · 01:15–01:24 (9초 계획)

**구도:** 피노키오 MS → 제페토 TWO SHOT

**화면·동작:** 피노키오가 열린 문에서 귀뚜라미에게 시선을 돌려 자발적인 결심을 보인다. 같은 와이드 공간에서 제페토는 문틀 옆면 반대쪽 현재 위치에서 한 번 손을 뻗지만 직선 손 경로가 그 기존 면에 가림을 보인다. 힘이나 팔 길이 부족 설정이 아니다. 피노키오는 판의 접근 가능한 열린 면에 있다. 제페토는 반복 시도 대신 아이와 침착하게 눈을 맞춘다.

**음향·경계:** U007→U008→U009 자연스러운 대화. 도움 선택을 윤수보다 먼저 피노키오가 마음에 둔다.

원전 컷 대응(기존 19컷 번호 체계): S12-C04, S12-C05.

#### 피노키오 · S12-U008 [원문]

> But my friend needs help.

**상대·감정:** 자기 자신과 제페토 / 친구 걱정→결심

**연기:** But에서 자신의 급한 마음을 멈추고 friend에 따뜻한 걱정을 싣는다. needs help에서 결심이 선명해진다. 교훈을 외우는 말이 아니라 눈앞의 친구를 향한다.

**합성 지시(영문):** Turn away from the pull of the bell toward the friend who needs him. Let friend carry affection and needs help gather resolve; this is his own realization.

**강세·발음:** friend / needs help. needs의 /dz/, help의 /p/ 보존.

#### 제페토 · S12-U009 [원문]

> Pinocchio, your friend needs you.

**상대·감정:** 피노키오 / 침착한 신뢰

**연기:** 이미 친구를 걱정하는 아이에게 짧고 믿음 있게 말을 건넨다. 이름은 다정하게, your friend needs you는 책임을 겁주지 않고 할 수 있다는 신뢰를 담는다.

**합성 지시(영문):** Acknowledge the child's own concern. Speak his name warmly and give your friend needs you quiet conviction, not guilt or an order shouted across the yard.

**강세·발음:** friend / needs you. needs you를 자연스럽게 연결하되 끝 자음 보존.


## B03 — 친구를 구하기로 결정 (01:24–02:05)


### S12-C11 · 01:24–01:32 (8초 계획)

**구도:** I21 WAIT 목각 피노키오와 학교 문, 판 뒤 친구

**화면·동작:** 제페토가 윤수 쪽으로 시선을 옮긴다. 귀뚜라미는 안전 공간에서 안정된 자세를 유지하며, 피노키오는 아직 판과 문 사이에 있다. 판을 들어 올리는 사전 프레임은 금지한다.

**음향·경계:** U010 실제 끝 → I21. 대기 중 판·마법·구조 진행 금지, 공포 루프 금지.

원전 컷 대응(기존 19컷 번호 체계): S12-C06.

#### 제페토 · S12-U010 [원문]

> Yoonsu, what should Pinocchio do?

**상대·감정:** 윤수 / 진심 어린 부탁

**연기:** 윤수에게 차분하고 간절하게 묻는다. Yoonsu를 분명히 부르고 what should Pinocchio do를 짧고 알아듣기 쉽게 연결한다. 조급하게 재촉하지 말고 마지막 do에 답을 기다리는 공간을 남긴다.

**합성 지시(영문):** Address Yoonsu directly with caring urgency, not panic. Invite one simple next action and genuinely wait for a response.

**강세·발음:** Yoonsu / what / do. 두 이름의 승인 발음과 끝까지 이어진 질문 유지.

**🎤 I21 — Help the cricket!**

뜻을 보여 주는 화면: 친구가 다치지 않은 여유 공간, 낮게 막힌 앞 모서리·몸보다 좁은 옆 틈을 한 와이드에서 보인다. 제페토의 현재 직선 접근은 기존 옆면에 가리고 피노키오의 면은 열려 있다. 실제 승인 배경 부합 전 BLOCKED_LAYOUT.

대기: WOODEN / BLOCKED_UNINJURED / 안내판 FALLEN_STABLE. 다음 핵심 동작은 수용 전 금지.

외부 모델: 제페토 `S12-M003` 1회. 수용 뒤 결심→열린 면으로 이동→감속·굽힘→양손 접촉→다른 받침 접촉을 유지해 가까운 모서리 조금 들기→가까운 측면 틈으로 친구 탈출→전체 복원 경로 밖 안전 지점 확인→같은 기존 받침으로 판 안정→손 해제→안도.

재개: `S12-U011`. 친구 안전·판 안정·두 손 해제·안도 표정까지 완료을 먼저 확인한다.


### S12-C12 · 01:32–01:40 (8초 계획)

**구도:** FOLLOW 측면 MS

**화면·동작:** I21 수용 후에만 피노키오가 이미 보인 열린 접근 면으로 이동한다. 실제 보폭과 감속, 무릎 굽힘과 두 발 지지를 보인 뒤 작은 판의 보이는 두 잡기 지점에 양손을 닿게 한다. 가방은 어깨에 유지하며 벽이나 판을 손발이 관통하지 않는다. 양손 접촉 전 판 움직임 없음.

**음향·경계:** 모델·입력 대기는 본편 시간에서 제외. 접지와 손 접촉 전 판 움직임 금지. 대사 없음.

원전 컷 대응(기존 19컷 번호 체계): S12-C07.

**I21 반응:** 결심→열린 면으로 이동→감속·굽힘→양손 접촉→다른 받침 접촉을 유지해 가까운 모서리 조금 들기→가까운 측면 틈으로 친구 탈출→전체 복원 경로 밖 안전 지점 확인→같은 기존 받침으로 판 안정→손 해제→안도.

**반응 종료 조건:** 친구 안전·판 안정·두 손 해제·안도 표정까지 완료. 후속 대사 `S12-U011`는 조건 완료 뒤에만 시작한다.


### S12-C13 · 01:40–01:48 (8초 계획)

**구도:** 낮은 TWO SHOT 손·판·귀뚜라미 동시

**화면·동작:** 양손 접촉과 발 지지를 확보한 뒤 다른 실제 받침 접촉을 유지하며 판의 가까운 모서리만 조금 들어 올린다. 가장 가까운 측면 틈이 귀뚜라미 몸 전체보다 충분히 열리면 귀뚜라미가 그 옆 가장자리로 빠져나간다. 판 중앙 밑으로 새로 진입하거나 정면 낙하 경로를 횡단하지 않는다. 피노키오는 친구가 안전 지점에 도착할 때까지 판을 안정된 높이로 유지한다.

**음향·경계:** 가벼운 나무 마찰. 실제 손 소켓과 무게에 맞춰 시간 재산정. 대사 없음.

원전 컷 대응(기존 19컷 번호 체계): S12-C07.

**I21 반응:** 결심→열린 면으로 이동→감속·굽힘→양손 접촉→다른 받침 접촉을 유지해 가까운 모서리 조금 들기→가까운 측면 틈으로 친구 탈출→전체 복원 경로 밖 안전 지점 확인→같은 기존 받침으로 판 안정→손 해제→안도.

**반응 종료 조건:** 친구 안전·판 안정·두 손 해제·안도 표정까지 완료. 후속 대사 `S12-U011`는 조건 완료 뒤에만 시작한다.


### S12-C14 · 01:48–01:57 (9초 계획)

**구도:** 판과 두 인물의 전신 WS

**화면·동작:** 귀뚜라미가 판을 원래 위치로 돌릴 전체 회전 경로를 벗어난 뒤 같은 판을 기존 받침에 천천히 되돌린다. 손 위치·피벗을 옮길 때 한 곳 이상의 안정된 실제 지지가 이어져야 한다. 제페토는 열린 면으로 다가와 판의 안정 상태를 함께 확인할 수 있다. 판 안정→양손 해제→안도가 모두 끝나야 I21 반응 완료이며, U011 감사는 그 뒤다. 실제 무게와 복원 접촉 전환은 원화·리그에서 검수한다.

**음향·경계:** 판 안정·손 해제·친구 안전 상태 완료가 I21 REACT 종료. 감사는 다음 컷.

원전 컷 대응(기존 19컷 번호 체계): S12-C07, S12-C08.

**I21 반응:** 결심→열린 면으로 이동→감속·굽힘→양손 접촉→다른 받침 접촉을 유지해 가까운 모서리 조금 들기→가까운 측면 틈으로 친구 탈출→전체 복원 경로 밖 안전 지점 확인→같은 기존 받침으로 판 안정→손 해제→안도.

**반응 종료 조건:** 친구 안전·판 안정·두 손 해제·안도 표정까지 완료. 후속 대사 `S12-U011`는 조건 완료 뒤에만 시작한다.


### S12-C15 · 01:57–02:05 (8초 계획)

**구도:** 귀뚜라미 CU → 피노키오 반응

**화면·동작:** 귀뚜라미가 피노키오 발 앞 안전 지점에 선다. 놀란 어깨가 풀리고 얼굴이 환해진다. 피노키오는 손을 내리고 친구가 정말 괜찮은지 살핀다.

**음향·경계:** U011~U014는 연속. 여기서 새 입력 금지.

원전 컷 대응(기존 19컷 번호 체계): S12-C07, S12-C08.

#### 귀뚜라미 · S12-U011 [원문]

> Thank you, Pinocchio!

**상대·감정:** 피노키오 / 강한 안도와 감사

**연기:** Thank you는 버티던 긴장이 풀리며 한꺼번에 나온 감사. Pinocchio에 자신을 도와준 친구를 향한 깊은 반가움을 담는다.

**합성 지시(영문):** Let relief break through into heartfelt gratitude. Aim his name at the friend who actually helped him, not at the audience.

**강세·발음:** Thank you / Pinocchio. Thank의 /θ/와 이름의 마지막 음절 유지.

#### 귀뚜라미 · S12-U012 [원문]

> You helped me!

**상대·감정:** 피노키오 / 기쁜 감사

**연기:** You에서 친구에게 바로 시선을 붙이고 helped me를 기쁘게 확신한다. 첫 감사보다 조금 더 가벼워지며 친구가 한 행동을 인정한다.

**합성 지시(영문):** Look straight at him and celebrate what he did. Put a joyful, grateful emphasis on helped, with a warmer and lighter finish than the previous line.

**강세·발음:** You / helped me. helped의 /t/를 잃지 않는다.


## B04 — 두려움을 인정하고 친구를 살피다 (02:05–02:56)


### S12-C16 · 02:05–02:14 (9초 계획)

**구도:** 친구 눈높이 TWO SHOT

**화면·동작:** 피노키오가 무릎을 조금 굽혀 귀뚜라미와 눈높이를 맞춘다. 처음부터 영웅처럼 가슴을 펴지 않고 친구에게 손바닥을 열어 보인다. 귀뚜라미가 미소로 받는다.

**음향·경계:** 구조 후 음악은 조용히 완화. U013 U014 이어 말하기.

원전 컷 대응(기존 19컷 번호 체계): S12-C08.

#### 피노키오 · S12-U013 [원문]

> You're my friend.

**상대·감정:** 귀뚜라미 / 다정한 확신

**연기:** You're my friend는 너무 당연한 사실을 다정하게 건넨다. my friend에 친근함을 담고 작은 확신으로 마친다.

**합성 지시(영문):** Say it as something obvious and precious between friends. Keep the intimacy of my friend instead of announcing a heroic moral.

**강세·발음:** my friend. You're my를 부드럽게 이어 friend 끝 /d/ 유지.

#### 피노키오 · S12-U014 [원문]

> I couldn't leave you there.

**상대·감정:** 귀뚜라미 / 솔직한 우정

**연기:** I couldn't에서 단호함을 보여 주되 과시하지 않는다. leave you there에는 친구를 두고 갈 수 없었던 솔직한 마음이 내려앉는다.

**합성 지시(영문):** Explain why leaving was never a choice for him. Make couldn't quietly firm, then soften into leave you there with genuine care.

**강세·발음:** couldn't / leave you there. couldn't 부정과 there의 자연스러운 끝.


### S12-C17 · 02:14–02:25 (11초 계획)

**구도:** 제페토와 피노키오 MS

**화면·동작:** 제페토가 아이 곁에 눈높이를 낮추고 방금 무서웠는지 묻는다. 피노키오는 잠깐 자신을 돌아보며 겁났던 사실을 숨기지 않고 말한다. 귀뚜라미는 안전하게 곁에서 듣는다.

**음향·경계:** 오늘(D2)의 작은 진실을 실제로 말하는 추가 대화. U040의 today와 정합. 마법 없음.

원전 컷 대응(기존 19컷 번호 체계): S12-C08.

#### 제페토 · S12-N008 [신규]

> Were you scared, Pinocchio?

**상대·감정:** 피노키오 / 공감

**연기:** 겁을 내도 괜찮다는 다정한 질문이다. scared에서 공감의 온기를 주고 이름은 판단하지 않는 낮은 확신으로 부른다.

**합성 지시(영문):** Ask gently, making it safe to admit fear. Put sympathy into scared and leave an honest answer open.

**강세·발음:** scared / Pinocchio. Were you의 자연스러운 연결, scared 끝 /d/.

#### 피노키오 · S12-N009 [신규]

> Yes. I was scared.

**상대·감정:** 제페토 / 솔직한 두려움 인정

**연기:** Yes는 망설이다 진실을 선택한 짧은 응답. I was scared에서는 목소리를 조금 낮춰 솔직히 인정하고 scared를 흐리지 않는다. 부끄럽게 꾸짖는 내면 독백 금지.

**합성 지시(영문):** Admit the fear without hiding it. Give Yes a small honest beat, then let I was scared emerge plainly with vulnerable courage, not shame.

**강세·발음:** Yes / scared. Yes의 /s/와 scared 끝 /d/ 보존. 두 문장 사이 짧은 자연 쉼.

#### 제페토 · S12-N010 [신규]

> Thank you for telling me.

**상대·감정:** 피노키오 / 다정한 감사

**연기:** 어제의 고백을 기억하는 할아버지가 오늘의 솔직함을 따뜻하게 받아 준다. telling me에 감사의 무게를 싣고 훈계 없이 마친다.

**합성 지시(영문):** Receive his honest answer with tenderness. Thank him for telling you, without turning the moment into a lecture.

**강세·발음:** Thank you / telling me. Thank와 telling의 자음을 흐리지 않는다.


### S12-C18 · 02:25–02:34 (9초 계획)

**구도:** 귀뚜라미와 피노키오의 눈높이

**화면·동작:** 안전한 귀뚜라미를 향해 제페토가 먼저 짧게 눈높이를 낮추고 얼굴과 두 발을 살피는 시범을 보인다. 피노키오는 그 행동을 보고 윤수에게 질문하며 자신의 전체 확인 동작은 아직 하지 않는다. 친구는 이미 구조 완료, 자유롭게 서 있는 상태다.

**음향·경계:** 제페토의 상태 확인 시범 완료 뒤 N011. 질문 실제 종료에서 P03 대기. 구조는 다시 시작하지 않는다.

원전 컷 대응(기존 19컷 번호 체계): S12-C08.

#### 피노키오 · S12-N011 [신규]

> Yoonsu, shall I check on Cricket?

**상대·감정:** 윤수 / 배려

**연기:** 이미 안전해진 친구를 한 번 더 살피고 싶다. Yoonsu를 믿고 부른 뒤 check on Cricket에 배려의 마음을 모은다.

**합성 지시(영문):** Invite Yoonsu to help him check how his rescued friend feels. Be caring and curious, not urgently afraid again.

**강세·발음:** Yoonsu / check on Cricket. check on 연결, Cricket 이름 보존.

**🎤 S12-P03 — Check on Cricket.**

뜻을 보여 주는 화면: 제페토가 먼저 눈높이를 낮추어 귀뚜라미 얼굴과 두 발을 살피는 시범. 피노키오 자신의 확인 동작은 수용 후. 이미 위험 해소.

대기: WOODEN / SAFE_FREE / 안내판 UPRIGHT_STABLE. 다음 핵심 동작은 수용 전 금지.

외부 모델: 피노키오 `S12-M004` 1회. 수용 뒤 눈높이를 낮추고 친구 얼굴과 발을 살핀다. 귀뚜라미는 괜찮다는 몸짓과 두 발 지지를 보여 준다.

재개: `S12-N012`. 눈맞춤·친구의 안정된 두 발 확인을 먼저 확인한다.


### S12-C19 · 02:34–02:48 (14초 계획)

**구도:** 친구 CU → 제페토 MS

**화면·동작:** P03 후 피노키오가 고개를 숙이고 손바닥을 바닥 가까이에 열어 상태를 살핀다. 귀뚜라미가 두 발을 번갈아 디디며 괜찮음을 보여 준다. 피노키오가 고개를 들고 제페토는 흐뭇한 표정으로 대답한다.

**음향·경계:** 실제 확인 뒤 N012. 이어 U015, U016. 강요된 영웅 축하 효과 금지.

원전 컷 대응(기존 19컷 번호 체계): S12-C08.

**S12-P03 반응:** 눈높이를 낮추고 친구 얼굴과 발을 살핀다. 귀뚜라미는 괜찮다는 몸짓과 두 발 지지를 보여 준다.

**반응 종료 조건:** 눈맞춤·친구의 안정된 두 발 확인. 후속 대사 `S12-N012`는 조건 완료 뒤에만 시작한다.

#### 귀뚜라미 · S12-N012 [신규]

> I'm not hurt. I'm all right!

**상대·감정:** 피노키오 / 안심→밝은 회복

**연기:** not hurt는 안심시키려는 차분한 확인. 두 번째 문장은 두 발로 서서 다시 기운이 돌아온 밝은 확신이다.

**합성 지시(영문):** First reassure him that there is no injury. Then brighten into I'm all right as his posture recovers; show relief through the words.

**강세·발음:** not hurt / all right. not의 /t/, hurt와 right 끝을 선명히.

#### 제페토 · S12-U015 [원문]

> I'm proud of you, Pinocchio.

**상대·감정:** 피노키오 / 깊은 자랑스러움

**연기:** I'm proud of you는 그 아이를 바라보며 깊은 마음을 담는다. Pinocchio에는 가족의 자랑스러움이 가까이 전달된다. 크게 선포하지 않는다.

**합성 지시(영문):** Let pride rise from the quiet relief of seeing him choose kindness. Make his name intimate and affectionate, not an award announcement.

**강세·발음:** proud of you / Pinocchio. proud의 /d/ 유지, of you 자연 연결.

#### 제페토 · S12-U016 [원문]

> You did the right thing.

**상대·감정:** 피노키오 / 온화한 인정

**연기:** You did the right thing에서 did와 right에 아이의 실제 행동을 인정하는 힘을 준다. thing은 온화하고 확실하게 닫는다.

**합성 지시(영문):** Affirm the choice, not the child's worth. Put steady conviction into right thing, with a tender, settled ending.

**강세·발음:** did / right thing. right의 /t/와 thing의 /ŋ/ 보존.


### S12-C20 · 02:48–02:56 (8초 계획)

**구도:** 문 옆 안전 공간 WS

**화면·동작:** 제페토가 안내판의 회전 경로가 아닌 문 옆 안전한 발 디딤 위치를 가리킨다. 피노키오와 귀뚜라미는 이미 자유롭고 판은 지지점에 안정되어 있다. 제페토가 손바닥으로 자기 옆 위치를 보여 준다.

**음향·경계:** P04 질문 끝에만 정지. 요정·푸른빛 없음.

원전 컷 대응(기존 19컷 번호 체계): S12-C08.

#### 제페토 · S12-N013 [신규]

> Yoonsu, where should he stand?

**상대·감정:** 윤수 / 안전한 안내

**연기:** 안전한 위치를 보여 주고 윤수의 말을 기다린다. stand에 지시 대상이 분명해지도록 따뜻한 질문을 건넨다.

**합성 지시(영문):** Invite Yoonsu to help Pinocchio join him in the clear space beside the doorway. Ask gently and leave room for the answer.

**강세·발음:** where / stand. stand 끝 /d/와 이름 보존.

**🎤 S12-P04 — Stand beside Grandpa.**

뜻을 보여 주는 화면: 제페토가 옆 안전 발 위치를 가리킨다.

대기: WOODEN / SAFE_FREE / 안내판 UPRIGHT_STABLE. 다음 핵심 동작은 수용 전 금지.

외부 모델: 제페토 `S12-M005` 1회. 수용 뒤 발걸음으로 제페토 옆에 합류해 안정되게 멈추고 귀뚜라미가 따라온다. 푸른빛은 이후 U017에서 시작.

재개: `S12-N014`. 셋이 안전한 위치에 정착을 먼저 확인한다.


## B05 — 익숙한 파란빛과 지난 선택 (02:56–03:48)


### S12-C21 · 02:56–03:08 (12초 계획)

**구도:** 옆으로 이동하는 FOLLOW → 고개를 든 얼굴

**화면·동작:** P04 후 피노키오가 제페토 옆의 실제 안전 지점까지 몇 걸음 이동하고 멈춘다. 귀뚜라미가 발치로 따라온다. 셋이 정착한 뒤에만 학교 문 위쪽에 익숙한 푸른빛이 생기고 모두가 자연스럽게 고개를 든다.

**음향·경계:** P04 REACT 실제 종료 뒤 N014, U017. U017부터 U033과 실제 포옹 해제까지 입력·모델 없음.

원전 컷 대응(기존 19컷 번호 체계): S12-C08, S12-C09.

**S12-P04 반응:** 발걸음으로 제페토 옆에 합류해 안정되게 멈추고 귀뚜라미가 따라온다. 푸른빛은 이후 U017에서 시작.

**반응 종료 조건:** 셋이 안전한 위치에 정착. 후속 대사 `S12-N014`는 조건 완료 뒤에만 시작한다.

#### 피노키오 · S12-N014 [신규]

> Here we are.

**상대·감정:** 제페토와 귀뚜라미 / 정착한 만족

**연기:** 제페토 옆에 자리를 잡은 뒤 친구까지 함께 있다는 작은 만족을 건넨다. here에 정착감, are에 편한 미소.

**합성 지시(영문):** Settle beside Grandpa and acknowledge that they are together in the clear spot. Make the line quiet and content.

**강세·발음:** Here. Here we are를 세 단어 낱독으로 끊지 않는다.

#### 내레이션 · S12-U017 [원문]

> Then, a familiar blue light filled the air.

**상대·감정:** 윤수와 관객 / 익숙한 경이로움

**연기:** Then에서 다음 변화에 귀를 열고 familiar blue light에 기억과 놀라움을 함께 싣는다. filled the air는 따뜻한 빛이 주변으로 번지듯 넓어진다.

**합성 지시(영문):** Notice a familiar magic returning. Make familiar tender and blue light luminous in the voice, then gently widen filled the air without shouting.

**강세·발음:** familiar / blue light. familiar의 자연 강세, filled의 /d/ 보존.


### S12-C22 · 03:08–03:17 (9초 계획)

**구도:** 학교 문 위 TILT_UP → 일행 포함 WS

**화면·동작:** 푸른빛 속에서 기존 파란 요정 실루엣이 서서히 선명해진다. 기존 날개·지팡이·의상을 유지한다. 제페토는 눈이 커지며 안경 너머로 올려다보고 피노키오는 고개를 들어 알아본다. 귀뚜라미는 안전한 자리에서 함께 올려다본다. 피노키오는 목각 그대로.

**음향·경계:** 기존 마법 모티프. 푸른빛은 실제 등장 전 동시 변신을 일으키지 않는다. 대사 없이 시선 반응이 이어진다.

원전 컷 대응(기존 19컷 번호 체계): S12-C09.


### S12-C23 · 03:17–03:28 (11초 계획)

**구도:** 요정과 목각 피노키오 TWO SHOT

**화면·동작:** 요정이 적정 높이에서 안정되게 떠 있고 피노키오에게 따뜻하게 시선을 맞춘다. 피노키오는 호기심과 기억을 담아 듣는다. 제페토는 옆에서 미소를 되찾는다.

**음향·경계:** U018 U019 이어짐. 회상으로 시간·공간을 끊지 않는다.

원전 컷 대응(기존 19컷 번호 체계): S12-C10.

#### 파란 요정 · S12-U018 [원문]

> Pinocchio, I have watched you grow.

**상대·감정:** 피노키오 / 애정과 인정

**연기:** 이름을 오랜 시간 지켜본 아이에게 건네듯 다정하게 부른다. I have watched you grow에서 오래 쌓인 경험을 인정하는 따뜻한 확신이 커진다.

**합성 지시(영문):** Speak his name with recognition. Let I have watched you grow carry the warmth of having seen his choices over time, rather than ceremonial grandeur.

**강세·발음:** watched you grow. watched의 /t/와 grow의 자연 연결.

#### 파란 요정 · S12-U019 [원문]

> You told Grandpa the truth.

**상대·감정:** 피노키오 / 진실에 대한 존중

**연기:** told Grandpa the truth에는 10화의 힘든 고백을 기억하는 이해를 담는다. 오늘의 솔직한 말도 들은 듯 작은 미소. truth는 단단하고 부드럽게 닫는다.

**합성 지시(영문):** Remember the difficult honesty he showed Grandpa. Give truth warm conviction, never the sound of a judge listing a score.

**강세·발음:** Grandpa / truth. truth /θ/ 마찰을 살린다.


### S12-C24 · 03:28–03:38 (10초 계획)

**구도:** 요정 MS → 피노키오 표정 CU

**화면·동작:** 요정이 한 손을 천천히 펼친다. 피노키오는 사과의 기억에 고개를 살짝 낮췄다가 약속을 지킨 오늘을 떠올리며 시선을 올린다. 가방과 책이 그대로 어깨에 있다.

**음향·경계:** U020~U021은 연속. 이름이나 핵심어마다 불필요한 효과음 금지.

원전 컷 대응(기존 19컷 번호 체계): S12-C10.

#### 파란 요정 · S12-U020 [원문]

> You said you were sorry.

**상대·감정:** 피노키오 / 용기 인정

**연기:** You said you were sorry는 용기 내어 사과한 마음을 인정한다. sorry에서 다정하게 내려오며 아이가 안심할 수 있게 한다.

**합성 지시(영문):** Acknowledge the courage of his apology. Soften sorry with understanding, not pity or judgment.

**강세·발음:** said / sorry. said의 끝 /d/와 sorry의 자연 발음.

#### 파란 요정 · S12-U021 [원문]

> You kept your promise.

**상대·감정:** 피노키오 / 따뜻한 만족

**연기:** kept your promise에 오늘 실제로 학교에 온 행동을 기뻐하는 확신을 준다. promise 끝에 작게 반짝이는 미소를 남긴다.

**합성 지시(영문):** Celebrate that he followed through on his promise today. Make kept firm and promise warmly satisfied.

**강세·발음:** kept / promise. kept /pt/, promise 끝 /s/ 유지.


### S12-C25 · 03:38–03:48 (10초 계획)

**구도:** 요정·귀뚜라미·피노키오를 함께 담는 MS

**화면·동작:** 요정이 귀뚜라미 쪽을 바라봤다가 피노키오에게 돌아온다. 피노키오는 친구를 한 번 보고 겸손한 표정으로 대답한다. 목각 정상 코 유지.

**음향·경계:** U022→U023을 일반 대화 간격으로 연결. 아직 마법 변화 없음.

원전 컷 대응(기존 19컷 번호 체계): S12-C10, S12-C11.

#### 파란 요정 · S12-U022 [원문]

> And today, you helped a friend.

**상대·감정:** 피노키오 / 오늘의 행동에 대한 자부심

**연기:** And today에서 지금 있었던 행동을 발견한 기쁨이 살아난다. helped a friend에 진심 어린 자랑스러움을 모아 넉넉하게 끝낸다.

**합성 지시(영문):** Move from remembered choices to what just happened. Let today brighten and helped a friend become the warm emotional peak of the recognition.

**강세·발음:** today / helped a friend. helped /t/와 friend /d/ 보존.

#### 피노키오 · S12-U023 [원문]

> I only wanted to help him.

**상대·감정:** 파란 요정 / 겸손한 솔직함

**연기:** I only wanted to는 겸손한 솔직함. help him에서 친구 쪽에 시선을 주며 자기에게 상이 필요해서 한 일이 아니라는 따뜻한 확신을 전한다.

**합성 지시(영문):** Answer simply and honestly, almost surprised by the praise. Let help him carry his real motive, without false modesty or boasting.

**강세·발음:** only / help him. wanted to 연결, him /m/ 보존.


## B06 — 마지막 마법과 인간형 변신 (03:48–04:34)


### S12-C26 · 03:48–03:58 (10초 계획)

**구도:** 요정과 아이 CU 교차

**화면·동작:** 요정의 표정이 부드러워지고 지팡이를 쥐지 않은 손을 가슴 앞으로 가져온다. 피노키오는 눈을 맞추고 귀뚜라미는 고개를 들어 조용히 듣는다.

**음향·경계:** 대사 사이 감정 변화만, 입력·리워드 없음.

원전 컷 대응(기존 19컷 번호 체계): S12-C11.

#### 파란 요정 · S12-U024 [원문]

> That is what makes you kind.

**상대·감정:** 피노키오 / 다정한 긍정

**연기:** That is what에서 바로 피노키오가 방금 말한 이유를 받아 준다. kind에는 작지만 깊은 긍정이 깃든다.

**합성 지시(영문):** Respond directly to his motive. Put the whole tenderness of the moment into kind, rather than sounding like a definition in a lesson.

**강세·발음:** kind. kind의 /d/를 유지.

#### 파란 요정 · S12-U025 [원문]

> You have a brave and caring heart.

**상대·감정:** 피노키오 / 존중→배려

**연기:** brave와 caring을 서로 다른 감정으로 표현한다. brave는 두려워도 도운 선택을 존중하고 caring은 친구를 향한 부드러움으로 마친다.

**합성 지시(영문):** Honor the courage of acting despite fear, then soften caring into affection. Let heart finish with calm, heartfelt conviction.

**강세·발음:** brave / caring heart. brave의 /v/, heart의 /t/ 명료하게.


### S12-C27 · 03:58–04:06 (8초 계획)

**구도:** 요정 중심 MS → 지팡이 CU

**화면·동작:** 요정이 피노키오를 안심시키는 미소와 함께 지팡이를 천천히 준비한다. 피노키오가 고개를 살짝 갸웃하며 다음 일을 기다린다. 모두의 시선은 같은 지팡이로 이동한다. 목각·정상 코.

**음향·경계:** U026 말끝 이후 지팡이 들어 올리기 시작. 변신은 아직 없음.

원전 컷 대응(기존 19컷 번호 체계): S12-C11.

#### 파란 요정 · S12-U026 [원문]

> Now, it's time for one last bit of magic.

**상대·감정:** 피노키오 / 선물을 앞둔 기대

**연기:** Now는 조용한 전환, one last bit에는 오래 간직한 선물을 열어 보이는 기대를 준다. magic에서 환하게 펼치되 경박한 진행자 말투를 쓰지 않는다.

**합성 지시(영문):** Reveal that something special is about to happen. Gather affectionate anticipation through one last bit, then let magic shine with wonder.

**강세·발음:** Now / one last bit / magic. last bit의 /st b/와 magic /k/ 보존.


### S12-C28 · 04:06–04:12 (6초 계획)

**구도:** 발끝에서 얼굴로 이어지는 TILT / MS

**화면·동작:** 요정이 지팡이를 실제 손목·팔 동작으로 올린다. 기존 푸른 입자가 발끝에서 몸 주변을 따라 올라간다. 피노키오는 호기심에서 신뢰로 표정이 바뀌고 눈을 감고 두 팔을 편다. 무릎과 발의 지지는 그대로, 모자·가방 고정. 목재 나뭇결과 관절은 아직 그대로다.

**음향·경계:** 마법 효과는 말 전 준비. 단순 플래시·흰 화면으로 변신을 숨기지 않는다. 대사 없음.

원전 컷 대응(기존 19컷 번호 체계): S12-C12.


### S12-C29 · 04:12–04:20 (8초 계획)

**구도:** 요정 지팡이와 피노키오 얼굴 CLOSE

**화면·동작:** 요정이 아이에게 지팡이를 향하되 직접 닿지 않는다. 피노키오는 눈을 감고 목각 모습으로 기다린다. 빛이 몸을 감싸고 마지막 약속을 전달한다.

**음향·경계:** U027 마지막 발음이 끝날 때까지 인간형 외형 노출 금지. 입력 금지.

원전 컷 대응(기존 19컷 번호 체계): S12-C12.

#### 파란 요정 · S12-U027 [원문]

> Pinocchio, you can become a real boy!

**상대·감정:** 피노키오 / 깊은 기쁨과 경이로운 약속

**연기:** Pinocchio에서 이 아이에게 선물을 직접 건넨다. you can에 깊은 확신, become a real boy에는 희망이 열리는 놀라움을 풍성하게 모아 끝맺는다. 소리를 키우는 것만으로 마법을 표현하지 않는다.

**합성 지시(영문):** Make this a personal, deeply joyful promise. Build certainty through you can and open into wonder on a real boy, with the tenderness of a gift rather than a command.

**강세·발음:** you can / real boy. real과 boy의 모음을 명확히, 이름은 기존 승인 발음.


### S12-C30 · 04:20–04:34 (14초 계획)

**구도:** 변신 전용 전신 → 손·얼굴 CLOSE

**화면·동작:** U027 종료 후에만 발끝→다리→몸통→팔·손→얼굴 순으로 목재 색·관절·나뭇결이 단계적으로 사라진다. 동일 시점의 승인 CHAR_YOONSU_HUMAN 포즈를 정렬하고 같은 발 접지·팔끝·모자 위치·가방 접촉점으로 사람형이 완성된다. 새 얼굴은 승인 윤수 원화와 일치해야 한다. 얼굴·손·몸을 모두 사람형으로 정착시키고 빛을 걷어낸다.

**음향·경계:** U027 실제 종료 후 목각→인간형을 정확히 한 번 전환. 실제 변신 완료 뒤 U028. U028 실제 종료 뒤 짧은 발견 표정만 연결하고 곧바로 C31의 U029; 질문·모델·고정 잔여시간 채우기 없음. 코 성장 효과 없음. 승인 인간형 원화 없으면 BLOCKED_RESOURCE.

원전 컷 대응(기존 19컷 번호 체계): S12-C13.

#### 내레이션 · S12-U028 [원문]

> And just like that, the wooden puppet became a real little boy.

**상대·감정:** 윤수와 관객 / 경이로움→감동

**연기:** And just like that은 긴 마법이 실제로 이루어진 순간의 경이로움. wooden puppet에서 지난 모습을 짚고 became a real little boy에 따뜻한 감동이 크게 열린다. 마지막은 아이를 만난 미소처럼 마친다.

**합성 지시(영문):** Witness the change as it finishes. Carry the memory of the wooden puppet into the wonder of became a real little boy. Open with awe and finish with intimate joy.

**강세·발음:** wooden puppet / became / real little boy. wooden의 모음, became의 끝 /m/, little boy의 자연 연결.


## B07 — 첫 환희·가족 포옹을 먼저 나누다 (04:34–05:22)


### S12-C31 · 04:34–04:42 (8초 계획)

**구도:** 변신 직후 얼굴 CU → 제페토와 TWO SHOT

**화면·동작:** 인간형으로 안정된 피노키오가 눈을 뜨고 자기 몸을 짧게 내려다본 뒤 가장 먼저 제페토를 바라본다. 즉시 얼굴이 환해지고 팔을 조금 벌려 자기를 보여 준다. 제페토는 처음 보는 인간형 모습에 놀라며 감격한다. 손 탐색 시범이나 윤수 질문을 끼우지 않는다.

**음향·경계:** U028 실제 종료→짧은 발견 반응→U029, U030. U031로 감정을 이어 준다. 계획 컷 시간을 채우려고 침묵하지 않는다.

원전 컷 대응(기존 19컷 번호 체계): S12-C14.

#### 피노키오 · S12-U029 [원문]

> Grandpa! Look at me!

**상대·감정:** 제페토 / 폭발적 기쁨

**연기:** Grandpa!는 가장 먼저 사랑하는 사람에게 소식을 전하고 싶은 폭발적인 기쁨. Look at me!에서 몸을 보여 주는 들뜸을 크게 펼친다.

**합성 지시(영문):** Burst out toward the person he loves most. Throw Grandpa with joyful urgency, then open Look at me into a child's amazed delight.

**강세·발음:** Grandpa / Look / me. 두 문장의 끝을 삼키지 않고 Look at 연결.

#### 피노키오 · S12-U030 [원문]

> I'm a real boy!

**상대·감정:** 제페토 / 믿기 어려운 감격과 환희

**연기:** I'm에서 자기 자신을 새롭게 발견한 놀람이 시작된다. real boy에서 믿기 어려운 감격과 기쁨을 정점으로 만들고 boy는 환하게 열린다. U029와 같은 억양을 복제하지 않는다.

**합성 지시(영문):** Discover the reality of it in his own voice. Let real become the emotional revelation and boy release it into exuberant joy; make this different from the call before it.

**강세·발음:** real / boy. I'm의 /m/, real의 /l/, boy의 이중모음 유지.


### S12-C32 · 04:42–04:51 (9초 계획)

**구도:** 제페토 얼굴 CU → TWO SHOT

**화면·동작:** 제페토의 눈이 커지고 안경 아래 표정이 놀라움에서 벅찬 애정으로 바뀐다. 손을 입 가까이 가져갔다가 아이를 안으려 천천히 연다. 아이는 제페토의 눈을 바라본다.

**음향·경계:** U031, U032는 첫 인간형 발견에 대한 실제 응답. 마지막 말 뒤 C33 포옹으로 연속. 입력·모델 없음.

원전 컷 대응(기존 19컷 번호 체계): S12-C15.

#### 제페토 · S12-U031 [원문]

> Pinocchio! My dear boy!

**상대·감정:** 피노키오 / 놀라움→벅찬 애정

**연기:** Pinocchio!에서는 놀라움과 사랑이 한꺼번에 솟는다. My dear boy!는 가슴 깊은 곳에서 따뜻하게 떨리는 애정. 같은 크기의 두 감탄사를 기계적으로 이어 읽지 않는다.

**합성 지시(영문):** The name should escape him in astonished joy. Then My dear boy is an intimate surge of love; soften the projection and let the warmth tremble naturally.

**강세·발음:** Pinocchio / my dear boy. 기존 고정 음색. dear boy 연결과 이름 끝 유지.

#### 제페토 · S12-U032 [원문]

> You are real!

**상대·감정:** 피노키오 / 감격과 기쁨

**연기:** You are real!에서 눈앞의 변화가 믿기지 않는 기쁨을 다시 확인한다. real에 감격을 모으고 아이를 바라보는 미소로 마친다. 사랑의 조건이 인간이 되는 것이 아니라는 흐름을 유지한다.

**합성 지시(영문):** Let him realize what he sees, with quiet astonishment swelling into joy on real. This is wonder at a change, never a condition for his love.

**강세·발음:** real. are를 없애지 않고 real /l/ 명료하게.


### S12-C33 · 04:51–05:02 (11초 계획)

**구도:** 전신 TWO SHOT → 친밀한 MS

**화면·동작:** 제페토가 팔을 실제로 벌리고 피노키오가 한 발 다가간다. 제페토가 무릎을 굽혀 키 차이를 맞추고 둘의 손과 팔이 서로의 등·어깨 옆 안전 접촉점에 닿는다. 아이도 양팔로 할아버지를 안는다. 가방은 등 뒤 그대로이며 손이 가방을 관통하지 않는다. 모자는 떨어지지 않고 약간 기울 뿐이다.

**음향·경계:** 서로의 포옹 접촉이 안정된 뒤 N020→N021. 같은 사랑을 재확인하며 입력·모델로 끊지 않는다.

원전 컷 대응(기존 19컷 번호 체계): S12-C16.

#### 제페토 · S12-N020 [신규]

> I love you, just the same.

**상대·감정:** 피노키오 / 변하지 않는 사랑

**연기:** 아이를 안은 상태에서 목각이든 인간이든 변하지 않는 사랑을 진심으로 전한다. love you는 가깝고 낮게, just the same에는 오래 지켜온 확신을 싣는다.

**합성 지시(영문):** Hold the child and reassure him that the love has not changed. Make just the same a tender certainty, not a moral speech.

**강세·발음:** love you / just the same. love의 /v/, same의 /m/ 보존.

#### 피노키오 · S12-N021 [신규]

> I love you too, Grandpa.

**상대·감정:** 제페토 / 안온한 행복

**연기:** 품에 기대어 말하는 작은 행복이다. too에서 마음이 즉시 되돌아오고 Grandpa를 안심하고 부른다. 환호와 다른 가까운 목소리.

**합성 지시(영문):** Answer from the comfort of the embrace. Let too return the affection naturally and Grandpa finish with safe, quiet happiness.

**강세·발음:** too / Grandpa. too와 이름을 끊어 읽지 않는다.


### S12-C34 · 05:02–05:10 (8초 계획)

**구도:** 귀뚜라미 전신 → 가족 WS

**화면·동작:** 귀뚜라미가 준비·도약·착지가 보이는 작은 축하 점프를 한다. U033을 들으며 피노키오와 제페토가 서로의 팔과 손을 천천히 풀어 안정된 두 발로 선다. 눈맞춤과 미소가 이어지고 요정은 따뜻하게 지켜본다.

**음향·경계:** U033 실제 종료와 포옹 해제 동작이 모두 완료된 다음에만 C35의 손 탐색. 변신→환희→응답→포옹→축하 구간에는 참여 없음.

원전 컷 대응(기존 19컷 번호 체계): S12-C16.

#### 귀뚜라미 · S12-U033 [원문]

> You did it, Pinocchio!

**상대·감정:** 피노키오 / 친구의 성장에 대한 축하

**연기:** You did it은 함께한 친구가 성장한 것이 기뻐 터지는 축하. Pinocchio에 친구다운 친근함을 더한다. 인간형이 돼서 이제야 친구가 된다는 의미가 아니다.

**합성 지시(영문):** Celebrate his journey with a bright little burst of shared pride. Say his name with familiar friendship; he was already your friend before the magic.

**강세·발음:** did it / Pinocchio. did it 연결, 이름 끝 유지.


### S12-C35 · 05:10–05:22 (12초 계획)

**구도:** 손과 얼굴 MS → 제페토 TWO SHOT

**화면·동작:** 포옹 후 피노키오가 자기 손의 낯선 촉감을 느끼며 손바닥과 손등을 천천히 살핀다. 손가락을 일부러 굽히는 과제는 아직 하지 않는다. 제페토가 자기 두 손바닥을 보이도록 펴서 보여 주기 동작을 먼저 시범 보인다. 피노키오는 손을 자기 쪽에 둔 채 관찰하고, 제페토가 윤수를 본다.

**음향·경계:** 첫 감격을 이미 나눈 뒤의 호기심. N015→제페토 시범 완료→N016 실제 종료→P05. 변신이나 사랑을 기다리는 대기가 아니다.

원전 컷 대응(기존 19컷 번호 체계): S12-C14, S12-C16.

#### 피노키오 · S12-N015 [신규]

> My hands feel different!

**상대·감정:** 자기 자신과 제페토 / 포옹 후 촉감에 대한 세밀한 호기심

**연기:** 포옹과 첫 환희를 나눈 뒤 자기 손의 촉감을 자세히 알아본다. 손으로 느끼는 different에 부드럽고 생생한 호기심을 준다. 사람이 됐다는 사실을 처음 발견하거나 가족에게 재발표하는 연기가 아니다.

**합성 지시(영문):** After the first joyful reunion and embrace, explore the tactile difference in his hands. Let different reveal close, delighted curiosity about the texture, not a second discovery that he has become human.

**강세·발음:** hands / different. hands의 /dz/, different의 마지막 자음 보존.

#### 제페토 · S12-N016 [신규]

> Yoonsu, can he show me his hands?

**상대·감정:** 윤수 / 편안한 호기심과 다정한 부탁

**연기:** 첫 감격이 지나간 뒤 아이의 손을 가까이 보고 싶어 하는 다정한 부탁. 윤수에게 손바닥을 보여 주는 시범을 먼저 건네고 show me his hands를 편안하게 연결한다. 변신 승인이나 가족의 사랑을 기다리는 질문처럼 들리지 않는다.

**합성 지시(영문):** After their joyful embrace, warmly invite a closer look at his hands. This is relaxed shared curiosity, never a condition for the magic or the family reunion.

**강세·발음:** Yoonsu / show / hands. show me 자연 연결, hands 끝 보존.

**🎤 S12-P05 — Show your hands.**

뜻을 보여 주는 화면: 변신·첫 환희·가족 포옹·귀뚜라미 축하와 포옹 해제 완료. 제페토가 자신의 두 손바닥을 보여 주는 시범을 먼저 한다. 아이는 자기 쪽에서 손을 보고, 제페토에게 펼치는 동작은 수용 후.

대기: CHAR_YOONSU_HUMAN / SAFE_FREE / 안내판 UPRIGHT_STABLE. 다음 핵심 동작은 수용 전 금지.

외부 모델: 제페토 `S12-M006` 1회. 수용 뒤 양팔을 자연스럽게 펼쳐 두 손을 제페토가 볼 수 있게 보여 준다.

재개: `S12-N017`. 두 손의 자세 안정·제페토 시선 도착을 먼저 확인한다.


## B08 — 손의 감촉을 함께 살피다 (05:22–06:09)


### S12-C36 · 05:22–05:31 (9초 계획)

**구도:** 보여 주는 손 CLOSE → 제페토 시선

**화면·동작:** P05 수용 후 피노키오가 어깨·팔꿈치·손목으로 두 손을 제페토 쪽에 펼친다. 제페토는 잡아당기지 않고 눈높이를 낮춰 손을 바라본다. 아이의 손 자세와 제페토 시선이 안정된 뒤 다정하게 반응한다.

**음향·경계:** 손 보여 주기 완료 뒤 N017. 이 컷에는 새 질문 없음. 다음 질문 전 제페토의 별도 시범으로 의미를 잇는다.

원전 컷 대응(기존 19컷 번호 체계): S12-C14, S12-C16.

**S12-P05 반응:** 양팔을 자연스럽게 펼쳐 두 손을 제페토가 볼 수 있게 보여 준다.

**반응 종료 조건:** 두 손의 자세 안정·제페토 시선 도착. 후속 대사 `S12-N017`는 조건 완료 뒤에만 시작한다.

#### 제페토 · S12-N017 [신규]

> Look at those little hands!

**상대·감정:** 피노키오 / 가까이서 살펴보는 애정

**연기:** 손을 실제로 보여 준 데 대한 다정한 반응. little hands에 가까이서 발견한 섬세함과 애정을 싣는다. 첫 인간형 발견의 큰 놀라움은 앞서 끝났으므로 같은 감탄을 재연하지 않는다.

**합성 지시(영문):** Respond to the hands now being shown up close. Give little hands tender, intimate appreciation; the first astonished discovery of his human form has already happened.

**강세·발음:** Look / little hands. Look의 /k/, hands의 끝 자음 유지.


### S12-C37 · 05:31–05:40 (9초 계획)

**구도:** 제페토 자기 손 시범 → 피노키오 눈맞춤

**화면·동작:** 제페토가 자기 손을 들어 자기 손가락을 천천히 굽혔다 펴는 시범을 한 번 보인다. 피노키오는 그 손과 자기 손을 번갈아 보고 자기 손가락은 과제 동작 전 자세로 유지한다. 제페토 시범이 끝난 뒤 피노키오가 윤수를 바라본다.

**음향·경계:** 제페토 자기 손 시범 완료→N018 실제 종료→P06. 시범은 제페토, 수용 후 과제 수행은 피노키오로 분리.

원전 컷 대응(기존 19컷 번호 체계): S12-C14, S12-C16.

#### 피노키오 · S12-N018 [신규]

> Yoonsu, shall I bend my fingers?

**상대·감정:** 윤수 / 신기함과 기대

**연기:** 자기 손가락을 보며 궁금증이 살아난다. bend my fingers를 손가락 쪽 시선과 맞추고 실제 동작을 기다리는 질문으로 마친다.

**합성 지시(영문):** Invite Yoonsu to explore this new feeling with him. Sound eager and curious, with a true questioning finish.

**강세·발음:** bend / fingers. bend의 /d/, fingers의 /z/ 보존.

**🎤 S12-P06 — Bend your fingers.**

뜻을 보여 주는 화면: 제페토가 자기 손가락을 굽혔다 펴서 먼저 시범을 보인다. 피노키오는 보고 질문하며 자신의 굽힘 동작은 아직 하지 않는다.

대기: CHAR_YOONSU_HUMAN / SAFE_FREE / 안내판 UPRIGHT_STABLE. 다음 핵심 동작은 수용 전 금지.

외부 모델: 피노키오 `S12-M007` 1회. 수용 뒤 손가락을 실제 관절로 굽혔다 펴고 다른 손으로 손바닥을 가볍게 만진다.

재개: `S12-N019`. 손가락 굽힘·펴짐 및 손바닥 접촉 완료을 먼저 확인한다.


### S12-C38 · 05:40–05:50 (10초 계획)

**구도:** 피노키오 인간형 손 CLOSE → 얼굴

**화면·동작:** P06 수용 후 피노키오가 자기 손가락을 실제 관절대로 굽혔다 펴고 다른 손으로 손바닥을 가볍게 만진다. 목각 때도 움직였던 손이므로 움직임 능력이 새로 생긴 연기가 아니라 부드러운 촉감에 대한 발견이다. 동작이 끝나면 팔을 편히 낮춘다.

**음향·경계:** 손가락 굽힘·펴짐과 손바닥 접촉 완료 뒤 N019. 중복 손이나 순간 교체 금지. 다음 손잡기 질문 전 자세 안정.

원전 컷 대응(기존 19컷 번호 체계): S12-C14, S12-C16.

**S12-P06 반응:** 손가락을 실제 관절로 굽혔다 펴고 다른 손으로 손바닥을 가볍게 만진다.

**반응 종료 조건:** 손가락 굽힘·펴짐 및 손바닥 접촉 완료. 후속 대사 `S12-N019`는 조건 완료 뒤에만 시작한다.

#### 피노키오 · S12-N019 [신규]

> They feel so soft!

**상대·감정:** 제페토 / 촉감의 경이로움

**연기:** 자기 손바닥을 만진 순간 부드러움을 발견한다. so soft를 정말 신기한 촉감처럼 따뜻하게 펼치고 기쁜 표정으로 마친다.

**합성 지시(영문):** React to the texture he has just felt. Let soft carry genuine tactile amazement rather than a flat description.

**강세·발음:** feel / so soft. soft /ft/ 보존.


### S12-C39 · 05:50–05:59 (9초 계획)

**구도:** 제페토와 아이 손이 보이는 MS

**화면·동작:** 제페토가 손바닥을 위로 열어 아이에게 내민다. 피노키오는 제페토의 얼굴에서 내민 손으로 시선을 옮기고 자기 손을 준비하되 아직 닿지 않는다. 제페토가 윤수를 바라본다.

**음향·경계:** 시범은 손 내밀기만. N022 실제 종료→P07. 손 접촉은 수용 후 C40에서.

원전 컷 대응(기존 19컷 번호 체계): S12-C16.

#### 제페토 · S12-N022 [신규]

> Yoonsu, can he take my hand?

**상대·감정:** 윤수 / 포옹 이후의 편안한 초대

**연기:** 따뜻한 포옹을 나눈 뒤 아이에게 손을 내미는 조용한 초대. take my hand를 가까운 상대에게 편안하게 건네며, 처음 접촉하는 순간처럼 새로 놀라지 않는다.

**합성 지시(영문):** Offer a quiet, affectionate hand after the embrace they have already shared. Make take my hand an easy invitation, without replaying the first emotional reunion.

**강세·발음:** take my hand. take /k/와 hand /d/ 보존.

**🎤 S12-P07 — Take Grandpa's hand.**

뜻을 보여 주는 화면: 포옹은 끝났고 제페토가 손을 내민다. 두 손은 미접촉.

대기: CHAR_YOONSU_HUMAN / SAFE_FREE / 안내판 UPRIGHT_STABLE. 다음 핵심 동작은 수용 전 금지.

외부 모델: 제페토 `S12-M008` 1회. 수용 뒤 아이 손이 제페토 손에 실제 닿고 자연스럽게 감싸서 잡는다. N023~N024 대화 뒤 손을 해제한다.

재개: `S12-N023`. 공유 손 접촉 안정(해제는 N024 이후, P08 이전)을 먼저 확인한다.


### S12-C40 · 05:59–06:09 (10초 계획)

**구도:** 공유 손 CLOSE → 두 얼굴

**화면·동작:** P07 수용 뒤 피노키오의 손이 제페토 손에 실제로 닿고 자연스럽게 감싼다. 서로의 온기를 느끼며 눈을 맞춘다. N023과 N024가 끝난 뒤 양쪽 손가락을 풀고 실제로 손을 떨어뜨린다. 손 해제를 완료한 상태로 다음 컷에 넘긴다.

**음향·경계:** 공유 손 접촉 안정→N023→N024 실제 종료→손 해제 완료. 이 컷에는 모자 질문 없음.

원전 컷 대응(기존 19컷 번호 체계): S12-C16.

**S12-P07 반응:** 아이 손이 제페토 손에 실제 닿고 자연스럽게 감싸서 잡는다. N023~N024 대화 뒤 손을 해제한다.

**반응 종료 조건:** 공유 손 접촉 안정(해제는 N024 이후, P08 이전). 후속 대사 `S12-N023`는 조건 완료 뒤에만 시작한다.

#### 제페토 · S12-N023 [신규]

> Your hand is warm.

**상대·감정:** 피노키오 / 따뜻한 발견

**연기:** 작은 손을 잡고 느낀 감동을 속삭이듯 가까이 전한다. warm에서 따뜻한 감격이 부풀었다가 잔잔해진다.

**합성 지시(영문):** Discover the warmth of the hand he is holding. Let warm carry a quiet, emotional realization, with clear speech rather than a whisper that loses words.

**강세·발음:** hand / warm. hand is 연결, warm /m/ 유지.

#### 피노키오 · S12-N024 [신규]

> So is yours!

**상대·감정:** 제페토 / 장난스러운 반가움

**연기:** 할아버지의 손에서도 따뜻함을 느낀 아이의 즐거운 응답. So에서 즉시 반응하고 yours에 친근한 확신을 준다.

**합성 지시(영문):** Reply with a small delighted discovery that Grandpa's hand is warm too. Keep the conversational bounce and affection.

**강세·발음:** So / yours. yours /z/ 보존.


## B09 — 약속과 마지막 인사 (06:09–06:56)


### S12-C41 · 06:09–06:18 (9초 계획)

**구도:** 기울어진 모자 MS → 제페토 손짓

**화면·동작:** 포옹 때 조금 기울어진 같은 빨간 모자가 보인다. 제페토가 모자의 기울기를 가리킨 뒤 자기 빈 손바닥을 기운 각도에서 수평으로 바꾸어 바로 맞추기의 뜻을 보여 준다. 제페토에게 새 모자를 만들지 않는다. 피노키오는 아직 모자에 손을 대지 않는다.

**음향·경계:** C40의 실제 손 해제 완료→기울기/수평 시범→N025 실제 종료→P08. 단어를 몰라도 대상과 필요한 변화가 보인다.

원전 컷 대응(기존 19컷 번호 체계): S12-C16.

#### 제페토 · S12-N025 [신규]

> Yoonsu, can you help with his hat?

**상대·감정:** 윤수 / 다정한 미소

**연기:** 모자 가장자리를 가리키며 흐뭇하게 웃는다. help with his hat에 사소한 준비를 함께 돕는 친근함을 준다.

**합성 지시(영문):** Point to the slightly tilted hat and invite a simple finishing adjustment. Be gently amused and affectionate, not urgent.

**강세·발음:** help / hat. help /p/, hat /t/ 보존.

**🎤 S12-P08 — Straighten your hat.**

뜻을 보여 주는 화면: C40의 실제 손 해제 완료 뒤 제페토가 같은 기울어진 모자를 가리키고 빈 손바닥을 기운 각도에서 수평으로 바꾸는 시범. 피노키오의 모자 접촉은 수용 후.

대기: CHAR_YOONSU_HUMAN / SAFE_FREE / 안내판 UPRIGHT_STABLE. 다음 핵심 동작은 수용 전 금지.

외부 모델: 제페토 `S12-M009` 1회. 수용 뒤 양손을 테두리에 대고 모자 방향을 바로잡고 손을 놓는다.

재개: `S12-N026`. 같은 모자 정렬·손 해제 완료을 먼저 확인한다.


### S12-C42 · 06:18–06:26 (8초 계획)

**구도:** 모자·양손 CLOSE → 학교 방향 MS

**화면·동작:** P08 수용 뒤 피노키오가 양손으로 같은 모자 테두리에 실제 접촉하고 모자의 기울기를 바로잡는다. 안정된 모자를 놓고 가방끈을 가볍게 확인한 뒤 열린 학교 문을 바라본다. 모자·책·가방 교체나 입장 없음.

**음향·경계:** 모자 정렬과 손 해제 완료 뒤 N026. 차분한 만족에서 다시 학교를 기대하는 표정으로.

원전 컷 대응(기존 19컷 번호 체계): S12-C16.

**S12-P08 반응:** 양손을 테두리에 대고 모자 방향을 바로잡고 손을 놓는다.

**반응 종료 조건:** 같은 모자 정렬·손 해제 완료. 후속 대사 `S12-N026`는 조건 완료 뒤에만 시작한다.

#### 피노키오 · S12-N026 [신규]

> There. I'm ready.

**상대·감정:** 제페토 / 만족→기대

**연기:** There는 모자가 제대로 놓인 것을 확인한 작은 만족. I'm ready에서 다시 학교에 갈 기대가 밝고 단단하게 돌아온다.

**합성 지시(영문):** Finish the adjustment with a satisfied There, then become ready for school again with a calm, bright determination.

**강세·발음:** There / ready. 두 문장 사이 짧은 자연 쉼, I'm /m/ 보존.


### S12-C43 · 06:26–06:38 (12초 계획)

**구도:** 요정과 피노키오 TWO SHOT → 아이 CU

**화면·동작:** 요정이 가까운 안정 위치에서 마지막 축복을 건네고 피노키오는 몸을 돌려 올려다본다. U034를 들은 뒤 아이가 고개를 끄덕이고 가슴 가까이에 손을 잠깐 올렸다가 감사하며 내린다. 제페토와 귀뚜라미는 곁에서 듣는다.

**음향·경계:** U034 실제 종료→자연 응답→U035. 두 대사 사이 질문·모델 없음. 실제 반응 간격은 최종 음원에 맞추며 계획 여백을 의무 침묵으로 쓰지 않는다.

원전 컷 대응(기존 19컷 번호 체계): S12-C16.

#### 파란 요정 · S12-U034 [원문]

> Stay kind, and keep telling the truth.

**상대·감정:** 피노키오 / 따뜻한 축복

**연기:** Stay kind는 앞으로도 지금처럼 살아가길 바라는 따뜻한 축복. keep telling the truth에는 어려워도 솔직할 수 있다는 믿음을 싣는다. 벌을 암시하지 않는다.

**합성 지시(영문):** Offer a loving farewell blessing, not a rule backed by punishment. Keep kind warm and telling the truth quietly steadfast.

**강세·발음:** kind / keep telling the truth. kind /d/ 및 truth /θ/ 보존.

#### 피노키오 · S12-U035 [원문]

> I will. Thank you!

**상대·감정:** 파란 요정 / 다짐→감사

**연기:** I will은 자신이 계속 배워 나가겠다는 또렷한 다짐. Thank you!에서는 요정을 향한 감사가 환하게 번진다. 기계적인 응답이 아닌 따뜻한 진심이다.

**합성 지시(영문):** Answer with his own sincere commitment on I will, then let gratitude brighten Thank you. Keep a clear emotional shift between the two sentences.

**강세·발음:** I will / Thank you. will /l/, Thank /θ/ 명확히.


### S12-C44 · 06:38–06:46 (8초 계획)

**구도:** 피노키오·요정·윤수 시선 구도

**화면·동작:** 요정이 지팡이를 낮추며 작별 준비를 한다. 피노키오가 그녀를 향해 시선을 두고 손을 들기 직전 윤수에게 고개를 돌린다. 요정은 아직 사라지거나 손인사를 먼저 하지 않는다.

**음향·경계:** N027 실제 종료→P09. 실제 손인사와 요정 후퇴는 수용 후 C45.

원전 컷 대응(기존 19컷 번호 체계): S12-C16.

#### 피노키오 · S12-N027 [신규]

> Yoonsu, shall we wave to the fairy?

**상대·감정:** 윤수 / 애틋한 초대

**연기:** 윤수와 함께 고마운 요정을 보내고 싶다는 밝고 애틋한 초대. wave to the fairy가 부드럽게 이어지며 진짜 대답을 기다린다.

**합성 지시(영문):** Invite Yoonsu to share a warm farewell. Let wave to the fairy be affectionate and a little wistful, with a genuine open question.

**강세·발음:** Yoonsu / wave / fairy. wave /v/와 fairy의 끝 음절 보존.

**🎤 S12-P09 — Wave goodbye, please.**

뜻을 보여 주는 화면: 요정과 아이의 눈이 마주치고 손인사 준비 상태.

대기: CHAR_YOONSU_HUMAN / SAFE_FREE / 안내판 UPRIGHT_STABLE. 다음 핵심 동작은 수용 전 금지.

외부 모델: 피노키오 `S12-M010` 1회. 수용 뒤 피노키오가 요정에게 손을 흔들고 요정이 손인사를 되돌려 주며 물러난다. 아이가 손을 내린 뒤 윤수 쪽을 향한다.

재개: `S12-U036`. 요정과 손인사 완료·요정 거리 확보·윤수로 시선 이동을 먼저 확인한다.


### S12-C45 · 06:46–06:56 (10초 계획)

**구도:** WS → 피노키오 CU

**화면·동작:** P09 수용 뒤 피노키오가 실제 손목과 팔을 움직여 요정에게 손을 흔든다. 요정이 손인사를 되돌려 주고 천천히 학교 지붕 위로 물러난다. U042가 멀리서 들릴 만큼 화면상 거리 확보. 피노키오가 손을 내린 뒤 윤수를 바라보고 별도의 작은 손인사를 건넨다.

**음향·경계:** 요정은 사라졌다는 선언 없이 멀어진다. 동작 끝 뒤 U036. 이후 입력·모델 없음.

원전 컷 대응(기존 19컷 번호 체계): S12-C16.

**S12-P09 반응:** 피노키오가 요정에게 손을 흔들고 요정이 손인사를 되돌려 주며 물러난다. 아이가 손을 내린 뒤 윤수 쪽을 향한다.

**반응 종료 조건:** 요정과 손인사 완료·요정 거리 확보·윤수로 시선 이동. 후속 대사 `S12-U036`는 조건 완료 뒤에만 시작한다.

#### 피노키오 · S12-U036 [원문]

> See you later, Yoonsu!

**상대·감정:** 윤수 / 밝고 애틋한 작별

**연기:** 윤수를 정말 함께한 친구처럼 바라본다. See you later는 다시 만날 기쁜 약속의 느낌, Yoonsu에는 지금까지 함께해 준 마음을 담아 밝고 다정하게 마친다.

**합성 지시(영문):** Say goodbye directly to the friend who has shared the journey. Let see you later sound hopeful and Yoonsu feel personal, with a warm wave in the voice.

**강세·발음:** See you later / Yoonsu. see you later를 끊지 않고 이름은 기존 승인 발음.


## B10 — 학교로 들어가는 진짜 아이 (06:56–07:48)


### S12-C46 · 06:56–07:06 (10초 계획)

**구도:** 학교 문 앞 WS → 서서히 PULL

**화면·동작:** 윤수에게 마지막 인사를 한 뒤 피노키오가 문 안쪽을 바라본다. 제페토는 가까이서 배웅하고 귀뚜라미는 안전하게 곁에 있다. 교사는 말 없이 문 안쪽에서 아이가 지나갈 공간을 마련한다. 피노키오가 자세를 바로 잡는다.

**음향·경계:** U037~U044 보호 구간. 음악은 따뜻하되 말을 덮지 않는다.

원전 컷 대응(기존 19컷 번호 체계): S12-C17.

#### 내레이션 · S12-U037 [원문]

> Pinocchio was still learning.

**상대·감정:** 윤수와 관객 / 부드러운 희망

**연기:** still learning에 아이의 앞으로 남은 많은 시간을 따뜻하게 발견한다. 완벽해졌다고 선언하는 승리의 말투가 아니다.

**합성 지시(영문):** Look at a child who is only beginning to learn. Warm still learning with hope rather than declaring that the journey is perfect or finished.

**강세·발음:** still learning. still /l/과 learning /ŋ/ 유지.

#### 내레이션 · S12-U038 [원문]

> He would make more mistakes.

**상대·감정:** 윤수와 관객 / 편안한 인정

**연기:** more mistakes를 무겁게 비난하지 않고 자연스럽게 예상한다. 실수할 수 있어도 사랑과 배움이 계속된다는 편안한 확신.

**합성 지시(영문):** Acknowledge future mistakes without disappointment or threat. Let the words sound like a gentle truth about growing up.

**강세·발음:** more mistakes. mistakes 끝 /ks/ 보존.


### S12-C47 · 07:06–07:17 (11초 계획)

**구도:** 피노키오와 열린 문 MS

**화면·동작:** 아이의 눈이 문 안쪽을 살피고 가방끈에 손을 가볍게 댄다. 제페토는 옆에서 미소 짓는다. 화면 안 행동만으로 새 배움의 기대를 전달하며 회상 삽입 없음.

**음향·경계:** 문턱은 아직 밖. U040은 C17에서 명시된 오늘의 진실과 이어진다.

원전 컷 대응(기존 19컷 번호 체계): S12-C17.

#### 내레이션 · S12-U039 [원문]

> And he would learn many new things.

**상대·감정:** 윤수와 관객 / 미래에 대한 기대

**연기:** learn many new things에서 학교 안의 미래에 대한 기대가 조금씩 넓어진다. 끝을 환하게 열되 급하지 않다.

**합성 지시(영문):** Open the horizon toward all the new things he will discover. Let new things expand in quiet excitement.

**강세·발음:** learn / new things. things의 /ŋz/ 끝과 learn 연결.

#### 내레이션 · S12-U040 [원문]

> But today, he chose to tell the truth.

**상대·감정:** 윤수와 관객 / 솔직함에 대한 확신

**연기:** But today에서 지금 이 아침의 선택으로 돌아온다. chose to tell the truth에는 오늘 겁났다고 솔직하게 말한 장면을 기억하는 따뜻한 확신을 준다.

**합성 지시(영문):** Return to this particular morning. Recognize the honesty he showed when he admitted being scared; put gentle conviction into chose and truth.

**강세·발음:** today / chose / truth. chose /z/와 truth /θ/ 보존.


### S12-C48 · 07:17–07:27 (10초 계획)

**구도:** 학교 문·지붕 위 먼 요정이 함께 보이는 WS

**화면·동작:** 피노키오가 학교 쪽으로 몸을 돌려 발을 내딛을 준비를 한다. 같은 책 든 가방을 유지한다. 지붕 위로 물러난 요정은 작은 모습으로 마지막 축복을 건넨다. 제페토와 귀뚜라미가 조용히 듣는다.

**음향·경계:** U041 뒤 U042. 먼 목소리는 위치감만, 발음을 흐릴 정도의 잔향 금지.

원전 컷 대응(기존 19컷 번호 체계): S12-C17, S12-C18.

#### 내레이션 · S12-U041 [원문]

> And he kept his promise.

**상대·감정:** 윤수와 관객 / 깊은 만족

**연기:** kept his promise에 11화에서 다시 학교를 선택하고 이곳까지 온 이야기가 닿는다. promise에는 안도와 인정이 따뜻하게 정착된다.

**합성 지시(영문):** Recognize the promise he has followed through on by coming to school. Put quiet satisfaction into kept and promise, not a triumphant announcement.

**강세·발음:** kept / promise. kept /pt/, promise /s/ 보존.

#### 파란 요정 · S12-U042 [원문]

> Every good choice is a new beginning.

**상대·감정:** 피노키오와 일행 / 먼 곳에서의 따뜻한 희망

**연기:** 멀어지며 마지막 축복을 건넨다. Every good choice에는 넓은 따뜻함, a new beginning에는 끝이 아니라 앞으로 열릴 하루라는 희망을 담는다. 먼 거리 효과를 낭독의 속삭임으로 대신하지 않는다.

**합성 지시(영문):** From farther away, offer one last tender blessing. Let every good choice carry affection and a new beginning open into hope; retain intelligible, close enough articulation.

**강세·발음:** good choice / new beginning. choice /s/, beginning /ŋ/ 유지. 공간 믹스는 별도.


### S12-C49 · 07:27–07:38 (11초 계획)

**구도:** 문 쪽 FOLLOW → 카메라 후퇴

**화면·동작:** 피노키오가 학교 쪽으로 실제 발걸음을 내딛고 문턱을 한 번 넘는다. 교사가 옆으로 비켜 공간을 내주고 피노키오는 문 안으로 들어간다. 제페토와 귀뚜라미는 문 밖 안전 위치에서 배웅한다. 모자·가방·책·신발을 유지하며 학교 안으로 이어지는 한 방향 이동.

**음향·경계:** U043은 입장 동작과 연결. 출입문 순간 닫힘이나 다른 화 시작 금지.

원전 컷 대응(기존 19컷 번호 체계): S12-C18, S12-C19.

#### 내레이션 · S12-U043 [원문]

> And so, Pinocchio's wonderful adventure continued.

**상대·감정:** 윤수와 관객 / 충만한 여운

**연기:** And so에서 긴 여행을 따뜻하게 돌아본다. wonderful adventure continued에는 더 배울 미래가 남았다는 즐거운 믿음이 넓게 퍼진다. 완결이지만 앞날의 여운.

**합성 지시(영문):** Bring the long journey gently to its closing image while leaving the child's future open. Let wonderful adventure continued feel warm, expansive, and hopeful.

**강세·발음:** wonderful adventure / continued. adventure와 continued의 마지막 음절·/d/ 보존.


### S12-C50 · 07:38–07:48 (10초 계획)

**구도:** 학교 외부에서 마을 전경으로 연속 PULL / DISSOLVE

**화면·동작:** 문 안으로 들어간 인간형 피노키오의 이동이 완료되고 제페토와 귀뚜라미가 배웅을 마친다. 학교와 같은 마을 배경이 차츰 넓게 보인다. 구름이 흐르고 햇빛이 부드럽게 비친다. 짧은 엔딩 표시는 U044 뒤, 이야기 완료 상태를 한 번만 기록한다.

**음향·경계:** U044는 학교 입장 완료 뒤. 기존 음악 모티프의 마지막 해결. 재참여·새 화 예고 없음.

원전 컷 대응(기존 19컷 번호 체계): S12-C19.

#### 내레이션 · S12-U044 [원문]

> The end.

**상대·감정:** 윤수와 관객 / 따뜻한 완결

**연기:** The end를 따뜻한 동화를 덮어 주는 목소리로 짧고 충만하게 말한다. end에 편안하게 내려앉으며 과장된 슬픔이나 다음 편 예고를 넣지 않는다.

**합성 지시(영문):** Close the story as gently as closing a beloved picture book. Give end a full, warm resolution, without sadness or a sequel announcement.

**강세·발음:** end. The와 end 자연 연결, end의 /d/ 보존.


## 화면 밖 따라 말하기 모델 10개

이 음성은 캐릭터 본편 입모양이나 본편 길이에 포함하지 않는다. 본편처럼 크게 연기하지 않고 윤수가 알아듣기 쉬운 따뜻한 연결 발음으로 말한다.

### S12-M001 · 제페토 (S12-P01)

> Look inside, please.

화면의 행동(열린 문 안쪽을 바라보기)과 연결되는 가까운 목소리. 세 단어를 자연스럽게 연결하고 핵심 동사를 또렷하게. 본편의 위기·환호 강도를 그대로 쓰지 않으며 따라 하기 편한 명료한 문장으로 말한다.

### S12-M002 · 제페토 (S12-P02)

> Hold your hat.

화면의 행동(바람에 움직이는 모자를 잡기)과 연결되는 가까운 목소리. 세 단어를 자연스럽게 연결하고 핵심 동사를 또렷하게. 본편의 위기·환호 강도를 그대로 쓰지 않으며 따라 하기 편한 명료한 문장으로 말한다.

### S12-M003 · 제페토 (I21)

> Help the cricket!

화면의 행동(막힌 친구를 안전하게 도와주기)과 연결되는 가까운 목소리. 세 단어를 자연스럽게 연결하고 핵심 동사를 또렷하게. 본편의 위기·환호 강도를 그대로 쓰지 않으며 따라 하기 편한 명료한 문장으로 말한다.

### S12-M004 · 피노키오 (S12-P03)

> Check on Cricket.

화면의 행동(구조 뒤 친구의 상태 살피기)과 연결되는 가까운 목소리. 세 단어를 자연스럽게 연결하고 핵심 동사를 또렷하게. 본편의 위기·환호 강도를 그대로 쓰지 않으며 따라 하기 편한 명료한 문장으로 말한다.

### S12-M005 · 제페토 (S12-P04)

> Stand beside Grandpa.

화면의 행동(할아버지 옆 안전한 곳에 서기)과 연결되는 가까운 목소리. 세 단어를 자연스럽게 연결하고 핵심 동사를 또렷하게. 본편의 위기·환호 강도를 그대로 쓰지 않으며 따라 하기 편한 명료한 문장으로 말한다.

### S12-M006 · 제페토 (S12-P05)

> Show your hands.

화면의 행동(사람이 된 손을 보여 주기)과 연결되는 가까운 목소리. 세 단어를 자연스럽게 연결하고 핵심 동사를 또렷하게. 본편의 위기·환호 강도를 그대로 쓰지 않으며 따라 하기 편한 명료한 문장으로 말한다.

### S12-M007 · 피노키오 (S12-P06)

> Bend your fingers.

화면의 행동(손가락을 굽혀 새로운 촉감 느끼기)과 연결되는 가까운 목소리. 세 단어를 자연스럽게 연결하고 핵심 동사를 또렷하게. 본편의 위기·환호 강도를 그대로 쓰지 않으며 따라 하기 편한 명료한 문장으로 말한다.

### S12-M008 · 제페토 (S12-P07)

> Take Grandpa's hand.

화면의 행동(할아버지의 손을 잡기)과 연결되는 가까운 목소리. 세 단어를 자연스럽게 연결하고 핵심 동사를 또렷하게. 본편의 위기·환호 강도를 그대로 쓰지 않으며 따라 하기 편한 명료한 문장으로 말한다.

### S12-M009 · 제페토 (S12-P08)

> Straighten your hat.

화면의 행동(기울어진 모자 바로 쓰기)과 연결되는 가까운 목소리. 세 단어를 자연스럽게 연결하고 핵심 동사를 또렷하게. 본편의 위기·환호 강도를 그대로 쓰지 않으며 따라 하기 편한 명료한 문장으로 말한다.

### S12-M010 · 피노키오 (S12-P09)

> Wave goodbye, please.

화면의 행동(요정에게 마지막 손인사하기)과 연결되는 가까운 목소리. 세 단어를 자연스럽게 연결하고 핵심 동사를 또렷하게. 본편의 위기·환호 강도를 그대로 쓰지 않으며 따라 하기 편한 명료한 문장으로 말한다.


## 마지막 완료 조건

학교 입장이 실제로 끝나고 U044 음성이 종료되며 마지막 카메라 이동까지 끝나면 스토리를 한 번만 완료한다. 10개 참여의 실제 종료 상태를 검증한다. V2 대본·제작 데이터의 수정 내용과 실제 미디어 제작 결과는 구분한다. 실제 음원 청취·원화 정합·영상렌더·앱 재생은 별도 검증 전까지 NOT_RUN이다.
