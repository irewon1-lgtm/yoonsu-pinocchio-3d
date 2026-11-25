# 12화 실제 음원 제작

V3 정본의 71개 본편 대사와 본편 밖 예문 열 개를 같은 승인 화자 참조로 녹음한다. 공식 IndexTTS2의 합성 감정 벡터는 대본 상황과 화자별 말하기 목적에 대응한다. 합성에 전달한 제어, 고정 참조 해시, 실제 파일 해시와 샘플 수는 개별 수락 기록에 있다. 피치·배속 변경은 적용하지 않았다. 명시된 감정 전환은 원문에 이미 있는 감탄사, 부름 또는 문장 사이에서만 분리한다.

다섯 승인 화자 참조는 이전 제작의 잠금 증거와 대조한다. 첨부 요정 C와 내레이션 A MP3의 바이트는 이전 승인 파일과 일치한다. 인식과 화자 검증을 통과한 원본 WAV는 `scenes/S12/v3/build/voices/`에 기록한다. 발음과 감정의 직접 청취는 자동 인식 대조와 별개다.

```bash
python -B scenes/S12/v3/voice/prepare.py
bash scenes/S12/v3/voice/run-native.sh native --lane 0 --beams 1
bash scenes/S12/v3/voice/run-native.sh cast
PYTHONPATH=/tmp/s02-audio-env python -Bu scenes/S12/v3/voice/run.py words
python -B scenes/S12/v3/voice/export.py complete
```

`native --lane`을 0~3으로 나눠 동시 실행한다. 이미 기록된 후보와 해시가 일치하면 해당 줄을 건너뛴다. 대사 한 줄만 다시 녹음하려면 해시 기록이 보존되는 새 버전으로 `native --line S12-U001 --beams 1 --seed-offset 1` 형태를 사용한다. 단계별 기록은 `/workspace/scratch/s12-v3/voice/`에 저장된다.

N012의 자동 인식에서 `all right`와 `alright` 표기가 갈리면 기존 인식 결과를 다시 사용한다. `resolve-alright.py --version retake-913`은 해당 음원만 별도 인식 모델로 비교해 `hurt`와 `heard`를 구분한다. 해당 판정도 발음과 감정의 직접 청취를 대신하지 않는다.
