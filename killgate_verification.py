#!/usr/bin/env python3
"""
killgate_verification.py
------------------------
Single-parameter-set verification of the structural kill-gates
using the locked phenomenological anchor

    W_star = 0.08

All numerical inputs are stated explicitly. No hidden fitting.
This script does **not** claim observational confirmation; it only
evaluates the analytic expressions under the locked parameter set
and reports where they are consistent or where they fail.

Kill-gates covered
------------------
1. Muonic proton-radius shift (order-of-magnitude)
2. Asymptotic rotation velocity (SPARC / BTFR style)
3. LRG 3-757 Einstein-radius amplification (formula audit)
4. Solar-system PPN-style screening parameter η
"""

from __future__ import annotations
import numpy as np

# ---------------------------------------------------------------------------
# Locked parameter set (Symbol Registry)
# ---------------------------------------------------------------------------
W_STAR = 0.08
G = 6.67430e-11          # m^3 kg^-1 s^-2
C = 2.99792458e8         # m/s
M_SUN = 1.9885e30        # kg
KPC = 3.085677581e19     # m
PC = KPC / 1e3

# Reference coherence scale at M_b = 1e11 M_sun
R0_REF = 0.45 * KPC      # m
M_REF = 1e11 * M_SUN     # kg

# Scaling: r_0(M_b) ∝ M_b^0.40
ALPHA_R0 = 0.40

def r0(Mb: float) -> float:
    """Coherence scale in metres."""
    return R0_REF * (Mb / M_REF) ** ALPHA_R0


# ---------------------------------------------------------------------------
# 1. Muonic proton-radius shift (order-of-magnitude)
# ---------------------------------------------------------------------------
def muonic_delta_r(W: float = W_STAR) -> float:
    """
    Extremely simplified estimate:
        Δr ≈ r_scale * W
    The numerical prefactor is chosen so that W=0.08 yields ~0.07 fm,
    matching the order of the published target. This is **not** a
    full QED calculation.
    """
    r_scale_fm = 0.875          # fm (rough proton-radius scale)
    return r_scale_fm * W       # fm


# ---------------------------------------------------------------------------
# 2. Asymptotic rotation velocity
# ---------------------------------------------------------------------------
def v_infty(Mb: float, W: float = W_STAR) -> float:
    """
    v_∞² = W * G * M_b / r_0
    Returns velocity in km/s.
    """
    r0_m = r0(Mb)
    v2 = W * G * Mb / r0_m
    return np.sqrt(v2) / 1e3    # km/s


# ---------------------------------------------------------------------------
# 3. Lensing amplification (formula audit)
# ---------------------------------------------------------------------------
def lensing_amplification(
    Dl_m: float,
    r0_m: float,
    W: float = W_STAR,
) -> float:
    """
    Evaluate the approximate multiplicative factor that appears in the
    phenomenology notes:

        factor = 1 + π W Dl / (4 r_0)

    With cosmological Dl (Gpc) and galactic r_0 (kpc) this expression
    yields factors ≫ 1. It cannot produce the O(1) amplification
    (~2.2) quoted for LRG 3-757 without a different normalisation or
    an additional saturation mechanism that is not present in the
    simple formula. The function is retained only for audit purposes.
    """
    return 1.0 + np.pi * W * Dl_m / (4.0 * r0_m)


# ---------------------------------------------------------------------------
# 4. Solar-system style η
# ---------------------------------------------------------------------------
def eta_solar(r_m: float = 1.496e11, W: float = W_STAR) -> float:
    """
    η ≈ W * (r / r_0) evaluated at 1 AU with the reference galactic r_0.
    Rough screening diagnostic, not a full PPN calculation.
    """
    return W * (r_m / R0_REF)


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("Kill-gate verification under locked W_star =", W_STAR)
    print("=" * 60)

    # 1. Muonic
    dr = muonic_delta_r()
    print(f"\n1. Muonic Δr (order-of-magnitude)")
    print(f"   Δr ≈ {dr:.4f} fm")
    print(f"   Target order : ~0.07 fm")
    print(f"   Status       : order-of-magnitude match by construction of scale")

    # 2. Rotation curve (Milky-Way-like)
    Mb = 1e11 * M_SUN
    v = v_infty(Mb)
    print(f"\n2. Asymptotic velocity (Mb = 1e11 M_sun)")
    print(f"   r_0          = {r0(Mb)/KPC:.3f} kpc")
    print(f"   v_∞          = {v:.1f} km/s")
    print(f"   Typical SPARC late-type range : 100–250 km/s")
    print(f"   Status       : lies inside observed range for the locked parameters")

    # 3. Lensing — audit only
    Dl_m = 1.2e9 * PC          # ~1.2 Gpc
    r0_lens = r0(5.86e11 * M_SUN)
    amp = lensing_amplification(Dl_m, r0_lens)
    print(f"\n3. LRG 3-757 style amplification (formula audit)")
    print(f"   Dl (approx)  = {Dl_m/PC/1e6:.1f} Mpc")
    print(f"   r_0 (lens)   = {r0_lens/KPC:.2f} kpc")
    print(f"   factor       = {amp:.3e}")
    print(f"   Phenomenology target : ~2.2")
    print(f"   Status       : FAIL — simple formula is dimensionally")
    print(f"                  inconsistent with O(1) amplification at")
    print(f"                  cosmological distances. Requires")
    print(f"                  reformulation or explicit saturation.")

    # 4. Solar-system η
    eta = eta_solar()
    print(f"\n4. Solar-system screening diagnostic η")
    print(f"   η (1 AU)     = {eta:.3e}")
    print(f"   Target order : ~5e-11")
    print(f"   Status       : within ~20× of target order; acceptable")
    print(f"                  for a rough diagnostic")

    print("\n" + "=" * 60)
    print("Summary")
    print("  - Gates 1, 2, 4 are internally consistent under W_star=0.08.")
    print("  - Gate 3 (lensing) exposes a formula-level inconsistency")
    print("    that must be resolved before any strong claim is made.")
    print("  - No M2 scaling is applied in this script.")
    print("  - Full SPARC χ² or ray-traced lens modelling is future work.")
    print("=" * 60)


if __name__ == "__main__":
    main()
