# Derivation inventory — what is proved in this work

**Date:** 2026-09-23 (Proof 5R pass)  
**Rule:** a derivation is a closed implication from stated axioms or an action variation. A matching convention, a fit, or a target back-solve is not a proof.

Companions: [AUDIT_2026-09-22.md](AUDIT_2026-09-22.md), [AUDIT_2026-09-23.md](AUDIT_2026-09-23.md), [AUDIT_2026-09-23_PROOF5R.md](AUDIT_2026-09-23_PROOF5R.md), [CONSTANT_W_ACTION_PRINCIPLE.md](CONSTANT_W_ACTION_PRINCIPLE.md).

Master local-W ledger: [beyond-repair/-ware-constant-derivation](https://github.com/beyond-repair/-ware-constant-derivation/blob/main/PROOF_AND_DERIVATION_LEDGER.md).

## A. Closed in-tree (keep)

| ID | Statement | Kind | Where |
|----|-----------|------|-------|
| D1 | E1–E4 ⇒ W★=1/(4π) | Conditional on four Model axioms | `WSTAR_ENTROPIC_DERIVATION.md` |
| D2 | Canonical monopole matching c★=1 ⇒ W_eff=1/(4π) | Matching convention, not bulk theorem | `WSTAR_ACTION_DERIVATION.md` |
| D3 | Option A: gravitational formulae use constant W★; M2 geometric only | Policy lock | `W3_RESOLUTION_NOTE.md` |
| D4 | Model A ratios 0.795:1:1.259 from W(n) alone | Algebra | m2 + freeze |
| D5 | Model B ratios 0.589:1:1.699 from W(n)(3α)^n | Algebra | m2 |
| D6 | Hybrid 0.795:1:1.993 is not D4 or D5 | Falsification | Sweep-137 |
| D7 | Gasket harmonic energy 3/5 | Deterministic | sierpinski |
| D8 | Two-corner R_n/R_{n-1}=5/3 | Deterministic | sierpinski |
| D9 | λ_max=6; Dirichlet λ_min → 1/5 | Deterministic | sierpinski SPECTRUM |
| D10 | Small-shear F∝γ | First-order identity | sierpinski |
| D11 | Constant-W Γ_E=S_W+(1/2)Tr ln(ω^{2}I-WL) ⇒ δS_W/δW=(1/2)Tr[K^{-1}L] | Action variation | CONSTANT_W_ACTION_PRINCIPLE.md |
| D12 | V''_1-loop<0 on K≻0 | Deterministic | same |
| D13 | Finite graph λ_max=6, ω=1 ⇒ W<1/6 | Operator positivity + D9 | same |
| D14 | K_sym[W0]=ω^{2}I-W0 H0; finite-graph K_sym Hermitian; continuum form Q_W | Operator identity | -ware-constant-derivation/PROOF_5R_KSYM.md |
| D15 | δ^{2}Γ_loop=-(1/2)Tr(G δV G δV) for linear V | Exact variation | PROOF_AND_DERIVATION_LEDGER.md |
| D16 | I2(k)>0 for stated A(k,p) kernel, d≥2 ⇒ unrenormalized Z_loop<0 | Symbolic + script | verify_proofs_5R_7.py |

D11–D16 do **not** derive 0.08, ξ=0.23, Z_ren, or a healthy Lorentzian W(x).

## B. Rejected in the 5R pass

| ID | Claim | Disposition |
|----|-------|-------------|
| R1 | Silent swap K=ω^{2}I-(1-W)H0 | Different model. Removed. |
| R2 | Kato-Rellich for the whole Jordan insertion | Insertion is second-order. Rejected. |
| R3 | W≥1 or ∇^{2}W>2ω^{2} ⇒ K_sym≻0 | Not a theorem. Removed. |
| R4 | Z_loop<0 ⇒ W is a ghost | Needs Z_ren and Lorentzian residue. |

## C. Still not closed

U1–U8 unchanged from AUDIT_2026-09-22. Additional:

| ID | Gap |
|----|-----|
| U9 | Z_ren after regulator + counterterms |
| U10 | Lorentzian pole/residue/stability |
| U11 | Independent S_W |
| U12 | Coarse-graining W(x)→W(n) |
| U13 | Sign-changing continuum positivity domain |

## D. Honest sentences

- W★=1/(4π) is adopted matching / solid-angle, not a completed Proca-action theorem.
- Constant-W spectral source is derived. A propagating W(x) is not.
- Unrenormalized Z_loop<0 is a model-specific Euclidean result for K_sym, not a physical ghost theorem.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
