#!/usr/bin/env python3
"""
sparc_run.py — Canonical SPARC entrypoint
=========================================
Macro r0(Mb) is always frozen. W_star = 1/(4π).

Default: continuous local optimization (sparc_o1).

Usage:
  python sparc_run.py              # continuous fit (recommended)
  python sparc_run.py --mode o1
  python sparc_run.py --mode grid  # legacy grid tuner
  python sparc_run.py --mode chi2  # legacy transparent chi2

Requires: sparc_flat.csv (SPARC flat table) in cwd or path via SPARC_CSV.
"""
from __future__ import annotations
import argparse
import os
import sys
from pathlib import Path

def main():
    p = argparse.ArgumentParser(description="SPARC pipeline entrypoint")
    p.add_argument("--mode", choices=("o1", "grid", "chi2"), default="o1",
                   help="o1=continuous (default), grid=legacy local_tune, chi2=legacy report")
    args = p.parse_args()

    # ensure data hint
    csv = os.environ.get("SPARC_CSV", "sparc_flat.csv")
    if not Path(csv).exists():
        print(f"Note: {csv} not found in cwd. Scripts may look under /tmp paths.")
        print("Download SPARC flat CSV and set SPARC_CSV= or place sparc_flat.csv here.")

    if args.mode == "o1":
        import sparc_o1
        sparc_o1.main()
    elif args.mode == "grid":
        print("DEPRECATED mode=grid → sparc_local_tune (prefer mode=o1)")
        import sparc_local_tune
        sparc_local_tune.main()
    else:
        print("DEPRECATED mode=chi2 → sparc_chi2 (prefer mode=o1)")
        import sparc_chi2
        sparc_chi2.main()

if __name__ == "__main__":
    main()
