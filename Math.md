---
# Mathematical & Numerical Framework: Ware Constant Phenomenology (v0.3.7)

**Last update:** 2026-08-14  
**W_star:** \(1/(4\pi)\) at tree level under canonical boundary matching (see WSTAR_ACTION_DERIVATION.md)  
**SPARC:** Macro verified; local median χ²_red ~11.9

## 1. Core Invariant

\[
W_\star = \frac{1}{4\pi}\approx 0.079577
\]

Origin: monopole spherical-harmonic normalization on a 2-sphere screen, with canonical matching \(c_\star=1\). E2–E4 reduced to matching conditions; E1 (existence of screen) remains an infrared input. Bulk confirmation of \(c_\star=1\) open.

## 2. Macro Scaling — Verified

\[
r_0(M_b)=0.45\,\mathrm{kpc}\,(M_b/10^{11}M_\odot)^{0.40}
\]

## 3. Lensing

Multiplicative boost + soft saturation recovers factor 2.2.  
Geodesic integration of additive Φ_W at \(b=R_E\) yields only O(0.1) corrections — **cannot** produce 2.2. Therefore δ_sat for the multiplicative formula remains phenomenological (mapped to ξ); it is not the additive geodesic δ.

## 4. Local Rotation Curves

Median χ²_red ~11.9 (additive Ware + soft radial). RAR-style interpolating law with \(a_0=WGM/r_0^2\) fails badly and is rejected.

## 5. Ledger

| Component | Status |
|-----------|--------|
| \(W_\star=1/(4\pi)\) | Tree-level matching from boundary effective action |
| Macro \(r_0\) | Verified |
| Local SPARC | Median ~11.9 (open toward O(1)) |
| Lensing factor 2.2 | Multiplicative formula; δ_sat phenomenological |
| Bulk proof of \(c_\star=1\) | Open |

## 6. Priority Open Problems

1. Bulk Proca → boundary reduction confirming \(c_\star=1\).
2. Local law for median χ²_red → O(1).
3. Projection of \(T^{\rm info}\) onto the lens plane to derive multiplicative δ_sat.
4. Bullet Cluster lag.

### Cross References

WSTAR_ACTION_DERIVATION.md · WSTAR_ENTROPIC_DERIVATION.md · delta_sat_geodesic.py · sparc_local_tune.py · multiplane_lensing.py
