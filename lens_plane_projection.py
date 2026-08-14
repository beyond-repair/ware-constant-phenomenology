#!/usr/bin/env python3
"""Lens-plane projection of T_info: multiplicative factor from Σ_info/Σ_b."""
from __future__ import annotations
import numpy as np

W = 1.0 / (4.0 * np.pi)
G = 6.6743e-11
C = 2.99792458e8
KPC = 3.085677581e19
MPC = 1e3 * KPC
M_SUN = 1.9885e30

def main():
    M = 5.86e11 * M_SUN
    Rd = 3.0 * KPC
    r0 = 0.91 * KPC
    Dl, Ds = 1188 * MPC, 1652 * MPC
    Dls = max(Ds - Dl, 0.1 * Ds)
    RE = np.sqrt(4 * G * M / C**2 * Dls / (Dl * Ds)) * Dl
    r_sat = 0.19 * r0
    R = np.linspace(1e-4 * Rd, 3 * RE, 2000)
    dR = R[1] - R[0]
    Sb = M / (2 * np.pi * Rd**2) * np.exp(-R / Rd)
    Si = Sb / (1.0 + (R / r_sat)**2)
    mask = R <= RE
    Mb = 2 * np.pi * np.sum(Sb[mask] * R[mask] * dR)
    Mi = 2 * np.pi * np.sum(Si[mask] * R[mask] * dR)
    xi = Mi / Mb
    xi_cap = 1.2 / W
    xi_eff = xi / (1.0 + xi / xi_cap)
    print("=" * 60)
    print("Lens-plane T_info projection")
    print(f"ξ={xi:.4f}  factor_unsat={1+W*xi:.4f}  factor_sat={1+W*xi_eff:.4f}")
    print("δ_sat=1.2 recovered via ξ_cap=1.2/W (matching); |A|^4 derivation open.")
    print("=" * 60)

if __name__ == "__main__":
    main()
