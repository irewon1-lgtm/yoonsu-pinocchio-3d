# S02-S12 확정 성우 재생성 기준 (GitHub 음원 직접 등록)

**S01 확정 캐스트:** 내레이터 A / 파란 요정 C / 피노키오 A / 제페토 A. **S01 26대사 실제 엔진 기록:** Chatterbox-Nano 110M, 개별 화자 voice_reference ID 고정.

## 사용 가능한 확정 기준 음원 (이 브랜치 파일)
- **내레이션 A:** `assets/voice_refs/v6/narrator_V6_APPROVED.mp3` · MP3 SHA256 `ec7234237b687246af302db312994c6b9ddc46411c82085a5b1f3884bcfcbddf`
- **피노키오 A:** `assets/voice_refs/v6/pinocchio_V6_APPROVED.mp3` · MP3 SHA256 `a32569705a717ac92c8ecbe1c515b9e31e389f508164458ed22a06adcbba0b3d`
- **제페토 A:** `assets/voice_refs/v6/geppetto_V6_APPROVED.mp3` · MP3 SHA256 `80237e647e1e480987a3cf0a6ac1dc33a3d6b3a40dc62d577f4a0290e338af55`
- **파란 요정 C:** `assets/voice_refs/v6/blue_fairy_V6_APPROVED.mp3` · MP3 SHA256 `c65e44b9c4d221c1fe9052ff201a3d3a0f5bc867c29460130fe2944f59c5965b`

과거 V6 승인 HTML 안의 **기준 MP3 오디오 4개를 원본 바이트 그대로** 이 저장소에 등록했다. 화자별 기본 라벨: 내레이터 `am_fenrir`, 파란 요정 `af_kore`, 피노키오 밝은 소년, 제페토 다정한 노년 남성. **V7 생성은 모두 Chatterbox Nano**이므로 `am_fenrir` 등은 V6 샘플의 라벨일 뿐 Nano 모델의 voice-id로 해석하지 않는다.

- **사람/모델 매핑과 원본 해시:** `assets/voice_refs/v6/VOICE_REFERENCES.json`
- **S01 26개 출력 음원(비교 기준):** `downloads/s01-complete/S01_V7_VOICES.zip`
- **S01 대사별 화자·음원 해시:** `downloads/s01-complete/VOICE_LOCK.tsv`
- **S02 설계/대사:** `scenes/S02/scene_design_v2.json` 및 `scenes/S02/script_v2_draft.md`
- **S02 신규 대사 합성 시뮬레이션/미리듣기:** `scripts/s02_approved_voice_tts.py`

## 사용법 — Codex에서 바로 실행 가능

기본 검사(모델 다운로드/음성 합성 없음):

```bash
python3 scripts/s02_approved_voice_tts.py
```

소수 샘플만 생성(Chatterbox 설치 및 CPU 또는 GPU 환경 준비 후):

```bash
pip install chatterbox-tts torchaudio
python3 scripts/s02_approved_voice_tts.py --synthesize --limit 3 --device cpu
```

스크립트는 4개 기준 MP3를 검증하고 FFmpeg로 **24kHz mono PCM WAV를 파생 생성**한다. GitHub에 등록한 MP3는 원본 유지, 파생 WAV/새 대사는 `scenes/S02/audio/` 아래에서만 작업.

모델 사용 예:

```python
from chatterbox.tts_turbo import ChatterboxTurboTTS
model = ChatterboxTurboTTS.from_pretrained(device="cpu", nano=True)
wav = model.generate("Grandpa, look!", audio_prompt_path="scenes/S02/audio/reference_cache/pinocchio.wav")
```

## 음색 보존·품질 판정

- 승인된 V6 참조 MP3와 S01 V7 최종 26대사는 서로 다른 자산이다. V6=참조, V7=이전 출력.
- `S01 V7 voice_reference` 식별자는 **MP3 SHA가 아니다**. 실제 저장 파일은 `VOICE_REFERENCES.json`의 `sha256`으로 검증.
- 당시 생성 당시 정확한 모델 커밋/난수 seed/샘플러 파라미터는 확인되지 않았다. **완전히 같은 음색·억양을 보장하지 않는다**. 캐릭터별 기존 S01 영상과 직접 청감 비교(특히 제페토 나이·피노키오의 밝은 음색)를 통과한 샘플만 S02에 채택.
- 새 성우로 교체하거나 임의 목소리를 써서 S02 완료 처리하지 않는다. 만족스러운 미리듣기가 어려우면 `REVIEW_REQUIRED` 및 `BLOCKED_RESOURCE`로 기록.
- S01 승인 자산·음원은 재생성/덮어쓰기 금지.
- 파일은 현재 **공개 GitHub 저장소**에 위치하므로, 공유/라이선스 정책을 재확인할 필요가 있으면 사용자에게 알리고 추가 외부 배포를 자제.
