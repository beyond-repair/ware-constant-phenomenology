#!/usr/bin/env python3
"""
Bullet Cluster lag under locked r0(M).
RESULT: simple r0/c lag FAILS observed O(100 kpc) offsets.
"""
from __future__ import annotations
import numpy as np

KPC = 3.085677581e19
M_SUN = 1.9885e30
C = 2.99792458e8
YR = 365.25 * 24 * 3600

def r0_m(M):
    return 0.45 * KPC * (M / (1e11 * M_SUN)) ** 0.40

def main():
    print("=" * 60)
    print("Bullet Cluster lag — honest evaluation")
    v = 4000e3
    print(f"{'System':<22} {'r0(kpc)':>10} {'Δt(yr)':>12} {'Δx(kpc)':>10}")
    for name, M in [("MW 1e11", 1e11*M_SUN), ("Cluster 1e15", 1e15*M_SUN),
                    ("Bullet 2e14", 2e14*M_SUN)]:
        r0 = r0_m(M)
        print(f"{name:<22} {r0/KPC:10.2f} {r0/C/YR:12.1f} {v*r0/C/KPC:10.4f}")
    print(f"r0 needed for Δx=100 kpc @ 4000 km/s: {100*KPC*C/v/KPC:.0f} kpc")
    print("RESULT: simple r0/c lag FAILS. Open / potential falsifier.")
    print("=" * 60)

if __name__ == "__main__":
    main()
