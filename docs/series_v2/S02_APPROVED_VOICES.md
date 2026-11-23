# S02~S12 승인 성우 재사용 — 음원 위치와 생성 설정

**2026-11-23 조사 결과:** S01 V7의 확정 음원 26개는 이 브랜치 `downloads/s01-complete/S01_V7_VOICES.zip`, 대사별 화자/원문/원본 오디오 SHA는 `VOICE_LOCK.tsv`에 있음. 이 ZIP은 S02 새 대사 음원이 아니다.

## 1. V6 승인 기준 화자 및 원본 음원

S01 V7의 과거 검수 파일 `PINOCCHIO_S01_V7_APPROVED_A_C_A_A.html` 안에, 별도로 보존된 `sources` 4종 **V6 승인 기준 MP3**를 확인했다(사용자의 ChatGPT Library 파일). 해당 HTML의 `records`에는 **모든 26개 S01 대사에 Chatterbox-Nano 110M** 엔진과 캐릭터별 동일 `voice_reference` 식별자가 기록돼 있다.

| 캐릭터 | 승인 후보 | V6 기준 보이스 식별/설명 | V6 MP3 SHA-256 | V7 참조 ID* |
|---|---|---|---|---|
| 내레이션 | A | `am_fenrir` | `ec7234237b687246af302db312994c6b9ddc46411c82085a5b1f3884bcfcbddf` | `d38f0b8b8d9b5b0413eae736633354b35fe421cdf4922e9c434d418492daa32c` |
| 피노키오 | A | 밝은 소년, 8-year-old boy | `a32569705a717ac92c8ecbe1c515b9e31e389f508164458ed22a06adcbba0b3d` | `7cc295611dbd96a7d60573ed4ae6b233ff13d170f6baea1958329b845eedf703` |
| 제페토 | A | 다정한 노년 남성, 82-year-old | `80237e647e1e480987a3cf0a6ac1dc33a3d6b3a40dc62d577f4a0290e338af55` | `97884b61a37d580d5dd0b1fed537752bce960f7a73cda3c67b3f57e1767d61c2` |
| 파란 요정 | C | `af_kore` | `c65e44b9c4d221c1fe9052ff201a3d3a0f5bc867c29460130fe2944f59c5965b` | `72b38e466ccb3c7daebb67beaed156d71f554c41c2f5fe458e53dcbbe9405f8c` |

*V7 `voice_reference` ID는 MP3 파일 SHA-256과 일치하지 않는다. **둘을 같은 해시로 취급하지 말 것.**

**경로 주의:** V6 기준 HTML은 현재 GitHub에 존재하는 파일이 아니라 ChatGPT Library 자산. 이 대화에서 사용자가 다운로드할 수 있는 `S02_APPROVED_V6_VOICES_AND_SETTINGS.zip`에 기준 MP3·24kHz mono WAV 4종과 `voice_manifest.json`을 추출해 두었다. 이 ZIP을 Codex 작업 공간의 `local_assets/approved_voice_refs/`에 풀어야 실제 WAV를 사용할 수 있다. **별도 전달 전 GitHub 저장소에 WAV/MP3 원본이 있다는 주장은 금지.**

## 2. 실제 경로

**GitHub/모든 작업자가 읽을 수 있는 S01 대조용**
- `downloads/s01-complete/S01_V7_VOICES.zip`: S01 확정 26대사, 인물별 샘플 대조
- `downloads/s01-complete/VOICE_LOCK.tsv`: 화자, A/C 승인 번호, 개별 오디오 SHA/대사
- `downloads/s01-complete/SCREENING_KO.md`: 26개 실음성 검수 범위와 한계

**별도로 전달되는 V6 승인 화자 원본 ZIP 압축 해제 후(로컬 경로)**
- `local_assets/approved_voice_refs/approved_v6_reference_audio/narrator_V6_APPROVED.wav`
- `local_assets/approved_voice_refs/approved_v6_reference_audio/pinocchio_V6_APPROVED.wav`
- `local_assets/approved_voice_refs/approved_v6_reference_audio/geppetto_V6_APPROVED.wav`
- `local_assets/approved_voice_refs/approved_v6_reference_audio/blue_fairy_V6_APPROVED.wav`
- `local_assets/approved_voice_refs/voice_manifest.json`

## 3. 같은 성우로 S02 새로운 대사 합성

V7과 같은 **Chatterbox-Nano** 아키텍처를 우선 사용한다. `am_fenrir`/`af_kore`는 **V6 원본 선택 정보**이며, V7 엔진을 Kokoro로 바꾸라는 뜻이 아니다.

공식 라이브러리 사용 형태:

```python
import torchaudio as ta
from chatterbox.tts_turbo import ChatterboxTurboTTS
model = ChatterboxTurboTTS.from_pretrained(device="cpu", nano=True)
wav = model.generate(
    "Grandpa, look!",
    audio_prompt_path="local_assets/approved_voice_refs/approved_v6_reference_audio/pinocchio_V6_APPROVED.wav"
)
ta.save("scenes/S02/audio/pinocchio_preview.wav", wav, model.sr)
```

S02 대본은 `scenes/S02/scene_design_v2.json`과 `script_v2_draft.md`, 신규 81개 영어 문장과 원본 21개 문장(총 102개). **Codex는 대본/캐릭터 배정을 새로 쓰면 안 된다.** `python3 scripts/s02_approved_voice_tts.py --dry-run`으로 입력을 검토할 수 있다. 원본 reference ZIP이 준비되면 `--synthesize --limit 2`로 소수의 샘플만 만들어 V7과 청감 비교 후 나머지를 진행한다.

## 4. 복원 범위·미확인

- 확인됨: 4개 승인 기준 MP3 실물, MP3 SHA, WAV 변환 파일, S01 V7 생성 기록의 엔진/화자별 참조 ID.
- **미확인:** 당시 Chatterbox 패키지 정확한 커밋/모델 가중치 버전, 난수 시드 및 샘플링 세부 값. 재합성의 **음색·억양/감정이 바이트 단위 동일함을 보장하지 못한다**.
- S02 기존/신규 영어 음성 제작은 아직 별도 PASS 아님. 목소리 교체/다른 성우 사용은 사용자 승인 전 금지.
- S01 다운로드/오디오/서명/원본은 재합성·덮어쓰기 금지. 참고 음원은 외부로 임의 재배포하지 말 것.
