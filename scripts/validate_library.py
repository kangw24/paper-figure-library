#!/usr/bin/env python3
"""Check library metadata, local references, recorded hashes, and SVG portability."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from pathlib import Path
from urllib.parse import urlparse
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"schema_version", "id", "title", "category", "kind", "tags", "formats",
            "primary_file", "preview", "source", "license", "editability", "changes", "added_date"}
KINDS = {"template", "paper-example", "tutorial-example"}


def valid_figure_number(value: object) -> bool:
    if type(value) is int:
        return value > 0
    return isinstance(value, str) and re.fullmatch(r"[1-9]\d*(?:\.[1-9]\d*)+", value) is not None


def validate(root: Path) -> tuple[list[str], dict[str, int]]:
    root = root.resolve()
    errors: list[str] = []
    counts = {"teaser": 0, "architecture": 0, "multipanel": 0, "element": 0, "mechanism": 0, "layout-template": 0, "svg": 0}
    ids: set[str] = set()

    def error(path: Path | str, message: str) -> None:
        label = str(path.relative_to(root)) if isinstance(path, Path) and path.is_relative_to(root) else str(path)
        errors.append(f"{label}: {message}")

    def local_file(base: Path, raw: object, label: str) -> Path | None:
        if not isinstance(raw, str) or not raw or Path(raw).is_absolute():
            error(base, f"{label} 必须为非空相对路径")
            return None
        path = (base / raw).resolve()
        if not path.is_relative_to(root):
            error(base, f"{label} 越出仓库目录: {raw}")
            return None
        if not path.is_file() or path.stat().st_size == 0:
            error(base, f"{label} 文件缺失或为空: {raw}")
            return None
        return path

    def read_json(path: Path) -> dict | None:
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                raise ValueError("顶层必须为对象")
            return data
        except (OSError, ValueError) as exc:
            error(path, f"无法读取 JSON: {exc}")
            return None

    def unique_id(item: dict, path: Path) -> None:
        value = item.get("id")
        if not isinstance(value, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value):
            error(path, "id 应使用小写字母、数字和连字符")
        elif value in ids:
            error(path, f"重复 id: {value}")
        else:
            ids.add(value)

    for category, directory in (("teaser", "teaser"), ("architecture", "architecture"), ("multipanel", "multipanel"), ("mechanism", "references/mechanisms"), ("layout-template", "templates/layouts")):
        folder = root / directory
        for entry in sorted(folder.iterdir()) if folder.is_dir() else []:
            if not entry.is_dir() or entry.name.startswith("."):
                continue
            metadata = entry / "metadata.json"
            item = read_json(metadata)
            if item is None:
                continue
            counts[category] += 1
            missing = REQUIRED - item.keys()
            if missing:
                error(metadata, "缺少字段: " + ", ".join(sorted(missing)))
            unique_id(item, metadata)
            if item.get("category") != category:
                error(metadata, f"目录对应的 category 应为 {category}")
            if category == "multipanel":
                publication = item.get("publication", {})
                if not publication.get("venue") or type(publication.get("year")) is not int:
                    error(metadata, "大图须记录发表刊物或会议及整数年份")
                if item.get("editability", {}).get("level") not in {"vector", "vector-and-raster", "raster-reference"}:
                    error(metadata, "大图缺少可识别的编辑性分类")
                layout = item.get("curation", {})
                if not layout.get("layout_family") or not layout.get("reading_order"):
                    error(metadata, "缺少大图的编排或面板阅读说明")
                if not layout.get("panel_labels") or not isinstance(layout.get("panel_count"), int) or layout["panel_count"] < 2:
                    error(metadata, "应记录原图面板编号和数量")
                source = item.get("source", {})
                if not valid_figure_number(source.get("figure_number")):
                    error(metadata, "缺少原论文图号")
            if item.get("kind") not in KINDS:
                error(metadata, "kind 不是支持的条目类型")
            if not isinstance(item.get("tags"), list) or not item["tags"]:
                error(metadata, "tags 应为非空数组")
            if not isinstance(item.get("formats"), list) or not item["formats"]:
                error(metadata, "formats 应为非空数组")
            if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(item.get("added_date", ""))):
                error(metadata, "added_date 应为 YYYY-MM-DD")
            local_file(entry, item.get("primary_file"), "primary_file")
            local_file(entry, item.get("preview"), "preview")
            local_file(entry, "README.md", "条目说明")
            source = item.get("source", {})
            urls = source.get("urls", []) if isinstance(source, dict) else []
            if not urls:
                error(metadata, "外部素材必须记录 source.urls")
            for url in urls:
                parsed = urlparse(str(url))
                if parsed.scheme not in {"https", "http"} or not parsed.netloc:
                    error(metadata, f"无效来源 URL: {url}")
            license_data = item.get("license", {})
            if not isinstance(license_data, dict) or not license_data.get("status") or not license_data.get("name"):
                error(metadata, "license 必须包含 status 和 name")
            elif license_data.get("file"):
                local_file(entry, license_data["file"], "license.file")
            for record in item.get("files", []):
                path = local_file(entry, record.get("path"), "files.path")
                if path is None:
                    continue
                if "bytes" in record and path.stat().st_size != record["bytes"]:
                    error(path, "文件大小与 metadata.files 不符")
                if record.get("sha256") and hashlib.sha256(path.read_bytes()).hexdigest() != record["sha256"]:
                    error(path, "SHA256 与 metadata.files 不符")
            if item.get("origin") == "extracted-from-author-pdf":
                publication = item.get("publication", {})
                if not publication.get("venue") or not publication.get("year"):
                    error(metadata, "论文摘图必须记录会议与年份")
                if publication.get("presentation") == "oral" and not publication.get("evidence_url"):
                    error(metadata, "Oral 必须有官网或作者明确声明的依据链接")
                if publication.get("evidence_url") not in source.get("urls", []):
                    error(metadata, "会议身份依据应列入 source.urls")
                if type(source.get("page_number")) is not int or source["page_number"] < 1:
                    error(metadata, "page_number 必须为正整数")
                if not valid_figure_number(source.get("figure_number")):
                    error(metadata, "figure_number 应为正整数或带章节的图号")
                box = source.get("crop_bbox_pt")
                if not isinstance(box, list) or len(box) != 4 or not all(isinstance(v, (int, float)) and math.isfinite(v) for v in box):
                    error(metadata, "论文摘图必须有四个有限坐标")
                elif box[2] <= box[0] or box[3] <= box[1]:
                    error(metadata, "裁剪坐标范围无效")
                if not re.fullmatch(r"[0-9a-f]{64}", str(source.get("full_pdf_sha256", ""))):
                    error(metadata, "必须记录原论文 PDF 的 SHA256")
                local_file(entry, "figure.pdf", "原矢量或位图 PDF 摘图")
                editability = item.get("editability", {})
                if editability.get("level") == "raster-reference":
                    if "svg" in item.get("formats", []) or editability.get("vector_shapes"):
                        error(metadata, "整图位图不能标为可编辑 SVG")
                elif not editability.get("pdf_drawing_objects"):
                    error(metadata, "矢量摘图应有原 PDF 图形对象")
                if not item.get("curation", {}).get("why_selected"):
                    error(metadata, "精选原图必须说明选择理由")
            if item.get("origin") == "downloaded":
                primary = entry / item['primary_file']
                if primary.is_file() and hashlib.sha256(primary.read_bytes()).hexdigest() != source.get('original_sha256'):
                    error(primary, "原始下载文件与来源哈希不符")
                if primary.is_file() and source.get('git_blob_sha'):
                    raw = primary.read_bytes()
                    actual_blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
                    if actual_blob != source['git_blob_sha']:
                        error(primary, '原始下载文件与上游 Git blob 不符')

    element_file = root / "element" / "catalog.json"
    elements = read_json(element_file)
    if elements is not None:
        items = elements.get("items", [])
        if elements.get("count") != len(items):
            error(element_file, "count 与 items 数量不一致")
        for item in items:
            unique_id(item, element_file)
            counts["element"] += 1
            for key in ("title_zh", "category", "source", "rights", "editability"):
                if not item.get(key):
                    error(element_file, f"{item.get('id')}: 缺少 {key}")
            source = item.get("source", {})
            if isinstance(source, dict):
                if source.get("kind") not in {"external-download", "extracted-existing-vectors"}:
                    error(element_file, f"{item.get('id')}: 只收录外部原素材或原图提取节点")
                if not source.get("urls"):
                    error(element_file, f"{item.get('id')}: 外部元素必须记录 source.urls")
                license_data = item.get("license", {})
                if not isinstance(license_data, dict) or not license_data.get("name") or not license_data.get("status"):
                    error(element_file, f"{item.get('id')}: 外部元素必须单独记录 license.name 和 license.status")
            local_file(root, item.get("svg_path"), "elements.svg_path")
            local_file(root, item.get("preview_path"), "elements.preview_path")
            svg_file = root / item.get('svg_path', '')
            if svg_file.is_file() and hashlib.sha256(svg_file.read_bytes()).hexdigest() != item.get('sha256'):
                error(svg_file, '元素 SHA256 与来源索引不符')
            if source.get('kind') == 'external-download' and item.get('sha256') != source.get('original_sha256'):
                error(svg_file, '外部原素材的字节发生变化')
            if source.get('kind') == 'extracted-existing-vectors':
                original = root / source.get('local_original', '')
                if not original.is_file() or hashlib.sha256(original.read_bytes()).hexdigest() != source.get('original_sha256'):
                    error(svg_file, '提取来源缺失或原图哈希不符')
        for name in ("README.md", "all-elements.svg", "preview.png"):
            local_file(root / "element", name, "元素库总览")

    if (root / "relationships.json").exists():
        from build_links import load as load_links
        try:
            load_links(root)
        except (ValueError, KeyError, OSError) as exc:
            error("relationships.json", "范例与元素关联无效: " + str(exc))

    for path in sorted(root.rglob("*.svg")):
        if ".git" in path.parts:
            continue
        counts["svg"] += 1
        try:
            raw = path.read_text(encoding="utf-8")
            if "<!ENTITY" in raw.upper():
                error(path, "不允许 XML 实体声明")
                continue
            svg = ET.fromstring(raw)
            if svg.tag.rsplit("}", 1)[-1] != "svg":
                error(path, "根节点不是 SVG")
            for node in svg.iter():
                tag = node.tag.rsplit("}", 1)[-1].lower()
                if tag in {"script", "foreignobject"}:
                    error(path, f"不允许 {tag} 节点")
                values = list(node.attrib.values())
                if tag == "style":
                    values.append("".join(node.itertext()))
                for key, value in node.attrib.items():
                    key = key.rsplit("}", 1)[-1].lower()
                    if key.startswith("on"):
                        error(path, f"不允许事件属性 {key}")
                    if key == "href" and not (value.startswith("#") or re.match(r"^data:image/(png|jpeg|jpg|gif|webp);base64,", value)):
                        error(path, f"外部或不支持的 href: {value[:90]}")
                for value in values:
                    if "@import" in value.lower():
                        error(path, "不允许外部 CSS import")
                    for target in re.findall(r"url\(\s*['\"]?([^)'\"]+)", value, re.I):
                        if not target.strip().startswith("#"):
                            error(path, f"外部 CSS URL: {target[:90]}")
        except (OSError, ET.ParseError, UnicodeError) as exc:
            error(path, f"SVG 无法解析: {exc}")
    return errors, counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    errors, counts = validate(args.root)
    if errors:
        print("校验未通过：")
        for message in errors:
            print("- " + message)
        return 1
    print(f"校验通过：{counts['teaser']} teaser，{counts['architecture']} architecture，"
          f"{counts['multipanel']} 大图，{counts['element']} 元素；{counts['svg']} 个 SVG 已检查。")
    print(f"另含 {counts['mechanism']} 张机制参考图、{counts['layout-template']} 份原生版式模板；分别计数。")
    print("仅检查结构、引用、已记录校验和及 SVG 自包含性；不证明桌面 Illustrator 兼容性或素材授权。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
