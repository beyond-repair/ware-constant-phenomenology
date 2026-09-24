# Audit addendum — Proof 6A regulated Hessian — 2026-09-23

Does not change W★. Does not unfreeze Stage 1. Does not derive 0.08, 0.23, or Z_ren.

Canonical files:
https://github.com/beyond-repair/-ware-constant-derivation/blob/main/PROOF_6A_REGULATED_HESSIAN.md
https://github.com/beyond-repair/-ware-constant-derivation/blob/main/verify_proof_6A_dimreg.py

## Locked here

- I2_bar^DR = -ω^{2}/(32π^{2}ε) + ω^{2}/(32π^{2})[γ_E-log(4π)-4/3+log(ω^{2})] + O(ε)
- Under Z_loop = -I2_bar/2: Z_loop^DR pole = +ω^{2}/(64π^{2}ε)
- Hard cutoff leading piece +Λ^{2}/(64π^{2}) in I2_bar, so Z_loop^cut < 0 at leading power
- Those signs differ. Unrenormalized Z_loop is regulator-dependent.
- δZ_W = -ω^{2}/(64π^{2}ε) + finite scheme term cancels the DR pole
- Finite Z_ren is not fixed by the determinant

Inventory IDs: D17 (DR pole of I2_bar), D18 (cutoff comparison / regulator dependence).

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
