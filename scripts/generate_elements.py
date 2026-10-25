#!/usr/bin/env python3
"""Generate the repository's original, self-contained scientific SVG elements.

Python standard library only. Optional PNG rendering uses an installed Inkscape.
No scientific data are represented by the illustrative sample/trajectory elements.
"""
from __future__ import annotations

import argparse
import html
import json
import math
from pathlib import Path
import random
import shutil
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "elements"
WIDTH, HEIGHT = 240, 160
COLORS = {
    "ink": "#334155", "muted": "#64748B", "line": "#94A3B8",
    "blue": "#7395B6", "blue_light": "#E8F0F7", "blue_dark": "#416789",
    "green": "#81A99B", "green_light": "#EAF3EF", "green_dark": "#4D7B69",
    "orange": "#D1A077", "orange_light": "#FBF0E6", "orange_dark": "#9B6843",
    "paper": "#FFFFFF", "gray_light": "#F1F5F9",
}
FONT = "Arial, Helvetica, sans-serif"


def attrs(**values):
    return " ".join(f'{k.replace("_", "-")}="{html.escape(str(v), quote=True)}"' for k, v in values.items() if v is not None)


def text(x, y, label, size=16, fill=None, weight=None, anchor="middle"):
    return f'<text {attrs(x=x, y=y, font_family=FONT, font_size=size, fill=fill or COLORS["ink"], font_weight=weight, text_anchor=anchor)}>{html.escape(label)}</text>'


def rect(x, y, w, h, fill=None, stroke=None, rx=8, sw=1.8):
    return f'<rect {attrs(x=x, y=y, width=w, height=h, rx=rx, fill=fill or COLORS["blue_light"], stroke=stroke or COLORS["blue_dark"], stroke_width=sw)}/>'


def circle(x, y, r, fill=None, stroke=None, sw=1.8):
    return f'<circle {attrs(cx=x, cy=y, r=r, fill=fill or COLORS["paper"], stroke=stroke or COLORS["ink"], stroke_width=sw)}/>'


def line(x1, y1, x2, y2, stroke=None, sw=2.2, dash=None):
    return f'<line {attrs(x1=x1, y1=y1, x2=x2, y2=y2, stroke=stroke or COLORS["ink"], stroke_width=sw, stroke_linecap="round", stroke_dasharray=dash)}/>'


def path(d, stroke=None, fill="none", sw=2.2, dash=None):
    return f'<path {attrs(d=d, stroke=stroke or COLORS["ink"], fill=fill, stroke_width=sw, stroke_linecap="round", stroke_linejoin="round", stroke_dasharray=dash)}/>'


def polygon(points, fill=None, stroke=None, sw=1.8):
    return f'<polygon {attrs(points=points, fill=fill or COLORS["blue_light"], stroke=stroke or COLORS["blue_dark"], stroke_width=sw, stroke_linejoin="round")}/>'


def head(x, y, angle=0, color=None, size=8):
    color = color or COLORS["ink"]
    back_x, back_y = x - size * math.cos(angle), y - size * math.sin(angle)
    side = size * .55
    px, py = -math.sin(angle) * side, math.cos(angle) * side
    points = f"{x:.2f},{y:.2f} {back_x+px:.2f},{back_y+py:.2f} {back_x-px:.2f},{back_y-py:.2f}"
    return polygon(points, fill=color, stroke=color, sw=.4)


def arrow(x1, y1, x2, y2, color=None, dash=None, both=False):
    a = math.atan2(y2-y1, x2-x1)
    color = color or COLORS["ink"]
    # Explicit arrowheads remain individually editable in Illustrator.
    s = line(x1, y1, x2-5*math.cos(a), y2-5*math.sin(a), color, dash=dash)
    s += head(x2, y2, a, color)
    return s + (head(x1, y1, a+math.pi, color) if both else "")


def svg_document(body, title, desc):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{HEIGHT}" '
            f'viewBox="0 0 {WIDTH} {HEIGHT}" role="img">\n'
            f'<title>{html.escape(title)}</title>\n<desc>{html.escape(desc)}</desc>\n'
            f'<g id="element">{body}</g>\n</svg>\n')


def create_items():
    items = []

    def add(id_, zh, en, category, tags, body, notes=""):
        items.append(dict(id=id_, title_zh=zh, title_en=en, category=category,
                          tags=tags, body=body, notes=notes))

    add("module-block", "通用模块", "Module block", "modules", ["module", "process", "architecture"],
        arrow(18,80,52,80)+rect(60,46,120,68)+text(120,86,"Module",18)+arrow(188,80,222,80))
    add("encoder", "编码器", "Encoder", "modules", ["encoder", "compression", "representation"],
        arrow(18,80,45,80)+polygon("54,28 170,52 170,108 54,132")+text(110,86,"Encoder",17)+arrow(178,80,222,80))
    add("decoder", "解码器", "Decoder", "modules", ["decoder", "generation", "reconstruction"],
        arrow(18,80,54,80)+polygon("64,52 180,28 180,132 64,108",COLORS["green_light"],COLORS["green_dark"])+text(127,86,"Decoder",17)+arrow(188,80,222,80))
    add("tensor-stack", "特征张量", "Tensor stack", "data", ["tensor", "feature-map", "channels"],
        rect(85,25,93,76,COLORS["gray_light"],COLORS["line"],rx=2)
        +rect(74,37,93,76,COLORS["blue_light"],COLORS["blue"],rx=2)
        +rect(63,49,93,76,"#D9E8F3",COLORS["blue_dark"],rx=2)
        +text(120,149,"C × H × W",15))
    matrix = text(38,87,"X",22)
    for row in range(4):
        for col in range(4):
            matrix += rect(70+col*25,29+row*25,23,23,
                           COLORS["blue_light"] if (row+col)%2 else "#C7DBEB",COLORS["paper"],rx=1,sw=.8)
    matrix += path("M 65 25 H 59 V 132 H 65 M 175 25 H 181 V 132 H 175",sw=1.8)
    add("matrix", "矩阵", "Matrix", "data", ["matrix", "features", "linear-algebra"],matrix)
    tokens = ""
    for i, label in enumerate(["CLS","x₁","x₂","x₃","x₄"]):
        tokens += rect(19+i*42,52,34,48,COLORS["orange_light"] if i==0 else COLORS["blue_light"],COLORS["orange_dark"] if i==0 else COLORS["blue_dark"],rx=5)
        tokens += text(36+i*42,81,label,12 if i==0 else 16)
    tokens += text(120,127,"Token sequence",15,fill=COLORS["muted"])
    add("token-sequence", "Token 序列", "Token sequence", "data", ["tokens", "transformer", "sequence"],tokens)
    tile = rect(64,25,112,108,COLORS["blue_light"],COLORS["blue_dark"],rx=6)
    tile += circle(145,53,10,COLORS["orange_light"],COLORS["orange"],sw=1.5)
    tile += polygon("74,116 104,73 126,98 143,81 166,116",COLORS["green_light"],COLORS["green_dark"],sw=1.6)
    add("image-tile", "图像占位块", "Image tile", "data", ["image", "input", "placeholder"],tile,
        "Illustrative placeholder; replace with an actual image when needed.")
    nodes = [[(46,y) for y in (45,80,115)],[(120,y) for y in (28,63,98,133)],[(194,y) for y in (60,100)]]
    mlp = ""
    for left,right in zip(nodes,nodes[1:]):
        for a in left:
            for b in right:
                mlp += line(*a,*b,COLORS["line"],sw=1)
    for idx,layer in enumerate(nodes):
        for x,y in layer:
            mlp += circle(x,y,9,[COLORS["blue_light"],COLORS["green_light"],COLORS["orange_light"]][idx],COLORS["ink"],sw=1.5)
    add("mlp", "全连接网络", "MLP", "modules", ["mlp", "neural-network", "fully-connected"],mlp)
    attn = rect(67,56,112,70,COLORS["blue_light"],COLORS["blue_dark"],rx=8)+text(123,86,"Attention",17)+text(123,108,"Attn(Q, K, V)",13,fill=COLORS["muted"])
    for x,label in [(84,"Q"),(123,"K"),(162,"V")]:
        attn += text(x,23,label,15)+arrow(x,30,x,48,COLORS["blue_dark"])
    attn += arrow(187,91,224,91)
    add("attention", "注意力模块", "Attention", "modules", ["attention", "transformer", "qkv"],attn,
        "Symbolic function label; adapt it to the actual attention definition.")
    add("sum-node", "加法节点", "Sum node", "operations", ["sum", "add", "residual"],
        arrow(28,82,86,82)+arrow(120,19,120,48)+circle(120,82,26,COLORS["paper"],COLORS["blue_dark"])
        +line(108,82,132,82,COLORS["blue_dark"])+line(120,70,120,94,COLORS["blue_dark"])+arrow(154,82,212,82))
    concat = rect(93,35,54,92,COLORS["green_light"],COLORS["green_dark"],rx=7)
    concat += line(112,59,112,103,COLORS["green_dark"],sw=3)+line(128,59,128,103,COLORS["green_dark"],sw=3)
    concat += arrow(25,57,85,57)+arrow(25,105,85,105)+arrow(155,81,215,81)
    concat += text(120,150,"Concat",14,fill=COLORS["muted"])
    add("concat-node", "拼接节点", "Concatenation", "operations", ["concat", "fusion", "merge"],concat)
    loss = polygon("120,31 170,81 120,131 70,81",COLORS["orange_light"],COLORS["orange_dark"])+text(120,88,"Loss",18)
    loss += arrow(16,81,62,81)+arrow(178,81,224,81)
    add("loss", "损失函数", "Loss", "operations", ["loss", "objective", "training"],loss)
    add("arrow-solid", "实线箭头", "Solid arrow", "connections", ["arrow", "flow", "connection"],
        arrow(27,80,213,80))
    add("arrow-dashed", "虚线箭头", "Dashed arrow", "connections", ["arrow", "optional", "auxiliary"],
        arrow(27,80,213,80,dash="7 6"))
    add("arrow-bidirectional", "双向箭头", "Bidirectional arrow", "connections", ["arrow", "bidirectional", "interaction"],
        arrow(27,80,213,80,both=True))
    add("skip-connection", "跳跃连接", "Skip connection", "connections", ["skip", "residual", "bypass"],
        path("M 29 115 V 55 Q 29 44 40 44 H 199 Q 211 44 211 55 V 108",COLORS["blue_dark"])
        +head(211,117,math.pi/2,COLORS["blue_dark"]))
    snow = rect(48,43,144,74,COLORS["blue_light"],COLORS["blue_dark"],rx=12)
    for angle in [0,math.pi/3,2*math.pi/3]:
        dx,dy=16*math.cos(angle),16*math.sin(angle)
        snow+=line(81-dx,80-dy,81+dx,80+dy,COLORS["blue_dark"],sw=2)
    snow += text(139,86,"Frozen",16)
    add("frozen-badge", "冻结参数", "Frozen parameters", "training", ["frozen", "parameters", "finetuning"],snow)
    train = rect(43,43,154,74,COLORS["green_light"],COLORS["green_dark"],rx=12)
    train += path("M 67 91 V 70 H 88",COLORS["green_dark"],sw=2)+head(93,70,0,COLORS["green_dark"],size=7)
    train += text(141,86,"Trainable",16)
    add("trainable-badge", "可训练参数", "Trainable parameters", "training", ["trainable", "parameters", "finetuning"],train)
    latent = text(46,86,"z",23)
    for i,value in enumerate([.38,.76,.52,.23,.65,.9]):
        latent += rect(73+i*21,44,17,76,COLORS["gray_light"],COLORS["line"],rx=2,sw=1)
        latent += rect(73+i*21,120-value*76,17,value*76,COLORS["blue_light"] if i%2 else "#C7DBEB",COLORS["blue_dark"],rx=2,sw=1)
    add("latent-vector", "隐变量向量", "Latent vector", "data", ["latent", "embedding", "vector"],latent,
        "Illustrative feature values, not measured data.")
    rng=random.Random(42)
    samples=""
    for i in range(36):
        x=min(198,max(42,rng.gauss(120,28))); y=min(129,max(28,rng.gauss(80,23)))
        samples+=circle(round(x,2),round(y,2),3.2,COLORS["blue"] if i%3 else COLORS["green"],COLORS["paper"],sw=.3)
    add("sample-cloud", "样本点云", "Sample cloud", "data", ["distribution", "samples", "generative"],samples,
        "Deterministic illustrative points generated with seed 42; not experimental data.")
    times=""
    for i,label in enumerate(["uₜ","uₜ₊₁","uₜ₊₂"]):
        times+=rect(17+i*77,51,53,57,COLORS["green_light"],COLORS["green_dark"],rx=7)+text(43.5+i*77,86,label,19)
        if i<2: times+=arrow(74+i*77,79,88+i*77,79,COLORS["green_dark"])
    times += text(120,135,"Time rollout",14,fill=COLORS["muted"])
    add("time-rollout", "时间推进", "Time rollout", "science", ["time-series", "dynamics", "ai4pde", "rollout"],times)
    physics=rect(49,36,142,90,COLORS["orange_light"],COLORS["orange_dark"],rx=9)
    physics+=text(120,70,"Physics",18)+line(71,82,169,82,COLORS["orange"],sw=1)+text(120,107,"R(u) = 0",19)
    add("physics-constraint", "物理约束", "Physics constraint", "science", ["physics", "pde", "residual", "prior"],physics)
    weights=rect(17,66,83,54,COLORS["blue_light"],COLORS["blue_dark"],rx=7)+text(58,98,"Model",16)
    weights+=rect(140,66,83,54,COLORS["blue_light"],COLORS["blue_dark"],rx=7)+text(181,98,"Model",16)
    weights+=path("M 58 58 V 30 H 181 V 58",COLORS["muted"],dash="4 4",sw=1.6)
    weights+=rect(99,17,42,28,COLORS["paper"],COLORS["paper"],rx=3,sw=0)+text(120,38,"θ",21)
    add("shared-weights", "参数共享", "Shared weights", "training", ["shared-weights", "siamese", "parameters"],weights)
    add("distribution-map", "分布映射", "Distribution mapping", "science", ["distribution", "mapping", "transport", "teaser"],
        path("M 19 117 C 30 116 34 114 40 91 C 48 45 65 45 73 91 C 80 114 84 116 94 117",COLORS["blue_dark"],COLORS["blue_light"],sw=2)
        +path("M 146 117 C 152 116 158 108 165 80 C 172 57 180 57 186 80 C 192 100 199 101 204 94 C 212 82 217 95 222 117",COLORS["green_dark"],COLORS["green_light"],sw=2)
        +arrow(102,80,136,80)+text(120,60,"T",16,fill=COLORS["muted"]),
        "Illustrative distribution shapes, not fitted probability densities.")
    assert len(items)==24
    return items


def make_overview(items):
    cols, rows = 4, 6
    cell_w, cell_h = 270, 208
    width, height = 48 + cols*cell_w, 110 + rows*cell_h + 30
    s=f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">'
    s+='<title>Scientific figure elements — original SVG collection</title>'
    s+=rect(0,0,width,height,COLORS["paper"],COLORS["paper"],rx=0,sw=0)
    s+=text(28,43,"SCIENTIFIC FIGURE ELEMENTS",25,weight="700",anchor="start")
    s+=text(28,73,"24 editable SVG primitives · transparent backgrounds · shared visual style",14,fill=COLORS["muted"],anchor="start")
    for i,item in enumerate(items):
        x=24+(i%cols)*cell_w; y=102+(i//cols)*cell_h
        s+=rect(x,y,cell_w-12,cell_h-12,COLORS["paper"],"#E2E8F0",rx=9,sw=1)
        s+=f'<g id="{item["id"]}" transform="translate({x+9},{y+6})">{item["body"]}</g>'
        s+=text(x+18,y+177,f'{i+1:02d}  {item["title_en"]}',13,fill=COLORS["muted"],anchor="start")
    return s+'</svg>\n'


def validate_svg(file):
    root=ET.parse(file).getroot()
    assert root.tag.endswith("svg"), file
    assert root.get("viewBox"), file
    for e in root.iter():
        assert e.tag.split("}")[-1] not in {"script","foreignObject","image","use"}, (file,e.tag)
        for k,v in e.attrib.items():
            assert not k.split("}")[-1].lower().startswith("on"), (file,k)
            assert "href" not in k and "url(" not in v, (file,k,v)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--render",action="store_true",help="Render preview.png with Inkscape.")
    args=parser.parse_args()
    (OUT/"svg").mkdir(parents=True,exist_ok=True)
    items=create_items()
    catalog=[]
    for item in items:
        destination=OUT/"svg"/(item["id"]+".svg")
        destination.write_text(svg_document(item["body"],item["title_en"],item["notes"] or "Original editable scientific figure element."),encoding="utf-8")
        validate_svg(destination)
        catalog.append({k:v for k,v in item.items() if k!="body"} | {
            "svg_path":destination.relative_to(ROOT).as_posix(),
            "preview_path":destination.relative_to(ROOT).as_posix(),
            "source":{"kind":"original","created_for":"paper-figure-library","date":"2026-10-25"},
            "rights":"original; no public redistribution license specified",
            "editability":"vector shapes and live text; no external assets",
        })
    overview=OUT/"all-elements.svg"
    overview.write_text(make_overview(items),encoding="utf-8")
    validate_svg(overview)
    (OUT/"catalog.json").write_text(json.dumps({"schema_version":1,"count":len(catalog),"items":catalog},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    (OUT/"style-tokens.json").write_text(json.dumps({"colors":COLORS,"font_family":FONT,"canvas":{"width":WIDTH,"height":HEIGHT,"background":"transparent"},"stroke_width":2.2,"corner_radius":8,"base_font_size":16},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    if args.render:
        executable=shutil.which("inkscape")
        if not executable:
            raise SystemExit("Inkscape is required for --render; SVG files were generated successfully.")
        subprocess.run([executable,str(overview),"--export-type=png",f"--export-filename={OUT/'preview.png'}","--export-width=1800"],check=True,capture_output=True,text=True)
    print(f"Generated and validated {len(catalog)} standalone SVGs and an editable overview in {OUT}")


if __name__=="__main__":
    main()
