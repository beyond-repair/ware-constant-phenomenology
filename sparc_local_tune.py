#!/usr/bin/env python3
"""
sparc_local_tune.py
-------------------
Local velocity-curve tuning under FROZEN macro scaling.

Macro lock:
    r_0(M_b) = 0.45 kpc * (M_b / 1e11 M_sun)^0.40
    W_star   = 0.08

Local freedom: Υ_disk, β (radial shape).
"""
from __future__ import annotations
import numpy as np
import pandas as pd
from pathlib import Path

W_STAR = 0.08
G = 4.30091e-6
M_REF = 1e11
R0_REF = 0.45
ALPHA_R0 = 0.40

def r0_kpc(Mb):
    return R0_REF * (max(Mb, 1e6) / M_REF) ** ALPHA_R0

def load_sparc(path):
    df = pd.read_csv(path)
    return df[(df.survey == "SPARC") & (df.errV > 0)].copy()

def estimate_Mb(gdf, ups_d, ups_b):
    r = gdf.Rad.values
    Vbar2 = gdf.Vgas.values**2 + ups_d*gdf.Vdisk.values**2 + ups_b*gdf.Vbul.values**2
    i = np.argmax(r)
    if r[i] <= 0 or Vbar2[i] <= 0:
        return M_REF
    return max(Vbar2[i] * r[i] / G, 1e6)

def v_model(gdf, ups_d, ups_b, beta, Mb, r0):
    r = gdf.Rad.values
    Vbar2 = gdf.Vgas.values**2 + ups_d*gdf.Vdisk.values**2 + ups_b*gdf.Vbul.values**2
    VW2_amp = W_STAR * G * Mb / r0
    f = (r0 / (r + r0))**beta * np.exp(-r / (r0 + r))
    return np.sqrt(np.maximum(Vbar2 + VW2_amp * f, 0.0))

def chi2(gdf, ups_d, beta):
    ups_b = 1.4 * ups_d if (gdf.Vbul.values > 0).any() else 0.0
    Mb = estimate_Mb(gdf, ups_d, ups_b)
    r0 = r0_kpc(Mb)
    Vmod = v_model(gdf, ups_d, ups_b, beta, Mb, r0)
    resid = (gdf.Vobs.values - Vmod) / gdf.errV.values
    return float(np.sum(resid**2)), len(resid), Mb, r0

def fit_galaxy(gdf):
    best = {"chi2": np.inf}
    for ups in np.linspace(0.1, 1.5, 15):
        for beta in np.linspace(0.0, 1.5, 16):
            c2, n, Mb, r0 = chi2(gdf, ups, beta)
            if c2 < best["chi2"]:
                best = {"chi2": c2, "n": n, "ups_disk": ups, "beta": beta,
                        "chi2_red": c2 / max(n - 2, 1), "Mb": Mb, "r0": r0}
    return best

def main():
    path = Path("sparc_flat.csv")
    if not path.exists():
        path = Path("/tmp/work/sparc_flat.csv")
    df = load_sparc(str(path))
    rows = []
    for name, gdf in df.groupby("galaxy"):
        if len(gdf) < 4:
            continue
        res = fit_galaxy(gdf)
        res["galaxy"] = name
        rows.append(res)
    tab = pd.DataFrame(rows)
    print("=" * 60)
    print("Local SPARC tuning (macro r0(Mb) FROZEN)")
    print(f"Median χ²_red : {tab.chi2_red.median():.3f}")
    print(f"P16/P50/P84   : {np.percentile(tab.chi2_red,16):.2f} / "
          f"{tab.chi2_red.median():.2f} / {np.percentile(tab.chi2_red,84):.2f}")
    print(f"Fraction < 5  : {(tab.chi2_red<5).mean()*100:.1f}%")
    print(f"Fraction < 10 : {(tab.chi2_red<10).mean()*100:.1f}%")
    tab.to_csv("sparc_local_tune_results.csv", index=False)
    print("Macro relation was never varied.")
    print("=" * 60)

if __name__ == "__main__":
    main()
