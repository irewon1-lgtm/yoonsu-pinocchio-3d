# S05 원본 보존과 V2.1 수정 내역

사용자가 검토 지적 수정과 문장별 음성 연기 작성을 요청한 범위다. 정본 두 파일과 1·2화 완료본은 변경하지 않는다. 실제 음성·렌더·립싱크는 NOT_RUN이다.

**수량:** 원본 18 + 신규 69 = 본편 87 발화. 별도 모델 예시10개. 10비트·50컷·10참여. **수정 후 본편 계획 472초(7:52)**, 실측값 아님.

## 원본 발화 1:1 매핑

|ID|화자|원본 영어|수정 컷|
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

## 참여10회와 예시

|ID|세 단어 모델|질문 ID|첫 재개 ID|본편 정지 경계|
|---|---|---|---|---|
|S05-P01|Cup your ears!|S05-N005|S05-N006|24초|
|I08|I hear music!|S05-U004|S05-U005|69초|
|S05-P02|Point to school!|S05-N016|S05-N017|114초|
|S05-P03|Duck your head!|S05-N023|S05-N024|156초|
|S05-P04|Move the leaves!|S05-N030|S05-N031|201초|
|I09|Look over there!|S05-U013|S05-U014|251초|
|S05-P05|Touch your bag!|S05-N042|S05-N043|301초|
|S05-P06|Let them through!|S05-N050|S05-N051|347초|
|S05-P07|Move your bag!|S05-N059|S05-N060|398초|
|S05-P08|Step back, please!|S05-N067|S05-N068|450초|

모델 예시는 첫 실행에서 질문 후 외부 시계로 한 번 들려준 뒤 입력을 받는다. 정확한 단어/발음 채점은 하지 않으며 부모 터치로 예시를 생략하고 진행할 수 있다. 예시 재생 중 마이크는 꺼지고 예시·WAIT는 본편 분량에 포함되지 않는다.

## 수정 근거

[기존 검토 보고서](../../reviews/S03_S05_REVIEW_2026-11-23.md)와 [수정·음성 지시 결과](../../docs/series_v2/S03_S05_CORRECTION_AND_VOICE_REPORT.md)를 함께 본다. 원본 대사 문구·화자·상대 순서는 그대로이며 변경된 신규 대사는 수정 기록에 별도로 적는다.

[각 대사의 음성 제작표](voice_direction_plan.json) · [캐릭터 음색 기준](../../docs/series_v2/VOICE_PERFORMANCE_BIBLE_V2_1.md)
