#!/usr/bin/env python3
"""Continuous local SPARC under frozen macro r0(Mb), W=1/(4π)."""
from __future__ import annotations
import numpy as np
import pandas as pd
from pathlib import Path
from scipy.optimize import minimize

W = 1.0/(4.0*np.pi)
G = 4.30091e-6
M_REF = 1e11
R0_REF = 0.45
ALPHA = 0.40

def r0_kpc(Mb):
    return R0_REF * (max(Mb, 1e6)/M_REF)**ALPHA

def load(path):
    df = pd.read_csv(path)
    return df[(df.survey=="SPARC")&(df.errV>0)].copy()

def Mb_est(gdf, ud, ub):
    r = gdf.Rad.values
    Vb2 = gdf.Vgas.values**2 + ud*gdf.Vdisk.values**2 + ub*gdf.Vbul.values**2
    i = np.argmax(r)
    return max(Vb2[i]*r[i]/G, 1e6) if r[i]>0 and Vb2[i]>0 else M_REF

def chi2_params(x, gdf, hasb):
    ud, gamma, beta, p = x[0], x[1], x[2], x[3]
    ub = x[4] if hasb else 0.0
    Mb = Mb_est(gdf, ud, ub)
    r0 = r0_kpc(Mb)
    r = np.maximum(gdf.Rad.values, 1e-4)
    Vb2 = gdf.Vgas.values**2 + ud*gdf.Vdisk.values**2 + ub*gdf.Vbul.values**2
    f = (r0/(r+r0))**beta / (1.0 + (r/r0)**max(p,0))
    VW2 = gamma * W * G * Mb / r0 * f
    Vm = np.sqrt(np.maximum(Vb2 + VW2, 0.0))
    res = (gdf.Vobs.values - Vm)/gdf.errV.values
    return float(np.sum(res**2))

def fit(gdf):
    hasb = bool((gdf.Vbul.values>0).any())
    n = len(gdf)
    best_c2, best_x = np.inf, None
    if hasb:
        bounds = [(0.1,1.5),(0.2,2.5),(0.0,2.0),(0.0,2.0),(0.0,1.8)]
        starts = [[0.5,0.8,0.2,0.3,0.7],[0.3,1.2,0.0,0.0,0.5],[0.8,0.5,0.8,0.5,1.0]]
    else:
        bounds = [(0.1,1.5),(0.2,2.5),(0.0,2.0),(0.0,2.0)]
        starts = [[0.5,0.8,0.2,0.3],[0.3,1.2,0.0,0.0],[0.8,0.5,0.8,0.5]]
    for x0 in starts:
        res = minimize(chi2_params, x0, args=(gdf, hasb), bounds=bounds, method="L-BFGS-B",
                       options={"maxiter": 80})
        if res.fun < best_c2:
            best_c2, best_x = res.fun, res.x
    k = 5 if hasb else 4
    return {"chi2": best_c2, "n": n, "ups_disk": best_x[0], "gamma": best_x[1],
            "beta": best_x[2], "p": best_x[3], "chi2_red": best_c2/max(n-k,1)}

def main():
    path = Path("sparc_flat.csv")
    if not path.exists():
        path = Path("/tmp/front/sparc_flat.csv")
    df = load(str(path))
    rows = []
    for name, gdf in df.groupby("galaxy"):
        if len(gdf) < 6: continue
        res = fit(gdf)
        res["galaxy"] = name
        rows.append(res)
    tab = pd.DataFrame(rows)
    print("="*60)
    print(f"Continuous SPARC: median χ²_red = {tab.chi2_red.median():.3f}")
    print(f"Frac <5: {(tab.chi2_red<5).mean()*100:.1f}%  <10: {(tab.chi2_red<10).mean()*100:.1f}%")
    tab.to_csv("sparc_o1_results.csv", index=False)
    print("Macro r0 never varied.")
    print("="*60)

if __name__ == "__main__":
    main()
