#!/usr/bin/env python3
"""Photograph registered S12 whole-action cels using the existing S11 camera."""
from argparse import ArgumentParser
from copy import deepcopy
from hashlib import sha256
import json
from math import ceil, floor
from pathlib import Path
import runpy
import subprocess
from tempfile import TemporaryDirectory

from PIL import Image

HERE = Path(__file__).resolve().parent
V3 = HERE.parent
BUILD = V3 / "build"
ENGINE = runpy.run_path(str(HERE.parents[2] / "S11/v2/art/render.py"))
FPS = 24
LAYOUTS = ("layout-opening.json", "layout-rescue-full.json", "layout-rescue.json",
           "layout-fairy.json", "layout-transform.json", "layout-hug.json", "layout-hands.json",
           "layout-ending.json")


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


def picture_timing(edit):
    def samples(time):
        return round(time * 24000)

    cuts = [(cut["id"], cut["first"], cut["end"],
             [(line["id"], line["speaker"], samples(line["start"]), samples(line["end"]))
              for line in cut["audio"]]) for cut in edit["cuts"]]
    return cuts, [(gate["id"], gate["frame"]) for gate in edit["events"]]


def reuse_pictures(section, prior_picture, prior_edition, voices, output):
    prior = read(prior_edition)
    evidence = read(prior_picture.with_suffix(".json"))
    if picture_timing(section) != picture_timing(prior) or evidence["frames"] != section["frames"]:
        raise ValueError(f"Reused picture timing differs from the measured edit: {prior_picture}")
    ids = [cut["id"] for cut in section["cuts"]]
    if evidence["cuts"] != ids or ENGINE["digest"](prior_picture) != evidence["output_sha256"]:
        raise ValueError(f"Reused picture does not match its checked exposure report: {prior_picture}")
    for cut in section["cuts"]:
        for line in cut["audio"]:
            name = line["id"] + ".wav"
            if ENGINE["digest"](voices/name) != ENGINE["digest"](prior_edition.parent/"audio"/name):
                raise ValueError(f"The measured spoken take changed for {name}")
    if not output.is_file():
        pending = output.with_suffix(".pending.mp4")
        subprocess.run(["ffmpeg","-hide_banner","-v","error","-xerror","-y","-i",str(prior_picture),
                        "-map","0:v:0","-c","copy","-video_track_timescale","24000",
                        "-movflags","+faststart",str(pending)],check=True)
        pending.replace(output)
    return evidence


def picture_groups(edit, cut_ids, prior_pictures):
    inherited = {}
    for path, edition in prior_pictures:
        ids = [cut["id"] for cut in read(edition)["cuts"]]
        first = cut_ids.index(ids[0])
        if cut_ids[first:first+len(ids)] != ids or first in inherited:
            raise ValueError(f"Reused picture range is outside this edit: {path}")
        inherited[first] = (ids, (path, edition))
    cursor = 0
    while cursor < len(cut_ids):
        if cursor in inherited:
            ids, source = inherited[cursor]
        else:
            stop = min((start for start in inherited if start>cursor), default=len(cut_ids))
            ids, source = cut_ids[cursor:min(stop,cursor+4)], None
        yield ENGINE["select"](edit,ids)[0], source
        cursor += len(ids)


def optical_frames(report, specs, edit, photos):
    cameras = {}
    for cut in edit["cuts"]:
        spec = specs[cut["id"]]
        cues = spec.get("camera_cues")
        if not cues:
            continue
        count = cut["end"]-cut["first"]
        starts = [cue["frame"] for cue in cues]
        if "@" in spec["plate"] or starts[0] != 0 or sorted(set(starts)) != starts or starts[-1] >= count:
            raise ValueError(f"Camera cues must start at frame 0 on an uncropped plate: {cut['id']}")
        views = []
        for cue in cues:
            x,y,width = cue["crop"]
            if any(type(value) is not int for value in (x,y,width)) or (
                    x<0 or y<0 or width<2 or x+width>1280 or y+round(width*9/16)>720):
                raise ValueError(f"Camera crop lies outside the approved stage: {cut['id']}")
            if views:
                first = len(views)-1
                distance = cue["frame"]-first
                source = views[first]
                for index in range(1,distance):
                    views.append(tuple(round(a+(b-a)*index/distance) for a,b in zip(source,cue["crop"]))
                                 if cue.get("interpolate") else source)
            views.append(tuple(cue["crop"]))
        views.extend([views[-1]]*(count-len(views)))
        cameras[cut["id"]] = (cut["first"], views)
        report["plates"][cut["id"]]["camera_cues"] = cues

    rows = []
    for row in report["rows"]:
        if row["cut"] not in cameras:
            rows.append(row)
            continue
        offset,views = cameras[row["cut"]]
        first = row["first"]
        while first<row["end"]:
            crop = views[first-offset]
            end = first+1
            while end<row["end"] and views[end-offset]==crop:
                end+=1
            x,y,width = crop
            box = (x,y,x+width,y+round(width*9/16))
            active = {cue["speaker"] for cue in report["speech"] if cue["cut"]==row["cut"]
                      and cue["first"]<end and cue["end"]>first}
            for layer in row["layers"]:
                if layer.get("speaker") not in active or not layer.get("mouth_bounds"):
                    continue
                left,top,right,bottom = layer["mouth_bounds"]
                if not (x<=left<right<=box[2] and y<=top<bottom<=box[3]):
                    raise ValueError(f"Camera crop hides {layer['speaker']} at {row['cut']} frame {first-offset}")
            key = row["photo"] if crop==(0,0,1280) else sha256(
                f"{row['photo']}:{crop}".encode()).hexdigest()[:24]
            target = photos/(key+".png")
            if not target.is_file():
                with Image.open(photos/(row["photo"]+".png")) as source:
                    source.crop(box).resize((1280,720),Image.Resampling.LANCZOS).save(target,compress_level=2)
            rows.append(row | {"first":first,"end":end,"photo":key,"camera_crop":crop})
            first=end
    report["rows"] = rows


def photograph_optical(section, specs, art, voices, output):
    layers = [{"id":cut["id"],"plate":specs[cut["id"]]["plate"],
               "layout":[ENGINE["timed_layer"](cut,row) for row in specs[cut["id"]]["layout"]],
               "camera_cues":specs[cut["id"]].get("camera_cues",[])} for cut in section["cuts"]]
    fingerprint = sha256((ENGINE["input_fingerprint"](art,section,layers,voices,False)
                          +ENGINE["digest"](Path(__file__))).encode()).hexdigest()
    receipt = output.with_suffix(".json")
    if output.is_file() and receipt.is_file():
        prior = read(receipt)
        if prior.get("input_sha256")==fingerprint and prior.get("output_sha256")==ENGINE["digest"](output):
            return prior
    with TemporaryDirectory(prefix="s12-optical-",dir=output.parent) as directory:
        photos=Path(directory)
        report=ENGINE["camera_engine"]()["render_shots"](section,layers,art,voices,photos,silent=False)
        optical_frames(report,specs,section,photos)
        pending=photos/"photographed.mp4"
        ENGINE["CAMERA"]["encode"](report,section,photos,pending)
        pending.replace(output)
    report.update(input_sha256=fingerprint,output_sha256=ENGINE["digest"](output),media_encoded=True)
    ENGINE["dump"](receipt,report)
    print(f"Photographed {section['cuts'][0]['id']}–{section['cuts'][-1]['id']}: {section['frames']} frames.",flush=True)
    return report


def merge_picture_streams(target, segments, edit, mix, subs):
    # The inherited encoder can use a 12288 video timescale. Make every
    # stream use the same ticks before packet-copy concatenation.
    normal = []
    for index,(path,frames) in enumerate(segments):
        time_base = subprocess.check_output(["ffprobe","-v","error","-select_streams","v:0",
            "-show_entries","stream=time_base","-of","default=nw=1:nk=1",str(path)],text=True).strip()
        if time_base!="1/24000":
            converted = target.parent/f"clocked-segment-{index:02}.mp4"
            subprocess.run(["ffmpeg","-hide_banner","-v","error","-xerror","-y","-i",str(path),
                "-map","0:v:0","-c","copy","-video_track_timescale","24000",str(converted)],check=True)
            path=converted
        normal.append((path,frames))
    ENGINE["merge"](target,normal,edit,mix,subs)


def photograph_segments(edit, cut_ids, registered, build, voices, target, mix, subs, prior_pictures):
    """Photograph in bounded groups, then use the existing single-mix muxer."""
    report={"fps":FPS,"frames":edit["frames"],"frame_size":[1280,720],"cuts":[],
            "rows":[],"speech":[],"plates":{},"mouths_animated":True,
            "speech_render_mode":"whole-figure","segments":[],"media_encoded":True}
    segments=[]
    offset=0
    cache=build/"photographed-sections"
    cache.mkdir(exist_ok=True)
    for section, source in picture_groups(edit,cut_ids,prior_pictures):
        prefix=f"{section['cuts'][0]['id']}-{section['cuts'][-1]['id']}"
        if source:
            picture, edition = source
            local=cache/f"{prefix}-reuse-{ENGINE['digest'](picture)[:12]}.mp4"
            photos=reuse_pictures(section,picture,edition,voices,local)
        else:
            rows=resolve_layout(section,registered)
            local=cache/f"{prefix}.mp4"
            if any(rows[cut["id"]].get("camera_cues") for cut in section["cuts"]):
                photos=photograph_optical(section,rows,build/"art",voices,local)
            else:
                photos,_=ENGINE["photograph"](section,rows,build/"art",voices,local,
                                              local.with_suffix(".json"),True,False)
        ENGINE["archive_rows"](report,photos,offset)
        report["segments"].append({"first":offset,"frames":section["frames"],
                                   "picture_source_sha256":photos.get("input_sha256", photos["output_sha256"]),
                                   "reused_picture":bool(source)})
        segments.append((local,section["frames"]))
        offset+=section["frames"]
    if offset!=edit["frames"] or cut_ids!=report["cuts"]:
        raise ValueError("Segment ledger lost story frames or cuts")
    merge_picture_streams(target,segments,edit,mix,subs)
    return report


def photograph(edit, bounds, build, voices, target, mix, subs, draft=False, segmented=False, prior_pictures=()):
    cut_ids=[cut["id"] for cut in edit["cuts"]]
    expected=list(range(int(cut_ids[0][-2:]),int(cut_ids[-1][-2:])+1))
    if [int(cut[-2:]) for cut in cut_ids]!=expected:
        raise ValueError("A media file must cover one contiguous sequence of authored cuts")
    registered=register_shots(build,cut_ids)
    target.parent.mkdir(parents=True,exist_ok=True)
    with TemporaryDirectory(prefix="s12-photo-",dir=target.parent) as directory:
        scratch=Path(directory)
        if (prior_pictures or segmented or len(cut_ids)>5
                or any(shot.get("camera_cues") for shot in registered.values())) and not draft:
            final=scratch/"story.mp4"
            report=photograph_segments(edit,cut_ids,registered,build,voices,final,mix,subs,prior_pictures)
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
    cli.add_argument("--prior-picture",action="append",nargs=2,type=Path,default=[],
                     metavar=("MP4","EDIT_JSON"),help="Copy an already verified picture range at identical timing")
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
    photograph(edit,scope,args.build,voices,args.target,mix,subs,args.draft_opening,args.segmented,args.prior_picture)


if __name__=="__main__":
    main()
