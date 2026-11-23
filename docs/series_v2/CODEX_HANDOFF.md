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
