#!/usr/bin/env python3
"""Rebuild data/sparc_flat.csv from the public SPARC Rotmod_LTG.zip.

Source: Lelli, McGaugh & Schombert 2016, AJ 152, 157.
Zenodo: https://doi.org/10.5281/zenodo.16284118 (file Rotmod_LTG.zip).

This is a format adapter only. It does not rescale velocities or drop
galaxies. Surface-brightness columns are omitted because the scorers
do not read them. A survey column is added so the existing
``survey == "SPARC"`` filter keeps every row.
"""
from __future__ import annotations

import argparse
import csv
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "data" / "sparc_flat.csv"
FIELDS = ["survey", "galaxy", "Rad", "Vobs", "errV", "Vgas", "Vdisk", "Vbul"]


def rows_from_zip(zip_path: Path):
    with zipfile.ZipFile(zip_path) as archive:
        names = sorted(n for n in archive.namelist() if n.endswith("_rotmod.dat"))
        if len(names) != 175:
            raise SystemExit(f"expected 175 rotmod files, found {len(names)}")
        for name in names:
            galaxy = Path(name).name.replace("_rotmod.dat", "")
            text = archive.read(name).decode("utf-8", errors="replace")
            for line in text.splitlines():
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                parts = line.split()
                if len(parts) < 6:
                    continue
                rad, vobs, err, vgas, vdisk, vbul = parts[:6]
                yield {
                    "survey": "SPARC",
                    "galaxy": galaxy,
                    "Rad": rad,
                    "Vobs": vobs,
                    "errV": err,
                    "Vgas": vgas,
                    "Vdisk": vdisk,
                    "Vbul": vbul,
                }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("zip_path", type=Path, help="Rotmod_LTG.zip")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = parser.parse_args()
    rows = list(rows_from_zip(args.zip_path))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    galaxies = {row["galaxy"] for row in rows}
    print(f"wrote {args.out} rows={len(rows)} galaxies={len(galaxies)}")


if __name__ == "__main__":
    main()
