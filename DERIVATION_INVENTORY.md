# Derivation inventory — what is proved in this work

**Date:** 2026-09-22  
**Rule:** a derivation is a closed implication from stated axioms or an action variation. A matching convention, a fit, or a target back-solve is not a proof.

Companion: [AUDIT_2026-09-22.md](AUDIT_2026-09-22.md).

## A. Closed in-tree (keep)

| ID | Statement | Kind | Where |
|----|-----------|------|-------|
| D1 | E1–E4 ⇒ \(W_\star=1/(4\pi)\) | Conditional on four Model axioms | `WSTAR_ENTROPIC_DERIVATION.md` |
| D2 | Canonical monopole matching \(c_\star=1\) ⇒ \(W_{\rm eff}=1/(4\pi)\) | Matching convention, not bulk theorem | `WSTAR_ACTION_DERIVATION.md`, `bulk_boundary_reduction.py` |
| D3 | Option A: gravitational formulae use constant \(W_\star\); M2 is geometric only | Policy lock resolving W(3) vs 0.125 | `W3_RESOLUTION_NOTE.md` |
| D4 | Model A ratios \(0.795:1:1.259\) from \(W(n)\) alone | Algebra | m2 + freeze |
| D5 | Model B ratios \(0.589:1:1.699\) from \(W(n)(3\alpha)^n\) | Algebra | m2 |
| D6 | Hybrid \(0.795:1:1.993\) is not D4 or D5 | Falsification | Sweep-137 |
| D7 | Gasket harmonic energy \(\mathcal{E}_n/\mathcal{E}_{n-1}=3/5\) | Deterministic | sierpinski `KIGAMI_PCF.md` |
| D8 | Two-corner \(R_n/R_{n-1}=5/3\) | Deterministic | same |
| D9 | Dirichlet \(\lambda_{\min}\) ratios \(\to 1/5\); \(\lambda_{\max}=6\); mult(6) formula | Deterministic | sierpinski `SPECTRUM.md` |
| D10 | Small-shear \(F\propto\gamma\) on equal-rest-length edges | First-order identity | sierpinski FINDINGS |

D7–D10 do **not** imply D1. Finite-mesh spectral route to 0.08 already failed (`WSTAR_FIRST_PRINCIPLES_NOTE.md`).

## B. Written as derivations, not closed

| ID | Claim in TeX / notes | Gap |
|----|----------------------|-----|
| U1 | Proca Lagrangian ⇒ \(r_0\propto M_b^{0.40}\) | Formula in `PROVISIONAL_DERIVATIONS.tex` mixes Compton length, \(G\), \(\rho_b^\alpha\) without a completed Euler–Lagrange reduction and coefficient audit. Exponent uses assumed \(R\propto M^{0.3}\). |
| U2 | \(W<0.125\) ⇒ ghost-free | Stated, not derived from the kinetic operator of the written action. |
| U3 | \(\delta_{\rm sat}=1.2\) from \(|A|^4\) | Parameter chosen to recover ×2.2 lensing. |
| U4 | Bullet \(\Delta t=r_0/c\) | Simple model FAIL in CONSISTENCY / Math.md. |
| U5 | Bulk non-minimal confirmation of \(c_\star=1\) | Explicitly open. DtN script does not output 0.08. |
| U6 | \(\xi=0.23\) in \(W(n)\) | Model parameter. No \(\beta\)-function. |
| U7 | Thrust \(3\times10^{-8}\,\mathrm{N/W}\) from LDOS | Design target. Forbidden as a derivation of \(W\). |
| U8 | SPARC residual \(<5\%\) in June TeX | Contradicted by later median \(\chi^2_{\rm red}\sim 9.1\). Later number wins. |

## C. Internal conflicts still in tree

1. Weak-field law is not unique:
   - `Math.md`: \(a = GM/r^2 + W_\star GM/(r_0 r)\)
   - `Ware-Full-Action.tex`: \(a = -(GM/r^2)[1-W(r_0/r)^{1-2\alpha}e^{-r/r_0}]\)
   These are different functions. Do not quote both as “the” geodesic limit.
2. June TeX still uses deprecated \(W(n)=0.08 e^{0.23(n-1)}\) and hybrid ratios. CLAIM_STATUS / Sweep-137 override.
3. `-ware-constant-derivation` is README-only. GitHub description that derives W from the thrust target is **false** as a proof claim.

## D. Strongest remaining derivation path (not executed)

Only this would promote D2 from convention to theorem:

1. Fix the Proca + Einstein action with current (not deprecated) indexing.
2. Reduce monopole on a ball to a boundary quadratic form.
3. Show the DtN prefactor is exactly 1 after wave-function renormalization, or report the computed \(c_\star\).
4. Stop if \(c_\star\neq 1\). Do not reset W to 0.08 by hand.

Until that run exists, the honest sentence is: **\(W_\star=1/(4\pi)\) is the adopted matching / solid-angle value, not a completed action theorem.**

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
