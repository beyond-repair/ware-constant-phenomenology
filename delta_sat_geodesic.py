#!/usr/bin/env python3
"""
delta_sat_geodesic.py
---------------------
Thin-lens geodesic integration of the saturated Schwarzschild-Ware
potential. Demonstrates that additive Φ_W deflection at b=R_E cannot
produce a multiplicative factor ~2.2; δ_sat for the multiplicative
formula remains phenomenological pending a projection of T_info onto
the lens plane.
"""
from __future__ import annotations
import numpy as np

W = 1.0/(4.0*np.pi)
G = 6.6743e-11
C = 2.99792458e8
KPC = 3.085677581e19
MPC = 1e3*KPC
M_SUN = 1.9885e30

def ln_sat(r, r0, r_sat, W=W):
    lam = r0*np.exp(-1.0/(2.0*W))
    r = np.asarray(r, dtype=float)
    x = np.maximum(r, lam)/lam
    x_s = max(r_sat/lam, 1.0+1e-12)
    ln_x = np.log(x)
    return ln_x/(1.0 + ln_x/np.log(x_s))

def Phi_over_c2(r, M, r0, r_sat, W=W):
    return (W*G*M/(r0*C**2))*ln_sat(r, r0, r_sat, W)

def thin_lens_deflection(b, M, r0, r_sat, n=8000):
    zmax = 80*max(r0, b, r_sat)
    z = np.linspace(-zmax, zmax, n)
    dz = z[1]-z[0]
    eps = max(1e-4*b, 1e-7*r0)
    rp = np.sqrt((b+eps)**2+z**2)
    rm = np.sqrt((b-eps)**2+z**2)
    dPhi = (Phi_over_c2(rp,M,r0,r_sat)-Phi_over_c2(rm,M,r0,r_sat))/(2*eps)
    return 2.0*np.sum(dPhi)*dz

def gr_deflection(b, M):
    return 4*G*M/(C**2*np.maximum(b,1e-15))

def main():
    M = 5.86e11*M_SUN
    r0 = 0.91*KPC
    Dl, Ds = 1188*MPC, 1652*MPC
    Dls = max(Ds-Dl, 0.1*Ds)
    RE = np.sqrt(4*G*M/C**2*Dls/(Dl*Ds))*Dl
    aGR = gr_deflection(RE, M)
    print("="*60)
    print("Geodesic thin-lens constraint on δ_sat")
    print(f"R_E={RE/KPC:.3f} kpc  α_GR={aGR:.6e}")
    print(f"{'r_sat/r0':>10} {'α_W/α_GR':>12} {'factor_proxy':>12}")
    for ratio in (0.1, 0.19, 0.5, 1.0, 5.0):
        aW = thin_lens_deflection(RE, M, r0, ratio*r0)
        print(f"{ratio:10.2f} {aW/aGR:12.6e} {1+aW/aGR:12.6f}")
    print("Additive Φ_W cannot yield factor ~2.2; δ_sat stays phenomenological.")
    print("="*60)

if __name__ == "__main__":
    main()
