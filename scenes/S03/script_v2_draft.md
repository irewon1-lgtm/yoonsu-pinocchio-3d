# S03 상세 대본 — 수정본·문장별 음성 연기 V2.1

**본편 계획:** 598초 / 50컷 / 참여10회. 입력 대기·모델 예시는 별도 시간이다. 실제 영상·음성 길이 NOT_RUN.
**수정 범위:** 사용자 요청에 따른 검토 지적 수정과 모든 발화의 연기 지시. 1·2화 완료본과 승인 성우 참조는 유지한다.
**성우 기준:** [전체 캐릭터 음색·연기 기준](../../docs/series_v2/VOICE_PERFORMANCE_BIBLE_V2_1.md). 영어 대사만 읽고 연기 지시는 발화하지 않는다.
**기계용 제작표:** [voice_direction_plan.json](voice_direction_plan.json) · [voice_direction_sheet.csv](voice_direction_sheet.csv)

## 비트 시간표

|비트|내용|본편 구간|참여|
|---|---|---|---|
|B01|첫 등교 소식과 그림책|00:00–01:04|S03-P01|
|B02|친구에게 보여줄 장난감|01:04–02:10|S03-P02|
|B03|빨간 모자를 쓰고 싶은 피노키오|02:10–03:05|S03-P03|
|B04|서랍을 열어보자|03:05–04:01|S03-P04|
|B05|책 아래도 살펴보자|04:01–04:55|S03-P05|
|B06|의자 밑 빨간 모자 발견|04:55–05:47|I03|
|B07|거꾸로 든 모자|05:47–06:41|S03-P06|
|B08|제대로 모자를 써요|06:41–07:32|I04|
|B09|책가방을 열어 책을 넣어요|07:32–08:25|S03-P07|
|B10|끈을 묶고 할아버지와 약속|08:25–09:58|S03-P08|

## B01. 첫 등교 소식과 그림책

**목적:** 제페토가 '학교에 간다'는 추상적 이야기를 그림책의 실제 행동으로 보여줌. 영어를 몰라도 그림을 보면 사건을 따라갈 수 있음.

**연속성:** S02 마지막 아침 작업실, 피노키오는 제페토 옆에 서 있고 목각 상태. 원본 학교 책은 탁자 위에 있으며 가방은 아직 빈 상태. 의자 아래 빨간 모자 끝은 와이드 샷에서만 작게 보임.

### B01-C01 · 00:00–00:17 · NARRATIVE

**카메라:** WS 35mm 같은 작업실, 인물 눈높이

**자율 행동·연출:** 같은 아침에 제페토 옆에 선 피노키오의 시선을 먼저 받는다. 원본 학교 소식→되묻기→친구와 배움 설명 동안 피노키오가 눈을 크게 뜨고 손을 편다. 모자와 가방은 아직 손대지 않는다.

**시간 배정:** 발화 전 행동 1.5초 / 발화 뒤 행동 0.5초. 대사·쉼·지정 행동 계획 합계 16.13초. 실제 합성 길이는 별도 확인.

**[S03-U001 · ORIGINAL #1] 제페토:** “Today is your first day at school!”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 첫 등교 소식을 피노키오에게 직접 건넨다 / 감정: 따뜻한 기대  
**말하는 방식:** 손자를 보며 좋은 소식을 조용히 꺼낸다. first day에서 작은 미소가 생기고 school은 자랑스럽게 마친다.  
**속도·쉼 계획:** 96단어/분, 에너지 3/5, 앞 180ms / 뒤 420ms. 강조: first day · school. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Tell your grandson the good news directly; let first day brighten, then land school with warm pride, not an announcement.  
**피할 연기:** 학교 방송처럼 큰 소리로 선언하지 않기

**[S03-U002 · ORIGINAL #2] 피노키오:** “School?”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 처음 들은 장소 이름을 되묻는다 / 감정: 놀람에서 궁금함  
**말하는 방식:** 눈을 크게 뜨며 들은 단어를 짧게 되받는다. 끝을 조금 올리되 어른 흉내의 질문 억양은 피한다.  
**속도·쉼 계획:** 103단어/분, 에너지 3/5, 앞 100ms / 뒤 420ms. 강조: School. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Echo the unfamiliar word as a real child discovering it; one small upward turn, with no added gasp.  
**피할 연기:** 길게 늘인 유아식 비명

**[S03-U003 · ORIGINAL #3] 제페토:** “Yes! You'll meet new friends.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 새 친구가 있다는 사실로 학교를 가깝게 만든다 / 감정: 안심시키는 반가움  
**말하는 방식:** Yes는 아이의 눈을 받아 부드럽게 답하고 new friends에서 목소리가 조금 밝아진다.  
**속도·쉼 계획:** 96단어/분, 에너지 3/5, 앞 100ms / 뒤 320ms. 강조: new friends. Yes! 뒤 180ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Answer his look with a soft Yes; brighten new friends as a reassuring possibility, keeping the elderly voice.  
**피할 연기:** 선생님이 정답을 확인하는 채점 말투

**[S03-U004 · ORIGINAL #4] 제페토:** “And you'll learn many wonderful things.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 친구 외에도 배울 즐거움이 있음을 덧붙인다 / 감정: 차분한 설렘  
**말하는 방식:** 앞 문장의 숨을 이어 And로 시작한다. wonderful things를 넓게 펼치되 한 단어씩 끊지 않는다.  
**속도·쉼 계획:** 94단어/분, 에너지 3/5, 앞 120ms / 뒤 380ms. 강조: wonderful things. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Continue the same thought on And; open wonderful things with gentle wonder while staying conversational.  
**피할 연기:** 동화 제목을 낭독하듯 과장된 장중함

### B01-C02 · 00:17–00:36 · NARRATIVE

**카메라:** TWO 50mm → 그림책 INSERT

**자율 행동·연출:** 제페토가 탁자의 같은 학교책을 들어 눈높이에 편다. 피노키오의 친구 질문을 듣고 첫 그림을 가리키며 두 인물이 그림 속 함께 앉은 아이들을 눈과 손으로 따라간다. 삽화는 정지 그림이며 새 등장인물이 아니다.

**시간 배정:** 발화 전 행동 1.5초 / 발화 뒤 행동 0.5초. 대사·쉼·지정 행동 계획 합계 18.43초. 실제 합성 길이는 별도 확인.

**[S03-N001 · NEW] 피노키오:** “New friends? What do they look like?”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 새 친구의 모습을 상상하며 두 번 묻는다 / 감정: 호기심이 커짐  
**말하는 방식:** New friends를 되짚은 뒤 잠깐 생각하고 구체적인 얼굴을 떠올리며 뒤 질문을 던진다.  
**속도·쉼 계획:** 110단어/분, 에너지 3/5, 앞 140ms / 뒤 300ms. 강조: New friends · look like. New friends? 뒤 260ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Repeat New friends to yourself, pause to picture them, then genuinely ask what they look like.  
**피할 연기:** 두 질문 모두 같은 높이로 기계적으로 올리기

**[S03-N002 · NEW] 제페토:** “Look at this little picture book.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 말로 설명하는 대신 눈앞의 그림책으로 시선을 이끈다 / 감정: 다정한 안내  
**말하는 방식:** 아이에게 책을 가까이 내밀며 Look을 낮게 부른다. little picture book은 한 덩어리로 편하게 말한다.  
**속도·쉼 계획:** 92단어/분, 에너지 2/5, 앞 180ms / 뒤 260ms. 강조: picture book. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Invite his gaze down to the book in your hands; make little picture book one gentle phrase, not a vocabulary lesson.  
**피할 연기:** 관객 전체를 부르는 진행자 목소리

**[S03-N003 · NEW] 피노키오:** “There are children at a table!”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 그림 속 함께 앉은 아이들을 처음 알아본다 / 감정: 작은 발견의 기쁨  
**말하는 방식:** 그림에 손가락이 닿을 때 children이 밝아진다. table까지 시선이 따라가며 짧게 감탄한다.  
**속도·쉼 계획:** 110단어/분, 에너지 3/5, 앞 120ms / 뒤 320ms. 강조: children · table. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Notice the children as your finger finds them; let the sentence travel to the table in the picture with a fresh little lift.  
**피할 연기:** 처음부터 끝까지 같은 높은 환호

**[S03-N004 · NEW] 제페토:** “Yes. They are learning together.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 그림 속 행동을 학교의 배움과 연결한다 / 감정: 확인해 주는 온기  
**말하는 방식:** Yes를 작게 받고 learning together를 아이가 본 그림에 붙여 설명한다. 설명하느라 속도를 밀지 않는다.  
**속도·쉼 계획:** 92단어/분, 에너지 2/5, 앞 120ms / 뒤 320ms. 강조: learning together. Yes. 뒤 150ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Confirm what he has seen, then attach learning together to that picture; speak to him, not over him.  
**피할 연기:** 지식 전달용 무표정 낭독

### B01-C03 · 00:36–00:46 · PROMPT

**카메라:** 책 모서리와 얼굴이 함께 보이는 3/4 CU

**자율 행동·연출:** 제페토가 다음 페이지 모서리만 살짝 들고 다시 현재 그림이 보이는 각도에 둔다. 다음 그림을 묻는 말과 윤수 질문을 이어 말한다. 마지막 질문 종료가 이 컷 끝이다. 그 경계에서 본편 시계를 멈추며 예시 음성·입력 대기는 별도 시계로 처리한다. 다음 페이지는 아직 공개하지 않는다.

**시간 배정:** 발화 전 행동 1.2초 / 발화 뒤 행동 0초. 대사·쉼·지정 행동 계획 합계 9.48초. 실제 합성 길이는 별도 확인.

**[S03-N005 · NEW] 피노키오:** “Can I see the next picture?”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 다음 그림을 보고 싶다고 허락을 구한다 / 감정: 참기 어려운 기대  
**말하는 방식:** 다음 장 모서리를 바라보며 빠르게 마음이 앞서지만 next picture는 또렷이 남긴다.  
**속도·쉼 계획:** 108단어/분, 에너지 3/5, 앞 100ms / 뒤 250ms. 강조: next picture. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Ask eagerly while looking at the page corner; keep next picture clear without sounding impatient.  
**피할 연기:** 허락을 재촉하는 짜증

**[S03-N006 · NEW] 제페토:** “Yoonsu, help us turn the page!”

**음성 연기:** GEPPETTO_A → 윤수 / 의도: 윤수를 책장 넘기기에 초대한다 / 감정: 친근한 도움 요청  
**말하는 방식:** 카메라 쪽으로 시선을 옮겨 Yoonsu를 한 번 부른다. help us는 함께 하는 초대이고 명령은 아니다.  
**속도·쉼 계획:** 92단어/분, 에너지 3/5, 앞 180ms / 뒤 320ms. 강조: Yoonsu · turn the page. Yoonsu, 뒤 180ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Turn toward Yoonsu and invite help with the page; connect help us naturally, giving the child room to join.  
**피할 연기:** 정답을 당장 말하라는 시험 말투

**윤수 참여 1/10 · S03-P01 · 본편 밖 입력 대기**

- 질문 종료 시점: 46초. 본편 시계를 멈춘다.
- 첫 모델 예시: **“Turn the page!”** — 제페토의 같은 고정 목소리.
- 모델 예시를 한 번 들려준 뒤 마이크를 켠다. 정확한 단어·발음 채점은 하지 않는다.
- 보호자 터치는 예시를 생략하고 반응으로 진행할 수 있다. 무응답5초 뒤 다시 듣기/터치를 제시한다.
- 시범: 제페토가 다음 페이지 모서리를 살짝 들어 넘기는 방향만 보여 준다. 새 그림을 공개하거나 한 장을 끝까지 넘기지 않는다.
- 대기 상태: 책은 열린 상태, 넘길 페이지 모서리만 살짝 들림; 완전히 넘김 금지.
- 입력 뒤 한 번 실행: 피노키오 페이지 넘김→그림 변화→피노키오가 그림과 제페토를 번갈아 보며 기뻐함.
- 첫 재개: S03-N007 “Oh! Look at the paint and paper!”

**예시 음성 연기:**

**음성 연기:** GEPPETTO_A → 윤수 (본편 밖 예시) / 의도: 윤수가 책장 넘기기 표현을 한 번 편하게 따라 듣게 한다 / 감정: 부드러운 초대  
**말하는 방식:** Turn the page를 세 낱말이 아닌 한 동작 말로 연결한다. page를 조금 길게 남기되 글자별 발음은 하지 않는다.  
**속도·쉼 계획:** 82단어/분, 에너지 2/5, 앞 160ms / 뒤 450ms. 강조: Turn · page. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Model Turn the page as one easy invitation matching the lifted page corner; gently lengthen page, never spell or drill the words.  
**피할 연기:** 낱말마다 똑같이 끊는 학습 로봇 억양

### B01-C04 · 00:46–00:55 · REACT

**카메라:** 책→피노키오 얼굴 CU, 손 접촉 유지

**자율 행동·연출:** 입력 뒤 선행 동작 4초: 피노키오가 한 장을 끝까지 넘기고 제페토가 책 아래를 받친다. 색칠 그림이 드러나고 시선이 멈춘 뒤 첫 재개 대사를 말한다. 대사 중 paint와 paper를 차례로 손가락과 눈으로 짚는다.

**시간 배정:** 발화 전 행동 4.0초 / 발화 뒤 행동 0.5초. 대사·쉼·지정 행동 계획 합계 8.99초. 실제 합성 길이는 별도 확인.

**[S03-N007 · NEW] 피노키오:** “Oh! Look at the paint and paper!”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 넘긴 페이지의 새 재료를 보고 기뻐한다 / 감정: 신선한 놀람  
**말하는 방식:** 페이지가 멈춘 뒤 Oh를 가볍게 띄우고 paint와 paper를 눈으로 차례로 짚는다.  
**속도·쉼 계획:** 111단어/분, 에너지 4/5, 앞 150ms / 뒤 380ms. 강조: paint · paper. Oh! 뒤 180ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** React only after the page has turned; a light Oh, then discover paint and paper as your eyes move between them.  
**피할 연기:** 페이지가 바뀌기 전부터 미리 아는 감탄

### B01-C05 · 00:55–01:04 · NARRATIVE

**카메라:** MS 50mm, 책에서 제페토 얼굴로

**자율 행동·연출:** 제페토가 그림과 학교를 연결해 말하는 동안 피노키오는 이해하며 고개를 끄덕인다. 마지막 발화 뒤 두 사람이 책을 닫아 탁자 원래 자리에 내려놓고 손을 뗀다. 모자 의자 아래·빈 가방 탁자 상태를 유지한다.

**시간 배정:** 발화 전 행동 0.5초 / 발화 뒤 행동 2.5초. 대사·쉼·지정 행동 계획 합계 8.03초. 실제 합성 길이는 별도 확인.

**[S03-N008 · NEW] 제페토:** “That's something you can learn at school.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 새 그림을 등교의 기대와 연결해 마무리한다 / 감정: 조용한 격려  
**말하는 방식:** something은 과장하지 않고 learn at school에 따뜻한 확신을 준다. 열린 책 그림과 피노키오를 보며 말끝을 편안히 내린다. 책을 닫는 손동작은 발화가 끝난 뒤에만 한다.  
**속도·쉼 계획:** 94단어/분, 에너지 2/5, 앞 160ms / 뒤 400ms. 강조: learn at school. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Connect the open picture to what he can learn at school, looking between the page and the child. Finish with quiet confidence; the book stays open throughout this line and is closed only after it ends.  
**피할 연기:** 모든 답을 대신 알려주는 설교조

## B02. 친구에게 보여줄 장난감

**목적:** 학교 친구를 상상하며 인형극이 아닌 실제 모방놀이로 인사·나누기 관계를 익힘; S02에서 윤수에게 인사했던 경험을 연결.

**연속성:** S01/S02 장난감 선반의 기존 나무 블록·곰 인형 소품을 활용. 곰은 생명 없는 장난감, 새 캐릭터 보이스/의식 없음. 학교 책은 탁자.

### B02-C01 · 01:04–01:18 · NARRATIVE

**카메라:** WS 40mm 선반과 두 인물

**자율 행동·연출:** 피노키오가 선반 쪽으로 두 걸음 접근한다. 친구가 하는 일을 묻고 제페토의 놀이·도움 답을 들으며 블록을 발견한다. 만들고 싶다는 말에 시선과 손이 블록으로 간다.

**시간 배정:** 발화 전 행동 1.5초 / 발화 뒤 행동 0.5초. 대사·쉼·지정 행동 계획 합계 13.55초. 실제 합성 길이는 별도 확인.

**[S03-N009 · NEW] 피노키오:** “Grandpa, what can friends do?”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 친구와 무엇을 하는지 제페토에게 묻는다 / 감정: 새 관계에 대한 궁금함  
**말하는 방식:** Grandpa를 가까이 부르고 friends에서 이미 만난 윤수를 떠올린다. 질문 끝에 진짜 답을 기다리는 여백을 둔다.  
**속도·쉼 계획:** 104단어/분, 에너지 3/5, 앞 180ms / 뒤 420ms. 강조: friends · do. Grandpa, 뒤 160ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Ask Grandpa what friendship is for, carrying the memory of meeting Yoonsu; leave the question open rather than reciting it.  
**피할 연기:** 앞 장면을 잊은 낯선 사람처럼 묻기

**[S03-N010 · NEW] 제페토:** “They can play and help each other.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 친구 사이의 놀이와 도움을 알려 준다 / 감정: 편안한 확신  
**말하는 방식:** play와 help를 같은 크기로 부드럽게 이어 준다. each other에서는 아이와 눈을 맞춰 상호성을 느끼게 한다.  
**속도·쉼 계획:** 95단어/분, 에너지 2/5, 앞 140ms / 뒤 320ms. 강조: play · help each other. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Offer play and help as two ordinary pleasures; warm each other through eye contact instead of stressing a moral.  
**피할 연기:** 훈계 목록을 읽는 리듬

**[S03-N011 · NEW] 피노키오:** “I want to build something.”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 직접 만들기를 시작하고 싶다고 나선다 / 감정: 생겨난 의욕  
**말하는 방식:** 블록 선반을 발견하며 I want에 작은 추진력을 싣는다. something은 아직 정하지 않은 상상을 남긴다.  
**속도·쉼 계획:** 112단어/분, 에너지 3/5, 앞 100ms / 뒤 250ms. 강조: build. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Let spotting the blocks spark I want; leave something open as an idea he is just forming.  
**피할 연기:** 이미 외운 활동 안내문처럼 말하기

### B02-C02 · 01:18–01:35 · NARRATIVE

**카메라:** 손/블록 MS, 놓일 면을 함께 보여 줌

**자율 행동·연출:** 제페토가 세 블록을 작업면에 가져온다. One here/One more here 동안 피노키오는 놓을 자리만 손가락으로 짚는다. 큰 블록을 아래에 놓으라는 말이 끝난 뒤 큰 블록과 중간 블록을 순서대로 실제로 놓는다. 이미 놓은 뒤 뒤늦게 위치를 지시하지 않는다.

**시간 배정:** 발화 전 행동 1.0초 / 발화 뒤 행동 2.5초. 대사·쉼·지정 행동 계획 합계 16.52초. 실제 합성 길이는 별도 확인.

**[S03-N012 · NEW] 제페토:** “Here are three little wooden blocks.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 손에 가져온 블록 세 개를 소개한다 / 감정: 도와주는 즐거움  
**말하는 방식:** three를 또렷하게 하되 숫자 시험처럼 따로 외치지 않는다. wooden blocks는 손의 무게감을 느끼며 낮게 마친다.  
**속도·쉼 계획:** 94단어/분, 에너지 2/5, 앞 160ms / 뒤 300ms. 강조: three · wooden blocks. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Present the three blocks you have brought; make three clear inside the sentence, then settle wooden blocks with tactile warmth.  
**피할 연기:** 물건 이름마다 과장해 끊기

**[S03-N013 · NEW] 피노키오:** “One here. One more here.”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 블록을 놓을 자리를 먼저 손가락으로 정한다 / 감정: 생각하며 계획함  
**말하는 방식:** 첫 One here는 첫 자리를 짚고 다음 문장 전 짧게 두 번째 자리를 찾는다. 실제 쌓기 완료의 말투는 쓰지 않는다.  
**속도·쉼 계획:** 104단어/분, 에너지 2/5, 앞 120ms / 뒤 300ms. 강조: One here · One more. One here. 뒤 280ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Point out the first place, then find a second place after a small thinking beat; this is planning, not claiming the tower is built.  
**피할 연기:** 완성된 탑을 세듯 확정적으로 재촉하기

**[S03-N014 · NEW] 제페토:** “Put the big one at the bottom.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 큰 블록을 아래에 두어 안정시키도록 안내한다 / 감정: 차분한 실용적 도움  
**말하는 방식:** big one에서 큰 블록을 보여 주고 bottom을 낮은 손짓과 붙여 말한다. 꾸짖는 힘을 빼고 권한다.  
**속도·쉼 계획:** 91단어/분, 에너지 2/5, 앞 150ms / 뒤 380ms. 강조: big one · bottom. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Guide him toward the large base block; place a gentle weight on bottom as your hand points down, without correcting harshly.  
**피할 연기:** 잘못 쌓았다고 나무라는 명령

### B02-C03 · 01:35–01:46 · PROMPT

**카메라:** 마지막 블록과 지지면 CU

**자율 행동·연출:** 제페토가 빈 윗면에 내려놓는 궤적을 손가락으로 짧게 시범 보인다. 피노키오는 마지막 블록을 받쳐 들고 작은 흔들림을 조절하며 대사한다. 윤수 질문이 끝날 때 마지막 블록은 지지면 5cm 위에 있다. 그 지점부터 별도 예시·입력 대기이며 본편 길이에 정지시간을 더하지 않는다.

**시간 배정:** 발화 전 행동 1.2초 / 발화 뒤 행동 0초. 대사·쉼·지정 행동 계획 합계 10.58초. 실제 합성 길이는 별도 확인.

**[S03-N015 · NEW] 피노키오:** “This tall block is wobbly.”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 손에 든 마지막 블록의 흔들림을 알아차린다 / 감정: 조심스러운 집중  
**말하는 방식:** This tall block은 눈으로 따라가고 wobbly에서 살짝 불안정한 숨결만 준다. 목소리 자체를 우스꽝스럽게 떨지 않는다.  
**속도·쉼 계획:** 101단어/분, 에너지 2/5, 앞 160ms / 뒤 300ms. 강조: wobbly. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Notice the last block wobbling in your hands; let wobbly carry a small concern without physically wobbling the voice.  
**피할 연기:** 공포에 질린 과도한 떨림

**[S03-N016 · NEW] 제페토:** “Yoonsu, shall we help with the last block?”

**음성 연기:** GEPPETTO_A → 윤수 / 의도: 마지막 한 조각을 윤수와 함께 마치려 한다 / 감정: 안전한 참여 초대  
**말하는 방식:** Yoonsu를 부드럽게 부른 뒤 shall we를 함께 해보자는 제안으로 묶는다. last block은 눈앞의 물건을 가리킨다.  
**속도·쉼 계획:** 92단어/분, 에너지 2/5, 앞 200ms / 뒤 350ms. 강조: Yoonsu · last block. Yoonsu, 뒤 180ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Invite Yoonsu into the last small step; make shall we collaborative and last block concrete, not a challenge to pass.  
**피할 연기:** 성공 여부를 심사하는 질문

**윤수 참여 2/10 · S03-P02 · 본편 밖 입력 대기**

- 질문 종료 시점: 106초. 본편 시계를 멈춘다.
- 첫 모델 예시: **“Put it here!”** — 제페토의 같은 고정 목소리.
- 모델 예시를 한 번 들려준 뒤 마이크를 켠다. 정확한 단어·발음 채점은 하지 않는다.
- 보호자 터치는 예시를 생략하고 반응으로 진행할 수 있다. 무응답5초 뒤 다시 듣기/터치를 제시한다.
- 시범: 제페토가 블록을 위에 놓는 궤적을 손가락으로 보여주며 피노키오가 블록을 들고 대기.
- 대기 상태: 마지막 블록은 타워 위에서 떨어지지 않고 지지된 상태, 완성 전.
- 입력 뒤 한 번 실행: 마지막 블록 놓기→쌓기 성공→손 놓기→피노키오 기뻐함.
- 첫 재개: S03-N017 “It stands! I can show my new friends.”

**예시 음성 연기:**

**음성 연기:** GEPPETTO_A → 윤수 (본편 밖 예시) / 의도: 마지막 블록을 놓는 위치와 짧은 표현을 연결한다 / 감정: 차분한 자신감  
**말하는 방식:** Put it을 부드럽게 붙이고 here에서 보이는 빈자리를 가리키는 색을 낸다. 명령보다 함께 놓자는 권유다.  
**속도·쉼 계획:** 80단어/분, 에너지 2/5, 앞 160ms / 뒤 450ms. 강조: here. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Connect Put it smoothly, then give here the clarity of pointing to the open spot; invite participation without commanding it.  
**피할 연기:** 블록을 빨리 놓으라고 재촉하기

### B02-C04 · 01:46–01:59 · REACT

**카메라:** SIDE MS, 타워와 손이 한 프레임

**자율 행동·연출:** 입력 뒤 선행 동작 4초: 마지막 블록을 내려놓고 작은 흔들림이 가라앉은 뒤 손을 뗀다. 그 후 It stands!로 재개한다. 새 친구에게 보여 주고 싶은 눈빛과 제페토의 담백한 칭찬을 실제 눈맞춤으로 잇는다.

**시간 배정:** 발화 전 행동 4.0초 / 발화 뒤 행동 0.5초. 대사·쉼·지정 행동 계획 합계 12.54초. 실제 합성 길이는 별도 확인.

**[S03-N017 · NEW] 피노키오:** “It stands! I can show my new friends.”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 탑이 선 것을 보고 새 친구에게 보여 주고 싶어진다 / 감정: 성취에서 기대감으로  
**말하는 방식:** It stands는 손을 뗀 뒤 짧게 밝아진다. 다음 문장은 새 친구를 떠올리며 더 부드러운 설렘으로 잇는다.  
**속도·쉼 계획:** 113단어/분, 에너지 4/5, 앞 150ms / 뒤 400ms. 강조: It stands · new friends. It stands! 뒤 220ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Discover that the tower stands after letting go; then soften into imagining showing new friends, instead of sustaining one shout.  
**피할 연기:** 탑 안정 전에 성취를 선행 발화하기

**[S03-N018 · NEW] 제페토:** “Your tower is strong.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 완성된 탑을 인정해 아이를 안심시킨다 / 감정: 담백한 칭찬  
**말하는 방식:** Your tower를 아이의 성취로 돌려주고 strong은 짧게 단단히 놓는다. 과장된 박수 소리는 넣지 않는다.  
**속도·쉼 계획:** 94단어/분, 에너지 2/5, 앞 150ms / 뒤 320ms. 강조: Your tower · strong. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Give ownership back to him on your tower, then land strong simply and firmly, with no added cheering.  
**피할 연기:** 상장을 읽듯 거창한 칭찬

### B02-C05 · 01:59–02:10 · NARRATIVE

**카메라:** TWO 50mm 선반까지 짧은 동행

**자율 행동·연출:** 친구에게 친절하겠다는 다짐을 말하며 피노키오가 두 손으로 받친 작은 타워를 선반으로 옮긴다. 제페토는 받침 손만 보조한다. 칭찬 뒤 타워를 안정된 면에 내려놓고 두 손이 떨어지는 동작을 끝낸다. 책·가방·모자는 움직이지 않는다.

**시간 배정:** 발화 전 행동 0.5초 / 발화 뒤 행동 2.0초. 대사·쉼·지정 행동 계획 합계 10.37초. 실제 합성 길이는 별도 확인.

**[S03-N019 · NEW] 피노키오:** “I will be kind to my friends.”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 친구에게 잘해 주겠다는 스스로의 마음을 말한다 / 감정: 작고 진지한 다짐  
**말하는 방식:** 조금 전 들뜸을 낮추고 kind를 진심으로 말한다. 긴 선언 대신 할아버지에게 털어놓듯 끝낸다.  
**속도·쉼 계획:** 103단어/분, 에너지 2/5, 앞 180ms / 뒤 420ms. 강조: kind · my friends. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Let the excitement settle into a small sincere promise; give kind honest weight, speaking to Grandpa rather than making a speech.  
**피할 연기:** 성인이 교훈을 대신 읊는 말투

**[S03-N020 · NEW] 제페토:** “That's a wonderful start.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 친구를 생각한 마음을 짧게 받아 준다 / 감정: 애정 어린 인정  
**말하는 방식:** That에 아이의 말을 받아 주는 온기를 싣고 start에서 앞으로 이어질 기대를 남긴다. 문장을 크게 닫지 않는다.  
**속도·쉼 계획:** 92단어/분, 에너지 2/5, 앞 160ms / 뒤 420ms. 강조: wonderful start. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Receive his intention warmly on That; leave start gently open toward what comes next, not as a formal conclusion.  
**피할 연기:** 장면 종료를 선언하는 진행자 하강조

## B03. 빨간 모자를 쓰고 싶은 피노키오

**목적:** 학교에 쓸 모자를 떠올리고 머리의 위치를 손으로 직접 확인한 뒤 찾기를 시작한다. 참여 전 맨머리라는 결과를 말로 먼저 알려 주지 않으며, 참여 뒤에도 이미 아는 사실을 큰 발견처럼 과장하지 않는다.

**연속성:** 학교 책과 가방은 탁자, 모자는 의자 아래(끝만 살짝 보임). 피노키오가 스스로 머리를 만질 때 모자 소품을 생성하지 않는다.

### B03-C01 · 02:10–02:26 · NARRATIVE

**카메라:** 투샷 MS, 학교 기대에서 모자 기억으로

**자율 행동·연출:** 학교가 신날 것이라는 원본 반응부터 새 모자 허락까지 같은 대화로 이어간다. 허락 뒤 제페토가 기억을 더듬으며 주변을 살피되 의자 아래를 발견하지 않는다.

**시간 배정:** 발화 전 행동 0.8초 / 발화 뒤 행동 0.5초. 대사·쉼·지정 행동 계획 합계 15.08초. 실제 합성 길이는 별도 확인.

**[S03-U005 · ORIGINAL #5] 피노키오:** “That sounds exciting!”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 학교에서 함께 할 활동을 떠올리며 원래의 등교 기대를 받는다 / 감정: 가벼운 설렘  
**말하는 방식:** 블록 놀이에서 학교 생각으로 시선을 돌리며 exciting을 환하게 말한다. 새 사건을 발표하듯 분리하지 않는다.  
**속도·쉼 계획:** 110단어/분, 에너지 3/5, 앞 140ms / 뒤 320ms. 강조: exciting. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Carry the pleasure of the little tower back into the idea of school; brighten exciting without making a separate announcement.  
**피할 연기:** 블록만 칭찬하는 대사처럼 닫기

**[S03-U006 · ORIGINAL #6] 피노키오:** “Can I wear my new hat?”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 학교에 새 모자를 쓰고 갈 수 있는지 묻는다 / 감정: 자기 물건에 대한 기대  
**말하는 방식:** new hat에서 머리 쪽을 가볍게 가리키며 허락을 구한다. 아직 모자를 찾았다는 기쁨은 싣지 않는다.  
**속도·쉼 계획:** 108단어/분, 에너지 3/5, 앞 150ms / 뒤 350ms. 강조: new hat. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Ask permission with a glance toward your head; let new hat carry anticipation, not the joy of already finding it.  
**피할 연기:** 이미 모자를 손에 든 듯한 확신

**[S03-U007 · ORIGINAL #7] 제페토:** “Of course.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 모자를 써도 좋다고 흔쾌히 허락한다 / 감정: 편안한 수락  
**말하는 방식:** Of course는 한 호흡으로 낮고 다정하게 답한다. 아이에게 당연한 즐거움을 허락하는 작은 미소만 준다.  
**속도·쉼 계획:** 93단어/분, 에너지 2/5, 앞 100ms / 뒤 300ms. 강조: Of course. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Answer in one easy elderly breath, with a small smile that makes the permission feel natural.  
**피할 연기:** 정답을 알려 주는 단호한 단정

**[S03-U008 · ORIGINAL #8] 제페토:** “Now, where did I put that red hat?”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 허락한 뒤 모자를 둔 위치를 기억해 보려 한다 / 감정: 생각하다 생긴 가벼운 당혹감  
**말하는 방식:** Now 뒤 잠깐 눈길을 돌리고 where에서 기억을 더듬는다. red hat은 불안이 아니라 물건을 떠올리는 말이다.  
**속도·쉼 계획:** 91단어/분, 에너지 2/5, 앞 180ms / 뒤 450ms. 강조: where · red hat. Now, 뒤 260ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Turn from permission to searching your memory; pause after Now and let where sound genuinely thoughtful, never distressed.  
**피할 연기:** 분실 사고처럼 심각하게 걱정하기

### B03-C02 · 02:26–02:40 · NARRATIVE

**카메라:** 얼굴/머리 CU, 제페토 손짓 포함

**자율 행동·연출:** 피노키오가 빨간색을 좋아한다고 말한다. 제페토는 모자가 놓일 머리 위치를 물으며 자신의 머리를 가리킨다. 피노키오는 정수리 위를 가리켜 확인받는다. 맨머리라는 정답이나 새로운 발견의 놀람을 미리 말하지 않는다.

**시간 배정:** 발화 전 행동 0.8초 / 발화 뒤 행동 0.5초. 대사·쉼·지정 행동 계획 합계 13.54초. 실제 합성 길이는 별도 확인.

**[S03-N021 · NEW] 피노키오:** “A red hat! I love red.”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 모자의 색을 생각하며 자신의 취향을 말한다 / 감정: 밝은 애착  
**말하는 방식:** 첫 red hat은 떠올리는 즐거움, I love red는 할아버지에게 전하는 자기 취향이다. 두 문장의 크기를 다르게 한다.  
**속도·쉼 계획:** 111단어/분, 에너지 3/5, 앞 130ms / 뒤 300ms. 강조: red hat · love red. A red hat! 뒤 180ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Enjoy imagining the red hat, then tell Grandpa your own preference in a smaller, personal way.  
**피할 연기:** 같은 감탄을 두 번 같은 세기로 외치기

**[S03-N022 · NEW] 제페토:** “Show me where your hat will go.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 모자가 놓일 머리 위치를 몸으로 확인하게 한다 / 감정: 놀이처럼 이끄는 관심  
**말하는 방식:** where your hat will go를 머리 쪽 손짓과 연결한다. 모자가 없다는 결과를 미리 알려 주지 말고 위치 확인을 청한다.  
**속도·쉼 계획:** 93단어/분, 에너지 2/5, 앞 160ms / 뒤 300ms. 강조: where · hat will go. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Invite him to show the place the hat belongs; guide toward the head without announcing the result of the coming touch.  
**피할 연기:** 맨머리라는 답을 먼저 읽어 주는 말투

**[S03-N023 · NEW] 피노키오:** “Right up here on top?”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 자기 정수리 위치를 가리키며 확인받는다 / 감정: 생각하며 따라 하는 호기심  
**말하는 방식:** Right up here에서 손을 올리고 on top을 작은 질문으로 남긴다. 빈 머리를 새로 발견한 놀람은 아직 없다.  
**속도·쉼 계획:** 102단어/분, 에너지 2/5, 앞 140ms / 뒤 330ms. 강조: up here · on top. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Raise your hand while checking the top of your head; ask on top lightly, without pretending to discover an absent hat yet.  
**피할 연기:** 모자가 없음을 이미 발견한 감탄

### B03-C03 · 02:40–02:49 · PROMPT

**카메라:** 3/4 MS, 정수리 위 손과 눈맞춤

**자율 행동·연출:** 제페토가 자신의 머리에 가볍게 손을 대는 시범을 보인 뒤 Touch your head and see를 말한다. 피노키오는 손을 정수리 5cm 위로 올려 윤수에게 함께 확인해 달라고 묻는다. 질문 종료 경계에서 본편을 멈추고 별도 예시 음성 뒤 입력을 받는다.

**시간 배정:** 발화 전 행동 0.8초 / 발화 뒤 행동 0초. 대사·쉼·지정 행동 계획 합계 8.76초. 실제 합성 길이는 별도 확인.

**[S03-N024 · NEW] 제페토:** “Touch your head and see.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 가리키기에서 실제 촉감 확인으로 안내한다 / 감정: 느긋한 도움  
**말하는 방식:** Touch를 무겁게 명령하지 말고 손짓과 함께 부드럽게 제시한다. and see는 직접 확인해 보자는 여지를 준다.  
**속도·쉼 계획:** 90단어/분, 에너지 2/5, 앞 150ms / 뒤 320ms. 강조: Touch your head. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Offer touch as a gentle next action; let and see invite his own check instead of announcing a correct answer.  
**피할 연기:** 신체 동작을 강요하는 교관 어조

**[S03-N025 · NEW] 피노키오:** “Yoonsu, can you help me check?”

**음성 연기:** PINOCCHIO_A → 윤수 / 의도: 윤수에게 함께 머리 위치를 확인해 달라고 부탁한다 / 감정: 가까운 협력 요청  
**말하는 방식:** check를 확신 없는 시험이 아닌 함께 확인하는 말로 쓴다. 이름을 부른 뒤 눈맞춤을 한 번 유지한다.  
**속도·쉼 계획:** 104단어/분, 에너지 2/5, 앞 180ms / 뒤 350ms. 강조: Yoonsu · check. Yoonsu, 뒤 170ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Ask Yoonsu to check with you, using a direct friendly look; make check cooperative rather than anxious.  
**피할 연기:** 정답을 몰라 당황한 연기

**윤수 참여 3/10 · S03-P03 · 본편 밖 입력 대기**

- 질문 종료 시점: 169초. 본편 시계를 멈춘다.
- 첫 모델 예시: **“Touch your head!”** — 피노키오의 같은 고정 목소리.
- 모델 예시를 한 번 들려준 뒤 마이크를 켠다. 정확한 단어·발음 채점은 하지 않는다.
- 보호자 터치는 예시를 생략하고 반응으로 진행할 수 있다. 무응답5초 뒤 다시 듣기/터치를 제시한다.
- 시범: 제페토가 자기 머리를 톡톡 가리키고 피노키오도 따라 하려는 동작 시작.
- 대기 상태: 피노키오 손이 정수리 위 약 5cm 지점에 멈춘 상태.
- 입력 뒤 한 번 실행: 정수리를 한 번 살짝 만짐→빈자리를 직접 확인→손을 펴 보임→제페토와 수색 방향으로 시선 이동. 과장된 재발견 놀람은 없음.
- 첫 재개: S03-N026 “Nothing on my head!”

**예시 음성 연기:**

**음성 연기:** PINOCCHIO_A → 윤수 (본편 밖 예시) / 의도: 머리 위치를 만지는 몸동작에 영어를 붙여 준다 / 감정: 가까운 장난기  
**말하는 방식:** Touch your는 가볍게 이어 주고 head에 작은 밝음을 둔다. 어린아이 목소리를 더 높은 아기 소리로 바꾸지 않는다.  
**속도·쉼 계획:** 84단어/분, 에너지 2/5, 앞 140ms / 뒤 450ms. 강조: Touch · head. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Offer the head-touch phrase in the same natural young-boy voice; connect Touch your and brighten head slightly, without baby talk.  
**피할 연기:** 승인된 소년 목소리를 아기 소리로 높이기

### B03-C04 · 02:49–02:56 · REACT

**카메라:** 피노키오 얼굴/손 CU

**자율 행동·연출:** 입력 뒤 선행 동작 2.8초: 피노키오가 정수리를 한 번 살짝 만지고 손을 펴 빈자리를 확인한다. 갑작스러운 놀람 대신 확인한 사실로 Nothing on my head!를 말한다. 손과 머리 접촉을 실제로 보여 준다.

**시간 배정:** 발화 전 행동 2.8초 / 발화 뒤 행동 0.5초. 대사·쉼·지정 행동 계획 합계 6.11초. 실제 합성 길이는 별도 확인.

**[S03-N026 · NEW] 피노키오:** “Nothing on my head!”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 직접 만져 본 빈자리를 보고한다 / 감정: 확인 뒤 찾을 준비  
**말하는 방식:** 손으로 만져 확인한 사실을 담백하게 말한다. 놀라 소리치지 말고 head에서 다음 찾기로 마음이 넘어가게 한다.  
**속도·쉼 계획:** 103단어/분, 에너지 2/5, 앞 160ms / 뒤 320ms. 강조: Nothing · head. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Report the empty place you have just felt, simply and without shock; let the ending turn your attention toward searching.  
**피할 연기:** 이미 알던 맨머리를 과장해서 다시 발견하기

### B03-C05 · 02:56–03:05 · NARRATIVE

**카메라:** WIDE 35mm 작업대 방향

**자율 행동·연출:** 함께 모자를 찾자는 말에 피노키오가 고개를 끄덕이고 스스로 서랍 쪽으로 몸을 돌린다. 조심히 보겠다는 말 뒤 두 사람이 수색할 작업대까지 가까이 이동한다. 관객에게만 의자 밑 빨간 끝이 보이며 인물은 아직 모른다.

**시간 배정:** 발화 전 행동 0.5초 / 발화 뒤 행동 1.8초. 대사·쉼·지정 행동 계획 합계 8.72초. 실제 합성 길이는 별도 확인.

**[S03-N027 · NEW] 제페토:** “Let's look for your hat together.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 확인을 마치고 함께 찾기로 행동을 연결한다 / 감정: 차분한 동행  
**말하는 방식:** together에 둘이 같은 편이라는 온기를 둔다. 어디에 있는지 안다는 암시는 주지 않는다.  
**속도·쉼 계획:** 94단어/분, 에너지 2/5, 앞 150ms / 뒤 330ms. 강조: look · together. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Move the moment onward into a shared search; warm together while keeping the location genuinely unknown.  
**피할 연기:** 의자 아래를 이미 아는 듯한 유도

**[S03-N028 · NEW] 피노키오:** “I'll look carefully!”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 서랍부터 스스로 살펴보겠다고 나선다 / 감정: 기꺼이 집중함  
**말하는 방식:** carefully는 크게 강조하기보다 눈을 좁혀 살피는 집중으로 또렷하게 낸다. 짧고 앞으로 움직이는 말이다.  
**속도·쉼 계획:** 108단어/분, 에너지 3/5, 앞 120ms / 뒤 320ms. 강조: carefully. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Volunteer to look with fresh focus; make carefully precise through attention, then move into the search.  
**피할 연기:** 성취가 끝난 듯 승리하는 억양

## B04. 서랍을 열어보자

**목적:** 수색의 첫 번째 실패. 서랍 레일과 손 접촉, 제페토·피노키오가 스스로 관찰하는 연기를 구현.

**연속성:** 서랍은 작업대 왼쪽, 단색 회전문이 아닌 실제 슬라이드. 모자는 절대 서랍에서 발견하지 않음. 기존 S03 '서랍을 열어본다' 보존.

### B04-C01 · 03:05–03:16 · NARRATIVE

**카메라:** 작업대 WS, 서랍과 인물 손높이 확인

**자율 행동·연출:** 제페토가 서랍 앞에 서고 피노키오가 옆의 안전한 자리로 이동한다. 서랍에 물건을 넣었던 기억과 모자가 있을지 모른다는 추측을 나눈다. 손잡이를 만지기 전에 이동을 끝낸다.

**시간 배정:** 발화 전 행동 1.5초 / 발화 뒤 행동 0.5초. 대사·쉼·지정 행동 계획 합계 10.33초. 실제 합성 길이는 별도 확인.

**[S03-N029 · NEW] 제페토:** “I remember putting things in this drawer.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 서랍을 살필 구체적인 이유를 떠올린다 / 감정: 기억을 더듬는 관심  
**말하는 방식:** remember에서 잠깐 생각하고 this drawer를 눈앞의 서랍에 붙인다. 모자를 넣었다고 확신하는 말투는 피한다.  
**속도·쉼 계획:** 91단어/분, 에너지 2/5, 앞 180ms / 뒤 360ms. 강조: remember · this drawer. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Search your memory on remember, then ground this drawer in the object ahead; you recall storing things, not specifically the hat.  
**피할 연기:** 모자가 서랍에 있다고 확정하기

**[S03-N030 · NEW] 피노키오:** “Maybe the hat is inside!”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 그 기억을 듣고 가능한 위치를 제안한다 / 감정: 작은 기대  
**말하는 방식:** Maybe에 가능성을 남기고 inside를 서랍 안쪽으로 향하는 눈빛과 함께 올린다. 정답을 찾은 환호는 아니다.  
**속도·쉼 계획:** 109단어/분, 에너지 3/5, 앞 120ms / 뒤 300ms. 강조: Maybe · inside. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Offer a hopeful possibility on Maybe, glancing toward the drawer; keep inside curious rather than triumphant.  
**피할 연기:** 이미 모자를 보았다는 확신

### B04-C02 · 03:16–03:30 · NARRATIVE

**카메라:** 서랍 손잡이 CU, 레일 옆면도 보임

**자율 행동·연출:** 제페토가 손잡이에 손을 대고 당기는 방향을 보여 준다. 피노키오가 무게를 느끼는 대사 동안 약 2cm만 열었다 다시 닫아 본다. 내용물을 발견하지 않은 상태에서 손 놓을 위치를 안내하고 두 손을 다시 정확히 붙인다.

**시간 배정:** 발화 전 행동 1.0초 / 발화 뒤 행동 1.5초. 대사·쉼·지정 행동 계획 합계 13.17초. 실제 합성 길이는 별도 확인.

**[S03-N031 · NEW] 제페토:** “Let's pull it slowly.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 무거운 서랍을 천천히 다루도록 돕는다 / 감정: 안전한 배려  
**말하는 방식:** slowly를 실제로 조금 넓게 말하며 손의 당기는 방향과 맞춘다. 아이를 겁주지 않는다.  
**속도·쉼 계획:** 88단어/분, 에너지 2/5, 앞 160ms / 뒤 330ms. 강조: slowly. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Let slowly gently lengthen with the pulling demonstration; guide safe handling without alarming him.  
**피할 연기:** 위험 경고처럼 긴장시키기

**[S03-N032 · NEW] 피노키오:** “It's a little heavy.”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 손잡이에 느껴지는 무게를 말한다 / 감정: 힘을 살짝 쓰는 집중  
**말하는 방식:** little heavy에서 힘을 주는 숨의 색만 낸다. 신음이나 새 감탄사를 붙이지 않고 말은 깨끗이 유지한다.  
**속도·쉼 계획:** 99단어/분, 에너지 2/5, 앞 180ms / 뒤 350ms. 강조: little heavy. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Color little heavy with mild effort from the hands, but keep the words clear and add no grunt.  
**피할 연기:** 과장된 신음이나 실제 부상 같은 호흡

**[S03-N033 · NEW] 제페토:** “Put your hands on the handle.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 손을 놓을 정확한 부분을 짚어 준다 / 감정: 차분한 실무 안내  
**말하는 방식:** hands와 handle을 손 위치를 바꾸는 눈맞춤에 맞춰 말한다. 빠르게 지시를 쏟지 않는다.  
**속도·쉼 계획:** 90단어/분, 에너지 2/5, 앞 160ms / 뒤 340ms. 강조: hands · handle. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Guide the hand placement with calm precision on hands and handle, allowing him to follow physically.  
**피할 연기:** 급히 여러 명령을 쏟는 말투

### B04-C03 · 03:30–03:35 · PROMPT

**카메라:** 손 접촉 INSERT → 피노키오 얼굴

**자율 행동·연출:** 서랍이 완전히 닫힌 상태와 손잡이에 붙은 손을 보여 준다. 피노키오가 윤수 질문을 끝내면 본편 시계를 컷 끝에서 정지한다. 예시·입력 대기는 외부 시계이며 서랍을 더 열지 않는다.

**시간 배정:** 발화 전 행동 0.8초 / 발화 뒤 행동 0초. 대사·쉼·지정 행동 계획 합계 4.36초. 실제 합성 길이는 별도 확인.

**[S03-N034 · NEW] 피노키오:** “Yoonsu, help me open it!”

**음성 연기:** PINOCCHIO_A → 윤수 / 의도: 손잡이를 잡은 채 윤수의 도움을 청한다 / 감정: 조금 힘들지만 즐거운 협력  
**말하는 방식:** help me에는 함께 힘을 보태자는 기대를 담는다. 아이에게도 무거운 물건을 당기라고 강요하지 않는다.  
**속도·쉼 계획:** 105단어/분, 에너지 3/5, 앞 180ms / 뒤 350ms. 강조: Yoonsu · open it. Yoonsu, 뒤 170ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Ask for help while keeping the handle steady; sound collaborative and ready, not helpless or demanding.  
**피할 연기:** 울먹이는 구조 요청

**윤수 참여 4/10 · S03-P04 · 본편 밖 입력 대기**

- 질문 종료 시점: 215초. 본편 시계를 멈춘다.
- 첫 모델 예시: **“Open the drawer!”** — 피노키오의 같은 고정 목소리.
- 모델 예시를 한 번 들려준 뒤 마이크를 켠다. 정확한 단어·발음 채점은 하지 않는다.
- 보호자 터치는 예시를 생략하고 반응으로 진행할 수 있다. 무응답5초 뒤 다시 듣기/터치를 제시한다.
- 시범: 제페토가 손잡이를 잡고 살짝 당겨 서랍의 움직임 방향을 보여준 뒤 다시 닫음.
- 대기 상태: 서랍 완전 닫힘, 손잡이에 피노키오 손 접촉.
- 입력 뒤 한 번 실행: 서랍 열림→내용물 확인→모자 없음→실망.
- 첫 재개: S03-N035 “A wooden spoon and some string!”

**예시 음성 연기:**

**음성 연기:** PINOCCHIO_A → 윤수 (본편 밖 예시) / 의도: 서랍 손잡이 동작을 여는 표현으로 안내한다 / 감정: 조심스럽고 즐거운 협력  
**말하는 방식:** Open은 무거운 손잡이를 천천히 당기듯 부드럽게 시작한다. drawer 끝을 명료하게 두되 크고 힘센 소리로 외치지 않는다.  
**속도·쉼 계획:** 78단어/분, 에너지 2/5, 앞 170ms / 뒤 470ms. 강조: Open · drawer. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Begin Open gently, matching a careful pull of the drawer; keep drawer clear without shouting or straining the voice.  
**피할 연기:** 힘을 내라는 구호처럼 고함치기

### B04-C04 · 03:35–03:50 · REACT

**카메라:** 서랍 레일 SIDE에서 내부와 얼굴로

**자율 행동·연출:** 입력 뒤 선행 동작 4초: 서랍이 레일을 따라 18cm 열리고 두 사람이 안을 확인한다. 그 후 숟가락과 끈을 본 대사로 재개한다. 대사 중 제페토가 숟가락과 짧은 끈을 하나씩 들어 서랍 앞 작업면에 잠깐 놓아 확인하고 모자가 없음을 확인한다.

**시간 배정:** 발화 전 행동 4.0초 / 발화 뒤 행동 0.8초. 대사·쉼·지정 행동 계획 합계 14.97초. 실제 합성 길이는 별도 확인.

**[S03-N035 · NEW] 피노키오:** “A wooden spoon and some string!”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 열린 서랍의 숟가락과 끈을 차례로 발견한다 / 감정: 예상 밖 물건에 대한 호기심  
**말하는 방식:** spoon에서 시선이 멈추고 string으로 옮겨 간다. 모자를 못 찾았다는 실망은 이 관찰 뒤에 온다.  
**속도·쉼 계획:** 108단어/분, 에너지 3/5, 앞 150ms / 뒤 340ms. 강조: wooden spoon · string. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Discover the spoon first and then the string as your eyes travel; allow curiosity before disappointment about the hat.  
**피할 연기:** 아직 보지 않은 내용물을 미리 열거하기

**[S03-N036 · NEW] 제페토:** “Hmm, but no red hat.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 내용물을 보았지만 모자는 없음을 받아들인다 / 감정: 가벼운 아쉬움  
**말하는 방식:** Hmm을 원문 그대로 작게 생각하며 내고 no red hat은 담담하게 낮춘다. 긴 한숨을 추가하지 않는다.  
**속도·쉼 계획:** 90단어/분, 에너지 2/5, 앞 180ms / 뒤 360ms. 강조: no red hat. Hmm, 뒤 200ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Use the written Hmm as a small thinking sound, then acknowledge no red hat quietly without added sighs.  
**피할 연기:** 실패를 큰 좌절로 만들기

**[S03-U009 · ORIGINAL #9] 피노키오:** “It's not here!”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 자신도 서랍 속에 모자가 없음을 확인한다 / 감정: 짧은 실망  
**말하는 방식:** not here는 본 것을 확인하는 짧은 반응이다. 할아버지를 탓하지 말고 다음 수색으로 넘어갈 힘을 남긴다.  
**속도·쉼 계획:** 103단어/분, 에너지 2/5, 앞 150ms / 뒤 380ms. 강조: not here. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Confirm what your eyes found with a brief disappointment; do not blame Grandpa, and leave energy for looking elsewhere.  
**피할 연기:** 화를 내거나 책임을 묻는 억양

### B04-C05 · 03:50–04:01 · NARRATIVE

**카메라:** 투샷 MS, 손과 서랍 닫힘 포함

**자율 행동·연출:** 다른 곳을 보자는 제안에 두 사람이 눈을 맞춘다. 물건을 다시 놓자는 대사에 맞춰 숟가락과 끈을 제자리에 돌려놓고 마지막 발화 뒤 서랍을 완전히 닫는다. 책이 놓인 탁자로 시선을 돌린다.

**시간 배정:** 발화 전 행동 0.5초 / 발화 뒤 행동 2.0초. 대사·쉼·지정 행동 계획 합계 10.69초. 실제 합성 길이는 별도 확인.

**[S03-N037 · NEW] 피노키오:** “Maybe we need to look somewhere else.”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 다른 곳을 살펴보자는 생각을 스스로 낸다 / 감정: 다시 움직이는 의욕  
**말하는 방식:** Maybe로 생각을 시작했다가 somewhere else에 갈수록 마음이 또렷해진다. 물음표를 억지로 붙이지 않는다.  
**속도·쉼 계획:** 107단어/분, 에너지 3/5, 앞 170ms / 뒤 320ms. 강조: somewhere else. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Let Maybe begin a thought, then gain quiet purpose toward somewhere else; this is his own next idea.  
**피할 연기:** 실패할 것 같아 기가 죽은 낭독

**[S03-N038 · NEW] 제페토:** “Let's put these things back.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 꺼내 확인한 물건을 정리하고 다음 자리로 간다 / 감정: 질서 있는 다정함  
**말하는 방식:** these things에서 손에 든 숟가락과 끈을 내려다본다. back을 짧게 마무리해 실제 정리 동작을 받친다.  
**속도·쉼 계획:** 92단어/분, 에너지 2/5, 앞 160ms / 뒤 350ms. 강조: these things · back. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Refer to the spoon and string in your hands on these things; finish back simply as you return them safely.  
**피할 연기:** 정리 교육을 따로 설교하는 말투

## B05. 책 아래도 살펴보자

**목적:** 탁자 위의 학교 책을 이용해 두 번째 수색 실패를 구현하되 책의 위치 연속성을 보존. 관객에게 의자 아래 빨간 단서를 조금 더 명확히 보여준다.

**연속성:** 서랍은 닫힘. 학교 책은 B01에서 원래 놓았던 작업대 우측 위치 그대로. 나무 블록은 선반으로 복귀. 모자 의자 아래 이동 없음.

### B05-C01 · 04:01–04:09 · NARRATIVE

**카메라:** WIDE 낮은 시점, 탁자와 의자 동시

**자율 행동·연출:** 두 사람이 탁자로 다가와 다음 수색 장소를 제안한다. 책은 B01에서 닫아 내려놓은 위치 그대로이며 관객에게만 의자 아래 빨간 끝이 작게 보인다.

**시간 배정:** 발화 전 행동 1.2초 / 발화 뒤 행동 0.5초. 대사·쉼·지정 행동 계획 합계 7.46초. 실제 합성 길이는 별도 확인.

**[S03-N039 · NEW] 피노키오:** “What about the table?”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 다음 수색 장소로 탁자를 제안한다 / 감정: 스스로 찾는 호기심  
**말하는 방식:** table에 시선이 먼저 닿고 그 뒤 짧게 묻는다. 앞선 실패를 길게 끌지 않는다.  
**속도·쉼 계획:** 106단어/분, 에너지 3/5, 앞 140ms / 뒤 300ms. 강조: table. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Spot the table, then offer it as the next place to search; keep the question light and forward-moving.  
**피할 연기:** 서랍 실패를 반복해서 한탄하기

**[S03-N040 · NEW] 제페토:** “Look at the book.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 탁자에서 볼 물건을 책으로 좁혀 준다 / 감정: 조용한 주의 유도  
**말하는 방식:** Look은 작은 부름이고 book은 눈앞에 두는 말이다. 책 아래에 모자가 있다고 암시하지 않는다.  
**속도·쉼 계획:** 92단어/분, 에너지 2/5, 앞 150ms / 뒤 300ms. 강조: book. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Narrow his attention to the book with a small invitation; do not imply that you know what is underneath.  
**피할 연기:** 발견 정답을 미리 안 듯한 강조

### B05-C02 · 04:09–04:24 · NARRATIVE

**카메라:** 책 MS와 제페토 손의 빈 들어올리기 시범

**자율 행동·연출:** 모자가 책 아래 있을지 추측하는 대화다. 제페토가 책 모서리에 손을 대고 들어 올릴 방향을 손목 움직임으로 보이되 실제 책은 아직 들지 않는다. 피노키오는 같은 학교책임을 알아보고 두 손을 준비한다.

**시간 배정:** 발화 전 행동 1.0초 / 발화 뒤 행동 0.8초. 대사·쉼·지정 행동 계획 합계 14.50초. 실제 합성 길이는 별도 확인.

**[S03-N041 · NEW] 피노키오:** “Maybe my hat is hiding under it.”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 책 밑도 가능한 장소라고 추측한다 / 감정: 장난스러운 상상  
**말하는 방식:** hiding을 생물이 된 모자처럼 연기하지 말고 아이의 가벼운 상상으로 처리한다. Maybe는 가능성으로 남긴다.  
**속도·쉼 계획:** 105단어/분, 에너지 3/5, 앞 150ms / 뒤 320ms. 강조: Maybe · under it. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Let hiding be the child’s playful way of imagining a lost object, not evidence that the hat is alive; keep Maybe tentative.  
**피할 연기:** 모자가 실제로 스스로 움직인다는 의인화

**[S03-N042 · NEW] 제페토:** “Lift the book, but keep it safe.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 책을 다치지 않게 들어 보도록 안내한다 / 감정: 세심한 배려  
**말하는 방식:** Lift the book을 하나의 동작 말로 연결하고 but 뒤에는 조금 낮아져 keep it safe를 챙긴다.  
**속도·쉼 계획:** 89단어/분, 에너지 2/5, 앞 170ms / 뒤 360ms. 강조: Lift the book · safe. Lift the book, 뒤 180ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Connect Lift the book into one clear action, then soften after but to care for the book rather than scold.  
**피할 연기:** 책을 망가뜨릴 것이라며 겁주기

**[S03-N043 · NEW] 피노키오:** “It's our school book.”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 아까 함께 본 학교책임을 알아보고 소중히 여긴다 / 감정: 친숙한 애착  
**말하는 방식:** our school book을 처음 배운 이름처럼 떼지 않고 이미 만진 물건에 붙인다. 손은 조심스럽고 목소리는 작다.  
**속도·쉼 계획:** 103단어/분, 에너지 2/5, 앞 150ms / 뒤 320ms. 강조: school book. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Recognize the same school book you explored earlier; speak with familiar ownership and careful hands.  
**피할 연기:** 새 책이 갑자기 생긴 듯한 소개

### B05-C03 · 04:24–04:30 · PROMPT

**카메라:** 책 모서리 INSERT, 질문하는 얼굴 포함

**자율 행동·연출:** 피노키오가 책 아래 모서리에 양손을 댄다. 윤수 질문이 끝날 때까지 책은 탁자에 붙어 있다. 컷 종료 경계에서 예시와 입력 대기를 외부 시계로 시작하며 책을 미리 들거나 페이지를 펼치지 않는다.

**시간 배정:** 발화 전 행동 0.8초 / 발화 뒤 행동 0초. 대사·쉼·지정 행동 계획 합계 5.63초. 실제 합성 길이는 별도 확인.

**[S03-N044 · NEW] 피노키오:** “Yoonsu, can you help me look underneath?”

**음성 연기:** PINOCCHIO_A → 윤수 / 의도: 책을 들어 밑을 살피는 일에 윤수를 부른다 / 감정: 함께 알아보는 기대  
**말하는 방식:** look underneath는 한 호흡으로 부드럽게 이어 질문한다. 어려운 낱말을 시험하듯 또박또박 분리하지 않는다.  
**속도·쉼 계획:** 102단어/분, 에너지 2/5, 앞 180ms / 뒤 360ms. 강조: Yoonsu · look underneath. Yoonsu, 뒤 170ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Invite Yoonsu to look underneath with you; keep the phrase connected and understandable through the action, not spelled out.  
**피할 연기:** underneath를 발음 시험처럼 끊기

**윤수 참여 5/10 · S03-P05 · 본편 밖 입력 대기**

- 질문 종료 시점: 270초. 본편 시계를 멈춘다.
- 첫 모델 예시: **“Lift the book!”** — 피노키오의 같은 고정 목소리.
- 모델 예시를 한 번 들려준 뒤 마이크를 켠다. 정확한 단어·발음 채점은 하지 않는다.
- 보호자 터치는 예시를 생략하고 반응으로 진행할 수 있다. 무응답5초 뒤 다시 듣기/터치를 제시한다.
- 시범: 제페토가 책 모서리에 두 손을 대고 위로 드는 몸짓 시범.
- 대기 상태: 책은 탁자에 완전히 붙어 있고 피노키오 손이 아래 모서리에 닿음.
- 입력 뒤 한 번 실행: 책 들어 확인→아무것도 없음→책 같은 자리에 되돌림.
- 첫 재개: S03-N045 “Not under the book!”

**예시 음성 연기:**

**음성 연기:** PINOCCHIO_A → 윤수 (본편 밖 예시) / 의도: 책을 들어 보는 표현을 안전한 몸짓과 연결한다 / 감정: 집중하는 호기심  
**말하는 방식:** Lift the를 끊지 말고 book을 조심히 받쳐 드는 느낌으로 마친다. 아이가 따라 할 여유를 말 뒤에 남긴다.  
**속도·쉼 계획:** 80단어/분, 에너지 2/5, 앞 160ms / 뒤 470ms. 강조: Lift · book. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Keep Lift the connected, then support book gently as if lifting it with both hands; leave an inviting silence afterward.  
**피할 연기:** 책을 던지듯 강하게 튀는 끝소리

### B05-C04 · 04:30–04:41 · REACT

**카메라:** 책/탁자 CU → 조심스러운 얼굴

**자율 행동·연출:** 입력 뒤 선행 동작 4초: 책을 10cm 들어 빈 아래쪽을 보고, 원래 위치에 내려놓아 양손을 뗀다. 그 뒤 Not under the book!과 꼼꼼히 보았다는 격려를 나눈다. 책은 닫힌 상태를 유지한다.

**시간 배정:** 발화 전 행동 4.0초 / 발화 뒤 행동 0.5초. 대사·쉼·지정 행동 계획 합계 10.44초. 실제 합성 길이는 별도 확인.

**[S03-N045 · NEW] 피노키오:** “Not under the book!”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 책 아래를 직접 확인한 결과를 말한다 / 감정: 가벼운 아쉬움과 집중  
**말하는 방식:** 책을 제자리에 놓고 양손을 이미 뗀 상태에서 방금 확인한 빈 아래쪽의 결과를 제페토에게 짧게 전한다. Not under에 작은 아쉬움만 담고 탐색 의욕은 유지한다. 책을 다시 들거나 내려놓지 않는다.  
**속도·쉼 계획:** 103단어/분, 에너지 2/5, 앞 160ms / 뒤 340ms. 강조: Not under · book. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Report the empty space you have just checked after the book is already back in place and both hands are off it. Give Not under a small disappointment while staying engaged in the search; do not perform another lifting or lowering action.  
**피할 연기:** 찾기 놀이가 끝난 듯 포기하는 어조

**[S03-N046 · NEW] 제페토:** “You're looking very carefully.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 결과보다 꼼꼼히 살핀 태도를 인정한다 / 감정: 구체적인 격려  
**말하는 방식:** carefully에 아이의 실제 행동을 봤다는 따뜻함을 둔다. 잘했다는 상투 감탄으로 부풀리지 않는다.  
**속도·쉼 계획:** 92단어/분, 에너지 2/5, 앞 160ms / 뒤 340ms. 강조: carefully. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Recognize the care you have actually observed; give carefully warm specificity instead of a big generic cheer.  
**피할 연기:** 실패를 덮기 위한 과장된 칭찬

### B05-C05 · 04:41–04:55 · NARRATIVE

**카메라:** WIDE 공간 탐색, 인물과 관객 시선 구분

**자율 행동·연출:** 피노키오는 제페토를 보며 다음에 어디를 볼지 묻는다. 제페토가 방 전체를 손바닥으로 넓게 가리킨다. 카메라만 의자 쪽으로 약간 이동해 관객이 고정된 빨간 끝을 읽게 한다. 인물은 빨간 물건이나 움직임을 발견하지 않은 상태로 수색 의욕을 유지한다.

**시간 배정:** 발화 전 행동 0.5초 / 발화 뒤 행동 1.2초. 대사·쉼·지정 행동 계획 합계 13.31초. 실제 합성 길이는 별도 확인.

**[S03-N047 · NEW] 피노키오:** “Where should we look next?”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 아직 모자 단서를 발견하지 못한 채 다음 장소를 묻는다 / 감정: 차분한 탐색  
**말하는 방식:** next를 다음 선택을 묻는 가벼운 상승으로 마친다. 아래쪽 빨간 물건을 본 듯한 놀람이나 속삭임은 넣지 않는다.  
**속도·쉼 계획:** 104단어/분, 에너지 2/5, 앞 160ms / 뒤 350ms. 강조: look next. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Ask where to look next without any discovery in the voice; there is no glimpse of a moving red object for the character.  
**피할 연기:** 의자 아래를 발견한 듯 흥분하거나 비밀스럽게 말하기

**[S03-N048 · NEW] 제페토:** “Let's look around the whole room.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 특정 정답을 가리키지 않고 방 전체로 시야를 넓힌다 / 감정: 침착한 제안  
**말하는 방식:** whole room을 손바닥으로 넓게 보여 주며 한 문장으로 말한다. 의자라는 정답에 음성 단서를 붙이지 않는다.  
**속도·쉼 계획:** 93단어/분, 에너지 2/5, 앞 150ms / 뒤 330ms. 강조: whole room. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Open attention to the whole room with your hand; keep the search broad and give no vocal hint toward the chair.  
**피할 연기:** 위치를 이미 아는 유도 질문처럼 말하기

**[S03-N049 · NEW] 피노키오:** “I want to find my hat!”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 모자를 찾으려는 의욕을 유지한다 / 감정: 조금 간절하지만 씩씩함  
**말하는 방식:** want와 my hat에 애착을 담되 떼쓰지 않는다. 제페토와 다시 눈을 맞추며 계속 찾을 준비를 보인다.  
**속도·쉼 계획:** 107단어/분, 에너지 3/5, 앞 140ms / 뒤 360ms. 강조: find · my hat. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Keep a little longing for your own hat while staying willing to search; meet Grandpa’s eyes, without whining.  
**피할 연기:** 떼쓰는 울음이나 반복적인 조르기

## B06. 의자 밑 빨간 모자 발견

**목적:** V1.1의 I03 모자 위치·문장·반응을 절대 변경하지 않고 첫 번째 큰 서사 보상 제공.

**연속성:** I03 질문 전까지 모자는 의자 아래 고정, 빨간 끝 일부 관객에게 보임. 제페토가 질문을 모두 마친 후에만 I03에 반응. 모자 수색 전 내용물·결말 스포일러 금지.

### B06-C01 · 04:55–05:05 · NARRATIVE

**카메라:** WS 35mm, 탁자·의자·두 인물

**자율 행동·연출:** 두 사람이 확인한 서랍과 탁자를 가리키며 남은 수색 방향을 생각한다. 카메라는 의자 아래 빨간 끝을 관객에게 읽히게 유지한다. 피노키오와 제페토는 모자 위치를 알아차리지 않는다.

**시간 배정:** 발화 전 행동 1.0초 / 발화 뒤 행동 0.5초. 대사·쉼·지정 행동 계획 합계 9.92초. 실제 합성 길이는 별도 확인.

**[S03-N050 · NEW] 제페토:** “We checked the drawer and the table.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 확인한 두 장소를 정리해 다음 탐색을 준비한다 / 감정: 차분한 정리  
**말하는 방식:** drawer와 table을 이미 살펴본 자리로 짧게 짚는다. 찾기 과정을 처음부터 설명하는 긴 회상처럼 늘이지 않는다.  
**속도·쉼 계획:** 94단어/분, 에너지 2/5, 앞 160ms / 뒤 330ms. 강조: drawer · table. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Briefly account for the two places already checked, pointing to each; this is a useful next-step summary, not a recap narration.  
**피할 연기:** 이미 끝난 수색을 새 사건처럼 재연하는 말투

**[S03-N051 · NEW] 피노키오:** “Where else can it be?”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 남은 위치가 어디인지 진짜로 궁금해한다 / 감정: 가벼운 난감함  
**말하는 방식:** else에서 선택지가 줄어든 생각을 드러낸다. 아직 의자 아래를 알아보지 못했으므로 정답을 암시하는 웃음은 넣지 않는다.  
**속도·쉼 계획:** 103단어/분, 에너지 2/5, 앞 170ms / 뒤 380ms. 강조: Where else. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Wonder where else it could be with a small puzzled lift; you have not recognized the chair clue yet.  
**피할 연기:** 정답을 알고 윤수를 시험하는 질문

### B06-C02 · 05:05–05:12 · NARRATIVE

**카메라:** 투샷 50mm, 제페토의 관객 쪽 시선

**자율 행동·연출:** 제페토가 생각하던 눈빛에서 방 전체를 볼 수 있는 윤수를 떠올린 눈빛으로 바뀐다. 원본 Hmm. Yoonsu can see the whole room.을 말하며 자연스럽게 카메라를 본다. 손은 의자에서 떨어져 있다.

**시간 배정:** 발화 전 행동 0.8초 / 발화 뒤 행동 0.5초. 대사·쉼·지정 행동 계획 합계 6.72초. 실제 합성 길이는 별도 확인.

**[S03-U010 · ORIGINAL #10] 제페토:** “Hmm. Yoonsu can see the whole room.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 방 전체를 보는 윤수에게 도움을 청할 생각을 한다 / 감정: 생각이 열리는 안도  
**말하는 방식:** Hmm 뒤에 생각이 바뀌는 짧은 쉼을 둔다. Yoonsu와 whole room을 연결하며 카메라를 자연스럽게 바라본다.  
**속도·쉼 계획:** 91단어/분, 에너지 2/5, 앞 170ms / 뒤 380ms. 강조: Yoonsu · whole room. Hmm. 뒤 250ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Let the written Hmm mark a new thought; connect Yoonsu with seeing the whole room as you turn toward the camera.  
**피할 연기:** 모자 위치를 알아낸 발견의 환호

### B06-C03 · 05:12–05:17 · PROMPT

**카메라:** 의자와 인물의 시선이 함께 읽히는 3/4 MS

**자율 행동·연출:** 원본 질문 S03-U011을 이 컷에서 처음부터 끝까지 말한다. 질문이 끝나는 컷 경계에서 본편을 멈춘다. 모자 위치·배우 자세는 고정하고 외부 예시 Under the chair!가 인물의 지식을 바꾸거나 허리 숙이기를 시작시키지 않는다.

**시간 배정:** 발화 전 행동 0.8초 / 발화 뒤 행동 0초. 대사·쉼·지정 행동 계획 합계 4.97초. 실제 합성 길이는 별도 확인.

**[S03-U011 · ORIGINAL #11] 제페토:** “Yoonsu, where is Pinocchio's hat?”

**음성 연기:** GEPPETTO_A → 윤수 / 의도: 정본 질문으로 윤수에게 모자 위치를 묻는다 / 감정: 따뜻한 의존과 여유  
**말하는 방식:** 이름을 부르고 where를 또렷하게 전한다. hat의 끝을 살짝 열어 두며 결과를 재촉하지 않는다.  
**속도·쉼 계획:** 89단어/분, 에너지 2/5, 앞 200ms / 뒤 400ms. 강조: Yoonsu · where · hat. Yoonsu, 뒤 200ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Ask the canonical question directly and patiently; clarify where, then leave hat gently open without supplying a discovery.  
**피할 연기:** 정답을 말하라고 독촉하거나 모자를 미리 발견한 연기

**윤수 참여 6/10 · I03 · 본편 밖 입력 대기**

- 질문 종료 시점: 317초. 본편 시계를 멈춘다.
- 첫 모델 예시: **“Under the chair!”** — 제페토의 같은 고정 목소리.
- 모델 예시를 한 번 들려준 뒤 마이크를 켠다. 정확한 단어·발음 채점은 하지 않는다.
- 보호자 터치는 예시를 생략하고 반응으로 진행할 수 있다. 무응답5초 뒤 다시 듣기/터치를 제시한다.
- 시범: 관객에게만 의자 아래 고정된 빨간 끝이 보인다. 원본 질문 뒤 본편을 멈춘 외부 예시로 Under the chair!를 한 번 제공한다. 배우의 발견·허리 숙이기는 아동 입력이나 보호자 터치 뒤 시작한다.
- 대기 상태: 모자 의자 밑 고정, 제페토 허리 곧게 편 상태; 음성 종료 후 WAIT.
- 입력 뒤 한 번 실행: 제페토 허리 숙이기→의자 아래 모자 잡기→피노키오에게 건네기.
- 첫 재개: S03-U012 “Ah! Here it is!”

**예시 음성 연기:**

**음성 연기:** GEPPETTO_A → 윤수 (본편 밖 예시) / 의도: 관객에게 보이는 위치 표현을 본편 밖에서 한 번 들려준다 / 감정: 차분한 발견 도움  
**말하는 방식:** Under the chair는 위치를 보여 주는 예시로 편하게 연결한다. 제페토가 본편 안에서 이미 모자를 찾은 듯한 Ah나 웃음을 추가하지 않는다.  
**속도·쉼 계획:** 78단어/분, 에너지 2/5, 앞 180ms / 뒤 500ms. 강조: Under · chair. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Model the location phrase outside the story clock, connected and clear; do not perform Geppetto’s in-story discovery or add an Ah.  
**피할 연기:** 예시 때문에 본편 등장인물의 지식이 먼저 바뀐 듯한 발견 연기

### B06-C04 · 05:17–05:32 · REACT

**카메라:** SIDE 전신, 숙이기·손 접촉·전달 원테이크

**자율 행동·연출:** 입력 뒤 선행 동작 7초: 제페토가 허리와 무릎을 굽혀 의자 밑을 보고, 모자에 손이 닿은 뒤 집어 피노키오 손으로 전달한다. 인계 접촉이 끝난 뒤 원본 Ah! Here it is!→My red hat!으로 재개하고 색의 기쁨을 잇는다. 모자 복제·부유 없이 의자 아래는 비어 있다.

**시간 배정:** 발화 전 행동 7.0초 / 발화 뒤 행동 0.5초. 대사·쉼·지정 행동 계획 합계 14.99초. 실제 합성 길이는 별도 확인.

**[S03-U012 · ORIGINAL #12] 제페토:** “Ah! Here it is!”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 윤수의 도움으로 찾아 건넨 모자를 반갑게 확인한다 / 감정: 작은 발견의 안도  
**말하는 방식:** Ah는 원문 그대로 짧게 풀리고 Here it is는 손에 닿은 물건을 확인하는 따뜻한 확신으로 잇는다.  
**속도·쉼 계획:** 94단어/분, 에너지 3/5, 앞 150ms / 뒤 380ms. 강조: Here it is. Ah! 뒤 180ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Release a small written Ah after the retrieval, then warmly confirm the actual hat in hand; no extra celebratory sound.  
**피할 연기:** 물건을 잡기 전에 발견 대사를 선행시키기

**[S03-U013 · ORIGINAL #13] 피노키오:** “My red hat!”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 자기 빨간 모자를 받아 보고 기뻐한다 / 감정: 소유의 기쁨  
**말하는 방식:** My를 자신에게 돌아온 물건처럼 환하게 받고 red hat은 가슴에 안는 동작과 함께 따뜻하게 말한다.  
**속도·쉼 계획:** 113단어/분, 에너지 4/5, 앞 140ms / 뒤 360ms. 강조: My · red hat. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Recognize your own hat with a bright My, then warm red hat as you bring it close to your chest.  
**피할 연기:** 길고 날카로운 비명형 환호

**[S03-N052 · NEW] 피노키오:** “It's bright red!”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 가까이서 본 모자의 선명한 색을 즐긴다 / 감정: 잔잔해진 감탄  
**말하는 방식:** bright red는 새 위치 발견이 아니라 손안의 색을 보는 즐거움이다. 앞의 환호보다 한 단계 작게 말한다.  
**속도·쉼 계획:** 108단어/분, 에너지 3/5, 앞 150ms / 뒤 320ms. 강조: bright red. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Enjoy the vivid color close in your hands; make this a smaller, delighted observation after the first big recognition.  
**피할 연기:** My red hat과 똑같은 세기로 반복 환호하기

### B06-C05 · 05:32–05:47 · NARRATIVE

**카메라:** MS 축하, 빈 의자 밑과 모자 든 손

**자율 행동·연출:** 제페토가 이제 빈 의자 아래를 가리키며 찾은 위치를 확인한다. 피노키오는 모자를 가슴 앞에 든 채 고개를 끄덕인다. 윤수에게 감사하는 대사는 카메라 쪽 눈맞춤으로 전하며 모자는 아직 착용하지 않는다.

**시간 배정:** 발화 전 행동 0.5초 / 발화 뒤 행동 1.0초. 대사·쉼·지정 행동 계획 합계 14.51초. 실제 합성 길이는 별도 확인.

**[S03-N053 · NEW] 제페토:** “It was under this chair the whole time.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 찾은 위치를 뒤늦게 확인해 윤수의 도움을 연결한다 / 감정: 자기 실수에 미소 짓는 안도  
**말하는 방식:** under this chair를 실제 빈 의자 밑을 가리키며 말한다. whole time에 작은 웃음의 색만 주고 웃음소리는 추가하지 않는다.  
**속도·쉼 계획:** 92단어/분, 에너지 2/5, 앞 180ms / 뒤 350ms. 강조: under this chair · whole time. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Point to the now-empty place under the chair; let the whole time carry a rueful smile without adding a laugh.  
**피할 연기:** 아이가 못 찾았다고 놀리는 어조

**[S03-N054 · NEW] 피노키오:** “I can see it now.”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 모자를 손에 든 뒤 이제 분명히 보인다고 답한다 / 감정: 납득하는 기쁨  
**말하는 방식:** now에서 전과 달라진 확인을 작게 강조한다. 의자 밑으로 다시 찾으러 가는 듯한 질문조는 쓰지 않는다.  
**속도·쉼 계획:** 104단어/분, 에너지 2/5, 앞 150ms / 뒤 320ms. 강조: now. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Acknowledge that you can really see it now, with the hat already in your hands; use a small settled recognition.  
**피할 연기:** 아직 모자를 못 찾은 듯한 불확실한 상승조

**[S03-N055 · NEW] 제페토:** “Thank you for helping, Yoonsu.”

**음성 연기:** GEPPETTO_A → 윤수 / 의도: 윤수의 위치 도움에 구체적으로 고마움을 전한다 / 감정: 따뜻한 감사  
**말하는 방식:** Thank you는 크게 치켜세우지 않고 눈을 맞춰 전한다. 마지막 Yoonsu는 친근하게 낮춰 소중히 부른다.  
**속도·쉼 계획:** 91단어/분, 에너지 2/5, 앞 180ms / 뒤 430ms. 강조: Thank you · Yoonsu. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Thank the child for that specific help with direct eye contact; finish Yoonsu warmly and personally, not like a prize ceremony.  
**피할 연기:** 성공 점수를 주는 과장 칭찬

## B07. 거꾸로 든 모자

**목적:** 기존 '모자를 거꾸로 든다'를 실제 3D 오브젝트 회전, 부끄러움과 유머로 확장. I04의 해결을 빼앗지 않음.

**연속성:** I03 직후 모자는 피노키오 손에, 의자 아래는 비어 있음. 모자는 실제 착용 전이고 뒤집힌 방향으로 머리 위에만 들려야 한다.

### B07-C01 · 05:47–05:56 · NARRATIVE

**카메라:** 모자 소재 CU, 얼굴과 손끝 동시

**자율 행동·연출:** 피노키오가 모자를 두 손으로 받쳐 천을 살짝 눌러 보고 나무 머리와 촉감을 비교한다. 제페토는 챙을 가리켜 설명한다. 이때 모자 방향을 바로잡아 주거나 머리에 쓰지 않는다.

**시간 배정:** 발화 전 행동 0.8초 / 발화 뒤 행동 0.5초. 대사·쉼·지정 행동 계획 합계 8.96초. 실제 합성 길이는 별도 확인.

**[S03-N056 · NEW] 피노키오:** “It's softer than my wooden head.”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 모자와 나무 머리의 촉감을 비교한다 / 감정: 새 감각에 대한 호기심  
**말하는 방식:** softer에서 손끝으로 천을 눌러 보는 느낌을 담는다. wooden head는 자신을 놀리는 말이 아니라 몸의 재질을 아는 말이다.  
**속도·쉼 계획:** 105단어/분, 에너지 2/5, 앞 170ms / 뒤 330ms. 강조: softer · wooden head. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Feel the cloth on softer, then compare it matter-of-factly to your wooden head without mocking yourself.  
**피할 연기:** 나무 몸을 우스꽝스럽게 비하하기

**[S03-N057 · NEW] 제페토:** “It has a little brim.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 모자의 챙을 손으로 짚어 알려 준다 / 감정: 다정한 관찰  
**말하는 방식:** little brim을 한 호흡으로 말하며 손가락이 챙을 따라간다. 새 단어를 크게 외우게 하는 강세는 주지 않는다.  
**속도·쉼 계획:** 92단어/분, 에너지 2/5, 앞 150ms / 뒤 320ms. 강조: little brim. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Name the little brim as your finger traces it; keep the phrase tactile and conversational rather than a vocabulary drill.  
**피할 연기:** brim만 부자연스럽게 길게 분리하기

### B07-C02 · 05:56–06:08 · NARRATIVE

**카메라:** TWO 50mm, 빈 손으로 올리는 시범

**자율 행동·연출:** 위아래를 묻는 피노키오에게 제페토가 자기 빈 두 손을 올려 보기 좋은 높이를 시범 보인다. 피노키오는 자기 모자를 직접 잡은 채 시범을 눈으로 따라간다. 기존 모자를 새로 만들거나 교체하지 않는다.

**시간 배정:** 발화 전 행동 0.8초 / 발화 뒤 행동 0.8초. 대사·쉼·지정 행동 계획 합계 11.79초. 실제 합성 길이는 별도 확인.

**[S03-N058 · NEW] 피노키오:** “Which way is the top?”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 모자의 위아래 방향을 알아보려 한다 / 감정: 유쾌한 혼란  
**말하는 방식:** top을 찾듯 모자를 살피며 끝을 조금 올린다. 무섭거나 절망한 일이 아니라 직접 해보는 작은 난점이다.  
**속도·쉼 계획:** 102단어/분, 에너지 2/5, 앞 160ms / 뒤 380ms. 강조: Which way · top. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Look around the hat for its top with light, playful puzzlement; this is a small practical question, not distress.  
**피할 연기:** 자신이 서툴다는 과도한 수치심

**[S03-N059 · NEW] 제페토:** “First, hold it high where we can see it.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 직접 만져 볼 수 있도록 먼저 시야 높이로 들게 한다 / 감정: 침착한 단계 안내  
**말하는 방식:** First 뒤 작은 쉼을 두어 한 단계만 제안한다. high와 see를 손짓으로 연결하되 지금 모자를 바로 써 주지는 않는다.  
**속도·쉼 계획:** 90단어/분, 에너지 2/5, 앞 170ms / 뒤 360ms. 강조: hold it high · see it. First, 뒤 180ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Offer just the first step after a small First pause: lift it so you both can see, without solving the wearing action for him.  
**피할 연기:** 한꺼번에 모든 착용 방법을 설명하기

### B07-C03 · 06:08–06:14 · PROMPT

**카메라:** MS, 가슴 높이 모자와 카메라 눈맞춤

**자율 행동·연출:** 피노키오가 모자를 가슴 높이에서 안정적으로 받치고 윤수에게 들어 보이기를 부탁한다. 질문 종료 경계에서 외부 예시·입력 대기로 전환한다. 모자를 머리 위까지 드는 결과는 아직 일어나지 않는다.

**시간 배정:** 발화 전 행동 0.8초 / 발화 뒤 행동 0초. 대사·쉼·지정 행동 계획 합계 5.59초. 실제 합성 길이는 별도 확인.

**[S03-N060 · NEW] 피노키오:** “Yoonsu, can you help me lift it?”

**음성 연기:** PINOCCHIO_A → 윤수 / 의도: 윤수에게 모자를 들어 보이는 동작을 함께 청한다 / 감정: 친근한 기대  
**말하는 방식:** lift it은 양팔을 살짝 준비하는 몸과 연결한다. 도움을 기다리는 표정은 편안하며 울먹이지 않는다.  
**속도·쉼 계획:** 103단어/분, 에너지 2/5, 앞 180ms / 뒤 360ms. 강조: Yoonsu · lift it. Yoonsu, 뒤 170ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Ask Yoonsu to help with lifting it for a look; keep the request relaxed as your arms prepare, not needy.  
**피할 연기:** 모자 착용을 이미 끝내겠다는 성공 어조

**윤수 참여 7/10 · S03-P06 · 본편 밖 입력 대기**

- 질문 종료 시점: 374초. 본편 시계를 멈춘다.
- 첫 모델 예시: **“Hold it up!”** — 피노키오의 같은 고정 목소리.
- 모델 예시를 한 번 들려준 뒤 마이크를 켠다. 정확한 단어·발음 채점은 하지 않는다.
- 보호자 터치는 예시를 생략하고 반응으로 진행할 수 있다. 무응답5초 뒤 다시 듣기/터치를 제시한다.
- 시범: 제페토가 두 손으로 물건을 올리는 시범을 보이고 피노키오가 모자 든 팔을 살짝 들어 올린다.
- 대기 상태: 모자는 배~가슴 앞 두 손에 잡혀 있음, 완전 들어올리기 전.
- 입력 뒤 한 번 실행: 모자를 머리 위로 들기→뒤집힌 방향 발견→부끄럽게 웃음. 모자 착용 금지.
- 첫 재개: S03-N061 “Oh! It's upside down!”

**예시 음성 연기:**

**음성 연기:** PINOCCHIO_A → 윤수 (본편 밖 예시) / 의도: 모자를 들어 보이는 동작에 짧은 표현을 붙인다 / 감정: 가벼운 격려  
**말하는 방식:** Hold it은 부드럽게 붙이고 up을 손이 올라가는 방향처럼 조금 밝힌다. 모자를 쓰는 결과까지 예고하지 않는다.  
**속도·쉼 계획:** 84단어/분, 에너지 2/5, 앞 150ms / 뒤 450ms. 강조: up. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Connect Hold it and lift up lightly with the gesture; model only raising the hat for a look, not wearing it yet.  
**피할 연기:** 모자 착용 성공까지 미리 환호하기

### B07-C04 · 06:14–06:26 · REACT

**카메라:** MS 연속 동작, 모자 회전과 얼굴 반응

**자율 행동·연출:** 입력 뒤 선행 동작 4초: 두 손이 모자를 머리 위 높이로 올리는 동안 방향이 거꾸로인 것이 드러난다. 모자는 머리에 닿지 않는다. 그 후 upside down 대사와 제페토의 다정한 미소를 나눈다. 관절 각도와 손의 모자 지지를 유지한다.

**시간 배정:** 발화 전 행동 4.0초 / 발화 뒤 행동 0.5초. 대사·쉼·지정 행동 계획 합계 11.78초. 실제 합성 길이는 별도 확인.

**[S03-N061 · NEW] 피노키오:** “Oh! It's upside down!”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 올려 본 모자가 거꾸로임을 알아차린다 / 감정: 놀람에서 웃음 섞인 당황  
**말하는 방식:** Oh를 짧게 띄우고 upside down을 말하며 자기 실수를 가볍게 알아본다. 웃음은 목소리 색만 있고 원문 밖 웃음소리는 없다.  
**속도·쉼 계획:** 109단어/분, 에너지 3/5, 앞 150ms / 뒤 380ms. 강조: upside down. Oh! 뒤 180ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Discover the upside-down hat after raising it; turn the small Oh into amused embarrassment, without adding spoken laughter.  
**피할 연기:** 아이를 바보처럼 만드는 과장된 코미디

**[S03-N062 · NEW] 제페토:** “I can see your funny hat.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 어색한 모자를 함께 보며 긴장을 풀어 준다 / 감정: 놀리지 않는 미소  
**말하는 방식:** funny hat은 아이를 조롱하는 말이 아니라 함께 보이는 우스운 방향을 부드럽게 받아 준다.  
**속도·쉼 계획:** 93단어/분, 에너지 2/5, 앞 160ms / 뒤 340ms. 강조: funny hat. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Smile at the hat’s funny orientation with him, never at him; keep funny hat affectionate and small.  
**피할 연기:** 비웃거나 놀리는 웃음 섞인 음성

### B07-C05 · 06:26–06:41 · NARRATIVE

**카메라:** TWO 코믹, 지지된 모자와 표정 중심

**자율 행동·연출:** 거꾸로 든 모자를 계속 두 손으로 지지한 채 원본 tricky→still learning을 나눈다. 피노키오가 떨어뜨리기 싫다는 마음을 전하고 제페토가 천천히 하자고 받는다. 모자 재회전·착용은 I04 이후까지 하지 않는다.

**시간 배정:** 발화 전 행동 0.5초 / 발화 뒤 행동 0.8초. 대사·쉼·지정 행동 계획 합계 14.70초. 실제 합성 길이는 별도 확인.

**[S03-U014 · ORIGINAL #14] 피노키오:** “Grandpa, this is tricky.”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 모자를 쓰는 일이 아직 어렵다고 솔직히 말한다 / 감정: 조심스러운 도움 요청  
**말하는 방식:** Grandpa를 가까이 부른 뒤 tricky에 작은 난감함을 남긴다. 기가 꺾인 흐느낌 대신 계속 해보고 싶은 숨이다.  
**속도·쉼 계획:** 101단어/분, 에너지 2/5, 앞 180ms / 뒤 420ms. 강조: Grandpa · tricky. Grandpa, 뒤 180ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Confide the difficulty to Grandpa; let tricky carry mild frustration while keeping the willingness to try.  
**피할 연기:** 포기하거나 울어 버리는 연기

**[S03-U015 · ORIGINAL #15] 제페토:** “You're still learning.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 서툼이 자연스럽다는 사실로 안심시킨다 / 감정: 묵직한 수용  
**말하는 방식:** still learning을 천천히 이어 주며 기다려 줄 수 있다는 안정감을 낸다. 웃으며 빨리 고치라고 요구하지 않는다.  
**속도·쉼 계획:** 87단어/분, 에너지 2/5, 앞 200ms / 뒤 480ms. 강조: still learning. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Reassure him with the settled patience of an elderly grandfather; connect still learning into one accepting thought.  
**피할 연기:** 빈정대거나 은근히 서두르게 하는 억양

**[S03-N063 · NEW] 피노키오:** “I don't want to drop it.”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 모자를 떨어뜨리지 않으려 조심하는 마음을 말한다 / 감정: 작은 걱정  
**말하는 방식:** drop it에서 손에 힘을 조금 주는 조심스러움만 낸다. 실제로 떨어뜨린 듯 급히 비명을 지르지 않는다.  
**속도·쉼 계획:** 100단어/분, 에너지 2/5, 앞 170ms / 뒤 350ms. 강조: drop it. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Voice a small concern about dropping the hat while keeping it secure; let drop it focus the care, not panic.  
**피할 연기:** 이미 떨어지는 물건을 보고 외치는 연기

**[S03-N064 · NEW] 제페토:** “Then let's go slowly.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 속도를 늦추면 된다고 함께 방법을 찾는다 / 감정: 느긋한 동행  
**말하는 방식:** Then은 아이의 걱정을 받아 주는 연결이고 slowly는 실제 말속도도 편안히 풀린다. 짧은 문장으로 공간을 준다.  
**속도·쉼 계획:** 87단어/분, 에너지 2/5, 앞 180ms / 뒤 440ms. 강조: go slowly. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Let Then answer his concern; ease into slowly so he feels there is time, keeping the line short and companionable.  
**피할 연기:** 느리게 하라는 짜증 섞인 명령

## B08. 제대로 모자를 써요

**목적:** V1.1의 I04를 그대로 살려 거꾸로 든 모자를 회전해 정확히 머리에 쓰는 사건. 거울과 표정/자율 기쁨 표현.

**연속성:** I04 전까지 모자를 머리 위로 들고 서 있음, 완전히 쓴 상태가 되면 뒤에 벗지 않음. S04 출발에 같은 빨간 모자를 이어감.

### B08-C01 · 06:41–06:47 · NARRATIVE

**카메라:** 모자/머리 CU, 틈과 손 지지 확인

**자율 행동·연출:** 거꾸로 든 모자와 머리 사이 5~10cm 틈을 피노키오가 실제로 보고 현재 상태를 말한다. 모자의 위치를 확인하는 눈동자 이동과 팔의 작은 균형 조절만 하며 착용은 시작하지 않는다.

**시간 배정:** 발화 전 행동 0.8초 / 발화 뒤 행동 0.5초. 대사·쉼·지정 행동 계획 합계 5.95초. 실제 합성 길이는 별도 확인.

**[S03-N065 · NEW] 피노키오:** “It's still not sitting on my head.”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 모자가 아직 머리에 닿지 않은 상태를 확인한다 / 감정: 집중하며 해결하려 함  
**말하는 방식:** still not은 불평보다 현재 상태를 확인하는 말이다. head를 말할 때 모자와 머리 사이 틈을 본다.  
**속도·쉼 계획:** 102단어/분, 에너지 2/5, 앞 170ms / 뒤 360ms. 강조: still not · my head. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Observe the remaining gap between hat and head; make still not a practical status check, not a complaint.  
**피할 연기:** 같은 실패를 되풀이하며 짜증내기

### B08-C02 · 06:47–06:53 · NARRATIVE

**카메라:** TWO 50mm, 제페토 빈 손의 회전 시범

**자율 행동·연출:** 제페토가 빈 손으로 회전 방향을 먼저 보여 준 뒤 turn it around라고 말한다. 피노키오는 그 방향을 눈으로 따라가지만 실제 모자는 거꾸로 유지한다. 시범이 해결 동작을 대신하지 않는다.

**시간 배정:** 발화 전 행동 1.2초 / 발화 뒤 행동 0.5초. 대사·쉼·지정 행동 계획 합계 5.56초. 실제 합성 길이는 별도 확인.

**[S03-N066 · NEW] 제페토:** “You can turn it around.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 회전 방향을 손으로 보여 주며 가능성을 알려 준다 / 감정: 짧고 안정적인 도움  
**말하는 방식:** turn it around를 손의 빈 회전 시범과 부드럽게 맞춘다. 실제 모자를 대신 잡는 듯 소유권을 빼앗지 않는다.  
**속도·쉼 계획:** 90단어/분, 에너지 2/5, 앞 170ms / 뒤 360ms. 강조: turn it around. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Guide the turning idea with an empty-hand demonstration; keep it supportive, leaving the actual hat and decision with him.  
**피할 연기:** 아이의 손을 빼앗아 대신 해결하는 어조

### B08-C03 · 06:53–07:00 · PROMPT

**카메라:** 피노키오 얼굴/모자 3/4 CU

**자율 행동·연출:** 원본 질문 S03-U016을 이 컷에서 말한다. 마지막 음성 종료가 본편 컷 끝이며 그 지점에서 외부 예시와 입력 대기를 한다. 기다리는 동안 모자 회전·착용·자율 머리 움직임으로 결과를 먼저 내지 않는다.

**시간 배정:** 발화 전 행동 0.6초 / 발화 뒤 행동 0초. 대사·쉼·지정 행동 계획 합계 6.11초. 실제 합성 길이는 별도 확인.

**[S03-U016 · ORIGINAL #16] 피노키오:** “Yoonsu, what should I do with my hat?”

**음성 연기:** PINOCCHIO_A → 윤수 / 의도: 정본 질문으로 윤수에게 모자 사용을 함께 묻는다 / 감정: 믿고 청하는 호기심  
**말하는 방식:** what should I do에서 도움을 구하는 마음을 유지하고 with my hat을 자연스럽게 이어 마친다. 정답을 압박하지 않는다.  
**속도·쉼 계획:** 102단어/분, 에너지 2/5, 앞 200ms / 뒤 420ms. 강조: Yoonsu · my hat. Yoonsu, 뒤 180ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Ask Yoonsu the canonical question with trust; connect what should I do to with my hat as a genuine invitation, never an exam.  
**피할 연기:** 발음을 정확히 따라 하라고 요구하는 말투

**윤수 참여 8/10 · I04 · 본편 밖 입력 대기**

- 질문 종료 시점: 420초. 본편 시계를 멈춘다.
- 첫 모델 예시: **“Put it on!”** — 피노키오의 같은 고정 목소리.
- 모델 예시를 한 번 들려준 뒤 마이크를 켠다. 정확한 단어·발음 채점은 하지 않는다.
- 보호자 터치는 예시를 생략하고 반응으로 진행할 수 있다. 무응답5초 뒤 다시 듣기/터치를 제시한다.
- 시범: 제페토가 자기 머리를 가리키고 모자가 실제로 어떻게 올라가는지 손으로만 시범. 피노키오는 그대로 WAIT.
- 대기 상태: 피노키오 머리 위 뒤집힌 모자 유지, 모자 회전과 착용 금지.
- 입력 뒤 한 번 실행: 모자 180도 방향 고치기→머리에 쓰기→챙 잡기→거울에서 웃기.
- 첫 재개: S03-U017 “Now I'm ready!”

**예시 음성 연기:**

**음성 연기:** PINOCCHIO_A → 윤수 (본편 밖 예시) / 의도: 모자를 쓰는 원본 세 단어를 부담 없이 들려준다 / 감정: 자신 있게 함께 해보는 마음  
**말하는 방식:** Put it on을 한 호흡의 권유로 내고 on에서 편안히 마친다. 정답을 요구하거나 실제 착용 성공을 앞당기는 환호는 없다.  
**속도·쉼 계획:** 82단어/분, 에너지 2/5, 앞 170ms / 뒤 500ms. 강조: on. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Model Put it on in one friendly, confident breath outside the story clock; do not demand correctness or celebrate the wearing before input.  
**피할 연기:** 정답 발음을 재촉하거나 착용 반응을 먼저 연기하기

### B08-C04 · 07:00–07:14 · REACT

**카메라:** 전신 50mm, 손·머리 접촉과 거울 한 프레임

**자율 행동·연출:** 입력 뒤 선행 동작 7초: 모자를 바르게 회전→머리에 착용→챙 잡기→거울 앞 한 걸음→미소까지 완료한다. 그 뒤 원본 S03-U017과 가방을 잊지 말라는 S03-U018을 정확한 텍스트로 재생한다. 대사 중 제페토가 탁자의 가방을 가리킨다.

**시간 배정:** 발화 전 행동 7.0초 / 발화 뒤 행동 0.5초. 대사·쉼·지정 행동 계획 합계 13.83초. 실제 합성 길이는 별도 확인.

**[S03-U017 · ORIGINAL #17] 피노키오:** “Now I'm ready!”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 바르게 쓴 모자를 거울에서 보고 준비됐다고 느낀다 / 감정: 자랑스러운 성취  
**말하는 방식:** Now는 착용 완료를 확인한 뒤 또렷하게 시작한다. ready는 허리를 편 아이의 자연스러운 밝음으로 낸다.  
**속도·쉼 계획:** 112단어/분, 에너지 4/5, 앞 160ms / 뒤 400ms. 강조: Now · ready. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Only after wearing the hat and smiling in the mirror, brighten Now and let ready sound proudly upright.  
**피할 연기:** 모자가 닿기 전에 먼저 성공을 외치기

**[S03-U018 · ORIGINAL #18] 제페토:** “Almost. Don't forget your schoolbag.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 기쁨을 받아 주면서 가방 준비를 다정히 상기한다 / 감정: 온화한 현실 확인  
**말하는 방식:** Almost를 미소로 먼저 받고 잠깐 쉰다. Don’t forget은 꾸중이 아니라 남은 가방을 눈으로 보여 주는 말이다.  
**속도·쉼 계획:** 90단어/분, 에너지 2/5, 앞 180ms / 뒤 400ms. 강조: Almost · schoolbag. Almost. 뒤 250ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Smile through Almost, pause, then gently point out the remaining schoolbag; Don’t forget is a reminder, not a reprimand.  
**피할 연기:** 아이의 성취를 꺾는 단호한 정정

### B08-C05 · 07:14–07:32 · NARRATIVE

**카메라:** 투샷에서 탁자 방향으로 짧은 동행

**자율 행동·연출:** 피노키오가 모자와 아직 준비되지 않은 가방을 비교하며 이해한다. 제페토가 책 챙기기로 연결하고 피노키오는 챙을 한 번 만져 계속 쓰고 있겠다고 답한다. 마지막 대사 뒤 두 사람이 탁자 옆 가방에 도착한다. 모자를 벗지 않는다.

**시간 배정:** 발화 전 행동 0.5초 / 발화 뒤 행동 2.0초. 대사·쉼·지정 행동 계획 합계 17.26초. 실제 합성 길이는 별도 확인.

**[S03-N067 · NEW] 피노키오:** “My hat is ready, but my bag is not.”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 모자와 가방의 준비 상태를 비교해 이해한다 / 감정: 납득하며 전환  
**말하는 방식:** hat is ready는 뿌듯하게, but 뒤 bag is not은 가방을 보며 현실을 받아들인다. 두 절의 느낌을 다르게 한다.  
**속도·쉼 계획:** 105단어/분, 에너지 2/5, 앞 170ms / 뒤 350ms. 강조: hat is ready · bag is not. My hat is ready, 뒤 180ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Keep pride in hat is ready, then turn your gaze and tone toward the unfinished bag after but; make the contrast newly understood.  
**피할 연기:** 한 문장을 끝까지 같은 낭독조로 평평하게 읽기

**[S03-N068 · NEW] 제페토:** “Let's get the book and pack it.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 학교책을 챙기는 다음 실제 행동으로 이끈다 / 감정: 차분한 진행  
**말하는 방식:** get the book에서 탁자로 시선을 옮기고 pack it은 함께 준비하자는 말로 부드럽게 마친다.  
**속도·쉼 계획:** 94단어/분, 에너지 2/5, 앞 160ms / 뒤 330ms. 강조: book · pack it. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Move attention to the table on get the book, then invite the shared packing task with a quiet pack it.  
**피할 연기:** 장면 전환 안내 방송처럼 읽기

**[S03-N069 · NEW] 피노키오:** “I will keep my hat on.”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 모자를 그대로 쓰고 가방을 준비하겠다고 다짐한다 / 감정: 만족스러운 작은 책임감  
**말하는 방식:** keep my hat on을 가볍게 확인하며 챙을 한 번 만진다. 모자를 다시 벗는 듯한 장난은 목소리에 넣지 않는다.  
**속도·쉼 계획:** 105단어/분, 에너지 2/5, 앞 150ms / 뒤 380ms. 강조: keep my hat on. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Confirm that the hat stays on with a small touch to the brim; carry satisfaction into the next task without making a new joke.  
**피할 연기:** 모자를 다시 벗을 것 같은 장난스러운 반전

## B09. 책가방을 열어 책을 넣어요

**목적:** 모자 사건에서 가방/책을 챙기는 준비로 자연스럽게 연결. 원본 제페토의 책 넣기 주체를 그대로 유지.

**연속성:** 모자는 이제 피노키오 머리 위 고정. 원본 학교책은 탁자에 있으며 학교가방은 비어 있음. 가방끈은 아직 묶지 않음.

### B09-C01 · 07:32–07:41 · NARRATIVE

**카메라:** 책가방 MS, 탁자 위 책도 함께

**자율 행동·연출:** 두 사람이 아직 비어 있는 학교가방 앞에 선다. 피노키오가 가방을 살피며 빈 상태를 말하고 제페토는 탁자 위 책을 가리켜 필요한 준비를 알려 준다.

**시간 배정:** 발화 전 행동 1.0초 / 발화 뒤 행동 0.5초. 대사·쉼·지정 행동 계획 합계 8.58초. 실제 합성 길이는 별도 확인.

**[S03-N070 · NEW] 피노키오:** “My schoolbag is empty!”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 가방에 아직 책이 없음을 보고 알아차린다 / 감정: 새 준비 과제 발견  
**말하는 방식:** empty는 놀람을 과장하지 않고 열린 공간을 상상하며 또렷하게 말한다. 가방을 망가뜨린 듯 걱정하지 않는다.  
**속도·쉼 계획:** 108단어/분, 에너지 3/5, 앞 150ms / 뒤 340ms. 강조: empty. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Notice the bag is empty as the next practical thing to fix; keep empty clear and curious rather than alarmed.  
**피할 연기:** 심각한 분실 사건처럼 놀라기

**[S03-N071 · NEW] 제페토:** “We must put your book inside.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 학교책을 가방에 넣어야 하는 이유를 단순히 안내한다 / 감정: 믿음직한 준비  
**말하는 방식:** your book을 피노키오의 물건으로 다정하게 부른다. must는 강압적으로 누르지 말고 필요한 다음 일로 연결한다.  
**속도·쉼 계획:** 93단어/분, 에너지 2/5, 앞 160ms / 뒤 340ms. 강조: your book · inside. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Name your book with caring ownership; let must mean the sensible next task, not an authoritarian order.  
**피할 연기:** 명령을 거역하면 안 된다는 강압

### B09-C02 · 07:41–07:51 · NARRATIVE

**카메라:** TWO 50mm → 같은 학교책 INSERT

**자율 행동·연출:** 피노키오가 B01에서 함께 봤던 동일한 책을 알아본다. 제페토는 책을 아직 탁자에 둔 채 함께 학교에 갈 물건이라고 답한다. 다른 책이 생기거나 책이 이미 가방 안으로 이동하지 않는다.

**시간 배정:** 발화 전 행동 0.8초 / 발화 뒤 행동 0.5초. 대사·쉼·지정 행동 계획 합계 9.24초. 실제 합성 길이는 별도 확인.

**[S03-N072 · NEW] 피노키오:** “It's the book we looked at.”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 아까 함께 본 책과 같은 물건임을 알아본다 / 감정: 친숙한 반가움  
**말하는 방식:** looked at에서 앞서 그림을 봤던 기억이 작게 살아난다. 처음 보는 책을 소개하는 억양은 피한다.  
**속도·쉼 계획:** 104단어/분, 에너지 2/5, 앞 160ms / 뒤 340ms. 강조: book we looked at. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Recognize the same book you explored together earlier; let looked at carry a small shared memory, not a fresh introduction.  
**피할 연기:** 별도의 새 책처럼 소개하기

**[S03-N073 · NEW] 제페토:** “Yes. It's coming with you.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 그 책이 함께 학교에 간다고 안심시킨다 / 감정: 물건에 정을 붙여 주는 온기  
**말하는 방식:** Yes를 짧게 받아 주고 coming with you는 아이를 따라가는 익숙한 물건이라는 따뜻함으로 말한다.  
**속도·쉼 계획:** 91단어/분, 에너지 2/5, 앞 150ms / 뒤 360ms. 강조: coming with you. Yes. 뒤 170ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Answer Yes softly, then give coming with you the comfort of taking something familiar along.  
**피할 연기:** 책을 살아 있는 새 등장인물처럼 과장하기

### B09-C03 · 07:51–08:01 · PROMPT

**카메라:** 가방 플랩 CU와 질문하는 제페토

**자율 행동·연출:** 제페토가 플랩을 2cm 들어 힌지 방향만 보여 주고 다시 닫는다. 피노키오의 플랩 질문 뒤 제페토가 윤수 질문을 말한다. 질문 종료 경계에서 외부 예시·입력 대기를 시작하며 책은 탁자, 플랩은 닫힘 상태를 유지한다.

**시간 배정:** 발화 전 행동 1.2초 / 발화 뒤 행동 0초. 대사·쉼·지정 행동 계획 합계 9.34초. 실제 합성 길이는 별도 확인.

**[S03-N074 · NEW] 피노키오:** “Can we open this flap?”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 가방 플랩을 어떻게 열지 살핀다 / 감정: 실용적인 궁금함  
**말하는 방식:** this flap에서 실제 가장자리를 바라보며 묻는다. 가방이 이미 활짝 열린 듯 만족스럽게 말하지 않는다.  
**속도·쉼 계획:** 103단어/분, 에너지 2/5, 앞 170ms / 뒤 340ms. 강조: this flap. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Ask about the flap you are looking at, with genuine practical curiosity while it remains closed.  
**피할 연기:** 이미 열림을 확인한 말투

**[S03-N075 · NEW] 제페토:** “Yoonsu, help me open the schoolbag!”

**음성 연기:** GEPPETTO_A → 윤수 / 의도: 윤수에게 가방을 여는 첫 단계를 함께 청한다 / 감정: 차분한 도움 초대  
**말하는 방식:** open the schoolbag을 눈앞의 닫힌 플랩과 맞춘다. 이름 뒤 시선을 잠깐 만나고 재촉하지 않는다.  
**속도·쉼 계획:** 91단어/분, 에너지 2/5, 앞 200ms / 뒤 380ms. 강조: Yoonsu · open the schoolbag. Yoonsu, 뒤 180ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Invite Yoonsu to help with the closed flap in front of you; keep open the schoolbag connected and unhurried.  
**피할 연기:** 내용 인식을 검사하는 지시

**윤수 참여 9/10 · S03-P07 · 본편 밖 입력 대기**

- 질문 종료 시점: 481초. 본편 시계를 멈춘다.
- 첫 모델 예시: **“Open the bag!”** — 제페토의 같은 고정 목소리.
- 모델 예시를 한 번 들려준 뒤 마이크를 켠다. 정확한 단어·발음 채점은 하지 않는다.
- 보호자 터치는 예시를 생략하고 반응으로 진행할 수 있다. 무응답5초 뒤 다시 듣기/터치를 제시한다.
- 시범: 제페토가 가방 뚜껑을 2cm 들었다 내리며 경첩 동작 시범.
- 대기 상태: 가방 뚜껑 닫힘, 책은 탁자, 제페토 손잡이 접촉.
- 입력 뒤 한 번 실행: 가방 플랩 열기→제페토가 같은 책을 한 번 넣어 안착→피노키오가 확인. 이후 후속 대사는 이미 완료된 책 위치를 말함.
- 첫 재개: S03-N076 “It's open!”

**예시 음성 연기:**

**음성 연기:** GEPPETTO_A → 윤수 (본편 밖 예시) / 의도: 닫힌 가방을 여는 표현을 플랩 동작과 연결한다 / 감정: 다정하고 실용적인 안내  
**말하는 방식:** Open the bag을 손자의 눈높이에 맞춘 낮은 할아버지 목소리로 한 번 연결한다. bag에 물건을 가리키는 작은 강세만 둔다.  
**속도·쉼 계획:** 79단어/분, 에너지 2/5, 앞 180ms / 뒤 470ms. 강조: Open · bag. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Offer Open the bag once in the same warm elderly voice at the child’s level; give bag a small pointing emphasis, not a test accent.  
**피할 연기:** 젊은 교사 목소리로 바뀌거나 세 단어를 채점하기

### B09-C04 · 08:01–08:14 · REACT

**카메라:** REACT 소품 원테이크, 양손과 책 바닥 접촉

**자율 행동·연출:** 입력 뒤 선행 동작 5.5초: 플랩을 열고 제페토가 같은 책 한 권을 집어 가방 안에 한 번 넣어 안착시킨 뒤 피노키오가 확인한다. 그 후 열린 플랩을 확인하는 첫 재개 대사와 이미 책이 안에 있다는 완료 대사를 재생한다. 책을 다시 꺼내거나 재삽입하지 않는다.

**시간 배정:** 발화 전 행동 5.5초 / 발화 뒤 행동 0.5초. 대사·쉼·지정 행동 계획 합계 12.01초. 실제 합성 길이는 별도 확인.

**[S03-N076 · NEW] 피노키오:** “It's open!”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 반응 뒤 열려 있는 플랩을 확인한다 / 감정: 작은 성취 확인  
**말하는 방식:** open을 플랩 쪽을 보며 짧게 말한다. 다음 제페토의 책 상태 설명을 받을 수 있도록 큰 환호로 끝내지 않는다.  
**속도·쉼 계획:** 108단어/분, 에너지 3/5, 앞 140ms / 뒤 320ms. 강조: open. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Briefly recognize the open flap, leaving room for Grandpa to confirm where the book now is; keep this small and concrete.  
**피할 연기:** 책 넣기를 아직 시작하지 않았다는 암시

**[S03-N077 · NEW] 제페토:** “Your book is inside the bag.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 이미 넣은 책이 가방 안에 있음을 확인해 준다 / 감정: 완료된 준비의 안심  
**말하는 방식:** inside the bag을 손가락으로 보이는 책에 붙여 말한다. 이제 넣겠다는 예고가 아니라 완료된 위치 확인이다.  
**속도·쉼 계획:** 92단어/분, 에너지 2/5, 앞 170ms / 뒤 360ms. 강조: inside the bag. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Confirm the completed placement of the book inside the bag; point to its actual position, with no sense of a future insertion.  
**피할 연기:** 책을 한 번 더 넣겠다는 미래 동작의 억양

### B09-C05 · 08:14–08:25 · NARRATIVE

**카메라:** 투샷/가방 내부에서 풀린 끈으로

**자율 행동·연출:** 피노키오가 책이 잘 맞는 것을 말하고 제페토가 책 가장자리를 평평하게 정돈한다. 피노키오 시선이 열린 플랩의 풀린 끈으로 옮겨 다음 일을 묻는다. 가방은 탁자에 지지되어 있고 끈은 아직 묶지 않는다.

**시간 배정:** 발화 전 행동 0.5초 / 발화 뒤 행동 1.0초. 대사·쉼·지정 행동 계획 합계 10.38초. 실제 합성 길이는 별도 확인.

**[S03-N078 · NEW] 피노키오:** “The book fits!”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 책이 가방 크기에 잘 들어맞음을 본다 / 감정: 편안한 만족  
**말하는 방식:** fits는 책 가장자리를 보고 한 번 확인하듯 말한다. 새 사건의 큰 성공보다 정리가 잘 된 기쁨이다.  
**속도·쉼 계획:** 108단어/분, 에너지 3/5, 앞 150ms / 뒤 340ms. 강조: fits. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** See that the book fits neatly and acknowledge it once, with modest satisfaction rather than a grand victory.  
**피할 연기:** 같은 책이 다시 들어간 것처럼 놀라기

**[S03-N079 · NEW] 제페토:** “Keep it flat and safe.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 가방 안 책이 구겨지지 않도록 정돈한다 / 감정: 세심한 보호  
**말하는 방식:** flat과 safe를 두 번의 부드러운 손정리와 연결한다. 일어난 잘못을 꾸짖는 소리는 넣지 않는다.  
**속도·쉼 계획:** 89단어/분, 에너지 2/5, 앞 160ms / 뒤 360ms. 강조: flat · safe. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Link flat and safe to two gentle settling motions of the book; protect it without implying that the child has done wrong.  
**피할 연기:** 책을 망가뜨렸다고 나무라는 어조

**[S03-N080 · NEW] 피노키오:** “What about the straps?”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 아직 풀린 끈을 알아보고 다음 준비를 묻는다 / 감정: 한 단계 더 살피는 관심  
**말하는 방식:** straps에서 책에서 끈으로 시선이 이동한다. 앞의 준비를 무시하지 말고 남은 부분을 발견하는 작은 질문이다.  
**속도·쉼 계획:** 104단어/분, 에너지 2/5, 앞 160ms / 뒤 360ms. 강조: straps. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Shift your gaze from the settled book to the loose straps; make this a small next-step question after a success.  
**피할 연기:** 준비가 모두 실패했다는 불만

## B10. 끈을 묶고 할아버지와 약속

**목적:** 학교 갈 준비 완료와 '저녁 전에 돌아오라'는 약속을 감정적으로 마무리. S04 집 대문을 열거나 외출을 미리 시작하지 않음.

**연속성:** 빨간 모자는 계속 착용, 같은 학교책 한 권은 가방 안, 플랩과 결속 끈은 처음에 열림/미결속. 참여 뒤 플랩 결속을 끝내고 B10-C05에서 기존 어깨끈으로 실제 착용한다. 제페토와 작업실 안의 출구 앞까지만 이동한다. 실내 출입문은 아직 닫힘이고 집 앞 나무 대문은 S04 I05 전까지 반드시 닫힘이다.

### B10-C01 · 08:25–08:36 · NARRATIVE

**카메라:** 가방 CU에서 두 인물 MS

**자율 행동·연출:** 열린 플랩과 풀린 결속 끈을 먼저 보여 준다. 아직 열려 있다는 피노키오의 관찰을 제페토가 받아 닫기와 묶기의 순서를 안내한다. 책은 이미 가방 안에 있고 꺼내지 않는다.

**시간 배정:** 발화 전 행동 0.8초 / 발화 뒤 행동 0.5초. 대사·쉼·지정 행동 계획 합계 10.64초. 실제 합성 길이는 별도 확인.

**[S03-N081 · NEW] 피노키오:** “Grandpa, the bag is still open.”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 책을 넣었지만 플랩은 아직 열려 있음을 알린다 / 감정: 세심해진 관찰  
**말하는 방식:** Grandpa를 가까이 부르고 still open은 자신이 발견한 남은 일을 차분하게 전달한다. 같은 빈 가방 놀람을 반복하지 않는다.  
**속도·쉼 계획:** 103단어/분, 에너지 2/5, 앞 180ms / 뒤 360ms. 강조: still open. Grandpa, 뒤 170ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Tell Grandpa about the remaining open flap with newly careful attention; do not repeat the earlier surprise at an empty bag.  
**피할 연기:** 가방 속 책이 없다는 혼동을 주는 놀람

**[S03-N082 · NEW] 제페토:** “Let's close it and tie the straps.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 플랩을 닫고 끈을 묶는 순서를 함께 정한다 / 감정: 안정적인 준비  
**말하는 방식:** close it과 tie the straps를 부드럽게 이어 두 행동의 순서를 낸다. 손의 동작을 말보다 먼저 서두르지 않는다.  
**속도·쉼 계획:** 91단어/분, 에너지 2/5, 앞 170ms / 뒤 350ms. 강조: close it · tie the straps. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Set the simple order of closing and tying with gentle clarity; leave room for the hands to do each step.  
**피할 연기:** 한꺼번에 끝내라고 재촉하는 명령

### B10-C02 · 08:36–08:48 · NARRATIVE

**카메라:** 손·끈 INSERT, 두 배우 얼굴도 읽히는 각도

**자율 행동·연출:** 피노키오가 플랩을 잡겠다고 제안하며 실제로 닫힌 위치를 지지한다. 제페토는 도움을 받아들이고 결속 끈을 첫 교차까지만 시범 보인다. 어깨에 메는 끈과 플랩 결속 끈을 구분해 보여 준다. 매듭을 당겨 고정하지 않는다.

**시간 배정:** 발화 전 행동 1.0초 / 발화 뒤 행동 0.8초. 대사·쉼·지정 행동 계획 합계 11.91초. 실제 합성 길이는 별도 확인.

**[S03-N083 · NEW] 피노키오:** “I can hold the flap.”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 자신이 할 수 있는 도움을 먼저 제안한다 / 감정: 자라는 자신감  
**말하는 방식:** I can에 작은 용기를 싣고 flap은 실제 잡을 부분을 보며 말한다. 자랑을 크게 부풀리지 않는다.  
**속도·쉼 계획:** 106단어/분, 에너지 3/5, 앞 150ms / 뒤 330ms. 강조: I can · flap. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Offer your own useful job with a small confidence on I can, looking at the flap you can hold.  
**피할 연기:** 혼자 모든 일을 할 수 있다는 과장된 허세

**[S03-N084 · NEW] 제페토:** “You can help me. Look at this little knot.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 아이의 도움을 받아들이고 첫 교차를 보여 준다 / 감정: 협력하는 다정함  
**말하는 방식:** You can help me는 아이의 제안을 인정한다. 다음 Look에서 손의 작은 매듭 시범으로 조용히 시선을 옮긴다.  
**속도·쉼 계획:** 90단어/분, 에너지 2/5, 앞 180ms / 뒤 380ms. 강조: help me · little knot. You can help me. 뒤 240ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Accept his offered help first, then shift attention to the little knot in your hands; keep the two thoughts intimate and practical.  
**피할 연기:** 매듭 이름을 외우게 하는 강의

### B10-C03 · 08:48–08:54 · PROMPT

**카메라:** 정면 MS, 미완성 교차와 윤수 눈맞춤

**자율 행동·연출:** 두 배우의 손이 미완성 교차를 안정적으로 지지한 상태에서 제페토가 윤수 질문을 말한다. 질문 종료 경계에서 본편 시계를 멈춘다. 별도 예시·입력 대기 동안 새 매듭이나 준비 완료 동작을 실행하지 않는다.

**시간 배정:** 발화 전 행동 0.7초 / 발화 뒤 행동 0초. 대사·쉼·지정 행동 계획 합계 5.49초. 실제 합성 길이는 별도 확인.

**[S03-N085 · NEW] 제페토:** “Yoonsu, help us tie the bag!”

**음성 연기:** GEPPETTO_A → 윤수 / 의도: 윤수와 함께 마지막 결속을 마치려 한다 / 감정: 준비를 함께 끝내는 기대  
**말하는 방식:** help us를 한 호흡으로 묶어 세 사람이 함께 한다는 느낌을 준다. tie the bag은 힘주어 외치지 않는다.  
**속도·쉼 계획:** 90단어/분, 에너지 2/5, 앞 200ms / 뒤 400ms. 강조: Yoonsu · tie the bag. Yoonsu, 뒤 190ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Invite Yoonsu to help finish this last shared task; connect help us warmly and keep the tying request easy, not forceful.  
**피할 연기:** 정답을 말해야 끝난다는 압박

**윤수 참여 10/10 · S03-P08 · 본편 밖 입력 대기**

- 질문 종료 시점: 534초. 본편 시계를 멈춘다.
- 첫 모델 예시: **“Tie the strap!”** — 제페토의 같은 고정 목소리.
- 모델 예시를 한 번 들려준 뒤 마이크를 켠다. 정확한 단어·발음 채점은 하지 않는다.
- 보호자 터치는 예시를 생략하고 반응으로 진행할 수 있다. 무응답5초 뒤 다시 듣기/터치를 제시한다.
- 시범: 제페토가 매듭의 첫 교차만 시연하고 끈을 잡은 상태로 멈춤.
- 대기 상태: 피노키오가 닫힌 위치의 플랩을 지지하고 제페토가 결속 끈의 첫 교차만 잡고 있음. 매듭 당김·고정 전이며 이 상태의 예시/입력 대기는 본편 시간 밖.
- 입력 뒤 한 번 실행: 가방끈 교차→당겨 고정→안전한 책가방 완성→피노키오의 준비 완료 표정.
- 첫 재개: S03-N086 “Now the book is safe!”

**예시 음성 연기:**

**음성 연기:** GEPPETTO_A → 윤수 (본편 밖 예시) / 의도: 가방의 마지막 끈 결속에 쓸 표현을 알려 준다 / 감정: 여유 있게 함께 마무리함  
**말하는 방식:** Tie the를 자연스럽게 묶어 말하고 strap은 서두르지 않고 명확히 끝낸다. 동작을 성공시켰다는 말투 대신 시도할 여유를 준다.  
**속도·쉼 계획:** 77단어/분, 에너지 2/5, 앞 180ms / 뒤 520ms. 강조: Tie · strap. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Connect Tie the naturally and finish strap clearly at an unhurried pace; invite the attempt instead of pretending the knot is already finished.  
**피할 연기:** 매듭이 이미 완성된 듯한 축하 또는 군대식 명령

### B10-C04 · 08:54–09:22 · REACT

**카메라:** 매듭 CU→따뜻한 투샷, 약속까지 연결

**자율 행동·연출:** 입력 뒤 선행 동작 5.5초: 결속 끈을 교차해 당겨 고정하고 플랩이 닫혔음을 확인한다. 그 뒤 책이 안전하다는 첫 재개 대사와 세 물건 점검을 나눈다. 제페토가 아이 눈높이로 몸을 낮추고 원본 Listen carefully→학교에 가고 저녁 전 귀가하라는 말을 충분한 속도로 전한다. 점검과 눈맞춤은 배정된 발화 동안 진행한다.

**시간 배정:** 발화 전 행동 5.5초 / 발화 뒤 행동 0.8초. 대사·쉼·지정 행동 계획 합계 27.45초. 실제 합성 길이는 별도 확인.

**[S03-N086 · NEW] 피노키오:** “Now the book is safe!”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 끈이 고정되어 책이 안전해진 것을 확인한다 / 감정: 안도하는 성취  
**말하는 방식:** Now는 매듭이 실제로 고정된 뒤 시작한다. safe에서 책을 소중히 챙겼다는 작은 안도감을 준다.  
**속도·쉼 계획:** 108단어/분, 에너지 3/5, 앞 160ms / 뒤 360ms. 강조: Now · safe. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Speak only after the knot is secure; let safe carry the relief of having cared for the book, not a loud victory.  
**피할 연기:** 매듭 완성 전 먼저 성공 발화하기

**[S03-N087 · NEW] 제페토:** “Let me check everything.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 출발 전에 모자와 가방을 차분히 점검한다 / 감정: 돌보는 책임감  
**말하는 방식:** Let me check는 의심이 아니라 마지막으로 돌보는 말이다. everything을 길게 늘이지 않고 시선을 소품으로 옮긴다.  
**속도·쉼 계획:** 90단어/분, 에너지 2/5, 앞 180ms / 뒤 400ms. 강조: check everything. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Offer a final caring check, not a suspicious inspection; move the gaze across his things as the line settles.  
**피할 연기:** 아이의 작업을 믿지 못하는 심사 말투

**[S03-N088 · NEW] 피노키오:** “Red hat, little bag, and my book!”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 준비한 세 물건을 기쁘게 함께 확인한다 / 감정: 뿌듯하고 차분한 확인  
**말하는 방식:** red hat과 little bag을 실제로 한 번씩 만지고 my book에서는 가방을 가리킨다. 책을 꺼내지는 않는다.  
**속도·쉼 계획:** 105단어/분, 에너지 3/5, 앞 160ms / 뒤 380ms. 강조: Red hat · little bag · my book. Red hat, 뒤 140ms; little bag, 뒤 140ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Check the hat and bag with small touches, then indicate the book through the bag; make this a proud connected list, not a chant.  
**피할 연기:** 세 물건을 구호처럼 일정 박자로 외치기

**[S03-U019 · ORIGINAL #19] 제페토:** “Listen carefully, Pinocchio.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 중요한 등교와 귀가 약속을 말하기 전에 눈을 맞춘다 / 감정: 부드러운 진지함  
**말하는 방식:** Listen carefully는 목소리 크기 대신 속도를 낮춰 중요도를 낸다. Pinocchio를 다정히 부르며 아이의 주의를 받아 준다.  
**속도·쉼 계획:** 86단어/분, 에너지 2/5, 앞 260ms / 뒤 550ms. 강조: Listen carefully · Pinocchio. carefully, 뒤 180ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Lower the pace rather than raise the volume to gain his attention; address Pinocchio with gentle seriousness before the promise.  
**피할 연기:** 엄격한 벌칙을 예고하는 꾸중

**[S03-U020 · ORIGINAL #20] 제페토:** “Go to school and come home before supper.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 학교에 가고 저녁 전에 돌아오라는 핵심 약속을 분명히 전한다 / 감정: 보호하는 단단한 애정  
**말하는 방식:** Go to school을 한 뜻으로 분명히 말하고 and 뒤 귀가 부분은 따뜻하게 이어 간다. before supper에 기억할 시간의 무게를 둔다.  
**속도·쉼 계획:** 86단어/분, 에너지 2/5, 앞 220ms / 뒤 650ms. 강조: Go to school · come home · before supper. Go to school 뒤 250ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Give the school destination clearly, then turn warmly toward coming home; place memorable weight on before supper without threatening him.  
**피할 연기:** 위협하거나 노인 목소리를 거칠게 과장하기

### B10-C05 · 09:22–09:58 · NARRATIVE

**카메라:** 50mm 원테이크: 눈높이 투샷→착용하는 손을 포함한 3/4→두 얼굴→출구까지 후진하며 넓어지는 구도

**자율 행동·연출:** 36초 전체를 컷 전환 없는 한 테이크로 진행하되 같은 고정 와이드에서 낭독하지 않는다. S03-N089에서 피노키오는 제페토 눈을 보고 저녁 전 약속을 되새기며 닫힌 플랩을 한 번 확인한다. S03-N090 동안 카메라가 두 얼굴과 가방을 함께 보이는 3/4로 조금 이동한다. 피노키오가 기존 어깨끈을 직접 어깨에 걸고 제페토가 꼬임만 펴 주며 손/탁자→어깨 지지의 연속 이동을 가리지 않는다. S03-U021에서 카메라가 두 얼굴의 눈맞춤을 받아 피노키오의 단단한 대답과 고개 끄덕임을 보여 준다. S03-N091에서 피노키오는 가방 무게를 몸으로 받아 균형을 잡고 실내 출구를 한번 보았다가 제페토에게 시선을 돌린다. S03-N092 동안 제페토는 아이 눈높이에서 천천히 몸을 펴며 한 손을 가슴에 얹고, 피노키오는 칭찬을 들으며 작은 미소로 받는다. S03-U022의 마지막 원본 내레이션 동안 두 사람은 작업실 안의 출구 앞까지 몇 걸음 이동하고 카메라는 뒤로 움직여 발 접지·가방 착용·닫힌 실내 출입문을 함께 보여 준다. 모자 착용·책 든 가방·플랩 결속을 유지하며 실내문이나 집 앞 나무 대문을 열지 않는다. 발화 뒤 2초는 마지막 발을 놓고 잠시 잡던 어깨끈에서 손을 떼며 이동을 마치는 실제 동작이며 정지 화면을 유지하는 시간이 아니다.

**시간 배정:** 발화 전 행동 0.6초 / 발화 뒤 행동 2.0초. 대사·쉼·지정 행동 계획 합계 35.74초. 실제 합성 길이는 별도 확인.

**[S03-N089 · NEW] 피노키오:** “Before supper. I will remember.”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 저녁 전이라는 시간을 스스로 되뇌며 약속을 받아들인다 / 감정: 진지한 기억과 믿음  
**말하는 방식:** Before supper는 방금 들은 중요한 말을 자기 것으로 확인한다. I will remember는 작은 고개 끄덕임과 함께 조용히 단단하다.  
**속도·쉼 계획:** 98단어/분, 에너지 2/5, 앞 230ms / 뒤 500ms. 강조: Before supper · remember. Before supper. 뒤 330ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Repeat Before supper as you make the promise your own, then give I will remember a small, steady nod rather than a recitation.  
**피할 연기:** 시험 답안을 외워 읽는 기계적 반복

**[S03-N090 · NEW] 제페토:** “I will be waiting for you at home.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 돌아올 집과 기다리는 가족이 있음을 안심시킨다 / 감정: 가까운 애정  
**말하는 방식:** waiting for you는 오랜 할아버지의 편안한 온기로 말한다. at home에서 집의 안전함을 낮게 내려놓는다.  
**속도·쉼 계획:** 88단어/분, 에너지 2/5, 앞 220ms / 뒤 500ms. 강조: waiting for you · at home. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Offer the comfort of someone waiting for him; keep the elderly warmth close and settle at home into a safe, grounded ending.  
**피할 연기:** 떠나면 외롭다고 죄책감을 주는 슬픔

**[S03-U021 · ORIGINAL #21] 피노키오:** “I will, Grandpa!”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 제페토의 약속 요청에 원본 답으로 응한다 / 감정: 확신 있는 애정  
**말하는 방식:** I will은 짧게 단단하고 Grandpa에서 가까운 애정을 연다. 흥분 때문에 말끝을 날카롭게 치지 않는다.  
**속도·쉼 계획:** 103단어/분, 에너지 3/5, 앞 200ms / 뒤 450ms. 강조: I will · Grandpa. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Answer the promise firmly and briefly on I will, then warm Grandpa with affection; keep the certainty youthful and sincere.  
**피할 연기:** 장난스럽거나 건성으로 대답하기

**[S03-N091 · NEW] 피노키오:** “I want to learn so many things!”

**음성 연기:** PINOCCHIO_A → 제페토 / 의도: 준비와 약속을 마치고 배울 것에 다시 기대한다 / 감정: 책임을 품은 설렘  
**말하는 방식:** want to learn은 아까보다 조금 차분한 기대다. many things를 넓게 말하되 약속을 벌써 잊은 들뜸은 피한다.  
**속도·쉼 계획:** 108단어/분, 에너지 3/5, 앞 180ms / 뒤 400ms. 강조: learn · many things. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Return to excitement about learning, now grounded by the promise; widen many things without sounding as though you have forgotten Grandpa.  
**피할 연기:** 약속을 무시하고 뛰쳐나가는 과흥분

**[S03-N092 · NEW] 제페토:** “I am proud of your brave little heart.”

**음성 연기:** GEPPETTO_A → 피노키오 / 의도: 스스로 준비하고 약속한 아이를 인정한다 / 감정: 깊고 절제된 자부심  
**말하는 방식:** proud는 낮고 진실하게, brave little heart는 가까운 아이에게만 들려주는 애정으로 말한다. 달콤한 광고 문구처럼 부풀리지 않는다.  
**속도·쉼 계획:** 86단어/분, 에너지 2/5, 앞 240ms / 뒤 600ms. 강조: proud · brave little heart. 추가 내부 쉼 없음. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Let proud be low and sincere, then speak brave little heart privately to the child, with restrained grandfatherly affection.  
**피할 연기:** 과도하게 감상적인 울먹임이나 젊은 내레이터 톤

**[S03-U022 · ORIGINAL #22] 내레이션:** “With his red hat and little schoolbag, Pinocchio was ready for his first adventure outside.”

**음성 연기:** NARRATOR_A → 윤수와 시청자 / 의도: 준비된 모습과 바깥 모험의 시작을 관객에게 이어 준다 / 감정: 따뜻한 기대와 안정  
**말하는 방식:** 모자와 가방을 짚는 첫 구절은 눈앞의 장면을 담담히 받는다. 쉼 뒤 first adventure outside로 시선을 출구까지 넓히며 끝을 과하게 닫지 않는다.  
**속도·쉼 계획:** 108단어/분, 에너지 2/5, 앞 250ms / 뒤 650ms. 강조: red hat · little schoolbag · first adventure outside. little schoolbag, 뒤 320ms. 실제 음성 측정값 아님.  
**엔진 연기 지시(읽지 않음):** Observe the hat and schoolbag in a grounded adult voice; after the first phrase, widen toward the coming adventure as they approach the interior exit, without acting either character.  
**피할 연기:** 모든 등장인물을 대신 연기하거나 최종 엔딩처럼 웅장하게 닫기

## 실제 제작 상태

위 대사·연기·시간은 설계다. 실제 합성·청취·립싱크·VAD·영상 재생은 NOT_RUN이다. 귀뚜라미의 승인 참조 음색은 BLOCKED_RESOURCE이며 다른 성우로 대체하지 않는다.
