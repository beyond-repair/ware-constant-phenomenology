# Derivation inventory — what is proved in this work

**Date:** 2026-09-23  
**Rule:** a derivation is a closed implication from stated axioms or an action variation. A matching convention, a fit, or a target back-solve is not a proof.

Companion: [AUDIT_2026-09-22.md](AUDIT_2026-09-22.md), [AUDIT_2026-09-23.md](AUDIT_2026-09-23.md), [CONSTANT_W_ACTION_PRINCIPLE.md](CONSTANT_W_ACTION_PRINCIPLE.md).

## A. Closed in-tree (keep)

| ID | Statement | Kind | Where |
|----|-----------|------|-------|
| D1 | E1–E4 ⇒ W★=1/(4π) | Conditional on four Model axioms | `WSTAR_ENTROPIC_DERIVATION.md` |
| D2 | Canonical monopole matching c★=1 ⇒ W_eff=1/(4π) | Matching convention, not bulk theorem | `WSTAR_ACTION_DERIVATION.md`, `bulk_boundary_reduction.py` |
| D3 | Option A: gravitational formulae use constant W★; M2 is geometric only | Policy lock resolving W(3) vs 0.125 | `W3_RESOLUTION_NOTE.md` |
| D4 | Model A ratios 0.795:1:1.259 from W(n) alone | Algebra | m2 + freeze |
| D5 | Model B ratios 0.589:1:1.699 from W(n)(3α)^n | Algebra | m2 |
| D6 | Hybrid 0.795:1:1.993 is not D4 or D5 | Falsification | Sweep-137 |
| D7 | Gasket harmonic energy E_n/E_{n-1}=3/5 | Deterministic | sierpinski KIGAMI_PCF.md |
| D8 | Two-corner R_n/R_{n-1}=5/3 | Deterministic | same |
| D9 | Dirichlet λ_min ratios → 1/5; λ_max=6; mult(6) formula | Deterministic | sierpinski SPECTRUM.md |
| D10 | Small-shear F∝γ on equal-rest-length edges | First-order identity | sierpinski FINDINGS |
| D11 | Constant-W Euclidean Gaussian Γ_E=S_W+1/2 Tr ln(ω^{2}I-WL) implies δS_W/δW=1/2 Tr[K^{-1}L] | Action variation (A1–A4) | `CONSTANT_W_ACTION_PRINCIPLE.md` |
| D12 | V''_1-loop(W)<0 on K≻0; no convex determinant barrier | Deterministic | same + `verify_constant_W_action.py` |
| D13 | Finite normalized graph: λ_max=6, ω=1 ⇒ W<1/6 | Operator positivity + D9 | same |

D7–D10 do **not** imply D1. Finite-mesh spectral route to 0.08 already failed (`WSTAR_FIRST_PRINCIPLES_NOTE.md`). D11–D13 do **not** imply D1, do **not** select W=0.08, and do **not** promote W to a healthy local field.

## B. Written as derivations, not closed

| ID | Claim in TeX / notes | Gap |
|----|----------------------|-----|
| U1 | Proca Lagrangian ⇒ r_0 ∝ M_b^{0.40} | Formula in PROVISIONAL_DERIVATIONS.tex mixes Compton length, G, ρ_b^α without a completed Euler–Lagrange reduction and coefficient audit. Exponent uses assumed R∝M^{0.3}. |
| U2 | W<0.125 ⇒ ghost-free | Stated, not derived from the kinetic operator of the written action. Distinct from D13 (W<1/6 is positivity of K=ω^{2}I-WL, not a Proca ghost theorem). |
| U3 | δ_sat=1.2 from |A|^4 | Parameter chosen to recover ×2.2 lensing. |
| U4 | Bullet Δt=r_0/c | Simple model FAIL in CONSISTENCY / Math.md. |
| U5 | Bulk non-minimal confirmation of c★=1 | Explicitly open. DtN script does not output 0.08. |
| U6 | ξ=0.23 in W(n) | Model parameter. No β-function. |
| U7 | Thrust 3×10^{-8} N/W from LDOS | Design target. Forbidden as a derivation of W. |
| U8 | SPARC residual <5% in June TeX | Contradicted by later median χ^{2}_red ~ 9.1. Later number wins. |
| U9 | Local dynamical W(x), Z_ren, Γ^{(2)}(p) | Ordering, UV regulator, and counterterms unfixed. Unrenormalized Z_induced<0 for K_sym is model-specific. |

## C. Internal conflicts still in tree

1. Weak-field law is not unique:
   - Math.md: a = GM/r^{2} + W★ GM/(r_0 r)
   - Ware-Full-Action.tex: a = -(GM/r^{2})[1-W(r_0/r)^{1-2α}e^{-r/r_0}]
   These are different functions. Do not quote both as “the” geodesic limit.
2. June TeX still uses deprecated W(n)=0.08 e^{0.23(n-1)} and hybrid ratios. CLAIM_STATUS / Sweep-137 override.
3. `-ware-constant-derivation` now holds the constant-W freeze. It still does **not** derive numerical 0.08 from the thrust target. The GitHub *description* of that repo remains a false proof claim until edited at the GitHub metadata layer.

## D. Strongest remaining derivation paths (not executed)

Promote D2 from convention to theorem:

1. Fix the Proca + Einstein action with current indexing.
2. Reduce monopole on a ball to a boundary quadratic form.
3. Show the DtN prefactor is exactly 1 after wave-function renormalization, or report the computed c★.
4. Stop if c★≠1. Do not reset W to 0.08 by hand.

Promote constant W to a local field (D11 extension):

1. Fix Hermitian K[W(x)].
2. Fix a UV regulator.
3. Compute renormalized Γ^{(2)}(p) and Z_ren.
4. Derive S_W independently if Z_induced<0.

Honest sentences:

- W★=1/(4π) is the adopted matching / solid-angle value, not a completed Proca-action theorem.
- The constant-W spectral source is derived. A propagating W(x) is not.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
