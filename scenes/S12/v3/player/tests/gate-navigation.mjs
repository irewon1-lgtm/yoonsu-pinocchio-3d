import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { setImmediate } from "node:timers/promises";
import { fileURLToPath } from "node:url";
import vm from "node:vm";

const folder = fileURLToPath(new URL("../", import.meta.url));
const generated = spawnSync("python3", ["-B", "-c", [
  "from build import BASE_WEB, player",
  "print(player((BASE_WEB/'s11/player.js').read_text()))",
].join("\n")], { cwd: folder, encoding: "utf8" });
assert.equal(generated.status, 0, generated.stderr);

class Element {
  events = new Map();
  textContent = "";
  hidden = false;
  paused = true;
  ended = false;
  seeking = false;
  currentTime = 0;
  plays = 0;
  child = { textContent: "" };
  querySelector() { return this.child; }
  addEventListener(name, fn) { this.events.set(name, fn); }
  fire(name) { this.events.get(name)?.(); }
  pause() { this.paused = true; }
  play() {
    this.paused = false;
    this.ended = false;
    this.plays++;
    return Promise.resolve();
  }
}

const nodes = new Map();
const document = {
  getElementById(id) {
    if (!nodes.has(id)) nodes.set(id, new Element());
    return nodes.get(id);
  },
  addEventListener() {},
};
let listener, micStarts = 0;
const media = {
  parts: [
    { src: "before", start: 0, end: 8, id: "I21", gateStart: 5,
      cue: "Catch it!", example: "model", captions: [] },
    { src: "after", start: 8, end: 24, reactionEnd: 10, captions: [[10, 11, "Thank you!"]] },
  ],
  protectedOpeningEnd: 0,
  protectedRanges: [{ start: 8, end: 20 }],
};

const context = vm.createContext({
  MEDIA: media,
  document,
  window: { addEventListener() {} },
  location: { hostname: "localhost" },
  Audio: Element,
  AbortController,
  setTimeout,
  clearTimeout,
  mountSeekBar: () => () => {},
  watchWebRevision() {},
  createTalesMic(handlers) {
    listener = handlers;
    return { enter() { micStarts++; }, leave() {}, suspend() {}, resume() {}, dispose() {} };
  },
});
const evaluate = code => vm.runInContext(code, context);
evaluate(generated.stdout);

async function run(code) {
  evaluate(code);
  await setImmediate();
}

await run('el("play").onclick()');
await run("seek(22)");
assert.equal(evaluate("part"), 0);
assert.equal(evaluate("film.currentTime"), 5, "Forward seek must preserve the prompt and meaning demo");
await run('film.currentTime = 8; film.ended = true; film.fire("ended")');
assert.equal(evaluate("mode"), "example");
assert.equal(listener.enabled(), false, "Model stays outside active listening");
assert.equal(evaluate('el("mic").hidden'), false, "Protected narrative cannot hide the actual turn boundary");
await run("seek(20)");
assert.equal(evaluate("part"), 0, "Seeking past a live turn must not play unaccepted footage");
await run("promptAudio.ended = true; promptAudio.onended()");
assert.equal(evaluate("mode"), "waiting");
assert.equal(listener.enabled(), true);
assert.equal(micStarts, 1);
await run('el("parent").onclick(); el("parent").onclick()');
listener.onComplete();
assert.equal(evaluate("part"), 1);
assert.equal(evaluate("film.plays"), 3, "Guardian, late speech and duplicate input start the reaction once");
await run('film.currentTime = 9.95; film.fire("timeupdate"); seek(23)');
assert.equal(evaluate("film.currentTime"), 9.95, "The entire timed rescue remains locked during the reaction");
assert.equal(evaluate("caption.textContent"), "");
await run('film.currentTime = 10; film.fire("timeupdate")');
assert.equal(evaluate("caption.textContent"), "Thank you!");
assert.equal(evaluate('completedGates.has("I21")'), true);
await run("seek(6)");
await run('film.currentTime = 8; film.ended = true; film.fire("ended")');
assert.equal(evaluate("part"), 1, "Replaying dialogue does not replay an already completed model");
assert.equal(evaluate("promptAudio.plays"), 1);
await run('film.currentTime = 16; film.ended = true; film.fire("ended")');
await run('el("play").onclick()');
assert.equal(evaluate("completedGates.size"), 0, "A new viewing resets participation");
console.log("PASS S12 player navigation, protected I21 boundary, and gate completion (JavaScript harness)");
