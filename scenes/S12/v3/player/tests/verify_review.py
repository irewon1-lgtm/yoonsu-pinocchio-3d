"""Exercise a real, self-contained S12 cut review with Chromium media decoding."""

import argparse
import json
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from shutil import copyfileobj
from threading import Thread

from playwright.sync_api import Error, TimeoutError, sync_playwright


@contextmanager
def local_review(html):
    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path != "/review.html":
                self.send_error(404)
                return
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(html.stat().st_size))
            self.end_headers()
            with html.open("rb") as source:
                copyfileobj(source, self.wfile)

        def log_message(self, format, *args):
            pass

    with ThreadingHTTPServer(("127.0.0.1", 0), Handler) as server:
        runner = Thread(target=server.serve_forever, daemon=True)
        runner.start()
        try:
            yield f"http://127.0.0.1:{server.server_port}/review.html"
        finally:
            server.shutdown()
            runner.join()


def verify(html, chromium, output, microphone=None):
    errors = []
    requests = []
    gates = []
    with local_review(html) as url, sync_playwright() as playwright:
        flags = ["--no-sandbox"]
        if microphone:
            flags.extend(["--use-fake-device-for-media-stream",
                          f"--use-file-for-fake-audio-capture={microphone.resolve()}"])
        browser = playwright.chromium.launch(executable_path=chromium, args=flags)
        context = browser.new_context(viewport={"width": 1280, "height": 800})
        simulated = bool(microphone)
        if simulated:
            try:
                context.grant_permissions(["microphone"], origin=url.rsplit("/", 1)[0])
            except Error:
                simulated = False
        page = context.new_page()
        page.on("pageerror", lambda error: errors.append(str(error)))
        page.on("request", lambda request: requests.append(request.url))
        page.goto(url)
        context.set_offline(True)
        page.get_by_role("button", name="이야기 시작").click()
        description = page.evaluate("({title:document.title, clips:MEDIA.parts.map(({id, cue})=>({id, cue})), excerpt:MEDIA.reviewExcerpt})")
        for number, clip in enumerate(description["clips"]):
            page.wait_for_function("n=> part===n && mode==='playing' && film.readyState>=2 && film.currentTime>0", arg=number)
            assert page.evaluate("film.videoWidth === 1920 && film.videoHeight === 1080"), f"Clip {number} resolution"
            if number:
                page.wait_for_function("pendingReaction===null")
            if not clip.get("id"):
                continue
            page.evaluate("""() => {
                window.modelEvents = [];
                promptAudio.addEventListener('playing', () => modelEvents.push(['playing', promptAudio.currentTime, performance.now()]), {once:true});
                promptAudio.addEventListener('ended', () => modelEvents.push(['ended', promptAudio.currentTime, performance.now()]), {once:true});
                window.micTrace = [];
                const observe = () => {
                    if (['example', 'waiting', 'loading', 'playing'].includes(mode)) {
                        const state = `${part}:${mode}:${micState}`;
                        if (state !== micTrace.at(-1)?.state) micTrace.push({state, time:performance.now()});
                    }
                    window.micTraceFrame = requestAnimationFrame(observe);
                };
                window.micTraceFrame = requestAnimationFrame(observe);
                film.currentTime = film.duration - 0.12;
            }""")
            page.wait_for_function("mode==='waiting' && modelEvents.some(([event])=>event==='ended')")
            assert page.locator("#line").inner_text() == clip["cue"], clip["id"]
            events = page.evaluate("modelEvents")
            assert [name for name, _, _ in events] == ["playing", "ended"], clip["id"]
            assert events[1][1] > events[0][1], clip["id"]
            gate = {"id": clip["id"], "example_ended_seconds": events[1][1], "guardian": "NOT_RUN"}
            if simulated:
                try:
                    page.wait_for_function("n => part === n+1 || ['error','off'].includes(micState)",
                                           arg=number, timeout=15000)
                except TimeoutError:
                    pass
                trace = page.evaluate("micTrace")
                assert not any(row["state"].startswith(f"{number}:example:") and
                               row["state"].split(":")[-1] in ("listening", "speaking", "settling")
                               for row in trace), gate
                active = {row["state"].split(":")[-1]: row["time"] for row in trace
                          if row["state"].startswith(f"{number}:waiting:")}
                gate["simulated_microphone"] = "NOT_RUN" if "error" in active or "off" in active else "FAIL"
                if page.evaluate("part") == number + 1:
                    assert all(key in active for key in ("listening", "speaking", "settling")), gate
                    assert events[1][2] <= active["listening"] <= active["speaking"] <= active["settling"], gate
                    reaction = next((row["time"] for row in trace
                                     if row["state"].startswith(f"{number + 1}:")), None)
                    if reaction is None:
                        reaction = page.evaluate("performance.now()")
                    gate["simulated_microphone"] = "PASS"
                    gate["mic_ms_from_actual_model_end"] = {
                        name: round(active[name] - events[1][2]) for name in ("listening", "speaking", "settling")
                    }
                    gate["settling_to_reaction_ms"] = round(reaction - active["settling"])
            if gate.get("simulated_microphone") != "PASS":
                page.locator("#parent").click()
                gate["guardian"] = "PASS"
            page.evaluate("cancelAnimationFrame(micTraceFrame)")
            gates.append(gate)
        assert not errors, errors
        assert [request for request in requests if request.startswith(("https://", "http://"))] == [url]
        if output:
            page.screenshot(path=output)
        browser.close()
    return {
        "excerpt": description["excerpt"],
        "chromium_clips_decoded": len(description["clips"]),
        "gates": gates,
        "transport": "self-contained HTML served on loopback, then browser offline",
        "android_device_microphone": "NOT_RUN",
        "method": "Decoded every chapter, positioned near each prompt end, played the real models and reactions",
        "chromium_microphone": "fake PCM file in a scoped browser session" if simulated else "NOT_RUN",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("html", type=Path)
    parser.add_argument("--chromium", default="/usr/bin/chromium")
    parser.add_argument("--screenshot", type=Path)
    parser.add_argument("--fake-mic", type=Path, help="Test-only PCM waveform supplied to Chromium's simulated device")
    args = parser.parse_args()
    print(json.dumps(verify(args.html, args.chromium, args.screenshot, args.fake_mic), indent=2))
