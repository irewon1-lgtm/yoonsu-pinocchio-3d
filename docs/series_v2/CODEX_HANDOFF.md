# Codex 실행 인계 V2.1 — 설계는 ChatGPT / 구현은 Codex

**S02 상세 제작 설계는 ChatGPT가 직접 작성 완료했습니다.** Codex가 스토리·신규 영어 대사·윤수 참여 횟수나 카메라/동작을 새로 설계해서는 안 됩니다.

## 음성 자료 연결
- 승인 성우 4개 V6 MP3는 이제 이 브랜치의 `assets/voice_refs/v6/`에 **직접 존재**한다. [상세 경로·SHA·Nano 생성 안내](S02_APPROVED_VOICES.md)를 참고하라.
- `python3 scripts/s02_approved_voice_tts.py` 기본 실행은 정합성 확인 전용. 실제 합성은 `--synthesize --limit 3`로 샘플부터 비교한다. `downloads/s01-complete/S01_V7_VOICES.zip`은 이전 S01의 26개 고정 음성 **비교 기준**으로 보존한다.

## 최신 S02 설계 파일 (읽기 필수)
- `scenes/S02/script_v2_draft.md` — 7분 23초 목표, 신규 81문장+원본 21문장, 대사/동작·카메라 50컷
- `scenes/S02/scene_design_v2.json` — 상세 대사·연기·컷 시간표의 기계 판독 설계
- `scenes/S02/interaction_map_v2.json` — 윤수 참여 10회(신규 9+원본 I02 1), WAIT/REACT/보호자 터치
- `scenes/S02/source_delta.md` — 기존 V1.1 대사 순서 21/21 보존
- `scenes/S02/QA_G0_G1.md` — PASS/REVIEW_REQUIRED/NOT_RUN

## 즉시 실행 가능: 읽기 전용 자료/설계 검증
```bash
git fetch origin
git switch s01/full-story-production
git pull --ff-only origin s01/full-story-production
python3 scripts/validate_series_v2.py
python3 scripts/validate_s02_design.py
```

### 사용자 검토 전 상태
- G1 ChatGPT 상세 설계: **DESIGN_COMPLETE / REVIEW_REQUIRED**. 사용자 대본 승인 전.
- Codex가 할 수 있는 일: 원본/기존 S01 파일 보존 점검, 설계 무결성 검사, 3D 엔진/리그 기술적 실현 가능성 읽기 전용 검토 및 불가사항 문서 보고.
- Codex가 해서는 안 되는 일: 새 이야기 쓰기, 임의로 대사/컷/10회 이벤트 변경, 6분 요구를 정지 컷·반복으로 채우기, 승인 없이 G2~G6 제작 진행.

## 사용자가 S02 대본을 승인한 후 Codex에 전달할 실행 지시
> `scenes/S02/script_v2_draft.md`와 `scene_design_v2.json`을 제작 정본으로 삼아 **대사를 다시 작성하지 말고 실제 3D 영상으로 구현**하라. 피노키오·제페토의 눈빛·관절·손가락·발 접지·첫걸음 및 쿠션 착지·손잡기·다시 서기·숨기·첫 손 흔들기를 독립 애니메이션으로 제작한다. 50컷과 윤수 참여 총 10회를 정확히 구현하고, 기존 I02와 원본 대사 21개·상대 순서를 보존하라. 기준 443초는 설계 예상이므로 최종 MP4가 **실제 최소 360초**이고 WAIT/반복을 제외해도 그렇다는 사실을 ffprobe 및 에디트 목록으로 입증하라. 기존 S01을 수정하거나 삭제하지 마라. 모든 제작물·로그·SHA 및 회귀 검사 결과는 원본과 별도 경로에 저장하라. 기술적 불가/리소스 결손은 BLOCKED_RESOURCE로 보고하고 작가 승인 없는 축약·내용 변경을 하지 마라.

## 필수 게이트
- G0 원본 SHA 확인 → G1 사용자 상세 대본 승인 → G2 카메라 좌표/콘티 → G3 동작 시연 → G4 영상/음성 → G5 기술 QA·시각 검증 → G6 MP4/Blender/타임라인/로그 인계.
- S01은 기존 완료분 그대로 보호. S03~S12도 각 장면의 상세 설계는 ChatGPT가 작성한 뒤 Codex가 구현한다.

## S03 설계도 ChatGPT가 직접 작성 (2026-11-23)
- [S03 상세 대본](../../scenes/S03/script_v2_draft.md), [S03 구조화 설계](../../scenes/S03/scene_design_v2.json), [S03 베이스 엔진 호환성](S03_ENGINE_HANDOFF.md).
- Codex는 S03 새 대본 작성 금지. **S03 456초/50컷/10회(원본 I03·I04 포함)** 설계만 구현한다. `python3 scripts/validate_s03_design.py` 를 실행한다.
- S02 실제 구현 엔진은 현재 브랜치에 없고 설계 데이터만 존재. S02 `scene_design_v2.json` 스키마와 승인 성우·기존 S01 Blender를 참조한다. 엔진 미구현분은 구현 계획으로 보고하되 승인 없는 대사·장면·참여 변경 금지.
- S02 설계는 여전히 REVIEW_REQUIRED; S01/S02 원본 파일 삭제/수정 금지.

## S04 — ChatGPT 직접 제작 설계 (S02 데이터 엔진 계승)
- **정본 설계:** `scenes/S04/script_v2_draft.md`(479초 목표·50컷·기존 32문장+신규 77문장) / `scenes/S04/scene_design_v2.json` / `scenes/S04/interaction_map_v2.json`.
- 원본 I05/I06/I07를 포함해 윤수 참여 10회. 데이터 구조는 S02/S03 호환. 새 이야기 창작은 Codex 업무가 아니며, 설계의 3D 구현·검증만 한다.
- `docs/series_v2/S04_ENGINE_HANDOFF.md`에서 3화→4화 소품 연속성과 2화 베이스 스키마를 확인. S02 실제 Blender 엔진은 없으므로 `NOT_RUN` 상태 유지.
- **귀뚜라미 승인 성우가 미확보:** `BLOCKED_RESOURCE`. 기존 승인 성우로 바꾸지 말고 다른 캐릭터의 소리 합성과 캐릭터/카메라 연기 작업만 계속 가능(각 장면 G1 사용자 승인 이후).
- 검증 명령: `python3 scripts/validate_s04_design.py` 및 `python3 scripts/s04_approved_voice_tts.py` (기본 실행은 합성 없음).
- **S02, S03, S04 상세 신규 대본은 모두 REVIEW_REQUIRED.** 사용자 승인 전 G2 이상 제작을 자동으로 완료 처리하지 않는다.

## S05 — 4화의 음악에서 6화의 인형극으로 이어지는 상세 설계

- 정본 설계: [S05 전체 대본](../../scenes/S05/script_v2_draft.md), [구조화 설계](../../scenes/S05/scene_design_v2.json), [10회 참여](../../scenes/S05/interaction_map_v2.json), [S05 구현 인계](S05_ENGINE_HANDOFF.md).
- 432초 목표 / 50컷 / 원본 18줄 보존 / 원본 I08·I09 + 신규 8회. 모든 발화는 한 개의 컷에 배정된다. WAIT·예시 재생은 컷 사이 본편 시계 밖이며 분량에 넣지 않는다.
- [12장면 연결표](STORY_CONTINUITY_S01_S12.md)와 [구조화 연결 계약](STORY_CONTINUITY_S01_S12.json)을 함께 읽는다. 4화 마지막 미확인 소리·소품·동작을 그대로 받아 시작하고, 6화 첫 북소리와 닫힌 본무대 커튼에 이어진다. 6화의 커튼 개방·핍 소개·구조를 5화에서 먼저 실행하지 않는다.
- `python3 scripts/validate_s05_design.py`, `python3 scripts/validate_story_continuity.py`, `python3 scripts/s05_voice_preflight.py`를 실행한다. 첫 두 명령은 설계 자료 검증이며 마지막 명령은 승인 참조 음성과 캐스트 배정 검사다. 실제 음성 합성은 하지 않는다. `--require-ready`에서는 귀뚜라미 승인 음성 미확보로 종료 코드 2를 반환한다.
- S02 기반은 **설계 데이터 계약**이다. 실제 실행 엔진·S05 영상·음성·장치 작동은 NOT_RUN. S02~S05는 모두 G1 REVIEW_REQUIRED. 이 연결 설계는 G1 이후 승인 절차를 대체하지 않는다.
