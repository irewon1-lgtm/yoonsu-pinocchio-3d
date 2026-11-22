# Codex 실행 지시 / 제작 인계 V2.0

## 작업 브랜치
`irewon1-lgtm/yoonsu-pinocchio-3d`의 `s01/full-story-production`에서 시작. `main`은 README만 있는 상태로 S01 실제 산출물이 없다. 현재 GitHub에서 1장면 자료가 있는 브랜치를 기준으로 작업할 것.

~~~bash
git fetch origin
git switch s01/full-story-production
git pull --ff-only origin s01/full-story-production
python3 scripts/validate_series_v2.py
~~~

## 반드시 먼저 읽을 파일
- 루트 `AGENTS.md` (S01 기존 정책 보존 + V2 스코프 설명)
- `docs/series_v2/PRODUCTION_PRD_V2_0.md` (사용자 확정 요구)
- `docs/series_v2/series_manifest_v2.json` (12장면별 진행 상태)
- `docs/series_v2/S02_DEVELOPMENT_BRIEF.md` (다음 장면)
- `docs/series_v2/sources/` 원본 대본 + 138컷 콘티 (잠금)
- `downloads/s01-complete/` S01 영화/블렌더/QA (재작업 금지)

## 즉시 실행할 지시문
> 최신 `s01/full-story-production` 브랜치 SHA부터 이어서 작업해. `AGENTS.md`와 V2 제작 기준, V1.1 12장면 원본, S02 브리프를 읽고 `python3 scripts/validate_series_v2.py`를 실행해. S01은 이미 제작되었으므로 어떤 자산도 재작업/삭제/덮어쓰지 마. S02 '피노키오의 첫 친구'만 대상으로, 원본 사건과 대사를 그대로 유지하면서 실제 서사가 **최소 360초**, **윤수 참여 정확히 10회(원본 I02 포함)**가 되도록 새 사건·감정·대사·자연스러운 3D 동작을 포함한 상세 제작 대본을 작성해. 한국어 동작 지문과 원문/신규 영어 대사 식별, 실제 대사+연기 기준 타임라인, 10회 WAIT→REACT 맵, 원본 대비 증분표를 `scenes/S02/`에 기록해. 윤수는 영어 지시를 이해하지 못할 수 있으므로 행동을 먼저 보여준 뒤 짧은 영어를 연결하고, 소리 감지/보호자 터치로 참여시키며 발음 채점은 하지 마. **G1 대본은 사용자 검토 전 REVIEW_REQUIRED로 남겨두고 렌더/영상 제작을 시작하지 마.** 검증 로그·파일 링크·미확인 근거를 보고하고 승인 범위 내 일반 코딩·정합성 테스트는 자동 진행해.

## Codex 회차 운영
- G0 소스 감사 → G1 6분+ 10회 대본/비트/캐릭터 연기 검토
- 사용자 G1 주요 창작 승인 후 G2 콘티 → G3 어려운 동작 검증 → G4 전체 제작 → G5 실제 6분+ 영상 QA → G6 인계
- 빠르게 FAIL을 찾고 해당 부분만 수정/회귀. 완료하지 않은 단계를 PASS로 위장하지 않는다.
- 원본 정본/기존 완성 ZIP/MP4/BLEND/WAV를 덮지 않고 새 파일에 작업한다.
