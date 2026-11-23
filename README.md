# yoonsu-pinocchio-3d

## 실제 제작 및 Codex 시작 브랜치
**`s01/full-story-production`** — S01 완성 영상·Blender 프로젝트와 V1.1 12장면 대본/138컷 콘티/사용자 확정 V2.0 제작 정책이 함께 있는 작업 브랜치.
**`main`**은 현재 README만 있는 최소 브랜치이므로, Codex는 반드시 제작 브랜치로 이동한다.

~~~bash
git fetch origin
git switch s01/full-story-production
python3 scripts/validate_series_v2.py
~~~

- 시작 지시: `docs/series_v2/CODEX_HANDOFF.md`
- S02~S12 공통 요구: `docs/series_v2/PRODUCTION_PRD_V2_0.md`
- 원본 보존: `docs/series_v2/sources/`
- 장면별 목표/상태: `docs/series_v2/series_manifest_v2.json`
- 다음 작업: `docs/series_v2/S02_DEVELOPMENT_BRIEF.md`

**S01은 변경 없이 패스. S02부터 장면당 실제 서사 6분 이상, 윤수 참여 총 10회**를 기준으로 기존 이야기 위에 확장한다. V2.0 정책 작성 자체는 S02~S12 영상 완성을 의미하지 않는다.

## S02 직접 작성 설계
[7분 23초, 윤수 10회, 50컷 상세 대본](scenes/S02/script_v2_draft.md) · [구조화 설계](scenes/S02/scene_design_v2.json). S02 신규 창작은 ChatGPT가 작성하며 Codex는 승인 후 제작·검증합니다.

- [S02 승인 성우 기준 음원·재합성 설정 경로](docs/series_v2/S02_APPROVED_VOICES.md) (참조 MP3 4개 GitHub 직접 등록).

## S03 ChatGPT 직접 설계 (S02 베이스)
[전체 S03 7분 36초/50컷/윤수 10회 상세 대본](scenes/S03/script_v2_draft.md) · [구조화 설계](scenes/S03/scene_design_v2.json) · [S02 엔진 호환 인계](docs/series_v2/S03_ENGINE_HANDOFF.md). S02 실제 3D 렌더러는 아직 확인되지 않아 설계 구조만 재사용하는 상태입니다.

## S04 ChatGPT 상세 설계 (S02/S03 베이스)
[7분 59초·50컷·윤수 참여 10회 전체 대본](scenes/S04/script_v2_draft.md) · [JSON 제작 정본](scenes/S04/scene_design_v2.json) · [베이스 엔진 인계](docs/series_v2/S04_ENGINE_HANDOFF.md). 기존 대사 32문장 보존, 신규 77문장. 신규 귀뚜라미 성우는 미승인/음성 생성 차단. 실제 S02 렌더러는 확인되지 않아 설계 데이터 구조만 계승.
