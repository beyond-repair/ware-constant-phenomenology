# Derivation inventory — what is proved in this work

**Date:** 2026-09-23 (Proof 6A pass)  
**Rule:** a derivation is a closed implication from stated axioms or an action variation. A matching convention, a fit, or a target back-solve is not a proof.

Companions: [AUDIT_2026-09-23_PROOF5R.md](AUDIT_2026-09-23_PROOF5R.md), [AUDIT_2026-09-23_PROOF6A.md](AUDIT_2026-09-23_PROOF6A.md).

Master ledger: [beyond-repair/-ware-constant-derivation](https://github.com/beyond-repair/-ware-constant-derivation/blob/main/PROOF_AND_DERIVATION_LEDGER.md).

## A. Closed

| ID | Statement | Kind | Where |
|----|-----------|------|-------|
| D11–D15 | Constant-W action, source, concavity, W<1/6, K_sym form, exact Hessian | See prior inventory | action / 5R files |
| D16 | I2(k)>0 for stated kernel, d≥2 | Symbolic | verify_proofs_5R_7.py |
| D16q | Cutoff reading Z_loop^cut<0 at leading Λ^{2} | Asymptotic, regulator-specific | PROOF_6A |
| D17 | I2_bar^DR = -ω^{2}/(32π^{2}ε)+O(ε^0) at d=4-2ε | Dim-reg + script | verify_proof_6A_dimreg.py |
| D18 | Z_loop^DR pole = +ω^{2}/(64π^{2}ε) under Z=-I2_bar/2; δZ_W pole opposite | Convention + D17 | PROOF_6A_REGULATED_HESSIAN.md |

Older D1–D10 unchanged (W★ matching, Model A/B, gasket identities).

## B. Rejected / qualified

| ID | Claim | Disposition |
|----|-------|-------------|
| R4 | Z_loop<0 ⇒ W is a ghost | Rejected |
| R5 | I2(k)>0 ⇒ universal negative physical Z_ren | Rejected (6A). DR pole has the opposite sign from the cutoff power. |

## C. Open

Z_ren after a stated renormalization condition; full I(p); Lorentzian residue; S_W; W(x)→W(n); 0.08; 0.23.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
