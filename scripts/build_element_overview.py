#!/usr/bin/env python3
"""Rebuild the complete element browser and all SVG overviews."""
from pathlib import Path
from build_catalog import build
ROOT=Path(__file__).resolve().parents[1]
print(build(ROOT))
