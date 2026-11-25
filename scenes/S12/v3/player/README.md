# 12화 재생 연결

기존 11화 플레이어와 마이크 모듈을 사용한다. 12화에서 회차 전체를 앞으로 탐색해도 다음 미완료 참여의 시범 컷부터 재생한다. I21은 입력을 받은 뒤 C12부터 C14까지 재생하고, 구조 동작이 끝난 뒤 C15에서 U011 자막을 표시한다. 같은 재생 세션에서 완료한 예문은 탐색 후 자동으로 다시 틀지 않는다.

## 실제 렌더 검수본

`--source`에는 편집기의 `edit.json`, `mix.wav`, `audio/`가 있는 디렉터리를 사용한다. MP4는 컷 경계에 키프레임을 둔 1920×1080, 24fps H.264 영상이어야 한다. 장면을 잘라 만든 검수본은 캐릭터 반응과 첫 후속 대사가 모두 들어 있는 참여만 포함한다.

```sh
python3 scenes/S12/v3/player/build.py chapters --excerpt \
  --source "$S12_EDIT" --master "$S12_MASTER" --output "$S12_CHAPTERS"
python3 scenes/S12/v3/player/build.py standalone \
  --media "$S12_CHAPTERS" --output "$S12_REVIEW_HTML"
```

## 앱 로컬 후보

50컷, 참여 10회, 본편 360초 이상인 완성 편집과 표지가 필요하다. 12화만 추가한 v17 후보를 만들고 기존 v16과 비교해 카탈로그에 추가된 카드 외 파일이 같은지 확인한다. 공개 v15 기기에도 11화 파일이 전달되도록 v15에서 늘어난 객체를 모두 포함한다. 생성물은 로컬 경로에 저장한다.

```sh
python3 scenes/S12/v3/player/release.py \
  --source "$S12_EDIT" --master "$S12_MASTER" \
  --cover "$S12_COVER" --output "$S12_CANDIDATE"
```

## 검증 범위

`tests/gate-navigation.mjs`는 PC JavaScript 환경에서 I21의 탐색, 중복 진행 차단, 구조 완료 전 자막 억제를 재현한다. 네이티브 마이크는 기존 모듈을 그대로 연결한다. Android 단말 연결과 실제 마이크 검사는 별도다.

`tests/verify_review.py`는 Chromium으로 실제 영상을 디코딩하고, 질문 끝에서 모델 음성 종료와 반응을 기록한다. `--fake-mic`으로 입력한 테스트 WAV는 Chromium의 모의 마이크만 사용한다. 이 경우에도 Android 실기 마이크는 별도로 표기한다.
