#!/usr/bin/env python3
"""
geodesic_lensing_prefactor.py
-----------------------------
Thin-lens deflection from the soft-saturated Schwarzschild-Ware potential
and an estimate of the geometric prefactor for δ_sat.

Hard cutoff Φ=const for r>r_sat yields zero deflection at b>r_sat and is
therefore too crude for cosmological Einstein radii. Soft saturation
(motivated by |A|^4) is required.
"""

from __future__ import annotations
import numpy as np

W_STAR = 0.08
G = 6.6743e-11
C = 2.99792458e8
KPC = 3.085677581e19
M_SUN = 1.9885e30


def Phi_soft(r, M, r0, W=W_STAR, r_sat=None):
    if r_sat is None:
        r_sat = 0.19 * r0
    lam = r0 * np.exp(-1.0 / (2.0 * W))
    r = np.asarray(r, dtype=float)
    x = np.maximum(r, lam) / lam
    x_sat = r_sat / lam
    ln_x = np.log(x)
    ln_sat = np.log(x_sat)
    ln_eff = ln_x / (1.0 + ln_x / ln_sat)
    return (W * G * M / (r0 * C**2)) * ln_eff


def deflection_soft(b, M, r0, n=8000, W=W_STAR):
    r_sat = 0.19 * r0
    zmax = 50 * max(r0, b, r_sat)
    z = np.linspace(-zmax, zmax, n)
    dz = z[1] - z[0]
    eps = max(1e-4 * b, 1e-6 * r0)
    rp = np.sqrt((b + eps)**2 + z**2)
    rm = np.sqrt((b - eps)**2 + z**2)
    dPhi = (Phi_soft(rp, M, r0, W, r_sat) - Phi_soft(rm, M, r0, W, r_sat)) / (2 * eps)
    return 2.0 * np.sum(dPhi) * dz


def geometric_prefactor_estimate(M=1e11*M_SUN, r0=0.45*KPC, W=W_STAR):
    r_sat = 0.19 * r0
    results = []
    Phi_depth = Phi_soft(r_sat * 100, M, r0, W, r_sat)
    for ratio in (0.2, 0.5, 1.0, 2.0, 5.0, 10.0):
        b = ratio * r0
        alpha = deflection_soft(b, M, r0, W=W)
        alpha_char = 2.0 * Phi_depth
        pref = alpha / alpha_char if abs(alpha_char) > 0 else np.nan
        results.append((ratio, b/KPC, alpha, pref))
    return results, Phi_depth


def main():
    print("=" * 60)
    print("Soft-saturation thin-lens geometric_prefactor estimate")
    print("=" * 60)
    rows, Phi_depth = geometric_prefactor_estimate()
    print(f"Asymptotic Φ_depth / c² = {Phi_depth:.6e}")
    print(f"{'b/r0':>8} {'b(kpc)':>10} {'α(rad)':>14} {'prefactor':>10}")
    for ratio, b_kpc, alpha, pref in rows:
        print(f"{ratio:8.2f} {b_kpc:10.4f} {alpha:14.6e} {pref:10.4f}")
    print(f"\nRecommended geometric_prefactor (at b≈r0): {rows[2][3]:.4f}")
    print("Hard cutoff is inadequate; soft saturation required.")
    print("=" * 60)


if __name__ == "__main__":
    main()
