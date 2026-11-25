#!/usr/bin/env python3
"""Pack new S12 registered drawings into transparent, unscaled atlas pages."""
from argparse import ArgumentParser
from hashlib import file_digest
import json
from pathlib import Path

from PIL import Image

BUILD = Path(__file__).resolve().parents[1] / "build"
GUTTER = 3


def sha(path):
    with path.open("rb") as handle:
        return file_digest(handle, "sha256").hexdigest()


def export(root, output, edge):
    ledger = {"format":"s12.registered-rgba-page.v1","page_edge_px":edge,"gutter_px":GUTTER,"levels":[]}
    output.mkdir(parents=True,exist_ok=True)
    for registry in sorted((root/"cels").glob("S12*/registration.json")):
        name = registry.parent.name
        src = json.loads(registry.read_text(encoding="utf-8"))
        dst = {"name":name,"reference_height":src["reference_height"],"source_registry_sha256":sha(registry),
               "pages":[],"cells":[]}
        sheet=Image.new("RGBA",(edge,edge))
        x=y=GUTTER
        row_height=0
        page=1

        def save_page():
            texture = output/f"{name}-{page:02d}.png"
            sheet.save(texture,compress_level=4)
            dst["pages"].append({"number":page,"png":texture.name,"sha256":sha(texture)})

        for index, pose in enumerate(src["poses"]):
            for viseme, cell in [("body",pose),*pose.get("viseme_cels",{}).items()]:
                source = root/cell["file"]
                if cell.get("sha256") and sha(source)!=cell["sha256"]:
                    raise ValueError(f"Registered source changed: {source}")
                with Image.open(source) as frame:
                    if frame.mode!="RGBA" or frame.size!=tuple(cell["size"]):
                        raise ValueError(f"Invalid registered cel shape for {source}")
                    left, top, right, bottom = frame.getchannel("A").getbbox()
                    width, height = right-left, bottom-top
                    if width+2*GUTTER>edge or height+2*GUTTER>edge:
                        raise ValueError(f"Cel exceeds an atlas page: {source}")
                    if x+width+GUTTER>edge:
                        x=GUTTER
                        y+=row_height+GUTTER*2
                        row_height=0
                    if y+height+GUTTER>edge:
                        save_page()
                        sheet=Image.new("RGBA",(edge,edge))
                        x=y=GUTTER
                        row_height=0
                        page+=1
                    sheet.paste(frame.crop((left,top,right,bottom)),(x,y))
                anchors={key:[point[0]-left,point[1]-top] for key,point in cell.get("anchors",{}).items()}
                dst["cells"].append({"index":index,"viseme":viseme,"page":page,
                    "rect":[x,y,width,height],"trim":[left,top,right,bottom],
                    "untrimmed_size":cell["size"],"anchors":anchors,"source":cell["file"],
                    "source_sha256":cell.get("sha256")})
                row_height=max(height,row_height)
                x+=width+GUTTER*2
        if dst["cells"]:
            save_page()
            ledger["levels"].append(dst)
    if not ledger["levels"]:
        raise ValueError("No current S12 art levels were staged")
    manifest=output/"atlas.json"
    manifest.write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    return ledger


if __name__=="__main__":
    args=ArgumentParser(description=__doc__)
    args.add_argument("--art",type=Path,default=BUILD/"art")
    args.add_argument("--out",type=Path,required=True)
    args.add_argument("--page",type=int,default=2048)
    options=args.parse_args()
    result=export(options.art,options.out,options.page)
    print(f"{sum(len(level['cells']) for level in result['levels'])} actual RGBA cells at native resolution.")
