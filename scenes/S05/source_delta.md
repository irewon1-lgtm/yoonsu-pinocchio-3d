# S05 원본 보존과 V2 확장 내역

**상태: 상세 설계 작성 / 사용자 검토 필요. 원본 파일은 편집하지 않는다.**

## 보존한 정본

- `docs/series_v2/sources/01_STORY_MASTER_V1_1.md`의 장면 5, 원본 발화 18개.
- `docs/series_v2/sources/01_STEP2_PRODUCTION_STORYBOARD_SPEC.md`의 S05 9컷 베이스라인과 I08/I09의 질문 종료·반응·재개 계약.
- 원본 발화의 영어 텍스트·화자·상대 순서를 그대로 유지한다. 기존 9컷은 아래 50컷으로 확장되어도 사건 순서는 바뀌지 않는다.

## 원본 18문장 1:1 매핑

|원본 ID|화자|영어 대사|V2 컷|
|---|---|---|---|
|S05-U001|피노키오|“Cricket, what's that sound?”|B01-C01|
|S05-U002|귀뚜라미|“Listen carefully.”|B01-C01|
|S05-U003|귀뚜라미|“Yoonsu, can you hear it too?”|B02-C03|
|S05-U004|귀뚜라미|“What do you hear?”|B02-C03|
|S05-U005|귀뚜라미|“It's coming from the village square.”|B02-C04|
|S05-U006|피노키오|“Music! I love music!”|B02-C04|
|S05-U007|귀뚜라미|“But school is waiting.”|B03-C01|
|S05-U008|피노키오|“Just one little look!”|B03-C05|
|S05-U009|내레이션|“Pinocchio followed the sound.”|B04-C01|
|S05-U010|내레이션|“A bright red tent was hiding behind a big tree.”|B04-C05|
|S05-U011|피노키오|“I can hear the music, but where is it coming from?”|B06-C01|
|S05-U012|귀뚜라미|“Yoonsu can see the square.”|B06-C02|
|S05-U013|귀뚜라미|“Yoonsu, where should Pinocchio look?”|B06-C03|
|S05-U014|피노키오|“Wow! A puppet show!”|B06-C04|
|S05-U015|귀뚜라미|“Pinocchio, remember your promise.”|B07-C01|
|S05-U016|피노키오|“I know, I know.”|B07-C05|
|S05-U017|피노키오|“I'll only watch for a minute.”|B10-C01|
|S05-U018|내레이션|“But sometimes, one little minute can turn into a very long time.”|B10-C05|

## 원본 참여 2개 보존

|ID|질문 종료|목표|반응 순서|첫 재개|
|---|---|---|---|---|
|I08|U004 “What do you hear?”|I hear music!|귀뚜라미 귀 기울이기 → 피노키오 고개 돌리기 → 잎 움직이기|U005 “It's coming from the village square.”|
|I09|U013 “Yoonsu, where should Pinocchio look?”|Look over there!|카메라 팬 → 천막 등장 → 피노키오 눈 커짐|U014 “Wow! A puppet show!”|

두 이벤트의 질문과 재개 사이에는 신규 대사를 삽입하지 않는다. 원본 반응을 재생한 뒤 즉시 원본 후속 대사를 이어 간다. I08에서는 음악이 조금 또렷해지고, I09에서 빨간 천막과 움직이는 무대 인형을 최초로 공개한다.

## 신규 8개 참여와 인과

|ID|세 단어 예시|새 행동의 이유|
|---|---|---|
|S05-P01|Cup your ears!|4화의 미확인 소리를 같은 자리에서 받아, 걸음 소리를 멈추고 듣는 몸짓을 익힌다. 음악의 근원은 아직 가려 둔다.|
|S05-P02|Point to school!|학교가 목적지라는 사실을 다시 눈에 보이게 한 뒤 피노키오 스스로 잠깐 보겠다고 결정한다. 윤수에게 잘못된 길을 고르게 하지 않는다.|
|S05-P03|Duck your head!|음악을 향한 작은 우회가 실제 몸의 이동으로 보이게 한다. 낮은 가지 아래를 지나며 모자와 책가방을 스스로 지킨다.|
|S05-P04|Move the leaves!|세게 잡아당기지 않고 얼굴 옆 잎을 옮겨 지나갈 작은 공간을 만든다. 천막을 가린 주된 장애물은 큰 나무 줄기로 계속 남긴다.|
|S05-P05|Touch your bag!|원본 약속 경고를 추상적인 말로만 두지 않고 가방 속 책의 감촉과 연결한다. 피노키오는 목적을 몰라서가 아니라 알고도 망설인다.|
|S05-P06|Let them through!|광장 관객에게 접근하는 동선을 실제로 보여 주고, 자신의 발이 통로를 막고 있음을 알아차려 자리를 양보한다.|
|S05-P07|Move your bag!|새 공간에 들어왔어도 책을 잃거나 두고 가지 않는 연속성을 보장한다. 옆으로 튀어나온 가방을 몸 앞으로 옮겨 주변 관객을 배려한다.|
|S05-P08|Step back, please!|피노키오의 잠깐 보겠다는 원본 결정을 끝에 고정한다. 학교 약속을 아는 채 머무는 선택이 6화의 오래 머무름으로 이어지게 한다.|

신규 발화는 69문장이다. 모두 상세 JSON과 대본에 `NEW`/`신규`로 표시하며 승인된 원본으로 가장하지 않는다. 예시 음성 10개는 선택형 참여 보조 자료이고 정상 본편 발화 수에 포함하지 않는다.

## 연결을 위해 정한 해석과 경계

1. **S04→S05:** 같은 귀 기울이기 행동과 미확인 소리를 잇는다. 새 아침·새 길로 재시작하지 않으며 학교 지붕과 모자·가방·책·마른 신발·정상 코를 유지한다.
2. **가려진 무대:** 낮은 가지 아래로 지나고 통로 옆 잎을 움직여도 큰 줄기는 천막 전면을 계속 가린다. I09의 발견을 선점하지 않는다.
3. **움직이는 인형과 닫힌 커튼 양립:** I09에서 원본이 요구하는 움직이는 무대 인형 둘은 닫힌 본커튼 앞턱의 짧은 맛보기로 보인다. 이름과 대사가 없고 옆 가림판으로 물러난다. S06의 본커튼 개방, 핍의 첫 소개와 구조를 앞당기지 않는다. 이 배치 해석 역시 새 설계이므로 사용자 검토 대상이다.
4. **학교 약속과 자율 선택:** 손에 닿는 가방 속 책으로 약속을 상기한다. 윤수의 참여가 잘못된 길을 고르도록 하지 않는다. 피노키오가 “Just one little look!”과 “I'll only watch for a minute.”를 말하며 스스로 머문다.
5. **S05→S06:** 안전한 관객 자리까지 실제 동선으로 이동하고 가방을 몸 앞에 둔다. 닫힌 본커튼·무대 왼쪽 마라·북소리·옆 귀뚜라미를 이어받는다. S05 마지막 발화는 U018, S06 첫 발화는 마라의 “Welcome, everyone!”이다. 시간 경과와 본공연은 S06에서만 진행한다.

## 분량과 검증 범위

본편 계획은 432초, 10비트, 50컷이다. 각 C03 질문 종료 경계에서 외부 대기를 시작하고 C04로 재개하므로 대기·예시·재시도·반복은 이 시간에 포함되지 않는다. 실제 음성과 움직임이 아직 없으므로 실제 432초, 최종 360초 이상, 리그·접촉·립싱크·VAD·영상 경계 연결은 NOT_RUN이다. 귀뚜라미 승인 음원은 BLOCKED_RESOURCE이며 목소리 대체는 하지 않는다.
