# S04 제작 인계 — S02/S03 기본 엔진 계승

### 확인된 원본과 구현 상태
- `scenes/S02/scene_design_v2.json` · `scenes/S03/scene_design_v2.json`: 24fps, 10개 beat/50샷 설계. **이 두 작품의 실제 3D 렌더러/BLEND/MP4는 현재 브랜치에 발견되지 않음.**
- `downloads/s01-complete/S01_BLENDER_PROJECT.zip`: 실제 S01의 Blender 소스 참조; 변경 금지, S04 신규 프로젝트에만 복사해서 수정.
- `assets/voice_refs/v6/`: 내레이터/피노키오/제페토/요정의 확정 기준 MP3. **귀뚜라미 음성 없음**.
- `scripts/s03_approved_voice_tts.py`: 이전 화 목소리 해시 검증·미리듣기 방식. S04에서도 세 고정 성우는 재사용, 새 귀뚜라미는 승인 전 합성 차단.

### 베이스 실행 계약(구현 단계 인수)
1. 같은 구조화 스키마: `scenes/S04/scene_design_v2.json`, 10비트/50샷, 479초 목표/WAIT 제외.
2. 같은 음성 입력 게이트: 질문 음성 완전히 종료 → VAD 또는 부모 터치 → REACT 단 1회 → 후속 대사.
3. 같은 캐릭터 기본 리그: S01의 실제 3D 모델 기반, S02 설계의 눈·머리·손·발·걷기 연기 지침을 적용. 실물 S02 캐시가 없다면 S01에서 신규 개발하되 완료됐다고 주장하지 않는다.
4. 신규 샷의 상태 유지를 위해 모자 머리 착용 / 책가방 끈 결속 / 대문 닫힘→열림 / 2개 표지판 좌우 / 귀뚜라미 잎→바닥 / 물웅덩이 좌표 / 개구리 / 건너편 착지 / S05 진입 소리를 state ledger로 구현.
5. 귀뚜라미 디자인·연기 제안은 작성했지만 **승인받은 성우가 없으므로 귀뚜라미 음원 제작은 BLOCKED_RESOURCE.** 기존 캐스트 목소리 혼용·대사 제거 금지.
6. S04의 첫 2비트는 제페토+피노키오, 세 번째/네 번째는 피노키오 혼자, B05부터 귀뚜라미 등장. 제페토가 중간 길에 갑자기 나타나면 FAIL.
7. 독립 기본 모듈이 없어도 S04 스토리·샷·카메라·상호작용 설계까지 완성했으므로 Codex는 G1 재작성 금지. 사용자 승인 후 구현·QA만 진행.

### Codex 실행 전 확인
```bash
git switch s01/full-story-production
python3 scripts/validate_series_v2.py
python3 scripts/validate_s02_design.py
python3 scripts/validate_s03_design.py
python3 scripts/validate_s04_design.py
python3 scripts/s04_approved_voice_tts.py
```
마지막 명령은 합성이 아닌 해시·매핑·캐스트 미확보 확인용이며 귀뚜라미를 자동 합성하지 않는다.
