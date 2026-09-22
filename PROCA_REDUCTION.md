# Proca action reduction — what is derived, what is matched

**Date:** 2026-09-22  
**Does not set** \(c_\star=1\) **from the bulk. Does not unfreeze Stage 1.**

This note writes the reduction that `WSTAR_ACTION_DERIVATION.md` and
`BULK_PROCA_REDUCTION.md` sketch, with the missing steps named.

## 0. The action as written

`Ware-Full-Action.tex`:

$$
\mathcal{L}_{\rm Proca}
=
-\tfrac14 F_{\mu\nu}F^{\mu\nu}
+\tfrac{m^2}{2}A_\mu A^\mu
+\tfrac{W(n)}{2}(\bar\psi\gamma^\mu A_\mu\psi)\rho_b^\alpha
+\lambda(\partial_\mu A^\mu)^2
-\tfrac{\lambda_A}{4}(A_\mu A^\mu)^2.
$$

Einstein side (`Schwarzschild-Ware-metric.tex`):

$$
G_{\mu\nu}=8\pi G\bigl(T_{\mu\nu}+W\,T_{\mu\nu}^{\rm info}\bigr).
$$

Registered problems before any reduction:

1. \(W\) appears **inside** \(\mathcal{L}\) and **again** as a multiplier of \(T^{\rm info}\).
   Those are different roles. A clean reduction uses one of them.
2. \(W(n)\) in \(\mathcal{L}\) is the deprecated indexing in that TeX file.
   Option A: gravitational \(W\) is the constant \(W_\star\).
3. Mass-term sign depends on metric signature. The written
   \(+m^2 A_\mu A^\mu/2\) is not audited here as ghost-free.
4. \(T^{\rm info}\) is not obtained in-tree by
   \(T_{\mu\nu}=-(2/\sqrt{-g})\delta(\sqrt{-g}\mathcal{L}_{\rm int})/\delta g^{\mu\nu}\).

Everything below is the *screen reduction of a radial condensate*, not a
completed Einstein–Proca solution.

## 1. Monopole on a ball (executed structure)

Take a spatial ball \(B_R\) with \(\partial B\cong S^2\). Quasi-static radial
condensate \(\varphi=A_r|_{\partial B}\) (or a scalar proxy for the monopole).
Integrating out the bulk at tree level produces a Dirichlet-to-Neumann
operator \(\mathcal{K}\) on the sphere:

$$
S_\partial[\varphi]
=
\frac{1}{2g^2}\int_{\partial B}\varphi\,\mathcal{K}\,\varphi
-\int_{\partial B} J_{\rm info}\,\varphi.
$$

For a free massive Helmholtz field \((\Delta-m^2)u=0\) the regular monopole is
\(u(r)\propto \sinh(mr)/r\). The continuum DtN eigenvalue on radius \(R\) is

$$
\kappa(m,R)
=
\frac{u'(R)}{u(R)}
= m\coth(mR)-\frac{1}{R}.
$$

This is what `bulk_boundary_reduction.py` prints as `kappa_cont`.
Limits:

- \(mR\to 0\): \(\kappa\to 0\) (massless monopole in 3D has vanishing radial
  Neumann data at this order after the Coulomb piece is removed — the script
  reports 0).
- \(mR\to\infty\): \(\kappa\to m\).

\(\kappa\) is a **scale**. It is not \(1/(4\pi)\).

## 2. Where \(1/(4\pi)\) actually appears

Expand the boundary field in spherical harmonics:

$$
Y_{00}=\frac{1}{\sqrt{4\pi}},\qquad
\varphi=\bar\varphi\,Y_{00}=\frac{\bar\varphi}{\sqrt{4\pi}}.
$$

Then \(\int_{S^2}Y_{00}^2\,d\Omega=1\), so the monopole kinetic term is

$$
S_{00}
=
\frac{R^2\kappa}{2g^2}\,\bar\varphi^2
-\frac{R^2}{\sqrt{4\pi}}\bar J\,\bar\varphi
$$

(up to the convention that \(J\) is an areal density).

If the Einstein-side coupling is **defined** to be the coefficient that
multiplies a unit-normalized monopole source after this rescaling, one may
write

$$
W_{\rm eff}=\frac{c_\star}{4\pi},
$$

where \(c_\star\) absorbs \(R^2\kappa/g^2\) and wave-function renormalization.

**Canonical matching** is the extra sentence \(c_\star=1\). That sentence is
not implied by \(\kappa(m,R)\). It sets the leftover factor to 1 by hand.

Proven (pure monopole, angular integrals only):

$$
\int_{S^2} Y_{00}^2\,d\Omega=1,
\qquad
\int_{S^2} Y_{00}^4\,d\Omega=\frac{1}{4\pi}.
$$

The second line is the \(|A|^4\) angular factor in `BULK_PROCA_REDUCTION.md`.
It multiplies \(\lambda_A\). It does not fix \(W_\star\).

## 3. What the Einstein equation then is *not*

A completed reduction would produce \(T_{\mu\nu}^{\rm info}[A]\) and solve

$$
G_{\mu\nu}=8\pi G\bigl(T_{\mu\nu}^{\rm bar}+T_{\mu\nu}^{\rm Proca}[A]\bigr)
$$

with no free prefactor \(W\), or with \(W\) identified as a specific
combination of \(g,\kappa,Y_{00}\). That identification is D2 in the
inventory: convention.

The written Schwarzschild–Ware potentials

$$
B(r)=1-\frac{2GM_b}{rc^2}+\frac{2W GM_b}{r_0 c^2}\ln\frac{r}{\lambda},
\qquad A=B^{-1}
$$

are an **ansatz**. They are not the standard static Proca star (Yukawa).
Circular-orbit algebra from this ansatz is closed:

$$
v_c^2\approx \frac{r c^2}{2}\partial_r B
=
\frac{GM_b}{r}+\frac{W GM_b}{r_0},
$$

which is the `Math.md` / `Schwarzschild-Ware-metric.tex` acceleration
\(GM/r^2+W GM/(r_0 r)\). The Yukawa-like law in `Ware-Full-Action.tex`

$$
a=-\frac{GM}{r^2}\Bigl[1-W\Bigl(\frac{r_0}{r}\Bigr)^{1-2\alpha}e^{-r/r_0}\Bigr]
$$

is a **different** reduction and is not implied by the log metric.

## 4. What would close \(c_\star\)

Minimum calculation, no new symbols:

1. Choose signature and drop either the in-Lagrangian \(W(n)\) or the
   Einstein-side \(W\) so the coupling is not double-counted.
2. Linearize the radial Proca equation with the written mass and, if kept,
   the \(\rho_b^\alpha\) source (non-minimal shift of \(\kappa\)).
3. Compute \(\kappa(m,R;\rho_b)\) and the boundary kinetic coefficient
   \(Z=R^2\kappa/g^2\).
4. Define \(\bar\varphi\) so the kinetic term is \(\tfrac12(\partial\bar\varphi)^2\)
   or \(\tfrac12\bar\varphi^2\). Read \(c_\star=4\pi W_{\rm eff}\) from that
   normalization against the Einstein prefactor.
5. Publish \(c_\star\). If it is not 1, \(W_\star\neq 1/(4\pi)\) at tree level.

`bulk_boundary_reduction.py` does step 2 only for a free scalar monopole
and then prints the convention. That is not step 4.

## 5. Status words

| Piece | Status |
|-------|--------|
| \(Y_{00}\) angular factor \(1/(4\pi)\) | Derived |
| \(\int Y_{00}^4=1/(4\pi)\) | Derived |
| DtN \(\kappa=m\coth(mR)-1/R\) | Derived (free massive monopole) |
| \(c_\star=1\) | Convention |
| Log metric from Proca \(T_{\mu\nu}\) | Not derived |
| Unique weak-field law | Conflict (log vs Yukawa-shaped) |
| Non-minimal \(\rho_b^\alpha\) shift of \(c_\star\) | Open |

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
