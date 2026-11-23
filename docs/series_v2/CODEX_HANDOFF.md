# Codex 현재 인계 V2.1 — 3·4·5화 수정과 대사 연기

**1·2화는 사용자 완료 선언에 따라 보존한다.** 현재 요청은 3·4·5화 검토 지적 수정과 모든 대사의 목소리·감정·말투·속도·쉼 지시다. 2화 제작부터 다시 시작하지 않는다.

## 먼저 읽기

1. [음성 제작 실행 지시](CODEX_VOICE_ACTING_HANDOFF.md)
2. [전체 캐릭터 음색·연기 기준](VOICE_PERFORMANCE_BIBLE_V2_1.md)
3. [3화 대본](../../scenes/S03/script_v2_draft.md), [4화 대본](../../scenes/S04/script_v2_draft.md), [5화 대본](../../scenes/S05/script_v2_draft.md)
4. 각 화 `scene_design_v2.json`, `interaction_map_v2.json`, `voice_direction_plan.json`, `voice_direction_sheet.csv`
5. [12장면 연결 인계](STORY_CONTINUITY_S01_S12.md)

## 유지할 조건

- 승인 성우는 내레이션 A·피노키오 A·제페토 A·파란 요정 C다. 원본 MP3와 참조 SHA를 바꾸지 않는다.
- 귀뚜라미·마라·핍은 음색·연기 방향이 작성됐지만 승인 참조가 없다. 다른 성우로 대체하지 않는다.
- 2화 기본 데이터 계약을 유지한다. 실제 실행 엔진 접근 여부를 이유로 완료본을 다시 만들지 않는다.
- 3~5화 각50컷·10참여와 원본72발화를 보존한다. 수정 후 시간은 각 JSON의 최신 값을 따른다. 이전456/479/432초에 음성을 억지로 맞추지 않는다.
- `text/spoken_text`만 읽고 연기 지시는 실제 지원 기능에 전달한다. 지시문을 읽게 하거나 중립 합성으로 대체하지 않는다.
- 질문 뒤 본편 밖에서 첫 모델 예시를 들려주고 예시 종료 후 입력을 받는다. 예시 중 마이크 OFF, 발음 채점 금지, 보호자 터치 진행 가능.
- 이전 S03/S04의 text+reference 단독 `--synthesize`는 지시를 무시하므로 차단된다. 기본 검사와 `--export-jobs`는 가능하다. 실제 합성 어댑터는 엔진 지원 기능을 확인해 연결한다.

## 검사

```bash
python3 scripts/voice_direction_tools.py validate --scenes S03 S04 S05
python3 scripts/validate_story_continuity.py
python3 scripts/s03_approved_voice_tts.py
python3 scripts/s04_approved_voice_tts.py
python3 scripts/s05_voice_preflight.py
```

이는 설계·원본·참조·제작표 검사다. 실제 합성·청취·립싱크·영상·기기는 증거 전 NOT_RUN, 새 성우는 BLOCKED_RESOURCE다. 사용자 요청에 따른 수정과 지시 작성 완료를 음색·영상 승인과 혼동하지 않는다.
