"""Locate the SPARC flat table used by the scoring scripts.

Resolution order:
1. SPARC_CSV, if set (must exist; no silent fallback).
2. data/sparc_flat.csv — committed Lelli, McGaugh & Schombert 2016 table.
3. ./sparc_flat.csv only if the committed table is absent.
4. Legacy /tmp paths.
5. data/sparc_flat_demo.csv last (synthetic; not SPARC).
"""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def sparc_csv():
    env = os.environ.get("SPARC_CSV")
    if env:
        path = Path(env)
        return path if path.is_file() else None
    candidates = [
        ROOT / "data" / "sparc_flat.csv",
        Path.cwd() / "sparc_flat.csv",
        ROOT / "sparc_flat.csv",
        Path("/tmp/front/sparc_flat.csv"),
        Path("/tmp/work/sparc_flat.csv"),
        ROOT / "data" / "sparc_flat_demo.csv",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return None


def is_demo(path: Path | None) -> bool:
    if path is None:
        return False
    name = Path(path).name.lower()
    if "demo" in name:
        return True
    # A root-level sparc_flat.csv is the old DEMO alias, not data/sparc_flat.csv.
    if name == "sparc_flat.csv" and Path(path).resolve().parent.name != "data":
        return True
    return False
