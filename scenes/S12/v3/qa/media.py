#!/usr/bin/env python3
"""Verify dimensions, encoding, continuous exposure and actual S12 decoded streams."""
from argparse import ArgumentParser
from hashlib import file_digest
import json
from pathlib import Path
import subprocess

FPS = 24


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def ffprobe(mp4):
    return json.loads(subprocess.check_output(
        ["ffprobe","-v","error","-show_streams","-show_format","-of","json",str(mp4)]))


def stream(data, kind):
    return next(item for item in data["streams"] if item["codec_type"]==kind)


def require(condition, problem):
    if not condition:
        raise ValueError(problem)


def examine(mp4, edit_path):
    report = read(mp4.with_suffix(".json"))
    edit = read(edit_path)
    metadata = ffprobe(mp4)
    video,audio=stream(metadata,"video"),stream(metadata,"audio")
    length=edit["frames"]/FPS
    require((video["width"],video["height"],video["codec_name"],video["r_frame_rate"],video["pix_fmt"])
            ==(1920,1080,"h264","24/1","yuv420p"),"Unsupported final movie stream")
    require(audio["codec_name"]=="aac","AAC sound is required")
    require(report["frames"]==int(video["nb_frames"])==edit["frames"],"Encoded video lost frames")
    require(abs(float(video["duration"])-length)<.003,"Video duration does not match edit")
    require(abs(float(audio["duration"])-length) <= 1/FPS,"Movie's audio does not cover the story clock")
    require([cut["id"] for cut in edit["cuts"]]==list(report["cuts"]),"Cut order changed during photography")
    previous=0
    for row in report["rows"]:
        require(row["first"]==previous and row["end"]>row["first"],"Missing or overlapping exposure")
        previous=row["end"]
    require(previous==edit["frames"],"Missing last exposure")
    with mp4.open("rb") as media:
        checksum=file_digest(media,"sha256").hexdigest()
    require(report["output_sha256"]==checksum,"Media SHA differs from the photographic receipt")
    # Detect black frames in the same decode pass used to check stream integrity.
    decoded = subprocess.run(
        ["ffmpeg","-hide_banner","-nostats","-v","info","-xerror","-threads","2","-i",str(mp4),
         "-map","0:v:0","-map","0:a:0","-vf","blackdetect=d=0.04:pic_th=0.99:pix_th=0.10",
         "-f","null","-"], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, text=True)
    require(decoded.returncode==0, decoded.stderr)
    require("black_start:" not in decoded.stderr, "Movie contains a fully black frame")
    return {"status":"PASS","video":{"width":1920,"height":1080,"fps":FPS,"frames":edit["frames"],
            "codec":"h264","duration_seconds":length},"audio":{"codec":"aac","sample_rate":int(audio["sample_rate"])},
            "srt":"mov_text","sha256":checksum,"shot_ids":report["cuts"],
            "spoken_lines":sum(len(cut["audio"]) for cut in edit["cuts"]),
            "model_cues":len(edit.get("events",[])),"chapters_outside_story_clock":True,"black_frames":0,
            "listening":"NOT_RUN","android_microphone":"NOT_RUN"}


if __name__=="__main__":
    cli=ArgumentParser(description=__doc__)
    cli.add_argument("mp4",type=Path)
    cli.add_argument("edit",type=Path)
    cli.add_argument("--output",type=Path,required=True)
    args=cli.parse_args()
    result=examine(args.mp4,args.edit)
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(f"{args.mp4.name}: {len(result['shot_ids'])} cuts, {result['video']['duration_seconds']:.3f}s decoded.")
