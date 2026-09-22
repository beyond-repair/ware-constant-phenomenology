# Calculation of \(c_\star\) — 2026-09-22

**Result:** \(c_\star\) is not fixed by the written Proca action.  
\(W_\star=1/(4\pi)\) remains a normalization convention. Freeze untouched.

## 1. Single-coupling setup (no double \(W\))

Drop \(W(n)\) from \(\mathcal{L}\). Keep Einstein

$$
G_{\mu\nu}=8\pi G\bigl(T_{\mu\nu}^{\rm bar}+T_{\mu\nu}^{\rm Proca}\bigr)
$$

or, if a dimensionless prefactor is restored by hand,

$$
G_{\mu\nu}=8\pi G\bigl(T_{\mu\nu}^{\rm bar}+W_{\rm eff}T_{\mu\nu}^{(\phi)}\bigr).
$$

The second line is allowed only if \(T^{(\phi)}\) is a unit-normalized monopole bilinear, not the raw Proca tensor. That is the matching step.

## 2. Boundary quadratic form (derived)

Free massive monopole DtN: \(\kappa=m\coth(mR)-1/R\).

$$
S_\partial
=
\frac{R^2\kappa}{2g^2}\int_{S^2}\varphi^2\,d\Omega
-\ R^2\int_{S^2} J\,\varphi\,d\Omega.
$$

Two normalizations of the same monopole:

| Convention | Field | \(\int\varphi^2\,d\Omega\) | Source integral for isotropic \(J_0\) |
|------------|-------|---------------------------|--------------------------------------|
| L² unit (A) | \(\varphi=\bar\varphi\,Y_{00}\), \(Y_{00}=1/\sqrt{4\pi}\) | \(\bar\varphi^2\) | \(J_0\bar\varphi R^2\sqrt{4\pi}\) wait: \(\int Y_{00}d\Omega=\sqrt{4\pi}\) |
| Raw (B) | \(\varphi=\tilde\varphi\) constant on \(S^2\) | \(4\pi\tilde\varphi^2\) | \(4\pi J_0\tilde\varphi R^2\) |

A and B differ by \(\tilde\varphi=\bar\varphi/\sqrt{4\pi}\). Completing the square,

$$
S_*
=
-\frac{R^2 g^2}{2\kappa}(4\pi)J_0^2
\qquad\text{(convention B)}
$$

and the same number in convention A after the \(Y_{00}\) Jacobian.
The solid angle enters as \(4\pi\) in the *source-squared* term, or as \(1/(4\pi)\) if one instead calls the coupling the weight of a single directed channel (axioms E2–E3).

## 3. Identification

The notes write \(W_{\rm eff}=c_\star/(4\pi)\) and set \(c_\star=1\).

Unpacking:

$$
c_\star
=
4\pi W_{\rm eff}
=
4\pi\cdot\frac{\text{(Einstein prefactor used on }T^{(\phi)})}{\text{(normalization of }T^{(\phi)})}.
$$

Objects **not** present in the repo, and required to compute a number:

- a value of \(g\)
- a preferred screen radius \(R\)
- a map \(T^{(\phi)}\leftrightarrow\) Proca \(T_{\mu\nu}\)
- the non-minimal \(\rho_b^\alpha\) shift of \(\kappa\)

\(\kappa(m,R)\) is known and is **not** dimensionless. It cannot equal \(1/(4\pi)\).

## 4. What is therefore proved

1. \(1/(4\pi)\) appears if and only if one uses L²-normalized \(Y_{00}\) *or* the uniform directional prior on \(S^2\).
2. The opposite factor \(4\pi\) appears in the raw-\(d\Omega\) completion-of-square.
3. Neither factor is selected by \(m\), \(\lambda_A\), or the gasket spectrum.
4. `delta_sat_from_A4.py` sets \(\xi_{\rm cap}=\delta_{\rm sat}/W=1.2\times 4\pi\approx 15.08\). That is a rewrite of the target \(1.2\), not a bulk output.
5. `spectral_Wstar.py` already reports mesh ratios \(\neq 0.08\).

**Theorem (underdetermination).**  
On the written action plus the executed DtN, \(c_\star\) is a free matching parameter. Adopting \(c_\star=1\) is equivalent to *defining* \(W_\star=1/(4\pi)\). It is not a solution of the field equations.

## 5. Status

| Quantity | Status |
|----------|--------|
| \(\kappa(m,R)\) | Derived |
| \(Y_{00}\) algebra | Derived |
| \(c_\star=1\) | Definition |
| Bulk non-minimal correction | Open, and not needed to see underdetermination |

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
