#!/usr/bin/env python3
"""Bulk → boundary monopole DtN + matching structure for c_star."""
from __future__ import annotations
import numpy as np

def dtn_monopole(R=1.0, m=1e-6, n_r=400):
    mR = m * R
    if mR < 1e-8:
        kappa_cont = 0.0
    else:
        kappa_cont = m * np.cosh(mR) / np.sinh(mR) - 1.0 / R
    r = np.linspace(0, R, n_r + 1)
    dr = r[1] - r[0]
    N = n_r - 1
    A = np.zeros((N, N))
    b = np.zeros(N)
    for i in range(N):
        A[i, i] = -2.0 / dr**2 - m**2
        if i > 0:
            A[i, i - 1] = 1.0 / dr**2
        if i < N - 1:
            A[i, i + 1] = 1.0 / dr**2
        else:
            b[i] -= (1.0 / dr**2) * R
    u_int = np.linalg.solve(A, b)
    phi_Rm = u_int[-1] / (R - dr)
    kappa_disc = (1.0 - phi_Rm) / dr
    return kappa_cont, kappa_disc

def main():
    print("=" * 60)
    print("Bulk → boundary reduction (monopole DtN)")
    for m in (0.0, 1e-3, 0.1, 1.0):
        kc, kd = dtn_monopole(R=1.0, m=max(m, 1e-15))
        print(f"m={m:.1e}  κ_cont={kc:.6e}  κ_disc={kd:.6e}")
    print("W_eff = c_star/(4π); c_star=1 under canonical matching.")
    print("Full non-minimal bulk confirmation still open.")
    print("=" * 60)

if __name__ == "__main__":
    main()
