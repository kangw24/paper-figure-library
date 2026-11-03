#!/usr/bin/env python3
"""Read-only structural SVG preflight. No rendering or external resource loading."""

from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET


URL = re.compile(r"url\(\s*(['\"]?)(.*?)\1\s*\)", re.I)
CJK = re.compile(r"[\u3400-\u4dbf\u4e00-\u9fff\uf900-\ufaff]")
MAX_BYTES = 64 * 1024 * 1024


def local_name(value: str) -> str:
    return value.rsplit("}", 1)[-1]


def audit(path: Path) -> dict:
    result = {"file": str(path), "errors": [], "attention": []}
    try:
        if path.stat().st_size > MAX_BYTES:
            raise ValueError("File exceeds the 64 MiB preflight limit")
        data = path.read_bytes()
        probe = data.replace(b"\x00", b"").upper()
        if b"<!DOCTYPE" in probe or b"<!ENTITY" in probe:
            raise ValueError("DOCTYPE/entity declarations are not supported; no external entities loaded")
        root = ET.fromstring(data)
        if local_name(root.tag) != "svg":
            raise ValueError("Root element is not svg")
    except (OSError, ValueError, ET.ParseError) as exc:
        result["errors"].append(str(exc))
        return result

    result["sha256"] = hashlib.sha256(data).hexdigest()
    result["bytes"] = len(data)
    result["dimensions"] = {key: root.get(key) for key in ("width", "height", "viewBox")}
    tags = Counter(local_name(node.tag) for node in root.iter())
    ids = Counter(node.get("id") for node in root.iter() if node.get("id"))
    fragments, external = set(), set()
    embedded_images = 0
    href_images = 0
    marker_attributes = 0
    cjk_samples = []

    def reference(value: str) -> None:
        value = value.strip()
        if not value or value.lower() == "none":
            return
        if value.startswith("#"):
            fragments.add(value[1:])
        elif not value.lower().startswith("data:"):
            external.add(value)

    for node in root.iter():
        tag = local_name(node.tag)
        for key, value in node.attrib.items():
            key = local_name(key)
            if key == "href":
                reference(value)
                if tag == "image":
                    if value.lower().startswith("data:"):
                        embedded_images += 1
                    else:
                        href_images += 1
            if key.startswith("marker-"):
                marker_attributes += 1
            for match in URL.finditer(value):
                reference(match.group(2))
        if tag == "style":
            for match in URL.finditer(node.text or ""):
                reference(match.group(2))
        if tag in {"text", "tspan", "textPath"}:
            for fragment in (node.text, node.tail):
                if fragment and CJK.search(fragment):
                    sample = fragment.strip()[:120]
                    if sample not in cjk_samples:
                        cjk_samples.append(sample)

    duplicates = sorted(key for key, count in ids.items() if count > 1)
    missing = sorted(fragments - set(ids))
    result.update({
        "element_counts": dict(sorted(tags.items())),
        "duplicate_ids": duplicates,
        "missing_fragment_ids": missing,
        "external_references": sorted(external),
        "images": {"embedded": embedded_images, "referenced": href_images},
        "marker_attributes": marker_attributes,
        "cjk_text_samples": cjk_samples[:10],
    })
    if duplicates:
        result["errors"].append("Duplicate IDs make fragment resolution ambiguous")
    if missing:
        result["errors"].append("Unresolved local fragment references")
    if not root.get("viewBox"):
        result["attention"].append("No viewBox; inspect viewport and scaling")
    if not root.get("width") or not root.get("height"):
        result["attention"].append("No explicit width/height; verify target-app artboard size")
    if external:
        result["attention"].append("External references present; existence/permission not checked")
    if tags["image"]:
        result["attention"].append("Raster or referenced images present; do not claim all-vector editability")
    if tags["marker"] or marker_attributes:
        result["attention"].append("Markers present; inspect arrowheads and shafts in target app")
    if cjk_samples:
        result["attention"].append("CJK text present; inspect against the figure-language requirement")
    for tag in ("clipPath", "mask", "filter", "foreignObject", "style", "script"):
        if tags[tag]:
            result["attention"].append(f"{tag} present; inspect rendering and target-app compatibility")
    if any("{http://www.w3.org/XML/1998/namespace}base" in n.attrib for n in root.iter()):
        result["attention"].append("xml:base present; relative resource bases are not resolved")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", type=Path)
    parser.add_argument("--recursive", action="store_true")
    parser.add_argument("--output", type=Path, help="Write JSON report; SVG inputs are never modified")
    args = parser.parse_args()
    files = set()
    errors = []
    for path in args.paths:
        if path.is_dir():
            candidates = path.rglob("*") if args.recursive else path.iterdir()
            files.update(p for p in candidates if p.is_file() and p.suffix.lower() == ".svg")
        elif path.is_file() and path.suffix.lower() == ".svg":
            files.add(path)
        else:
            errors.append(f"Not a readable SVG file or directory: {path}")
    if not files:
        errors.append("No SVG files found")
    if args.output and args.output.resolve() in {p.resolve() for p in files}:
        print("Refusing to overwrite an SVG input with the report", file=sys.stderr)
        return 2
    results = [audit(path) for path in sorted(files)]
    report = {
        "scope": "Structural inspection only; not a science, layout, or native-app validation",
        "errors": errors,
        "files": results,
    }
    text = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        try:
            args.output.write_text(text, encoding="utf-8")
        except OSError as exc:
            print(str(exc), file=sys.stderr)
            return 2
    else:
        print(text, end="")
    return 1 if errors or any(item["errors"] for item in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
