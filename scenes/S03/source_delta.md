# S03 원본 보존과 V2.1 수정 내역

사용자가 검토 지적 수정과 문장별 음성 연기 작성을 요청한 범위다. 정본 두 파일과 1·2화 완료본은 변경하지 않는다. 실제 음성·렌더·립싱크는 NOT_RUN이다.

**수량:** 원본 22 + 신규 92 = 본편 114 발화. 별도 모델 예시10개. 10비트·50컷·10참여. **수정 후 본편 계획 598초(9:58)**, 실측값 아님.

## 원본 발화 1:1 매핑

|ID|화자|원본 영어|수정 컷|
|---|---|---|---|
|S03-U001|제페토|“Today is your first day at school!”|B01-C01|
|S03-U002|피노키오|“School?”|B01-C01|
|S03-U003|제페토|“Yes! You'll meet new friends.”|B01-C01|
|S03-U004|제페토|“And you'll learn many wonderful things.”|B01-C01|
|S03-U005|피노키오|“That sounds exciting!”|B03-C01|
|S03-U006|피노키오|“Can I wear my new hat?”|B03-C01|
|S03-U007|제페토|“Of course.”|B03-C01|
|S03-U008|제페토|“Now, where did I put that red hat?”|B03-C01|
|S03-U009|피노키오|“It's not here!”|B04-C04|
|S03-U010|제페토|“Hmm. Yoonsu can see the whole room.”|B06-C02|
|S03-U011|제페토|“Yoonsu, where is Pinocchio's hat?”|B06-C03|
|S03-U012|제페토|“Ah! Here it is!”|B06-C04|
|S03-U013|피노키오|“My red hat!”|B06-C04|
|S03-U014|피노키오|“Grandpa, this is tricky.”|B07-C05|
|S03-U015|제페토|“You're still learning.”|B07-C05|
|S03-U016|피노키오|“Yoonsu, what should I do with my hat?”|B08-C03|
|S03-U017|피노키오|“Now I'm ready!”|B08-C04|
|S03-U018|제페토|“Almost. Don't forget your schoolbag.”|B08-C04|
|S03-U019|제페토|“Listen carefully, Pinocchio.”|B10-C04|
|S03-U020|제페토|“Go to school and come home before supper.”|B10-C04|
|S03-U021|피노키오|“I will, Grandpa!”|B10-C05|
|S03-U022|내레이션|“With his red hat and little schoolbag, Pinocchio was ready for his first adventure outside.”|B10-C05|

## 참여10회와 예시

|ID|세 단어 모델|질문 ID|첫 재개 ID|본편 정지 경계|
|---|---|---|---|---|
|S03-P01|Turn the page!|S03-N006|S03-N007|46초|
|S03-P02|Put it here!|S03-N016|S03-N017|106초|
|S03-P03|Touch your head!|S03-N025|S03-N026|169초|
|S03-P04|Open the drawer!|S03-N034|S03-N035|215초|
|S03-P05|Lift the book!|S03-N044|S03-N045|270초|
|I03|Under the chair!|S03-U011|S03-U012|317초|
|S03-P06|Hold it up!|S03-N060|S03-N061|374초|
|I04|Put it on!|S03-U016|S03-U017|420초|
|S03-P07|Open the bag!|S03-N075|S03-N076|481초|
|S03-P08|Tie the strap!|S03-N085|S03-N086|534초|

모델 예시는 첫 실행에서 질문 후 외부 시계로 한 번 들려준 뒤 입력을 받는다. 정확한 단어/발음 채점은 하지 않으며 부모 터치로 예시를 생략하고 진행할 수 있다. 예시 재생 중 마이크는 꺼지고 예시·WAIT는 본편 분량에 포함되지 않는다.

## 수정 근거

[기존 검토 보고서](../../reviews/S03_S05_REVIEW_2026-11-23.md)와 [수정·음성 지시 결과](../../docs/series_v2/S03_S05_CORRECTION_AND_VOICE_REPORT.md)를 함께 본다. 원본 대사 문구·화자·상대 순서는 그대로이며 변경된 신규 대사는 수정 기록에 별도로 적는다.

[각 대사의 음성 제작표](voice_direction_plan.json) · [캐릭터 음색 기준](../../docs/series_v2/VOICE_PERFORMANCE_BIBLE_V2_1.md)
