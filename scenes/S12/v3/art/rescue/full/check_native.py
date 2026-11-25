#!/usr/bin/env python3
"""Inspect the live renderer's actual registered school-rescue exposures."""
from pathlib import Path
import json
import runpy
from PIL import Image, ImageDraw

here=Path(__file__).resolve().parent
v3=here.parents[2]
build=v3/"build"
work=Path("/workspace/scratch/s12-full/rescue-proof")
edition=work/"edition"
photo=runpy.run_path(str(v3/"art/render.py"))
engine=photo["ENGINE"]
whole=json.loads((edition/"edit.json").read_text())
cuts=[f"S12-C{n:02d}" for n in range(6,15)]
edit,ranges=engine["select"](whole,cuts)
by_cut={row["id"]:row for row in json.loads((build/"layout-rescue-full.json").read_text())}
layout=photo["resolve_layout"](edit,by_cut)
report,_=engine["photograph"](edit,layout,build/"art",edition/"audio",work/"probe.mp4",work/"registration-proof.json",False,False,check=True)
artwork=engine["camera_engine"]()["render_shots"].__globals__["Artwork"](build/"art")
examples=((6,0),(6,42),(6,68),(6,90),
          (7,36),(8,54),(9,45),(10,32),
          (11,110),(12,35),(12,125),(12,178),
          (13,36),(13,73),(13,123),(13,188),
          (14,40),(14,108),(14,159),(14,215))
canvas=Image.new("RGB",(1920,((len(examples)+3)//4)*300),(35,31,28))
labels=ImageDraw.Draw(canvas)
starts={row["id"]: row["first"] for row in edit["cuts"]}
for idx,(cut,offset) in enumerate(examples):
    shot=f"S12-C{cut:02d}"
    n=starts[shot]+offset
    row=next(item for item in report["rows"] if item["first"]<=n<item["end"])
    assert row["cut"]==shot,(shot,row["cut"])
    still=artwork.photograph(row["plate"],row["layers"]).convert("RGB").resize((480,270),Image.Resampling.LANCZOS)
    x,y=(idx%4)*480,(idx//4)*300
    canvas.paste(still,(x,y))
    labels.text((x+10,y+275),f"{shot}    frame +{offset}",fill=(249,239,219))
canvas.save(work/"school-rescue-exposures.jpg",quality=91)
print(f"Actual school rescue render registration: {len(report['cuts'])} cuts, {len(report['speech'])} synchronized lines and {len(report['rows'])} composited exposure intervals.")
