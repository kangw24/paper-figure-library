#!/usr/bin/env python3
"""Validate source metadata, then rebuild catalog.json and CATALOG.md."""
from __future__ import annotations

import argparse
import html
import json
from pathlib import Path

from validate_library import ROOT, validate

KIND_LABELS = {"template": "通用模板", "paper-example": "论文范例", "tutorial-example": "教程范例", "original-example": "原创范例"}
ELEMENT_CATEGORIES = {"modules": "模块", "data": "数据表示", "operations": "运算", "connections": "连接", "training": "训练标识", "concepts": "概念表示", "science": "科学与动力学"}


def safe(value: object) -> str:
    return str(value).replace("|", "\\|").replace("\n", " ")


def build(root: Path) -> dict:
    examples = []
    for folder in ("teasers", "architectures"):
        for path in sorted((root / "examples" / folder).glob("*/metadata.json")):
            item = json.loads(path.read_text(encoding="utf-8"))
            base = path.parent.relative_to(root).as_posix()
            examples.append({**item, "path": base, "metadata_path": f"{base}/metadata.json",
                             "readme_path": f"{base}/README.md", "primary_path": f"{base}/{item['primary_file']}",
                             "preview_path": f"{base}/{item['preview']}"})
    raw_elements = json.loads((root / "elements" / "catalog.json").read_text(encoding="utf-8"))["items"]
    elements = []
    for item in raw_elements:
        original = item["source"].get("kind") == "original"
        license_data = item.get("license") or {"status": "original-unlicensed", "name": "本库原创；未设置对外再分发许可", "note": item["rights"]}
        elements.append({**item, "title": item["title_zh"], "category": "element", "element_category": item["category"],
                         "kind": "original-element" if original else "external-element", "formats": ["svg"], "primary_path": item["svg_path"],
                         "license": license_data})
    counts = {category: sum(item["category"] == category for item in examples + elements)
              for category in ("teaser", "architecture", "element")}
    catalog = {"schema_version": 1, "description": "Paper Figure Library — 按来源元数据生成的统一索引", "counts": counts, "items": examples + elements}
    (root / "catalog.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# 素材目录", "", "本页由 `python scripts/build_catalog.py` 根据各条目的元数据生成。编辑素材条目后重新运行命令即可更新。", "",
             "[仓库首页](README.md) · [新增与维护](CONTRIBUTING.md) · [机器可读索引](catalog.json)", "",
             "| 类别 | 数量 | 主要用途 |", "|---|---:|---|",
             f"| [Teaser](#teaser-范例) | {counts['teaser']} | 核心想法、动机与方法差异 |",
             f"| [Architecture](#architecture-范例) | {counts['architecture']} | 模型结构、整体框架与模块连接 |",
             f"| [最小可复用元素](#最小可复用元素) | {counts['element']} | 复制单个 SVG，组合成自己的图 |", ""]
    for category, label in (("teaser", "Teaser 范例"), ("architecture", "Architecture 范例")):
        lines += [f"## {label}", ""]
        for item in examples:
            if item["category"] != category:
                continue
            lines += [f"### [{item['title']}]({item['readme_path']})", "", item.get("summary", ""), "",
                      f"[<img src=\"{item['preview_path']}\" alt=\"{html.escape(item['title'], quote=True)}\" width=\"820\">]({item['readme_path']})", "",
                      f"**类型：** {KIND_LABELS[item['kind']]}　**格式：** {' / '.join(x.upper() for x in item['formats'])}", "",
                      f"**许可：** {item['license']['name']}（`{item['license']['status']}`）。{item['license'].get('note', '')}", "",
                      "**标签：** " + " · ".join(f"`{tag}`" for tag in item["tags"]), "",
                      f"[可编辑源文件]({item['primary_path']}) · [来源与修改记录]({item['metadata_path']}) · [使用说明]({item['readme_path']})", ""]
    original_count = sum(item["kind"] == "original-element" for item in elements)
    lines += ["## 最小可复用元素", "", f"共 {counts['element']} 个元素，其中 {original_count} 个为此仓库原创。来源与权利状态逐条保存在索引中；当前原创元素用于你的绘图复用，未设置对外再分发许可证。", "",
              "[![元素总览](elements/preview.png)](elements/README.md)", "",
              "[打开总览 SVG](elements/all-elements.svg) · [元素使用说明](elements/README.md) · [样式参数](elements/style-tokens.json)", "",
              "| 元素 | 分类 | 标签 | 来源 / 权利状态 |", "|---|---|---|---|"]
    for item in elements:
        license_label = "本库原创" if item["kind"] == "original-element" else item["license"]["name"]
        lines.append(f"| [{safe(item['title'])}]({item['primary_path']}) | {ELEMENT_CATEGORIES.get(item['element_category'], item['element_category'])} | {safe(', '.join(item['tags']))} | {safe(license_label)} |")
    lines += ["", "## 如何理解许可与可编辑性", "",
              "每条记录的许可单独适用，整个仓库没有为第三方素材重新授权。MIT 条目保留了原许可文件；reference-only 和 no-explicit-license 条目记录了可查证的状态。", "",
              "SVG 中的路径、形状和文字对象可进一步修改；嵌入的照片仍是位图。PDF 转换得到的文字可能被拆分。AI 原文件和配套素材保留了各自的来源说明。", ""]
    (root / "CATALOG.md").write_text("\n".join(lines), encoding="utf-8")
    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.root.resolve()
    errors, _ = validate(root)
    if errors:
        for error in errors:
            print(error)
        print("未写入索引；请先修复以上问题。")
        return 1
    counts = build(root)
    print("已更新 catalog.json 与 CATALOG.md：" + ", ".join(f"{k}={v}" for k, v in counts.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
