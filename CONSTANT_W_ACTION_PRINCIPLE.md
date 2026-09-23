# Constant-W Action Principle — Canonical Lock

**Date:** 2026-09-23  
**Claim level:** ≤ 2  
Canonical copy: https://github.com/beyond-repair/-ware-constant-derivation/blob/main/CONSTANT_W_ACTION_PRINCIPLE.md

Does **not** derive \(W=0.08\), \(W_\star=1/(4\pi)\), \(\xi=0.23\), or a healthy local field \(W(x)\).

## Assumptions

| ID | Class | Statement |
|----|-------|-----------|
| A1 | User | Real scalar with quadratic Euclidean action \(\tfrac12\phi\cdot K[W]\phi\). |
| A2 | Model | \(K(W)=\omega^2 I-WL\), \(L=L^\dagger\succeq 0\), constant \(W\). |
| A3 | Model | Domain \(K(W)\succ 0\). |
| A4 | User | \(S_W\) depends on \(W\) only; not derived here. |

## Derived identities

\[
S_E[\phi;W]=\tfrac12\phi^{\mathsf T}K(W)\phi+S_W[W],\qquad K(W)=\omega^2 I-WL.
\]

\[
\boxed{\Gamma_E[W]=S_W[W]+\tfrac12\operatorname{Tr}\ln K(W)+\mathrm{const}}
\]

\[
\boxed{\frac{\delta S_W}{\delta W}=\tfrac12\operatorname{Tr}[(\omega^2 I-WL)^{-1}L]=\tfrac12\sum_k\frac{\lambda_k}{\omega^2-W\lambda_k}}
\]

\[
\boxed{V''_{\mathrm{1-loop}}(W)=-\tfrac12\sum_k\frac{\lambda_k^2}{(\omega^2-W\lambda_k)^2}<0}
\]

Pole: \(W\to(\omega^2/\lambda_{\max})^-\implies V_{\mathrm{1-loop}}\to-\infty\).

Finite normalized gasket (\(\lambda_{\max}=6\), \(\omega=1\)):

\[
\boxed{0\le W<1/6}
\]

Continuum unbounded spectrum: no \(W>0\) keeps \(K\) globally positive without a UV cutoff. \(1/6\) is not a continuum theorem.

## Local \(W(x)\) — open

Hermitian ordering required, e.g. \(K_{\mathrm{sym}}=\omega^2 I-\tfrac12(WL+LW)\).

\[
\Gamma^{(2)}(p)=M_{\mathrm{eff}}^2+Z_{\mathrm{eff}}p^2+O(p^4)
\]

is not computed here. Unrenormalized \(Z_{\mathrm{induced}}<0\) for \(K_{\mathrm{sym}}\) is model-specific. Healthy Lorentzian propagation is not automatic.

## Ledger

| Component | Status |
|---|---|
| Constant-\(W\) action principle | DERIVED |
| 1-loop concavity | DERIVED |
| Finite-graph bound \(W<1/6\) | DERIVED |
| Local \(W(x)\), \(Z_{\mathrm{ren}}\), \(W(n)\) | OPEN |
| Parameters 0.08 and 0.23 | NOT DERIVED |

Check: `verify_constant_W_action.py`

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
