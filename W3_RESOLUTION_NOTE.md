# Working Note: Resolving the W(3) / Stability-Bound Tension

**Date:** 2026-08-14  
**Status:** Option A formally locked

---

## 1. Statement of the Conflict (Historical)

Two statements coexisted in the repository cluster:

1. Phenomenological / galactic / muonic formulae used the locked anchor \(W_\star\approx0.08\).
2. The M2 engineering table used \(W(n)=0.08\,e^{0.23(n-1)}\) giving \(W(3)\approx0.1267\), \(W(4)\approx0.1595\).
3. An earlier stability argument asserted a ghost-free bound \(W(n)<0.125\).

Statements 2 and 3 were mutually inconsistent.

---

## 2. Decision: Option A Locked

**Adopted policy (2026-08-14):**

- All gravitational, spectroscopic and lensing formulae use the constant \(W_\star=0.08\).
- The M2 exponential is re-interpreted as a **relative geometric / LDOS enhancement factor** \(f(n)\). It multiplies only engineering surface integrals, never the Einstein-equation coupling.
- The ghost-free bound is automatically satisfied in the gravitational sector.

Code consequence:
- `physics_evaluator.py` defaults to `model="star"`.
- `killgate_verification.py` never inserts M2 into any formula.
- Engineering force ratios become \(\Delta F(n)\propto W_\star\cdot f(n)\cdot\text{(geometric integral)}\) with \(f(3)=1\) by definition.

---

## 3. Rejected / Deferred Alternatives

- **Option B** (raise the 0.125 bound) — deferred until a new dispersion calculation exists.
- **Option C** (re-fit the exponent) — deferred until a first-principles spectral derivation of \(\xi\) is available.

---

## 4. Lensing Saturation (Companion Fix)

The historically written amplification formula produced factors \(\gg1\) at cosmological distances. A phenomenological saturation

\[
\delta_{\rm eff}=\frac{\delta_{\rm raw}}{1+\delta_{\rm raw}/\delta_{\rm sat}},\qquad\delta_{\rm sat}=1.2
\]

now recovers the target factor ~2.2. The parameter \(\delta_{\rm sat}\) is explicit and not yet derived from the Schwarzschild-Ware metric.

---

*End of working note.*
