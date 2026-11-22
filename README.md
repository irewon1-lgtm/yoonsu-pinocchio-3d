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
