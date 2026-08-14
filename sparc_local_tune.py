#!/usr/bin/env python3
"""Local SPARC fine-tuning: frozen macro r0, W=1/(4π), local Υ, β, γ."""
from __future__ import annotations
import numpy as np
import pandas as pd
from pathlib import Path

W_STAR = 1.0/(4.0*np.pi)
G = 4.30091e-6
M_REF = 1e11
R0_REF = 0.45
ALPHA_R0 = 0.40

def r0_kpc(Mb):
    return R0_REF*(max(Mb,1e6)/M_REF)**ALPHA_R0

def load_sparc(path):
    df = pd.read_csv(path)
    return df[(df.survey=="SPARC")&(df.errV>0)].copy()

def estimate_Mb(gdf, ups_d, ups_b):
    r = gdf.Rad.values
    Vbar2 = gdf.Vgas.values**2 + ups_d*gdf.Vdisk.values**2 + ups_b*gdf.Vbul.values**2
    i = np.argmax(r)
    if r[i]<=0 or Vbar2[i]<=0: return M_REF
    return max(Vbar2[i]*r[i]/G, 1e6)

def chi2(gdf, ups_d, ups_b, beta, gamma):
    Mb = estimate_Mb(gdf, ups_d, ups_b)
    r0 = r0_kpc(Mb)
    r = gdf.Rad.values
    Vbar2 = gdf.Vgas.values**2 + ups_d*gdf.Vdisk.values**2 + ups_b*gdf.Vbul.values**2
    VW2 = gamma*W_STAR*G*Mb/r0 * (r0/(r+r0))**beta * np.exp(-r/(r0+r))
    Vmod = np.sqrt(np.maximum(Vbar2+VW2, 0.0))
    resid = (gdf.Vobs.values-Vmod)/gdf.errV.values
    return float(np.sum(resid**2)), len(resid)

def fit_galaxy(gdf):
    best = {"chi2": np.inf}
    has_bul = (gdf.Vbul.values>0).any()
    for ups_d in np.linspace(0.15, 1.4, 8):
        for ups_b in (np.linspace(0.2,1.6,5) if has_bul else [0.0]):
            for beta in (0.0, 0.3, 0.7, 1.2):
                for gamma in (0.6, 0.9, 1.2, 1.5):
                    c2, n = chi2(gdf, ups_d, ups_b, beta, gamma)
                    if c2 < best["chi2"]:
                        best = {"chi2": c2, "n": n, "ups_disk": ups_d,
                                "ups_bul": ups_b, "beta": beta, "gamma": gamma,
                                "chi2_red": c2/max(n-3,1)}
    return best

def main():
    path = Path("sparc_flat.csv")
    if not path.exists():
        path = Path("/tmp/work/sparc_flat.csv")
    df = load_sparc(str(path))
    rows = []
    for name, gdf in df.groupby("galaxy"):
        if len(gdf)<5: continue
        res = fit_galaxy(gdf)
        res["galaxy"] = name
        rows.append(res)
    tab = pd.DataFrame(rows)
    print("="*60)
    print(f"Local SPARC fine-tuning (W=1/4π, macro frozen)")
    print(f"Median χ²_red : {tab.chi2_red.median():.3f}")
    print(f"Fraction < 5  : {(tab.chi2_red<5).mean()*100:.1f}%")
    print(f"Fraction < 10 : {(tab.chi2_red<10).mean()*100:.1f}%")
    tab.to_csv("sparc_local_tune_results.csv", index=False)
    print("Macro r0(Mb) never varied.")
    print("="*60)

if __name__ == "__main__":
    main()
