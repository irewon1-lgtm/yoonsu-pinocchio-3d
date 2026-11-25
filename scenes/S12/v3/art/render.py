#!/usr/bin/env python3
"""Photograph registered S12 whole-action cels using the existing S11 camera."""
from argparse import ArgumentParser
from copy import deepcopy
import json
from math import ceil, floor
from pathlib import Path
import runpy
import subprocess
from tempfile import TemporaryDirectory

HERE = Path(__file__).resolve().parent
V3 = HERE.parent
BUILD = V3 / "build"
ENGINE = runpy.run_path(str(HERE.parents[2] / "S11/v2/art/render.py"))
FPS = 24
LAYOUTS = ("layout-opening.json", "layout-rescue.json", "layout-fairy.json", "layout-human.json")


def read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def register_shots(build, cut_ids):
    layouts = {}
    for path in (build / name for name in LAYOUTS):
        if path.is_file():
            for shot in read(path):
                if shot["id"] in layouts:
                    raise ValueError(f"Duplicate approved layout for {shot['id']}")
                layouts[shot["id"]]=shot
    if missing:=set(cut_ids)-layouts.keys():
        raise ValueError(f"Shots lack accepted production drawings: {sorted(missing)}")
    return {key:layouts[key] for key in cut_ids}


def frame_marker(cut, name):
    if name == "start":
        return cut["first"]
    if name == "end":
        return cut["end"]
    if name.startswith("lead-point:"):
        window=cut["action_windows"]["lead"]
        return round((window["start"]+float(name.split(":")[1])*(window["end"]-window["start"]))*FPS)
    field, dialogue_id=name.split(":",1)
    if field not in ("before","after"):
        raise ValueError(f"Invalid timing marker: {name}")
    line=next((a for a in cut["audio"] if a["id"]==dialogue_id),None)
    if line is None:
        raise ValueError(f"Missing measured dialogue for {name}")
    if field=="before":
        return floor(line["start"]*FPS+1e-8)
    return ceil(line["end"]*FPS-1e-8)


def resolve_layout(edit, layout):
    layout=deepcopy(layout)
    for cut in edit["cuts"]:
        for layer in layout[cut["id"]]["layout"]:
            if not (markers:=layer.pop("span",None)):
                continue
            length=cut["end"]-cut["first"]
            begin,end=map(lambda marker:frame_marker(cut,marker),markers)
            if not cut["first"]<=begin<end<=cut["end"]:
                raise ValueError(f"{cut['id']} has out-of-bound action markers {markers}")
            layer["start"]=(begin-cut["first"])/length
            layer["end"]=(end-cut["first"])/length
    return layout


def draft_opening():
    # This 23s internal reel is used only to inspect drawing exposures while approved takes render.
    cuts=[]
    first=0
    for index,(frames,lead,tail) in enumerate(((120,36,12),(192,48,0),(132,48,12),(144,48,0),(156,48,12)),1):
        end=first+frames
        cuts.append({"id":f"S12-C{index:02}","first":first,"end":end,
                     "audio": [{"id":"S12-N007","start":(first+48)/FPS,"end":(first+82)/FPS}]
                              if index==5 else [],
                     "action_windows":{"lead":{"start":first/FPS,"end":(first+lead)/FPS},
                                       "story":{"start":first/FPS,"end":end/FPS},
                                       "tail":{"start":(end-tail)/FPS,"end":end/FPS},"between":[]}})
        first=end
    return {"fps":FPS,"frames":first,"duration":first/FPS,"cuts":cuts,"events":[],"silent_proof":True}


def photograph_segments(edit, cut_ids, registered, build, voices, target, mix, subs):
    """Photograph in bounded groups, then use the existing single-mix muxer."""
    report={"fps":FPS,"frames":edit["frames"],"frame_size":[1280,720],"cuts":[],
            "rows":[],"speech":[],"plates":{},"mouths_animated":True,
            "speech_render_mode":"whole-figure","segments":[],"media_encoded":True}
    segments=[]
    offset=0
    cache=build/"photographed-sections"
    cache.mkdir(exist_ok=True)
    for first in range(0,len(cut_ids),4):
        section,_=ENGINE["select"](edit,cut_ids[first:first+4])
        rows=resolve_layout(section,registered)
        local=cache/f"{section['cuts'][0]['id']}-{section['cuts'][-1]['id']}.mp4"
        photos,_=ENGINE["photograph"](section,rows,build/"art",voices,local,
                                      local.with_suffix(".json"),True,False)
        ENGINE["archive_rows"](report,photos,offset)
        report["segments"].append({"first":offset,"frames":section["frames"],
                                    "picture_source_sha256":photos["input_sha256"]})
        segments.append((local,section["frames"]))
        offset+=section["frames"]
    if offset!=edit["frames"] or cut_ids!=report["cuts"]:
        raise ValueError("Segment ledger lost story frames or cuts")
    ENGINE["merge"](target,segments,edit,mix,subs)
    return report


def photograph(edit, bounds, build, voices, target, mix, subs, draft=False, segmented=False):
    cut_ids=[cut["id"] for cut in edit["cuts"]]
    expected=list(range(int(cut_ids[0][-2:]),int(cut_ids[-1][-2:])+1))
    if [int(cut[-2:]) for cut in cut_ids]!=expected:
        raise ValueError("A media file must cover one contiguous sequence of authored cuts")
    registered=register_shots(build,cut_ids)
    target.parent.mkdir(parents=True,exist_ok=True)
    with TemporaryDirectory(prefix="s12-photo-",dir=target.parent) as directory:
        scratch=Path(directory)
        if (segmented or len(cut_ids)>5) and not draft:
            final=scratch/"story.mp4"
            report=photograph_segments(edit,cut_ids,registered,build,voices,final,mix,subs)
        else:
            photo=scratch/"photo.mp4"
            receipt=scratch/"photo.json"
            ledger=resolve_layout(edit,registered)
            ENGINE["photograph"](edit,ledger,build/"art",voices,photo,receipt,False,draft,mix)
            if subs and subs.is_file():
                final=scratch/"with-closed-captions.mp4"
                subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-xerror","-i",str(photo),
                                "-i",str(subs),"-map","0:v:0","-map","0:a:0","-map","1:s:0","-c","copy",
                                "-c:s","mov_text","-metadata:s:s:0","language=eng",
                                "-movflags","+faststart",str(final)],check=True)
            else:
                final=photo
            report=read(receipt)
        final.replace(target)
        report.update(output_sha256=ENGINE["digest"](target),scope=bounds,source_clock="internal planned rehearsal"
                      if draft else "actual selected PCM edit")
        ENGINE["dump"](target.with_suffix(".json"),report)


def main():
    cli=ArgumentParser(description=__doc__)
    origin=cli.add_mutually_exclusive_group(required=True)
    origin.add_argument("--edition",type=Path,help="Measured edit, mix and subtitles from the S12 editor")
    origin.add_argument("--draft-opening",action="store_true",help="Internal no-audio art check")
    cli.add_argument("--build",type=Path,default=BUILD)
    cli.add_argument("--voices",type=Path,help="Override the measured edition's exact PCM stems")
    cli.add_argument("--target",type=Path,required=True)
    cli.add_argument("--segmented",action="store_true",help="Reuse exact verified picture segments")
    args=cli.parse_args()
    if args.draft_opening:
        edit=draft_opening()
        mix=subs=None
    else:
        edit=read(args.edition/"edit.json")
        mix=args.edition/"mix.wav"
        subs=args.edition/"subtitles.srt"
        if not mix.is_file() or not subs.is_file():
            cli.error("Media edition requires the measured PCM mix and caption file")
        if sum(cut["end"]-cut["first"] for cut in edit["cuts"])!=edit["frames"]:
            cli.error("Measured clock and shot ledger disagree")
        if edit["cuts"][0]["id"]=="S12-C01" and edit["cuts"][-1]["id"]=="S12-C50" and (
                len(edit.get("events",[]))!=10 or edit["frames"]<360*FPS):
            cli.error("Full video requires all 10 gates and at least 360s excluding cue models and wait")
    scope=[edit["cuts"][edge]["id"] for edge in (0,-1)]
    voices=args.voices or (args.build/"voices" if args.draft_opening else args.edition/"audio")
    photograph(edit,scope,args.build,voices,args.target,mix,subs,args.draft_opening,args.segmented)


if __name__=="__main__":
    main()
