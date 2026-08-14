# Entropic / Solid-Angle Derivation of W_★ = 1/(4π)

**Date:** 2026-08-14  
**Status:** Derivation under explicit axioms (Route A). Not a theorem of the full Proca+Einstein action without those axioms.  
**Numerical value:** \(1/(4\pi) \approx 0.079577\) (matches the locked phenomenological anchor \(W_\star \approx 0.08\) to 0.5%).

---

## 1. Axioms (Registered)

| ID | Statement | Class |
|----|-----------|-------|
| E1 | The Primordial Informational Field (PIF) is defined on spatial slices with a preferred null/holographic screen that is topologically a 2-sphere | Model |
| E2 | The dimensionless gravitational–informational coupling is the ratio of the measure of directed informational flux through the screen to the full solid angle of the screen | Model |
| E3 | In the absence of preferred direction, the prior over flux directions is uniform on the sphere | Model |
| E4 | The coupling that multiplies \(T_{\mu\nu}^{\rm info}\) in the modified Einstein equation is identified with that measure ratio | Model |

These are **assumptions**, not theorems. The derivation below is conditional on E1–E4.

---

## 2. Solid-Angle Normalization

The total solid angle of a topological 2-sphere is
\[
\Omega_2 = \int_{S^2} d\Omega = 4\pi.
\]

Under E3 the uniform directional prior has density
\[
p(\hat{n}) = \frac{1}{4\pi}.
\]

Under E2 the dimensionless coupling is the weight assigned to a single directed channel relative to the full screen:
\[
W_\star \;=\; p(\hat{n}) \;=\; \frac{1}{4\pi}.
\]

**Numerical evaluation:**
\[
W_\star = \frac{1}{4\pi} \approx 0.07957747154.
\]

Agreement with the phenomenological lock \(W_\star \approx 0.08\):
\[
\left|\frac{1/(4\pi) - 0.08}{0.08}\right| \approx 0.53\%.
\]

---

## 3. Microcanonical / Path-Integral Sketch

Consider a microcanonical ensemble of PIF configurations on a spatial ball bounded by screen \(\partial B = S^2\), with fixed informational charge \(Q_{\rm info}\).

The density of states in the high-occupancy limit is dominated by the area measure of the screen. The saddle-point free energy per unit charge contains a factor
\[
\frac{1}{\Omega_2} = \frac{1}{4\pi}
\]
from the normalization of the spherical measure in the path integral
\[
\mathcal{Z} = \int \mathcal{D}A_\mu \; e^{-S[A]} \,,\qquad
\int_{S^2} d\Omega \, p(\hat{n}) = 1.
\]

Identifying the coefficient of the informational stress-energy in the effective Einstein equation with this saddle-point weight (axiom E4) again yields
\[
W_\star = \frac{1}{4\pi}.
\]

A fully controlled derivation from the Proca Lagrangian would require showing that the one-loop or saddle-point effective action produces exactly this normalization factor and no additional numerical coefficient. That step is **not** completed here; it is the remaining bridge between the solid-angle argument and the field action.

---

## 4. Relation to α = 0.45

The density exponent \(\alpha = 0.45\) is independent of the solid-angle argument. The solid-angle derivation does **not** currently fix \(\alpha\).

---

## 5. What This Does and Does Not Establish

**Establishes (conditional on E1–E4):**
- A first-principles origin for the number \(0.0796\ldots\) as a solid-angle normalization.
- Consistency with the locked phenomenological value at the 0.5% level.

**Does not establish:**
- That E1–E4 are theorems of the existing Proca + Einstein action.
- A derivation of \(\alpha = 0.45\).
- Uniqueness (other normalizations are possible under different screen topology or flux-counting conventions).

---

## 6. Adoption Policy

Preferred first-principles candidate:
\[
W_\star = \frac{1}{4\pi} \approx 0.079577.
\]
The rounded lock \(W_\star = 0.08\) remains acceptable for galactic phenomenology (difference \(<1\%\)).

---

*End of working note.*
