---
# Mathematical & Numerical Framework: Ware Constant Phenomenology (v0.3.5)

**Last update:** 2026-08-14  
**W-resolution status:** Option A locked  
**SPARC status:** Macro \(r_0(M_b)\) verified; local curve residuals open

### Purpose

Phenomenological evidence ledger. \(W_\star\approx0.08\) is the empirical gravitational anchor under Option A.

---

## 1. Core Invariant (Option A Locked)

\[
W_\star \approx 0.08
\]

M2 exponential is geometric / LDOS enhancement only.

---

## 2. Macro Scaling (Verified)

\[
r_0(M_b) = 0.45\,\mathrm{kpc}\,(M_b/10^{11}M_\odot)^{0.40}
\]

SPARC-derived coherence scales track this relation across ~3 dex in baryonic mass (see ontological-fit figure and SPARC_CHI2_REPORT.md).

---

## 3. Lensing Saturation

\(\delta_\mathrm{sat}\) mapped to \(\xi=\lambda_A\langle A^2\rangle/W\).  
Soft saturation required (hard cutoff kills deflection for \(b>r_\mathrm{sat}\)).  
Thin-lens geometric_prefactor at \(b\sim r_0\) ≈ 0.16 (see geodesic_lensing_prefactor.py).

---

## 4. Local Rotation-Curve Residuals

Median \(\chi^2_\mathrm{red}\sim 35\)–\(40\) under simple global-W models.  
This is a local profile problem, not a rejection of the macro trend.

---

## 5. Consistency Ledger

| Component | Status |
|-----------|--------|
| \(W_\star\) lock | Locked (Option A) |
| Macro \(r_0(M_b)\) | **Verified** |
| Local SPARC χ² | Open (elevated residuals) |
| Lensing δ_sat | Mapped to ξ; soft saturation; prefactor ~0.16 |
| First-principles \(W_\star\) | Open (see WSTAR_FIRST_PRINCIPLES_NOTE.md) |
| EM BVP | Electrostatic + magnetostatic + quasi-static RF BEM |

---

## 6. Priority Open Problems

1. Local acceleration-profile tuning without breaking macro \(r_0(M_b)\).
2. Full multi-plane lensing ray-trace.
3. Spectral derivation of \(W_\star\) (Routes A–E in working note).
4. Full-wave RF on the Sierpinski surface.

---

### Cross References

SPARC_CHI2_REPORT.md · geodesic_lensing_prefactor.py · derive_delta_sat.py · WSTAR_FIRST_PRINCIPLES_NOTE.md · killgate_verification.py
