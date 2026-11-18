# 윤수 피노키오 S01 — 3D 품질 기준

## Source of truth
- 사용자 승인된 V1.1 S01 26개 발화, V7 A/C/A/A 원본 MP3, CHAR_PIN / CHAR_GEP / CHAR_FAI 참고 원화, BG_WORKSHOP_02의 SHA를 불변 소스로 다룬다.
- BG_WORKSHOP_02 = image-gen-2(20261116-125801).png, SHA-256=18ebc03242c327d2f262a7e6dfa945917d8ca499abe3233af50b547592cbb1fa.
- 원본·기존 `.blend`·분석용 프록시는 수정/삭제하지 않고 별도의 LOOKDEV/PRODUCTION 컬렉션 또는 새 브랜치에 신규 모델을 생성한다.
- 3D 최종 조형이 필요할 때 UV sphere, capsule, tube를 이어붙인 러프 블로킹 모델을 최종 캐릭터로 승인하지 않는다.
- D1이 사용자 시각 승인되기 전에는 D2 실제 리깅 및 D3 C07 제작을 시작하지 않는다.

## Non-negotiable visual gates
- 규모: 제페토가 피노키오와 작업대에 비해 왜소하지 않음; 요정의 날개 포함 실루엣이 창문을 압도하지 않음. 3D 월드 실제 수치와 렌더 상 픽셀 비율을 모두 보고.
- 형상: 정면/3·4/측면과 얼굴 클로즈업에서 프리미티브 이음선, 근육·목·손·옷의 뚝 끊김이 명백하지 않음.
- 스타일: 승인 2D 배경을 프록시 단색 작업대·검은 창틀로 가리지 않음. 원화 배경을 덮는 진단용 메시들은 최종 렌더에서 별도 처리.
- 완료: 3명×3시점 + 얼굴 확대 + C06/C07 정지 장면 + 두 카메라·조명 조건 비교. 사용자 승인 이전 상태는 REVIEW_REQUIRED.

## Process
1. 원본/기존 산출물을 SHA-256으로 확인한다.
2. `scripts/inspect_blend.py`로 현재 메시/리깅/재질/카메라 설정을 JSON 덤프한다. 이는 수치 진단일 뿐 시각 품질 인증이 아니다.
3. `s01-character-sculpt` → `s01-scale-and-contact` → `s01-toon-lookdev` → `s01-visual-qa` 순서로 작업한다.
4. 작업마다 실제 수정 `.blend`, PNG, 원본 비교, 라이선스 원장, 검증 로그를 제출한다.
5. 무료 공개 GitHub Actions 표준 러너만 사용한다. 고비용 GPU/유료 서비스/무단 외부 업로드 금지.
