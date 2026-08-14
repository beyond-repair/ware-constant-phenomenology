#!/usr/bin/env python3
"""
derive_delta_sat.py
-------------------
Connect the |A|^4 saturation structure already present in the
Schwarzschild-Ware / Ware-Full-Action notes to a bounded lensing
correction.

What is derived vs what remains free
------------------------------------
From Ware-Full-Action.tex:
    r_sat ≈ r_0 * (W / (λ_A <A²>))^{1/2}

Define ξ ≡ λ_A <A²> / W.  Then r_sat / r_0 = ξ^{-1/2}.

A minimal map from the saturated log-potential depth to the
lensing amplitude is

    δ_sat = geometric_prefactor * (r_sat / r_0) / (2 W)
          = geometric_prefactor * ξ^{-1/2} / (2 W)

With geometric_prefactor = 1 and W = 0.08, the published target
δ_sat = 1.2 requires ξ ≈ 27.13 (r_sat ≈ 0.19 r_0).

δ_sat is therefore no longer an independent free number; it is
fixed once ξ is specified.  ξ itself remains a microscopic parameter
of the action.  A full ray-trace would replace geometric_prefactor=1
by a computed O(1) factor.
"""

from __future__ import annotations
import numpy as np

W_STAR = 0.08
DELTA_SAT_TARGET = 1.2


def r_sat_over_r0(xi: float) -> float:
    if xi <= 0:
        raise ValueError("xi must be positive")
    return xi ** (-0.5)


def delta_sat_from_xi(xi: float, geometric_prefactor: float = 1.0) -> float:
    return geometric_prefactor * r_sat_over_r0(xi) / (2.0 * W_STAR)


def xi_from_delta_sat(delta_sat: float, geometric_prefactor: float = 1.0) -> float:
    return (geometric_prefactor / (delta_sat * 2.0 * W_STAR)) ** 2


def main():
    print("=" * 60)
    print("Map: |A|^4 parameters → δ_sat")
    print("=" * 60)
    print(f"W_star = {W_STAR}")
    print(f"Target δ_sat = {DELTA_SAT_TARGET}")
    xi_req = xi_from_delta_sat(DELTA_SAT_TARGET)
    print(f"Required ξ = λ_A <A²> / W : {xi_req:.4f}")
    print(f"r_sat / r_0               : {r_sat_over_r0(xi_req):.4f}")
    print()
    print(f"{'ξ':>10} {'r_sat/r0':>10} {'δ_sat':>10} {'factor':>10}")
    for xi in [0.5, 1.0, 5.0, 10.0, xi_req, 50.0]:
        ds = delta_sat_from_xi(xi)
        print(f"{xi:10.4f} {r_sat_over_r0(xi):10.4f} {ds:10.4f} {1+ds:10.4f}")
    print()
    print("δ_sat is fixed by ξ; ξ remains a free microscopic parameter.")
    print("geometric_prefactor = 1 pending full ray-trace.")
    print("=" * 60)


if __name__ == "__main__":
    main()
