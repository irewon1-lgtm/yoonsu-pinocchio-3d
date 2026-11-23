# yoonsu-pinocchio-3d

## 현재 작업 상태 — S03~S05 수정 및 문장별 음성 연기 설계

이 프로젝트는 **12장면으로 이어지는 하나의 이야기**다. 현재 작업은 3·4·5화의 검토 지적을 수정하고, **본편 310개 발화와 참여 예시 30개 전체에 캐릭터별 음성 연기 지시를 작성한 V2.1 수정본**이다.

**S01·S02는 `USER_COMPLETED_PRESERVED`다.** 사용자가 완료한 두 장면의 본편·음원·기존 자산은 보존하며 이번 작업에서 재제작하거나 제작 검사를 다시 실행하지 않는다. 현재 다음 구현 안내는 [Codex 음성 연기 인계](docs/series_v2/CODEX_VOICE_ACTING_HANDOFF.md)다.

| 장면 | 대기 제외 본편 계획 | 본편 발화 | 참여 예시 | 컷 / 참여 |
|---|---:|---:|---:|---:|
| [S03 상세 대본](scenes/S03/script_v2_draft.md) | 598초 · 9분 58초 | 114개 | 10개 | 50컷 / 10회 |
| [S04 상세 대본](scenes/S04/script_v2_draft.md) | 527초 · 8분 47초 | 109개 | 10개 | 50컷 / 10회 |
| [S05 상세 대본](scenes/S05/script_v2_draft.md) | 472초 · 7분 52초 | 87개 | 10개 | 50컷 / 10회 |
| **합계** | **각 장면의 계획값** | **310개** | **30개** | **150컷 / 30회** |

위 시간은 문장별 계획 말속도·쉼·실제 행동을 컷에 배정한 **`PLANNED_NOT_MEASURED`** 값이다. WAIT·예시·반복은 본편 시계 밖에 둔다. 현재 검사 결과는 **`DIRECTED_DESIGN_PASS_ONLY`**이며 실제 음성 합성·청감 승인·립싱크·MP4·장치 QA는 **`NOT_RUN`**이다. 장면의 상세 설계 상태는 `G1_DESIGN_COMPLETE_REVIEW_REQUIRED`로 유지한다.

## 작업 브랜치와 현재 읽을 자료

작업 브랜치는 **`s01/full-story-production`**이다. 이 브랜치에는 보존할 S01 완성 영상·Blender 프로젝트, V1.1 정본 대본·콘티, 장면별 설계와 현재 수정 자료가 함께 있다.

```bash
git fetch origin
git switch s01/full-story-production
```

- [현재 수정·음성 설계 보고서](docs/series_v2/S03_S05_CORRECTION_AND_VOICE_REPORT.md)
- [Codex 음성 연기 구현 인계](docs/series_v2/CODEX_VOICE_ACTING_HANDOFF.md)
- [7명 캐릭터 목소리·연기 기준](docs/series_v2/VOICE_PERFORMANCE_BIBLE_V2_1.md)
- [현재 검증 범위와 실행 안내](docs/series_v2/VALIDATION.md) · [실행된 설계 검사 및 반례 결과](docs/series_v2/VOICE_DIRECTION_VALIDATION_2026-11-23.json)
- [12장면 연결표](docs/series_v2/STORY_CONTINUITY_S01_S12.md) · [연결 상태 JSON](docs/series_v2/STORY_CONTINUITY_S01_S12.json)
- [공통 제작 기준](docs/series_v2/PRODUCTION_PRD_V2_0.md) · [장면별 상태](docs/series_v2/series_manifest_v2.json)

각 장면의 영어 대사와 `voice_direction`은 `scene_design_v2.json`, 질문·예시·입력·재개 계약은 `interaction_map_v2.json`에 있다. 읽기용 대본과 음성 작업표는 이 JSON에 맞춰 동기화한다.

| 장면 | 설계 정본 | 참여 맵 | 본편·예시 음성 작업표 |
|---|---|---|---|
| S03 | [scene_design_v2.json](scenes/S03/scene_design_v2.json) | [interaction_map_v2.json](scenes/S03/interaction_map_v2.json) | [voice_direction_plan.json](scenes/S03/voice_direction_plan.json) |
| S04 | [scene_design_v2.json](scenes/S04/scene_design_v2.json) | [interaction_map_v2.json](scenes/S04/interaction_map_v2.json) | [voice_direction_plan.json](scenes/S04/voice_direction_plan.json) |
| S05 | [scene_design_v2.json](scenes/S05/scene_design_v2.json) | [interaction_map_v2.json](scenes/S05/interaction_map_v2.json) | [voice_direction_plan.json](scenes/S05/voice_direction_plan.json) |

## 캐릭터 목소리와 실제 합성의 경계

7명 발화 캐릭터 중 **피노키오·제페토·내레이션·파란 요정 4명은 기존 승인 참조를 유지**한다. **귀뚜라미·마라·핍 3명은 연기 프로필을 작성했으나 승인 음색 참조는 아직 없다.** 현재 S04·S05에서 발화하는 귀뚜라미는 `BLOCKED_RESOURCE`이며 다른 캐릭터의 음성으로 대체하지 않는다.

모든 본편 발화와 예시에 상대·의도·감정·한국어/영어 연기 지시·속도·강세·쉼을 작성했다. 실제로 읽는 것은 영어 `spoken_text`뿐이며, 연기 지시와 앞뒤 문맥은 발화에 섞지 않는다. 제페토의 노년 음색과 피노키오의 소년 음색 등 승인된 화자 정체성은 감정에 따라 바꾸지 않는다.

**문장별 지시를 실제 엔진의 지원 기능에 전달하는 어댑터는 아직 구현되지 않았다.** 이전의 대사+참조만 전달하는 `--synthesize` 경로는 지시가 누락된 합성을 막기 위해 `DIRECTED_ADAPTER_REQUIRED`와 **종료 코드 2**를 반환한다. 이 차단은 예상된 동작이며 오디오를 생성하지 않는다. 지원하지 않는 엔진 인수를 임의로 만들거나 지시를 무시한 중립 합성으로 대체하지 않는다.

현재 사용할 수 있는 경로는 설계 검사와 음성 작업표 내보내기다. 다음 명령은 음성을 합성하지 않는다.

```bash
python3 scripts/voice_direction_tools.py validate --scenes S03 S04 S05
python3 scripts/s03_approved_voice_tts.py --export-jobs /tmp/S03_voice_jobs.json
python3 scripts/s04_approved_voice_tts.py --export-jobs /tmp/S04_voice_jobs.json
python3 scripts/s05_voice_preflight.py --export-jobs /tmp/S05_voice_jobs.json
```

## 영어 초보자를 위한 첫 참여 경로

30개 참여 모두 **질문 종료 → 본편 시계 정지 → 해당 캐릭터의 세 단어 예시 1회 → 예시 종료 후 VAD 또는 보호자 터치 → 반응 1회 → 지정된 첫 재개 대사**로 진행한다. 첫 예시는 기본 경로에 포함하며, 보호자는 예시를 건너뛰고 진행할 수 있다. 예시 재생 중에는 마이크 판정을 막고, 무응답 5초 뒤에는 다시 듣기·보호자 터치를 제시한다. 단어 인식이나 발음 채점은 하지 않는다.

## 보존하는 과거 제작 자료

다음은 **S01 제작 및 초기 V2 확장의 역사적 자료**다. 현재 작업을 S02부터 다시 시작하라는 지시로 사용하지 않는다.

- S01의 완성 영상·Blender 소스와 기존 승인 음원을 보존한다. S01의 과거 조형·리깅 승인 절차는 해당 레거시 산출물의 기록이며 현재 S03~S05 수정의 신규 실행 단계가 아니다.
- [V1.1 정본 소스](docs/series_v2/sources/)의 12장면·138컷 기준과 원본 대사·참여를 보존한다.
- [S02 기존 상세 설계](scenes/S02/script_v2_draft.md), [당시 개발 브리프](docs/series_v2/S02_DEVELOPMENT_BRIEF.md), [기존 승인 성우 자료](docs/series_v2/S02_APPROVED_VOICES.md)는 참조 자료로 남긴다. S02 완료 상태는 이번 수정으로 되돌리지 않는다.
