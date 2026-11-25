# 12화 「친구를 구한 진짜 아이」 V3 제작

`canonical/`은 사용자 첨부 정본의 12화 폴더다. 대사, 참여 문구, 반응 순서와 컷 ID는 이 입력에서 가져온다. 승인된 S11 마지막 프레임과 기존 S04/S08/S11 2D 촬영기, 승인 참조를 사용한 IndexTTS2 합성 경로를 계승한다.

## 제작 재개

1. 이전 제작 작업공간의 S11 원화·촬영기와 S10 편집기를 연결한다. 오프닝은 `python3 scenes/S12/v3/art/opening.py`로 준비한다. C15~C19와 C20~C29 원화 재개 명령은 [구조 이후 원화](art/rescue/README.md)와 [요정 원화](art/fairy/build_fairy.py)에 있다.
2. `voice/prepare.py`에서 다섯 고정 음색의 출처와 해시를 연결하고, `voice/run.py`로 원 생성을 재개한다. `build/voices/`와 생성 로그에 기록된 줄별 선택 영수증을 보존한다. 인식, 길이, 파형 결과는 청취 결과와 구분한다.
3. `editor/assemble.py`에 실제 PNG 노출에 맞춘 동작 길이와 선택된 음원을 연결한다. `--range C01:C05`는 해당 구간만 재계산한다. 실제 편집과 PCM으로 `art/render.py --edition <edit-output> --target <preview.mp4>`를 실행한다. 촬영기는 필요한 모든 컷이 등록된 연속 구간을 요구한다. `art/export_atlas.py`는 투명 페이지, 각 셀 원본 해시, 트림 사각형과 기준점을 함께 출력한다.
4. [참여 재생기](player/README.md)는 기존 앱 브리지와 동일한 권한·모델·입력 대기 흐름으로 동작한다. 정본 50컷과 참여 10회, 입력 대기를 제외한 360초 이상을 확인한 뒤 앱 콘텐츠를 봉인한다.

## 전체 본편 원화

- 사용자 승인에 따라 C06~C14 학교 배경에 낮은 공간과 안내판 받침을 제작했다. [구조 원화·촬영 소스](art/rescue/full/build.py)와 구조 컷의 `layout-rescue-full.json`, `motion-rescue-full.json`을 사용한다.
- C30에서 기존 목각 윤수를 같은 모자·가방·신발을 지닌 인간형으로 변신시킨다. [인간형 기준점](art/human/source/registration.json)과 [변신 제작 소스](art/human/transform.py)를 이후 장면과 공유한다.
- C31~C34 [포옹](art/first_hug/build.py), C35~C42 [손과 모자 동작](art/hands/build.py), C43~C50 [학교 입장과 엔딩](art/ending/README.md)의 실제 2D 동작과 창을 전체 편집에 연결한다. 이전에 검증한 오프닝과 변신 직전 영상은 프레임과 대사 PCM이 일치할 때 촬영기에서 복사할 수 있다.
- [전체 앱 배포 도구](player/full_release.py)는 50컷 본편과 10회 참여가 담긴 MP4를 기존 앱의 인증 콘텐츠로 준비한다.
