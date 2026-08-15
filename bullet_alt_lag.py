#!/usr/bin/env python3
"""Alternative Bullet Cluster lag models beyond simple r0/c."""
from __future__ import annotations
import numpy as np

KPC = 3.085677581e19
M_SUN = 1.9885e30
C = 2.99792458e8
V = 4000e3
M_BULLET = 2e14 * M_SUN
M_GAL = 1e11 * M_SUN
TARGET = 100 * KPC

def r0_locked(M):
    return 0.45 * KPC * (M / M_GAL) ** 0.40

def main():
    print("=" * 64)
    print("Bullet alternative lag models")
    r0_b = r0_locked(M_BULLET)
    print(f"Locked r0(Bullet)={r0_b/KPC:.2f} kpc; simple Δx={V*r0_b/C/KPC:.4f} kpc (FAIL)")
    N_need = TARGET * C / (V * r0_b)
    print(f"\nModel A/C (c_eff or multi-pass): N required ≈ {N_need:.0f}")
    print(f"Model D (cluster-only ξ): ξ required ≈ {N_need:.0f} — preserves galactic lock")
    ratio = TARGET / (V / C * 0.45 * KPC)
    beta_need = np.log(ratio) / np.log(M_BULLET / M_GAL)
    print(f"Model B (universal β): β required ≈ {beta_need:.2f} — BREAKS galactic lock")
    print("Best candidate: Model D (cluster collective scale). Status: OPEN.")
    print("=" * 64)

if __name__ == "__main__":
    main()
