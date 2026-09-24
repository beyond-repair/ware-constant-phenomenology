# Derivation inventory — what is proved in this work

**Date:** 2026-09-23 (Proof 6B pass)  
**Rule:** a derivation is a closed implication from stated axioms or an action variation. A matching convention, a fit, or a target back-solve is not a proof.

Companions: [AUDIT_2026-09-23_PROOF5R.md](AUDIT_2026-09-23_PROOF5R.md), [AUDIT_2026-09-23_PROOF6A.md](AUDIT_2026-09-23_PROOF6A.md), [AUDIT_2026-09-23_PROOF6B.md](AUDIT_2026-09-23_PROOF6B.md).

Master ledger: https://github.com/beyond-repair/-ware-constant-derivation/blob/main/PROOF_AND_DERIVATION_LEDGER.md

## A. Closed (action / local-W track)

| ID | Statement | Where |
|----|-----------|-------|
| D11–D15 | Constant-W action, source, concavity, W<1/6, K_sym form, exact Hessian | 5R / action freeze |
| D16 | I2(k)>0 for stated kernel, d≥2 | verify_proofs_5R_7.py |
| D17 | I2_bar^DR pole -ω^{2}/(32π^{2}ε) | 6A |
| D18 | Z_loop^DR pole +ω^{2}/(64π^{2}ε) under Z=-I2_bar/2 | 6A |
| D19 | I(p)=A0+A1 p^{2}+A2 p^{4}+O(p^6); A0 pole 3ω^{4}/(16π^{2}ε); A1=D17; A2 pole integrates to 0, finite 1/(960π^{2}) | PROOF_6B_UV_LEDGER.md |
| D20 | MSbar + Z_W bare=0 leaves Z=ω^{2}/(64π^{2})[4/3-log(ω^{2}/μ^{2})]; this is a scheme remainder. MOM dGamma/dp^{2}|_μ^{2}=1 is a definition | same |

D1–D10 unchanged (W★ matching, Model A/B, gasket).

## B. Rejected

R4: Z_loop<0 ⇒ ghost. R5: I2>0 ⇒ universal negative Z_ren. R6: MSbar remainder is a derived physical coupling or equals 0.08.

## C. Open

Unique physical Z_ren; S_W; Lorentzian residue (6C not opened); W(x)→W(n); 0.08; 0.23; thrust.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
