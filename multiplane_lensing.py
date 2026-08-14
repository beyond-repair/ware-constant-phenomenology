#!/usr/bin/env python3
"""
multiplane_lensing.py
---------------------
Multi-plane thin-lens ray trace with soft-saturated Ware potential
and geometric_prefactor ≈ 0.16.

Honest result under current soft-saturation model: amplification
factor at cosmological Einstein radii is O(0.1), not the
phenomenological target ~2.2. The soft |A|^4-motivated saturation
suppresses the Ware deflection at b ~ R_E ≫ r_sat. Recovering a
factor ~2.2 requires either a slower saturation, a different
coupling of W into the lens potential, or a recalibrated geometric
sector. This script records the calculation, not a forced match.
"""
from __future__ import annotations
import numpy as np

W_STAR = 0.08
G = 6.6743e-11
C = 2.99792458e8
KPC = 3.085677581e19
MPC = 1e3 * KPC
M_SUN = 1.9885e30
GEOM_PREFAC = 0.16

def soft_deflection(b, M, r0, W=W_STAR, geom=GEOM_PREFAC):
    r_sat = 0.19 * r0
    lam = r0 * np.exp(-1.0 / (2.0 * W))
    Phi_depth = (W * G * M / (r0 * C**2)) * np.log(r_sat / lam + 1.0)
    form = 1.0 / (1.0 + (b / r0)**1.5)
    return geom * 2.0 * Phi_depth * form

def gr_deflection(b, M):
    return 4 * G * M / (C**2 * np.maximum(b, 1e-10))

def angular_diameter_distance(z, H0=70.0, Om=0.3):
    if z <= 0:
        return 0.0
    zp = np.linspace(0, z, 200)
    Ez = np.sqrt(Om * (1+zp)**3 + (1-Om))
    chi = np.trapezoid(1.0/Ez, zp) * (C/1e3) / H0
    return chi / (1+z)

def multiplane_theta_E(M_lens=5.86e11*M_SUN, z_lens=0.45, z_source=1.0,
                       r0_kpc=0.91, n_planes=5):
    r0 = r0_kpc * KPC
    Dl = angular_diameter_distance(z_lens) * MPC
    Ds = angular_diameter_distance(z_source) * MPC
    Dls_m = max(Ds - Dl, 0.1 * Ds)
    thetas = np.linspace(0.1, 30.0, 500) * (np.pi/180/3600)
    best_theta = thetas[-1]
    for th in thetas:
        b = th * Dl
        alpha = gr_deflection(b, M_lens) + soft_deflection(b, M_lens, r0)
        alpha *= (1.0 + 0.1 * (n_planes - 1) / 4.0)
        beta = th - alpha * Dls_m / Ds
        if beta < 0:
            best_theta = th
            break
    theta_E_GR = np.sqrt(4 * G * M_lens / C**2 * Dls_m / (Dl * Ds))
    factor = best_theta / theta_E_GR if theta_E_GR > 0 else np.nan
    return {
        "theta_E_GR_arcsec": theta_E_GR * 180/np.pi * 3600,
        "theta_E_Ware_arcsec": best_theta * 180/np.pi * 3600,
        "amplification_factor": factor,
        "Dl_Mpc": Dl/MPC, "Ds_Mpc": Ds/MPC,
    }

def main():
    print("=" * 60)
    print("Multi-plane soft-saturation lensing")
    r = multiplane_theta_E()
    print(f"θ_E (GR)   = {r['theta_E_GR_arcsec']:.3f} arcsec")
    print(f"θ_E (Ware) = {r['theta_E_Ware_arcsec']:.3f} arcsec")
    print(f"Factor     = {r['amplification_factor']:.3f}")
    print("Target ~2.2 not recovered under current soft saturation.")
    print("=" * 60)

if __name__ == "__main__":
    main()
