# S03 — S02 베이스 제작 엔진 호환/인계

**정확한 현황:** `scenes/S02/scene_design_v2.json`, `interaction_map_v2.json`, 50컷/10회 설계와 성우 재사용 도구는 확인됨. GitHub에는 **S02 완성 .blend/영상/실제 3D 런타임 코드가 확인되지 않음**. 따라서 '2화 엔진 재사용'은 우선 **JSON 스키마·연출 컨트롤러 계약·성우 기준·3D 리그 후보 사용**을 뜻하며, 존재하지 않는 구현을 만들었다고 표시하지 않는다.

## 코드/자산 상속 관계
| 재사용 항목 | S02 경로/상태 | S03 접근 |
|---|---|---|
| 비트/샷 스키마 | `scenes/S02/scene_design_v2.json` 설계 완료 | `scenes/S03/scene_design_v2.json` 호환 |
| WAIT/REACT 입력 | `scenes/S02/interaction_map_v2.json` 설계 완료 | 원본 I03·I04 포함 10회 |
| 캐릭터/카메라 연기 | S02 50컷 리그 동작 설계만 확인 | S02 rig 실물이 있으면 재사용, 없으면 S01 Blender 기본 자산 조사 후 새로 구현 |
| 승인 성우 참조 | `assets/voice_refs/v6/` 실파일 존재 | `scripts/s03_approved_voice_tts.py` 신규 대사 샘플 합성·검증 |
| S01 참조 영상/블렌더 | `downloads/s01-complete/` | 읽기전용/원본 보존 |

## S03 제작 단계
1. S02 아침 작업실·캐릭터 크기·햇살/카메라 설정·애니메이션 레이어의 실물 존재를 확인한다. 없으면 `BLOCKED_RESOURCE`를 기록하고 S01 Blender를 복원한 **새 S03 소스**를 만든다.
2. 새 대사를 작성하지 말고 `scenes/S03/script_v2_draft.md`와 `scene_design_v2.json`에 정의된 영어 문장·50컷·456초 목표를 그대로 사용한다.
3. 캐릭터 실물 리깅은 2화 기준의 발·손·시선·표정과 상호운용되도록. 신규 소품별 상태(모자 의자 아래, 책 탁자, 모자 머리, 가방) 트래커 필수.
4. 10개 이벤트별 `PROMPT_AUDIO_END → WAIT → (VAD_END | PARENT_TAP) → REACT_ONCE → RESUME` 로직을 적용하고 원본 I03/I04의 trigger/cue/resume를 바꾸지 않는다.
5. 새 합성 음성은 **검수용 preview**부터. 기존 V7과 청감 비교 후 캐릭터별 음색 통일. 이전 승인 음원을 덮어쓰지 않는다.
6. 사용자 상세 설계 검토 이후 G2+ 본편 제작을 진행한다. 구현 QA에는 ffprobe, 50컷 단절 여부, 10번 참여, 원본 22줄, 음성/자막/오디오, 소품 위치 및 품질 시각 검수를 포함한다.

## 참조/추가 파일
- `scenes/S03/script_v2_draft.md`: 사람이 읽는 전체 상세 제작 대본
- `scenes/S03/scene_design_v2.json`: 기계 판독 설계
- `scenes/S03/interaction_map_v2.json`: 10회 WAIT/REACT
- `scenes/S03/source_delta.md`: 원본 문장 대조
- `scenes/S03/QA_G0_G1.md`: 게이트 현황
- `scripts/validate_s03_design.py`: 무결성 검사
- `scripts/s03_approved_voice_tts.py`: S02 성우 합성 방법을 복제한 S03용 샘플 생성 도구
