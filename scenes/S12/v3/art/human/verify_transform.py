"""Check C30 registered artwork and its decoded camera cut."""
from argparse import ArgumentParser
from hashlib import sha256
from pathlib import Path
import json
import subprocess

import numpy as np
from PIL import Image
from normalize import SOURCE
from transform import ART, WOOD


def pose(path):
    with Image.open(path) as image:
        return image.convert("RGBA").tobytes()


def probe(path):
    return json.loads(subprocess.check_output(["ffprobe","-v","error","-select_streams",
        "v:0","-count_frames","-show_entries","stream=width,height,nb_read_frames,r_frame_rate,codec_name",
        "-of","json",str(path)]))["streams"][0]


def decoded(path, timestamp=None):
    seeks = ["-ss", str(timestamp)] if timestamp is not None else []
    data = subprocess.check_output(["ffmpeg","-v","error",*seeks,"-i",str(path),"-frames:v","1",
         "-vf","scale=384:216","-f","rawvideo","-pix_fmt","rgb24","pipe:1"])
    if len(data) != 384*216*3:
        raise ValueError(f"Missing decoded frame for {path}")
    return np.frombuffer(data,dtype=np.uint8).astype(np.int16)


def verify(film, edition, previous):
    vis = json.loads(film.with_suffix(".json").read_text())
    media = probe(film)
    assert media["nb_read_frames"] == "244" and media["r_frame_rate"] == "24/1"
    assert (media["width"],media["height"]) == (1920,1080)
    file = ART / "cels/S12T-metamorph"
    assert pose(WOOD) == pose(file / "000.png")
    assert pose(file / "095.png") == pose(SOURCE / "closed.png")
    track = lambda row: next(l for l in row["layers"] if l["track"] == "Pinocchio-transformation")
    assert all(track(row)["root"] == [561,643] and track(row)["height"] == 236 for row in vis["rows"])
    assert vis["rows"][0]["camera_crop"] == [420,271,694]
    assert vis["rows"][-1]["camera_crop"] == [440,399,297]
    edit = json.loads(edition.read_text())
    narration = edit["cuts"][0]["audio"][0]
    assert narration["id"] == "S12-U028" and round(24*narration["start"]) == 144
    assert pose(file / "068.png") == pose(SOURCE / "closed.png")
    previous_frame = decoded(previous,99.374)
    new_frame = decoded(film)
    difference = float(np.abs(previous_frame-new_frame).mean())
    if difference > 5.0:
        raise ValueError(f"Unexpected C29/C30 handoff difference after video decoding: {difference:.3f}")
    return {"cut":"S12-C30","output":str(film),
            "output_sha256":sha256(film.read_bytes()).hexdigest(),"decoded_video":media,
            "exact_original_first_and_final_cel_pixels":True,
            "preserved_child_stage_root_all_frames":[561,643],
            "opening_reuses_c29_crop":vis["rows"][0]["camera_crop"],
            "end_hands_face_crop":vis["rows"][-1]["camera_crop"],
            "distinct_camera_crops":len({tuple(row["camera_crop"]) for row in vis["rows"]}),
            "prior_last_vs_first_decoded_rgb_mean_absolute_error_0_255":round(difference,4),
            "human_form_complete_frame":136,"narration_starts_frame":144,"narration_id":narration["id"],
            "stage_cells":len({track(row)["cel"] for row in vis["rows"]})}


def main():
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("film",type=Path)
    parser.add_argument("edit",type=Path)
    parser.add_argument("previous",type=Path)
    parser.add_argument("output",type=Path)
    args = parser.parse_args()
    proof = verify(args.film,args.edit,args.previous)
    args.output.write_text(json.dumps(proof,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps(proof,ensure_ascii=False))


if __name__ == "__main__":
    main()
