"use strict";

const el = id => document.getElementById(id);
const film = el("film");
const caption = el("caption").querySelector("span");
const promptAudio = new Audio();
const duration = MEDIA.parts.at(-1).end;
const progress = mountSeekBar(el("playback"), seek);

let part = 0, loaded = -1, mode = "ready";
let navigation, requestedTime = 0, requestedPlay = false, videoURL;
let appPaused = false, pageCached = false;
let exampleGeneration = 0, hintTimer, micState = "idle";
const completedGates = new Set();
const heardExamples = new Set();
let automaticExample = null;
let pendingReaction = null;

const micStatus = {
  idle: "따라 말하거나 보호자가 터치해 주세요.",
  permission: "마이크 사용 권한을 확인하고 있어요.",
  preparing: "마이크를 준비하고 있어요.",
  armed: "따라 말하거나 보호자가 터치해 주세요.",
  listening: "듣고 있어요…",
  speaking: "듣고 있어요…",
  settling: "잠깐 기다려 주세요.",
  off: "마이크를 켜거나 보호자 터치로 이어볼 수 있어요.",
  error: "마이크를 열 수 없어요. 보호자 터치로 이어볼 수 있어요.",
};

const mic = createTalesMic({
  button: el("mic"),
  slider: el("mic-level"),
  level: el("level"),
  enabled: () => mode === "waiting" && !suspended(),
  status: showMicStatus,
  onSpeech: hideReplayHint,
  onComplete() {
    if (mode === "waiting" && !suspended()) advance();
  },
});

function suspended() {
  return appPaused || pageCached || document.hidden;
}

function promptActive() {
  return ["waiting", "example", "example-error"].includes(mode);
}

function protectedNarrative() {
  if (promptActive()) return false;
  const time = mode === "loading" || loaded !== part
    ? requestedTime : MEDIA.parts[part].start + film.currentTime;
  return time < MEDIA.protectedOpeningEnd || MEDIA.protectedRanges.some(({start, end}) => start <= time && (time < end || end === duration));
}

function finishReaction(clip, time) {
  if (pendingReaction !== null && part === pendingReaction + 1
      && !film.seeking && time + 1e-7 >= clip.reactionEnd) {
    completedGates.add(MEDIA.parts[pendingReaction].id);
    pendingReaction = null;
  }
}

function showPosition() {
  const hidden = protectedNarrative();
  el("mic").hidden = hidden;
  el("sensitivity").hidden = hidden;
  if (hidden && el("status").textContent) el("status").textContent = "";
  if (mode === "loading" || loaded !== part) {
    progress(duration, requestedTime);
    return;
  }
  const clip = MEDIA.parts[part];
  const time = Math.min(film.currentTime, clip.end - clip.start);
  progress(duration, clip.start + time);
  if (["playing", "paused"].includes(mode)) finishReaction(clip, time);
  const text = ["playing", "paused"].includes(mode) && !film.seeking && time >= (clip.reactionEnd || 0)
    ? clip.captions.find(([start, end]) => start <= time && time < end)?.[2] || ""
    : "";
  if (caption.textContent !== text) caption.textContent = text;
}

function clearPrompt() {
  el("turn").hidden = true;
  el("line").textContent = "";
  el("again").hidden = true;
  el("status").textContent = "";
  caption.textContent = "";
}

function stopListening() {
  clearTimeout(hintTimer);
  mic.leave();
}

function stopExample() {
  exampleGeneration++;
  promptAudio.onended = null;
  promptAudio.onerror = null;
  promptAudio.pause();
}

function capturingSpeech() {
  return micState === "speaking" || micState === "settling";
}

function hideReplayHint() {
  clearTimeout(hintTimer);
  el("again").hidden = true;
}

function scheduleReplayHint() {
  clearTimeout(hintTimer);
  const after = MEDIA.parts[part].repeatAfter;
  const offerReplay = () => {
    if (mode === "waiting" && !suspended() && !capturingSpeech()) el("again").hidden = false;
  };
  if (typeof after === "number") hintTimer = setTimeout(offerReplay, after * 1000);
  else offerReplay();
}

function showMicStatus(state) {
  const wasCapturingSpeech = capturingSpeech();
  micState = state;
  if (protectedNarrative()) return;
  if (suspended() || ["example", "example-error", "loading"].includes(mode)) return;
  if (mode === "waiting") {
    if (capturingSpeech()) hideReplayHint();
    else if (wasCapturingSpeech) scheduleReplayHint();
  }
  if (mode === "waiting" || state === "permission" || state === "error") {
    el("status").textContent = micStatus[state];
  }
}

function listen() {
  if (mode !== "waiting" || suspended()) return;
  showMicStatus(micState);
  if (!capturingSpeech()) scheduleReplayHint();
  mic.enter();
}

function playExample() {
  if (mode !== "example" || suspended()) return;
  const token = exampleGeneration;
  void promptAudio.play().catch(() => exampleError(token));
}

function exampleError(token) {
  if (token !== exampleGeneration || mode !== "example" || suspended()) return;
  stopExample();
  automaticExample = null;
  mode = "example-error";
  el("again").hidden = false;
  el("status").textContent = "예문을 다시 눌러 듣거나 보호자 터치로 이어볼 수 있어요.";
}

function startExample(automatic = false) {
  if (!["waiting", "example-error"].includes(mode)) return;
  stopListening();
  stopExample();
  mode = "example";
  el("again").hidden = true;
  el("status").textContent = "예문을 들어 보세요.";
  const token = exampleGeneration;
  const clip = MEDIA.parts[part];
  // Seeking away pauses this turn's automatic example. Keep its media position
  // if the viewer returns before it ends.
  if (!automatic || automaticExample !== clip.id) promptAudio.src = clip.example;
  automaticExample = automatic ? clip.id : null;
  promptAudio.onended = () => {
    if (token !== exampleGeneration || mode !== "example" || !promptAudio.ended) return;
    heardExamples.add(clip.id);
    automaticExample = null;
    stopExample();
    mode = "waiting";
    listen();
  };
  promptAudio.onerror = () => exampleError(token);
  playExample();
}

async function loadPart(target, signal) {
  if (loaded === target) return;
  let src = MEDIA.parts[target].src;
  if (location.hostname === "appassets.androidplatform.net") {
    const response = await fetch(src, {signal});
    if (!response.ok) throw new Error("Missing episode segment");
    const data = await response.blob();
    if (signal.aborted) return;
    src = URL.createObjectURL(data);
  }
  film.src = src;
  if (videoURL) URL.revokeObjectURL(videoURL);
  videoURL = src.startsWith("blob:") ? src : undefined;
  loaded = target;
}

async function startPart(target, time, play) {
  navigation?.abort();
  const signal = (navigation = new AbortController()).signal;
  part = target;
  requestedTime = MEDIA.parts[part].start + time;
  requestedPlay = play;
  stopListening();
  stopExample();
  clearPrompt();
  film.pause();
  mode = "loading";
  el("play").disabled = true;
  showPosition();
  try {
    await loadPart(target, signal);
    if (signal.aborted) return;
    film.currentTime = time;
    mode = requestedPlay && !suspended() ? "playing" : "paused";
    el("play").textContent = mode === "playing" ? "일시정지" : "재생";
    if (mode === "playing") await film.play();
    if (signal.aborted) return;
    showPosition();
  } catch {
    if (signal.aborted) return;
    mode = "paused";
    el("play").textContent = "재생";
    if (!suspended()) el("status").textContent = "영상을 열 수 없어요. 재생을 다시 눌러 주세요.";
  } finally {
    if (!signal.aborted) el("play").disabled = ["waiting", "example", "example-error"].includes(mode);
  }
}

function seek(time) {
  if (pendingReaction !== null) {
    showPosition();
    return;
  }
  const unanswered = MEDIA.parts.find(clip => clip.id && !completedGates.has(clip.id));
  if (unanswered && time >= unanswered.gateStart) {
    const atUnanswered = MEDIA.parts[part] === unanswered;
    const position = mode === "loading" || loaded !== part ? requestedTime : unanswered.start + film.currentTime;
    if (atUnanswered && (promptActive() || position >= unanswered.gateStart)) {
      showPosition();
      return;
    }
    time = unanswered.gateStart;
  }
  const target = MEDIA.parts.findIndex(clip => time < clip.end);
  const selected = target === -1 ? MEDIA.parts.length - 1 : target;
  const clip = MEDIA.parts[selected];
  const localTime = Math.min(clip.end - clip.start - .001, Math.max(0, time - clip.start));
  const play = mode === "loading" ? requestedPlay : ["playing", "waiting", "example", "example-error"].includes(mode);
  void startPart(selected, Math.max(0, localTime), play);
}

function advance() {
  if (!["waiting", "example", "example-error"].includes(mode) || suspended()) return;
  pendingReaction = part;
  automaticExample = null;
  void startPart(part + 1, 0, true);
}

film.addEventListener("ended", () => {
  if (mode !== "playing" || !film.ended) return;
  const ending = MEDIA.parts[part];
  finishReaction(ending, ending.end - ending.start);
  clearPrompt();
  const clip = MEDIA.parts[part];
  if (!clip.id) {
    mode = "finished";
    stopListening();
    el("play").disabled = false;
    el("play").textContent = "다시 보기";
  } else if (completedGates.has(clip.id)) {
    void startPart(part + 1, 0, true);
  } else {
    mode = "waiting";
    el("play").disabled = true;
    el("play").textContent = "말하기";
    el("line").textContent = clip.cue;
    el("turn").hidden = false;
    if (heardExamples.has(clip.id)) listen();
    else startExample(true);
  }
  showPosition();
});
for (const event of ["loadedmetadata", "timeupdate", "seeking", "seeked"]) {
  film.addEventListener(event, showPosition);
}
if ("requestVideoFrameCallback" in film) {
  const watch = () => {
    showPosition();
    film.requestVideoFrameCallback(watch);
  };
  film.requestVideoFrameCallback(watch);
}
showPosition();

el("parent").onclick = advance;
el("again").onclick = () => {
  if (!capturingSpeech()) startExample();
};
el("play").onclick = () => {
  if (mode === "playing") {
    film.pause();
    mode = "paused";
    el("play").textContent = "재생";
  } else if (["ready", "finished"].includes(mode)) {
    completedGates.clear();
    heardExamples.clear();
    automaticExample = null;
    pendingReaction = null;
    void startPart(0, 0, true);
  } else if (mode === "paused") {
    const time = loaded === part ? film.currentTime : requestedTime - MEDIA.parts[part].start;
    void startPart(part, time, true);
  }
};


function pausePlayback() {
  clearTimeout(hintTimer);
  mic.suspend();
  requestedPlay = false;
  if (mode === "example") promptAudio.pause();
  if (mode === "playing") {
    film.pause();
    mode = "paused";
    el("play").textContent = "재생";
  }
}
function resumePlayback() {
  if (suspended()) return;
  mic.resume();
  if (mode === "example") playExample();
  else listen();
}
window.addEventListener("app-pausing", () => {
  appPaused = true;
  pausePlayback();
});
window.addEventListener("app-resumed", () => {
  appPaused = false;
  resumePlayback();
});
document.addEventListener("visibilitychange", () => {
  if (document.hidden) pausePlayback();
  else resumePlayback();
});
window.addEventListener("pagehide", event => {
  pageCached = true;
  if (event.persisted) pausePlayback();
  else {
    clearTimeout(hintTimer);
    mic.dispose();
  }
});
window.addEventListener("pageshow", event => {
  if (!event.persisted) return;
  pageCached = false;
  resumePlayback();
});
watchWebRevision("../__revision", () => ["ready", "finished"].includes(mode));
