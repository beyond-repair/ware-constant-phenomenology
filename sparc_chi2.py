#!/usr/bin/env python3
"""
DEPRECATED as primary entrypoint — use sparc_run.py (mode=o1).

Transparent SPARC χ² under locked W and frozen macro r0.
Kept for reproducibility of earlier median~35–40 reports.
"""
from __future__ import annotations
import numpy as np
import pandas as pd
from pathlib import Path

W_STAR = 1.0 / (4.0 * np.pi)
G = 4.30091e-6
M_REF = 1e11
R0_REF = 0.45
ALPHA_R0 = 0.40

def r0_kpc(Mb):
    return R0_REF * (max(Mb, 1e6) / M_REF) ** ALPHA_R0

def load_sparc(path):
    df = pd.read_csv(path)
    return df[(df.survey == "SPARC") & (df.errV > 0)].copy()

def main():
    print("=" * 60)
    print("LEGACY sparc_chi2 — prefer: python sparc_run.py --mode o1")
    print(f"W_star={W_STAR:.6f}  macro r0 frozen")
    path = Path(os.environ.get("SPARC_CSV", "sparc_flat.csv")) if False else Path("sparc_flat.csv")
    import os
    path = Path(os.environ.get("SPARC_CSV", "sparc_flat.csv"))
    if not path.exists():
        path = Path("/tmp/front/sparc_flat.csv")
    if not path.exists():
        print("SPARC CSV not found.")
        return
    df = load_sparc(str(path))
    print(f"Rows={len(df)} galaxies={df.galaxy.nunique()}")
    print("See SPARC_CHI2_REPORT.md for historical untuned medians.")
    print("=" * 60)

if __name__ == "__main__":
    main()
