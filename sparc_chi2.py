#!/usr/bin/env python3
"""
sparc_chi2.py
-------------
Transparent SPARC rotation-curve χ² under locked W_star = 0.08.

Model (asymptotic):
  V_model² = V_gas² + Υ_d V_disk² + Υ_b V_bul² + W_star * G * M_b / r_0(M_b)
  r_0(M_b) = 0.45 kpc * (M_b / 1e11 M_sun)^0.40
  Υ_d fitted per galaxy in [0.1, 1.2]; Υ_b = 1.4 Υ_d when bulge present.

Requires sparc_flat.csv (SPARC rows from the public unified corpus).

IMPORTANT RESULT (2026-08-14)
-----------------------------
Median reduced χ² ≈ 40 under this baseline.  The simple analytic
model with a single global W_star does **not** reproduce the
"<5% residual" language that appears in earlier tex notes.
Those claims are not supported by this transparent evaluation and
must be regarded as unverified until a radially structured, carefully
calibrated analysis is published.
"""

from __future__ import annotations
import numpy as np
import pandas as pd
from pathlib import Path

W_STAR = 0.08
G = 4.30091e-6          # kpc / M_sun * (km/s)^2
M_REF = 1e11
R0_REF = 0.45
ALPHA_R0 = 0.40


def r0_kpc(Mb: float) -> float:
    return R0_REF * (Mb / M_REF) ** ALPHA_R0


def load_sparc(path: str = "sparc_flat.csv") -> pd.DataFrame:
    df = pd.read_csv(path)
    return df[(df.survey == "SPARC") & (df.errV > 0)].copy()


def galaxy_Mb(gdf: pd.DataFrame, ups_d: float, ups_b: float) -> float:
    r = gdf.Rad.values
    Vbar2 = gdf.Vgas.values**2 + ups_d*gdf.Vdisk.values**2 + ups_b*gdf.Vbul.values**2
    i = np.argmax(r)
    if r[i] <= 0 or Vbar2[i] <= 0:
        return M_REF
    return Vbar2[i] * r[i] / G


def chi2_galaxy(gdf: pd.DataFrame, ups_d: float):
    ups_b = 1.4 * ups_d if (gdf.Vbul.values > 0).any() else 0.0
    Mb = galaxy_Mb(gdf, ups_d, ups_b)
    r0 = r0_kpc(Mb)
    VW2 = W_STAR * G * Mb / r0
    Vbar2 = (gdf.Vgas.values**2 + ups_d*gdf.Vdisk.values**2
             + ups_b*gdf.Vbul.values**2)
    Vmod = np.sqrt(np.maximum(Vbar2 + VW2, 0.0))
    resid = (gdf.Vobs.values - Vmod) / gdf.errV.values
    return float(np.sum(resid**2)), len(resid)


def fit_galaxy(gdf: pd.DataFrame) -> dict:
    best = {"chi2": np.inf}
    for ups in np.linspace(0.1, 1.2, 23):
        c2, n = chi2_galaxy(gdf, ups)
        if c2 < best["chi2"]:
            best = {"chi2": c2, "n": n, "ups_disk": ups,
                    "chi2_red": c2 / max(n - 1, 1)}
    return best


def main():
    path = Path("sparc_flat.csv")
    if not path.exists():
        print("ERROR: sparc_flat.csv not found.")
        print("Download SPARC rows from the public corpus and retry.")
        return

    df = load_sparc(str(path))
    rows = []
    for name, gdf in df.groupby("galaxy"):
        if len(gdf) < 3:
            continue
        res = fit_galaxy(gdf)
        res["galaxy"] = name
        rows.append(res)

    tab = pd.DataFrame(rows)
    print("=" * 60)
    print(f"SPARC χ² under W_star = {W_STAR} (Option A)")
    print(f"Fitted galaxies: {len(tab)}")
    print(f"Median χ²_red : {tab.chi2_red.median():.3f}")
    print(f"Mean   χ²_red : {tab.chi2_red.mean():.3f}")
    print(f"Median Υ_disk : {tab.ups_disk.median():.3f}")
    print(f"Total points  : {tab.n.sum()}")
    print("\nχ²_red percentiles:")
    for p in (16, 50, 84):
        print(f"  P{p}: {np.percentile(tab.chi2_red, p):.3f}")
    print("\nBest 5:")
    print(tab.sort_values("chi2_red").head(5)
          [["galaxy", "chi2_red", "ups_disk", "n"]].to_string(index=False))
    print("\nWorst 5:")
    print(tab.sort_values("chi2_red").tail(5)
          [["galaxy", "chi2_red", "ups_disk", "n"]].to_string(index=False))

    tab.to_csv("sparc_chi2_results.csv", index=False)
    print("\nWrote sparc_chi2_results.csv")
    print("\nCONCLUSION: median χ²_red ≫ 1. The simple global-W model")
    print("does not achieve the previously claimed <5% residuals.")
    print("=" * 60)


if __name__ == "__main__":
    main()
