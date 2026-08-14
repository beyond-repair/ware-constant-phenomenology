---
# Mathematical & Numerical Framework: Ware Constant Phenomenology (v0.3.6)

**Last update:** 2026-08-14  
**W_star status:** Entropic candidate \(W_\star=1/(4\pi)\approx0.0796\) under axioms E1–E4  
**SPARC status:** Macro verified; local median χ²_red ~12

## 1. Core Invariant

\[
W_\star = \frac{1}{4\pi} \approx 0.079577
\]

Derived under solid-angle / holographic-screen axioms (see WSTAR_ENTROPIC_DERIVATION.md). Rounded value 0.08 acceptable for galactic work (<1% difference). Option A remains in force (M2 is geometric only).

## 2. Macro Scaling (Verified)

\[
r_0(M_b) = 0.45\,\mathrm{kpc}\,(M_b/10^{11}M_\odot)^{0.40}
\]

## 3. Lensing

Multiplicative boost with soft saturation:
\[
\delta_{\rm raw}=\frac{\pi W D_l}{4 r_0},\quad
\delta_{\rm eff}=\frac{\delta_{\rm raw}}{1+\delta_{\rm raw}/\delta_{\rm sat}},\quad
{\rm factor}=1+\delta_{\rm eff}
\]
With \(\delta_{\rm sat}=1.2\) the asymptotic factor is 2.2 (recovered). Additive galactic-potential deflection is too small at Gpc scales and is not used.

## 4. Local Rotation Curves

Median χ²_red ~12 with per-galaxy Υ, β, γ (macro frozen). Improved; not closed.

## 5. Consistency Ledger

| Component | Status |
|-----------|--------|
| \(W_\star=1/(4\pi)\) | Entropic derivation under E1–E4 |
| Macro \(r_0(M_b)\) | Verified |
| Local SPARC χ² | Median ~12 (open toward O(1)) |
| Lensing factor ~2.2 | Recovered (multiplicative + saturation) |
| Bridge axioms → Proca action | Open |

## 6. Priority Open Problems

1. Elevate E1–E4 from axioms to theorems of the Proca+Einstein action.
2. Local profile structure for median χ²_red → O(1).
3. First-principles origin of δ_sat (mapped to ξ; geometric_prefactor).

### Cross References

WSTAR_ENTROPIC_DERIVATION.md · multiplane_lensing.py · sparc_local_tune.py · SPARC_CHI2_REPORT.md
