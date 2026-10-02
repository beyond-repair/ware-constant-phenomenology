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

Requires a SPARC-style flat CSV. Offline default:
  data/sparc_flat_demo.csv (synthetic DEMO) or root sparc_flat.csv.
Override with SPARC_CSV=path/to/real_sparc_flat.csv
(e.g. SPARC_CSV=data/sparc_flat.csv for the optional Lelli+2016 table).
"""
from __future__ import annotations

import argparse

from data_paths import sparc_csv


def main():
    p = argparse.ArgumentParser(description="SPARC pipeline entrypoint")
    p.add_argument(
        "--mode",
        choices=("o1", "grid", "chi2"),
        default="o1",
        help="o1=continuous (default), grid=legacy local_tune, chi2=legacy report",
    )
    args = p.parse_args()

    found = sparc_csv()
    if found is None:
        print("Note: no SPARC CSV found. Scripts expect data/sparc_flat_demo.csv")
        print("or SPARC_CSV= pointing at a real SPARC flat table.")
    else:
        print(f"Using SPARC CSV: {found}")

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
