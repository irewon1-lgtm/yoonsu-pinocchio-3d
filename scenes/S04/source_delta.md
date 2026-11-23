# S04 원본 보존과 V2.1 수정 내역

사용자가 검토 지적 수정과 문장별 음성 연기 작성을 요청한 범위다. 정본 두 파일과 1·2화 완료본은 변경하지 않는다. 실제 음성·렌더·립싱크는 NOT_RUN이다.

**수량:** 원본 32 + 신규 77 = 본편 109 발화. 별도 모델 예시10개. 10비트·50컷·10참여. **수정 후 본편 계획 527초(8:47)**, 실측값 아님.

## 원본 발화 1:1 매핑

|ID|화자|원본 영어|수정 컷|
|---|---|---|---|
|S04-U001|제페토|“Here we are.”|B01-C01|
|S04-U002|제페토|“This road will take you to school.”|B01-C01|
|S04-U003|피노키오|“Everything looks so big!”|B01-C01|
|S04-U004|제페토|“And everything is new to you.”|B01-C01|
|S04-U005|피노키오|“Grandpa, what should I do first?”|B02-C02|
|S04-U006|제페토|“Let's ask our little friend.”|B02-C02|
|S04-U007|제페토|“Yoonsu, where should Pinocchio go today?”|B02-C03|
|S04-U008|피노키오|“Goodbye, Grandpa!”|B02-C04|
|S04-U009|제페토|“Have a lovely day!”|B02-C04|
|S04-U010|내레이션|“Pinocchio walked along the sunny road.”|B03-C01|
|S04-U011|내레이션|“He saw flowers, butterflies, and little houses.”|B03-C01|
|S04-U012|내레이션|“Then he came to two different paths.”|B04-C01|
|S04-U013|피노키오|“Oh dear!”|B04-C02|
|S04-U014|피노키오|“Which way should I go?”|B04-C02|
|S04-U015|귀뚜라미|“Good morning, Pinocchio!”|B05-C01|
|S04-U016|피노키오|“A talking cricket?”|B05-C01|
|S04-U017|귀뚜라미|“Yes! And I know these roads.”|B05-C02|
|S04-U018|귀뚜라미|“Look at the sign.”|B05-C02|
|S04-U019|피노키오|“Yoonsu, which way should I go?”|B06-C03|
|S04-U020|피노키오|“That's the school!”|B06-C04|
|S04-U021|귀뚜라미|“Keep walking.”|B06-C04|
|S04-U022|내레이션|“Pinocchio followed the little road.”|B07-C01|
|S04-U023|내레이션|“But after a while, a big puddle blocked his way.”|B08-C01|
|S04-U024|피노키오|“Oh no! My new shoes!”|B08-C02|
|S04-U025|귀뚜라미|“There's a way across.”|B08-C05|
|S04-U026|피노키오|“I don't want wet feet.”|B08-C05|
|S04-U027|피노키오|“Yoonsu, how can I cross this puddle?”|B09-C03|
|S04-U028|피노키오|“I did it!”|B09-C04|
|S04-U029|귀뚜라미|“Those are some strong wooden legs!”|B09-C04|
|S04-U030|내레이션|“Pinocchio continued down the road.”|B10-C01|
|S04-U031|내레이션|“He was getting closer to school.”|B10-C01|
|S04-U032|내레이션|“But then, he heard a strange and wonderful sound.”|B10-C05|

## 참여10회와 예시

|ID|세 단어 모델|질문 ID|첫 재개 ID|본편 정지 경계|
|---|---|---|---|---|
|S04-P01|Look over there!|S04-N005|S04-N006|41초|
|I05|Go to school!|S04-U007|S04-U008|95초|
|S04-P02|Watch the flower!|S04-N018|S04-N019|143초|
|S04-P03|Stop and look!|S04-N026|S04-N027|194초|
|S04-P04|Find firm ground!|S04-N034|S04-N035|249초|
|I06|Follow that sign!|S04-U019|S04-U020|284초|
|S04-P05|Hold your bag!|S04-N049|S04-N050|337초|
|S04-P06|Watch the frog!|S04-N059|S04-N060|395초|
|I07|Jump over it!|S04-U027|S04-U028|443초|
|S04-P07|Look far ahead!|S04-N073|S04-N074|499초|

모델 예시는 첫 실행에서 질문 후 외부 시계로 한 번 들려준 뒤 입력을 받는다. 정확한 단어/발음 채점은 하지 않으며 부모 터치로 예시를 생략하고 진행할 수 있다. 예시 재생 중 마이크는 꺼지고 예시·WAIT는 본편 분량에 포함되지 않는다.

## 수정 근거

[기존 검토 보고서](../../reviews/S03_S05_REVIEW_2026-11-23.md)와 [수정·음성 지시 결과](../../docs/series_v2/S03_S05_CORRECTION_AND_VOICE_REPORT.md)를 함께 본다. 원본 대사 문구·화자·상대 순서는 그대로이며 변경된 신규 대사는 수정 기록에 별도로 적는다.

[각 대사의 음성 제작표](voice_direction_plan.json) · [캐릭터 음색 기준](../../docs/series_v2/VOICE_PERFORMANCE_BIBLE_V2_1.md)
