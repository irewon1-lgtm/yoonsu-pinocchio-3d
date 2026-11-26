# 12화 「친구를 구한 진짜 아이」 제작 자료

정본은 `irewon1-lgtm/yoonsu-pinocchio-3d`의 `s12/final-v3-production` 기준 커밋 `17011177e1a32fb19d086eccce1355055890092e`에 있는 S12 V3다. 이번 자료는 해당 작업 트리에 적용하는 2D 변경분과 실제 촬영·편집 기록을 담는다. `canonical/story/`는 정본 대사와 참여 문장의 읽기용 사본이다.

- `registered/`의 `layout-*.json`과 `art/cels/` 아래 신규·교체 파일을 정본의 `scenes/S12/v3/build/`를 복사한 별도 디렉터리에 합친다. 기존 레벨 디렉터리에 PNG를 병합한다. 실제 노출과 좌표는 `timeline/photographed-frames.json`, 그림별 기준점과 음성 변형은 각 `registration.json`에 있다.
- `timeline/edit.json`으로 이전 승인 음성 81개와 이야기 믹스·자막을 다시 연결한다. 이전 제작 환경에 있던 승인 WAV와 `mix.wav`는 정확한 편집 믹스를 재현하는 입력이다. 별도 음원 묶음에 승인 작업 결과를 보관했다. 최종 재생은 `art/render.py --edition <확정 편집 디렉터리> --build <합친 build 디렉터리> --target <출력 MP4>`로 제작한다.
- 변신·첫 기쁨·포옹의 신규 원화, 걷기·손동작·작별의 재사용 가능한 셀을 `sections/`와 `registered/`에 보관했다. `sections/core/`와 `sections/farewell/run/`에 sprite-gen으로 추출·조립·검사한 아틀라스와 manifest가 있다. 원래 엔진은 동일 도화의 등록 PNG와 프레임 노출을 읽는다. `previews/`에서 실제 촬영본을 확인할 수 있다.
- `sprite-gen` 4.3.0 설치본 커밋은 `670ed36025103049c7d898ca75770a9151a499bf`다. CLI `gen-set --provider codex`는 `/home/agent/.codex/generated_images` 쓰기 제한으로 실패해 현재 세션의 ImageGen으로 준비한 장면을 그렸다. 스킬의 `prepare`, `extract`, `cutout`, `compose-atlas`, `inspect` 및 일부 동작의 `inspect-holds`를 실제 실행했다. 두 인물을 함께 그린 포옹의 원화는 공식 `cutout`으로 배경을 제거하고 기존 촬영 코드의 각 인물 기준점으로 등록했다.
- 새 윤수 그림은 별빛 사진첩 「Hello, Officer!」 제작에 실제 사용된 윤수 원화 10종을 바탕으로 만들었다. 입력 자산의 해시와 출처는 `provenance/`에 있다. 소유자 입력 사진과 키는 별도 비공개 보관한다.
- `app/s12/player.js`는 새 그림을 연결한 기존 앱에서 탐색할 때 질문을 건너뛰거나 모델이 자동 반복되는 경계를 처리한다. `timeline/participation.json`의 액션은 최종 영상이 쓰는 본편 시계와 별도 모델 파일에 연결된다.
