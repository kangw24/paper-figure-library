"""Build the multi-panel gallery from the figure metadata."""
from collections import Counter, defaultdict
from hashlib import sha256
from html import escape

FAMILIES = {
    "装置、过程与测量": "apparatus",
    "同一对象的多种证据": "evidence",
    "从整体到局部": "scales",
    "多工况与方法对照": "comparisons",
}
FORMATS = {
    "vector": "矢量",
    "vector-and-raster": "矢量与位图混合",
    "raster-reference": "位图参考",
}


def family_anchor(name):
    if name in FAMILIES:
        return FAMILIES[name]
    return "layout-" + sha256(name.encode()).hexdigest()[:12]


def gallery(root, entries):
    groups = defaultdict(list)
    for item in entries:
        groups[item["curation"]["layout_family"]].append(item)
    counts = Counter(item["editability"]["level"] for item in entries)
    families = [f for f in FAMILIES if f in groups] + sorted(groups.keys() - FAMILIES.keys())
    lines = [
        "# 大图 · 多面板正文图",
        "",
        "[仓库首页](../README.md) · [总目录](../CATALOG.md) · [Teaser](../teaser/README.md) · [Architecture](../architecture/README.md) · [Element](../element/README.md)",
        "",
        f"{len(entries)} 幅完整论文图，按面板之间的关系浏览。点击缩略图可查看高清图版、逐面板解读和出处。",
        "",
        f"其中 {counts['vector'] + counts['vector-and-raster']} 幅 PDF 保留可编辑的矢量路径，{counts['raster-reference']} 幅保留为位图参考。",
        "",
        " · ".join(f"[{g}（{len(groups[g])}）](#{family_anchor(g)})" for g in families),
    ]
    for family in families:
        lines.extend(("", f'<a id="{family_anchor(family)}"></a>', "", "## " + family, "", "| | |", "|---|---|"))
        cells = []
        for item in sorted(groups[family], key=lambda x: (x["publication"]["venue"], -x["publication"]["year"], x["id"])):
            pub = item["publication"]
            figure = item["source"]["figure_number"]
            labels = escape(item["curation"]["panel_labels"]).replace("|", "&#124;")
            href = item["id"] + "/README.md"
            title = escape(item["title"]).replace("|", "&#124;")
            summary = escape(item["summary"]).replace("|", "&#124;")
            fmt = FORMATS[item["editability"]["level"]]
            cells.append(f'<a href="{href}"><img src="{item["id"]}/{item["preview"]}" alt="{title}" width="340"></a><br>'
                         f'**[{title}]({href})**<br>{escape(pub["venue"])} {pub["year"]} · Fig. {figure} · '
                         f'{labels} · {fmt}<br>{summary}')
        for n in range(0, len(cells), 2):
            right = cells[n + 1] if n + 1 < len(cells) else ""
            lines.append(f"| {cells[n]} | {right} |")
    origami = "architecture/magnetic-bistable-origami-robot-design-actuation"
    if (root / origami / "README.md").is_file():
        lines.extend(("", f"[另见双稳态折纸机器人 Fig. 1 · A–J](../{origami}/README.md)。这张已收录在 Architecture 的图把折纸结构、力学曲线、装置和八种运动模式放在同一页。"))
    return lines
