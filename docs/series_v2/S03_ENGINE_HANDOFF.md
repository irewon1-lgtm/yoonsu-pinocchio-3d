# S03 구현 인계 V2.1 — 수정 대본과 음성 연기

**현재 범위:** 사용자 요청에 따른 오류 수정·각 대사 연기 지시. 실제 영상·음성 제작 완료가 아니다. 1·2화 완료본은 보존한다.

## 자료와 수량

- [대본](../../scenes/S03/script_v2_draft.md), [설계 JSON](../../scenes/S03/scene_design_v2.json), [참여 맵](../../scenes/S03/interaction_map_v2.json).
- 10비트·50컷·10참여 / 본편 114발화 / 모델 예시10개 / 계획 598초(9:58). 대기·모델·재시도는 본편 시계 밖. 실측 길이 NOT_RUN.
- [문장별 제작표](../../scenes/S03/voice_direction_plan.json), [CSV](../../scenes/S03/voice_direction_sheet.csv), [캐릭터 목소리 기준](VOICE_PERFORMANCE_BIBLE_V2_1.md), [Codex 음성 제작 실행 지시](CODEX_VOICE_ACTING_HANDOFF.md).

## 이번 수정의 연출 경계

책을 넣은 뒤 결과를 말하고, 모자를 찾기 전 인물의 정답 인지를 앞당기지 않는다. 마지막 약속은 여러 컷에 분배하며 가방 메기와 실내 출구 이동을 원본 내레이션 중 보여 준다. 작업실 문과 집 앞 대문은 구분한다.

## 구현 계약

1. S02 기본 데이터 필드를 유지한다. 실제 2화 실행 엔진 접근 여부를 이유로 사용자 완료본을 다시 만들지 않는다. 원본·승인 음원은 읽기 전용으로 재사용한다.
2. 각 컷 `dialogue_ids`를 순서대로 한 번만 재생한다. 문장별 `voice_direction`을 적용하고 영어 `text`만 읽는다. 지시문·화자명·문맥은 발화하지 않는다.
3. 질문 끝에서 외부 정지 → 첫 모델 예시1회(마이크 OFF) → 예시 끝에서 VAD/보호자 터치 → 반응 완료 → 지정 첫 재개 대사. 부모는 모델을 건너뛰고 진행할 수 있다.
4. `action_lead_seconds`, 대사·쉼, `between_dialogue_actions`, `action_tail_seconds`로 서사 시간을 나눈다. `before_dialogue_actions`는 lead에 포함하며 다시 더하지 않는다. 실제 음성을 측정한 뒤 필요한 컷만 다시 배정한다.
5. 승인 음색 정체성을 유지한다. 귀뚜라미 참조는 미확보이며 다른 캐릭터로 대체하지 않는다. 감정 지시가 엔진에 전달되지 않은 text+reference 합성으로 완료 처리하지 않는다.
6. 360초 이상 본편, 실제 음색·연기·립싱크·접촉·VAD·장면 경계는 실제 제작물로 확인한다. 현재는 NOT_RUN이다.

## 확인 명령

```bash
python3 scripts/validate_s03_design.py
python3 scripts/voice_direction_tools.py validate --scenes S03
```

수정·음성 지시의 작성 완료를 최종 음색 승인이나 영상 완성으로 표시하지 않는다.
