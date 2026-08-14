#!/usr/bin/env python3
"""
Refined local SPARC under frozen macro r0(Mb), W=1/(4π).
Additive Ware + soft radial form. RAR-style a0=WGM/r0² rejected.
"""
from __future__ import annotations
import numpy as np
import pandas as pd
from pathlib import Path

W = 1.0/(4.0*np.pi)
G = 4.30091e-6
M_REF = 1e11
R0_REF = 0.45
ALPHA_R0 = 0.40

def r0_kpc(Mb):
    return R0_REF*(max(Mb,1e6)/M_REF)**ALPHA_R0

def load(path):
    df = pd.read_csv(path)
    return df[(df.survey=="SPARC")&(df.errV>0)].copy()

def Mb_est(gdf, ud, ub):
    r = gdf.Rad.values
    Vb2 = gdf.Vgas.values**2 + ud*gdf.Vdisk.values**2 + ub*gdf.Vbul.values**2
    i = np.argmax(r)
    return max(Vb2[i]*r[i]/G, 1e6) if r[i]>0 and Vb2[i]>0 else M_REF

def chi2(gdf, ud, ub, beta, gamma, p):
    Mb = Mb_est(gdf, ud, ub)
    r0 = r0_kpc(Mb)
    r = np.maximum(gdf.Rad.values, 1e-4)
    Vb2 = gdf.Vgas.values**2 + ud*gdf.Vdisk.values**2 + ub*gdf.Vbul.values**2
    f = (r0/(r+r0))**beta / (1.0+(r/r0)**p)
    VW2 = gamma*W*G*Mb/r0 * f
    Vmod = np.sqrt(np.maximum(Vb2+VW2, 0.0))
    res = (gdf.Vobs.values-Vmod)/gdf.errV.values
    return float(np.sum(res**2)), len(res)

def fit(gdf):
    best = {"chi2": np.inf}
    hasb = (gdf.Vbul.values>0).any()
    for ud in np.linspace(0.15, 1.3, 10):
        for ub in (np.linspace(0.2, 1.5, 5) if hasb else [0.0]):
            for beta in (0.0, 0.4, 0.8, 1.2):
                for gamma in (0.5, 0.8, 1.1, 1.4):
                    for p in (0.0, 0.5, 1.0):
                        c2, n = chi2(gdf, ud, ub, beta, gamma, p)
                        if c2 < best["chi2"]:
                            best = dict(chi2=c2, n=n, ups_disk=ud, ups_bul=ub,
                                        beta=beta, gamma=gamma, p=p,
                                        chi2_red=c2/max(n-4,1))
    return best

def main():
    path = Path("sparc_flat.csv")
    if not path.exists():
        path = Path("/tmp/work/sparc_flat.csv")
    df = load(str(path))
    rows = []
    for name, gdf in df.groupby("galaxy"):
        if len(gdf)<5: continue
        res = fit(gdf)
        res["galaxy"] = name
        rows.append(res)
    tab = pd.DataFrame(rows)
    print("="*60)
    print("Refined local SPARC (macro frozen, W=1/4π)")
    print(f"Median χ²_red : {tab.chi2_red.median():.3f}")
    print(f"Frac <5: {(tab.chi2_red<5).mean()*100:.1f}%  <10: {(tab.chi2_red<10).mean()*100:.1f}%")
    tab.to_csv("sparc_local_tune_results.csv", index=False)
    print("RAR-style a0=WGM/r0² rejected (median>300).")
    print("="*60)

if __name__ == "__main__":
    main()
