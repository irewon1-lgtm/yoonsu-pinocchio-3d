# 시리즈 V2 + S02 설계 검증

```
python3 scripts/validate_series_v2.py
python3 scripts/validate_s02_design.py
```

첫 스크립트는 V1.1 원본 SHA·12장면·138컷·S01 보존·V2 정책을 확인합니다. 두 번째 스크립트는 실제 작성된 S02 대본이 원본 21문장을 순서·화자 그대로 보존했는지, 10개 참여가 모두 정의됐는지, 50컷의 타임코드 합계가 443초인지 검사합니다.

두 스크립트의 PASS는 **문서 정합성**만 뜻합니다. 사용자 창작 승인과 MP4 360초·3D 연기 품질·오디오·실기기 테스트는 별도입니다.

## S03 설계 추가 검증
`python3 scripts/validate_s03_design.py`와 `python3 scripts/s03_approved_voice_tts.py` 기본 dry-run 실행. V1.1 원본 S03 22문장 보존, 50컷 합계 456초 목표, 원본 I03·I04 포함 10회와 S02 설계 스키마 호환을 검증. 실제 동작 엔진, 렌더 영상, 음성 생성 여부는 이 테스트 대상이 아니므로 NOT_RUN.

## S04 상세 설계 검증
`python3 scripts/validate_s04_design.py`는 원본 S04 영어 32문장/화자/순서, 50개 촬영컷의 총 479초 목표, I05/I06/I07 포함 10개 참여, S02/S03 JSON 호환, 귀뚜라미 미승인 캐스트 잠금을 검증한다. `python3 scripts/s04_approved_voice_tts.py`는 기저 성우 참조 MP3 4개 SHA 검사와 귀뚜라미 음원 결손 보고만 한다. 합성은 명시적 `--synthesize` 미사용 시 실행하지 않는다. 이 PASS는 실제 MP4나 귀뚜라미 음성 PASS가 아니다.

## S05 및 12장면 연결 계약

```bash
python3 scripts/validate_s05_design.py
python3 scripts/validate_story_continuity.py
python3 scripts/s05_voice_preflight.py
python3 scripts/validate_s05_design.py --self-test
python3 scripts/validate_story_continuity.py --self-test
```

S05 검사: 원본 18줄과 I08·I09의 질문/반응/즉시 재개, 50컷의 연속 시간, 432초의 계획, 모든 대사의 컷 배정, 10개 이벤트, WAIT 외부 분리. 165wpm 상한 검사는 작성 단계의 과밀한 대사 배정을 찾는 보조 검사이며, 실제 음성 길이와 연기 타이밍 PASS가 아니다.

연결 검사: S01~S12와 11개 인접 경계의 누락/중복, 정본 이름, 4→5→6의 인계 자료. 자연스러움은 원본 대조 검토와 사용자 검토가 필요하고, 렌더의 소품/행동/음향 연속성은 별도 NOT_RUN이다.

음성 검사 기본 종료 코드 0은 참조 음성 SHA/배정의 정합성에 한정한다. 전체 S05 음성 준비 완료를 뜻하지 않는다. `python3 scripts/s05_voice_preflight.py --require-ready`는 현재 귀뚜라미 승인 음성 미확보를 감지하여 종료 코드 2를 반환해야 한다.

실행 명령·판정·입력 파일 해시는 `scenes/S05/validation_report.json`에, 해석과 남은 제작 게이트는 `scenes/S05/QA_G0_G1.md`에 기록한다.
