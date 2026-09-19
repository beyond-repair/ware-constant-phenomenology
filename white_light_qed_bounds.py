#!/usr/bin/env python3
"""
white_light_qed_bounds.py
-------------------------
Deterministic order-of-magnitude bounds for the Euler-Heisenberg
fractional energy correction at fixed mean intensity.

Claim cap: RESEARCH / claim 1. Not a measurement. Not a W_star derivation.

Prints:
  - EH prefactor alpha/(45 pi)
  - Delta u / u for representative laboratory fields
  - g^(2) quartic multiplier
  - scale comparison against W_star and 1/(4 pi)
"""
from __future__ import annotations

import math

ALPHA = 1.0 / 137.035999084
PI = math.pi
E_CRIT = 1.32e18  # V/m, Schwinger critical field (accepted rounded value)
W_STAR = 0.08
W_SOLID_ANGLE = 1.0 / (4.0 * PI)


def eh_prefactor() -> float:
    return ALPHA / (45.0 * PI)


def fractional_eh(E_v_per_m: float) -> float:
    """Electric-dominated leading EH fractional energy correction."""
    return eh_prefactor() * (E_v_per_m / E_CRIT) ** 2


def main() -> None:
    pre = eh_prefactor()
    print("=" * 64)
    print("White-Light / EH numeric bounds (claim 1)")
    print("=" * 64)
    print(f"alpha/(45 pi)           = {pre:.6e}")
    print(f"E_c                     = {E_CRIT:.3e} V/m")
    print()
    cases = [
        ("optical CW", 1.0e6),
        ("intense lab", 1.0e8),
        ("TW-class focus", 1.0e11),
        ("PW-class focus", 1.0e12),
        ("0.01 E_c", 0.01 * E_CRIT),
    ]
    print(f"{'case':20s} {'E (V/m)':>12s} {'(E/Ec)^2':>12s} {'Du/u':>12s}")
    for name, E in cases:
        frac = fractional_eh(E)
        ratio = (E / E_CRIT) ** 2
        print(f"{name:20s} {E:12.3e} {ratio:12.3e} {frac:12.3e}")
    print()
    print("g^(2) quartic multipliers at fixed <I>:")
    print("  coherent CW     g2=1  -> x1")
    print("  thermal white   g2=2  -> x2")
    print("  pulsed comb     ~1/duty cycle (not computed here)")
    print()
    print("Scale comparison (dimensionless couplings, not the same operator):")
    print(f"  W_star                 = {W_STAR:.6f}")
    print(f"  1/(4 pi)               = {W_SOLID_ANGLE:.6f}")
    print(f"  alpha/pi               = {ALPHA / PI:.6e}")
    print(f"  alpha/(45 pi)          = {pre:.6e}")
    print(f"  W_star / (alpha/45 pi) = {W_STAR / pre:.3e}")
    print()
    print("Conclusion: EH laboratory Du/u is 1e-29 .. 1e-17 in these cases.")
    print("EH does not produce W_star. Do not stack anomaly on top of EH.")
    print("=" * 64)


if __name__ == "__main__":
    main()
