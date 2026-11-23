# 시리즈 V2 + S02 설계 검증

```
python3 scripts/validate_series_v2.py
python3 scripts/validate_s02_design.py
```

첫 스크립트는 V1.1 원본 SHA·12장면·138컷·S01 보존·V2 정책을 확인합니다. 두 번째 스크립트는 실제 작성된 S02 대본이 원본 21문장을 순서·화자 그대로 보존했는지, 10개 참여가 모두 정의됐는지, 50컷의 타임코드 합계가 443초인지 검사합니다.

두 스크립트의 PASS는 **문서 정합성**만 뜻합니다. 사용자 창작 승인과 MP4 360초·3D 연기 품질·오디오·실기기 테스트는 별도입니다.

## S03 설계 추가 검증
`python3 scripts/validate_s03_design.py`와 `python3 scripts/s03_approved_voice_tts.py` 기본 dry-run 실행. V1.1 원본 S03 22문장 보존, 50컷 합계 456초 목표, 원본 I03·I04 포함 10회와 S02 설계 스키마 호환을 검증. 실제 동작 엔진, 렌더 영상, 음성 생성 여부는 이 테스트 대상이 아니므로 NOT_RUN.
