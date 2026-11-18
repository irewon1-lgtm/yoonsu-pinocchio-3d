---
name: s01-visual-qa
description: "윤수 피노키오 S01의 D1 시각 게이트에서 자동 검수 결과와 실제 캐릭터 외형·크기·작업실 합성 품질을 분리하고 PASS/FAIL/NOT_RUN 증거를 기록할 때 사용한다."
---
# Visual quality release gate

- 대상은 D1만. 사용자 승인 없는 D2/D3 진행 금지.
- 필수 제출: `D1_CHAR_COMPARE.png`(3명×전면/3·4/측면), `D1_FACE_CLOSEUPS.png`, `D1_WORLD_SCALE.png`, `D1_FAIRY_WINDOW.png`, `D1_C06_SLEEPING.png`, `D1_C07_STANDING.png`, `D1_LIGHTING_A_B.png`, `.blend`, source+asset SHA, license manifest, QA report.
- 3D 메시 데이터 검사는 `scripts/inspect_blend.py`로 수행. 메시 수, UV, Armature 유무, subdivision, 렌더 설정, bounds를 보존하되 정량 PASS를 미술 PASS로 혼동하지 않는다.
- **자동 PASS**: 원본 해시 불변, PNG가 열림, Blender 파일 재오픈, 좌표/높이/접촉 시뮬레이션, 렌더 수, 자료 중복 제거.
- **사용자 시각 승인만 가능**: 캐릭터 원화의 동일성, 성인 제페토·작은 요정의 규모감, 얼굴 연기/감정 표현 가능성, 작업실과 자연스러운 2.5D 합성, 프록시 느낌 제거.
- FAIL 시 무조건 전체 재제작하지 않는다. 근본 원인별로 대안 2개 이상을 비교하고 가장 작은 핵심 시안을 먼저 제작한다.
- 최소 품질 게이트: 최종 3인 캐릭터가 단순 구·원기둥 이어붙임으로 읽히지 않음; C06 잠든 피노키오 얼굴 완전히 보임; C07 한 발도 떠 있지 않음; 요정 날개가 창틀과 충돌하지 않음; 제페토가 작업대 기준 성인 크기임; 2D 배경과 3D 물체 색·그림자·가림이 큰 이질감 없이 이어짐.
- QA 보고서는 `STRUCTURE_PASS`, `VISUAL_REVIEW_REQUIRED`, `NOT_RUN`, `BLOCKED_RESOURCE`를 혼동하지 않는다. 원본 권리 불명확은 Public 업로드 중단.
