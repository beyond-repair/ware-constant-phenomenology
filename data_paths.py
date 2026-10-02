"""Locate the SPARC flat table used by the scoring scripts.

Resolution order (offline-first Claim-0):
1. SPARC_CSV, if set (must exist; no silent fallback).
2. ./sparc_flat.csv in the working directory (DEMO copy when shipped).
3. data/sparc_flat_demo.csv — synthetic DEMO (default stranger path).
4. data/sparc_flat.csv — optional Lelli+2016 adapter table if present.
5. Legacy /tmp paths for older local layouts.
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
        Path.cwd() / "sparc_flat.csv",
        ROOT / "sparc_flat.csv",
        ROOT / "data" / "sparc_flat_demo.csv",
        Path.cwd() / "data" / "sparc_flat_demo.csv",
        ROOT / "data" / "sparc_flat.csv",
        Path("/tmp/front/sparc_flat.csv"),
        Path("/tmp/work/sparc_flat.csv"),
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return None


def is_demo(path: Path | None) -> bool:
    if path is None:
        return False
    name = path.name.lower()
    if "demo" in name:
        return True
    # Root-level sparc_flat.csv is the DEMO alias; data/sparc_flat.csv is real SPARC.
    if name == "sparc_flat.csv" and path.resolve().parent.name != "data":
        return True
    return False
