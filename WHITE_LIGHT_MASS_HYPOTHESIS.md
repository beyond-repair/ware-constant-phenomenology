# Theoretical Foundations and Quantum Field Implications of the White-Light Mass Hypothesis

**Status:** RESEARCH companion note (claim level 1). Not a derivation of W_star. Not an experimental confirmation.
**Author:** William B. Ware — Atomic Dream Labs
**Date:** 2026-09-19
**Canonical repo:** https://github.com/beyond-repair/ware-constant-phenomenology
**Revision:** v0.2 (span-artifact removal, equation restoration, Tolman-sign correction, EH/trace double-count register, numeric bounds)

---

## Claim cap

| Item | Cap |
|------|-----|
| Classification | RESEARCH |
| Claim level | **1** (structured hypothesis + standard-QED estimates) |
| Experimental validation | **false** |
| Derives W_star ~ 0.08 | **false** |
| Laboratory dM/M detectable with current torsion / optomechanics | **unsupported** at the Euler-Heisenberg scale derived below |

---

## 1. Introduction and conceptual framework

Special relativity fixes the invariant mass M of an isolated system from total energy E and momentum P:

    E^2 = M^2 c^4 + P^2 c^2.

In the center-of-momentum frame P = 0 this is Einstein rest equivalence M = E/c^2. Any energy confined in that frame contributes to invariant mass.

The White-Light Mass Hypothesis asks whether spectral support, temporal peak structure, and quantum statistics of confined electromagnetic radiation can shift effective inertial or active gravitational mass at fixed E_tot and P = 0.

Define the comparison at equal total field-plus-wall energy and vanishing net momentum:

    dM_eff = M[config A] - M[config B]  at fixed E_tot, P = 0.

Typical pairs (A, B):
- polychromatic vs monochromatic
- thermal (g^(2)(0)=2) vs coherent (g^(2)(0)=1)
- phase-locked frequency comb (pulsed envelope) vs continuous-wave field of the same mean energy

The hypothesis is dM_eff != 0 at a level not already contained in linear Maxwell theory plus ordinary wall elasticity.

Two regimes must be kept separate:
1. Linear baseline. Isolated cavity radiation of energy E contributes M = E/c^2. Doubling E doubles that contribution, independent of spectrum, under Maxwell electrodynamics and von Laue closure.
2. Speculative correction. Nonlinear QED, the conformal anomaly, and (in this portfolio) a possible informational stress W T_info may introduce configuration dependence at fixed E_tot.

Four domains are required: relativistic boundary mechanics, Tolman active mass, Euler-Heisenberg QED, and field statistics.

---

## 2. Relativistic mechanics and von Laue theorem

The Maxwell stress-energy tensor in vacuum is symmetric, conserved, and traceless. Localized radiation cannot form a closed static system by itself: it needs boundaries or other binding stress.

Von Laue (1911): a closed system in static relativistic equilibrium satisfies integral_V T_ij d^3x = 0 in the rest frame. Only then do the integrated energy and momentum transform as a Lorentz four-vector.

The electromagnetic piece alone fails that test. Radiation-pressure T_ij^EM has a strictly positive spatial integral in a filled cavity. Walls must supply opposing tension so that integral T_ij^wall = - integral T_ij^EM.

The closed system then has a well-defined invariant mass M_total = (E_EM + E_wall)/c^2.

Linear Maxwell implication (A3): at fixed energy density the integrated radiation pressure does not depend on frequency partition. Polychromatic and monochromatic fields of equal E_EM produce equal wall counter-stress and equal invariant mass.

This bookkeeping is the same structure used in stress-tensor-modification and momentum-closure: a surface integral of T_ij is not a four-vector, and a leftover surface flux is not automatically thrust.

---

## 3. Active gravitational mass and the Tolman integral

Active gravitational mass in GR is the source in Einstein's equation. For a static localized isotropic fluid in the weak-field limit the relevant source density is rho + 3p/c^2.

SIGN CORRECTION relative to the draft: an unconfined photon gas has p = rho/3, hence rho + 3p/c^2 = 2 rho. It does NOT have vanishing active mass. The draft rho - 3p vanishing argument is rejected.

Standard cavity resolution:
- radiation contributes 2 E_EM / c^2 to the weak-field source
- wall tension p_wall = -p_rad contributes -E_EM / c^2
- wall rest energy contributes E_wall / c^2
- total: M_act = (E_EM + E_wall)/c^2

Unconfined propagating pulses are not static, so the Tolman integral does not apply to them. Their field is a null fluid plus multipoles, not zero active mass.

Tolman-Ehrenfest: T(x) sqrt(-g_00(x)) = constant. Planck spectral density therefore varies with gravitational potential. Volume-integrated active mass remains E_tot/c^2 in linear GR. Classical whiteness does not change total mass.

Portfolio cross-link: Schwarzschild-Ware g_00 = B(r) would imprint an additional logarithmic tilt. That is a Ware-metric prediction, not standard QED, and is not used as evidence here.

---

## 4. Nonlinear electrodynamics: Euler-Heisenberg

Low-energy QED generates an effective quartic via the electron loop. For E << E_c and hbar omega << m_e c^2 the Euler-Heisenberg Lagrangian contains

    (E^2 - c^2 B^2)^2 + 7 c^2 (E · B)^2

with Schwinger critical field E_c = m_e^2 c^3 / (e hbar) ~ 1.3e18 V/m.

Leading fractional correction for an electric-dominated configuration:

    Du/u ~ [alpha / (45 pi)] (E / E_c)^2 ~ 5.16e-5 (E / E_c)^2.

Worked values (white_light_qed_bounds.py):
- optical CW ~ 1e6 V/m  -> Du/u ~ 3e-29
- intense lab ~ 1e8 V/m -> Du/u ~ 3e-25
- TW-class ~ 1e11 V/m   -> Du/u ~ 3e-19
- PW-class ~ 1e12 V/m   -> Du/u ~ 3e-17

The draft phrase "~ 1e-32 (E/E_crit)^2" mixed a prefactor with a finished estimate and is replaced by the formula above.

Bandwidth is not automatically an enhancement. After time averaging, what survives is controlled by <I^2> and the field invariants, not by the label "white."

At fixed <I>:
- coherent CW: g2=1 baseline
- thermal / chaotic: g2=2, about 2x the quartic piece
- phase-locked comb that forms pulses: ~1/duty cycle; can exceed thermal
- broadband CW with random phases: not automatically larger than monochromatic CW

Rejected: more spectral channels => larger mass at fixed energy.
Surviving: larger <F^4> at fixed <F^2> => larger EH self-energy.
Whiteness is neither necessary nor sufficient. Peak structure and g^(2) are.

---

## 5. Trace anomaly and double-counting

Classically T^mu_mu = 0 for the Maxwell field. The QED trace anomaly is

    <T^mu_mu> = [beta(e)/(2e)] F_ab F^ab + ...

with beta(e) = e^3/(12 pi^2) + .... This is a real conformal-breaking effect.

It is NOT an independent mass channel stacked on Euler-Heisenberg. Both objects are one-loop QED. Adding EH self-energy and anomaly rest-mass density as two positive corrections double-counts the same electron loop.

Use EH as the effective energy functional at E << E_c, and treat the anomaly as the covariant language for why the effective tensor is no longer traceless. Do not sum them.

---

## 6. Field statistics

Coherent state: Poissonian, g^(2)(0)=1.
Thermal state: bunched, g^(2)(0)=2.
For an interaction proportional to I^2, <I^2> = g^(2)(0) <I>^2.
Thermal light supplies twice the quartic EH piece of a coherent field with the same mean intensity. That factor is standard quantum optics. It does not promote 1e-29 to a laboratory-easy number.

---

## 7. Comparison matrix (equal E_tot; linear mass identical)

| Metric | Mono coherent CW | Poly coherent (phase-locked) | Thermal white | Strong-field QED |
|--------|------------------|------------------------------|---------------|------------------|
| d omega | -> 0 | broad | broad | nonperturbative |
| g^(2)(0) | 1 | 1 (CW) or pulse-dependent | 2 | nonclassical |
| Classical M0 | E_tot/c^2 | E_tot/c^2 | E_tot/c^2 | same plus pairs |
| EH self-energy | baseline <F^4> | enhanced only if pulsing raises <F^4> | ~2x quartic vs coherent CW | EH breaks down |
| Anomaly | same loop as EH | same | same | same |
| Linear M_act | E_tot/c^2 (bounded) | same | same | plus pairs |
| dM/M from EH | ~[alpha/(45 pi)](E/E_c)^2 | duty-cycle times that | ~2x coherent CW | O(alpha/pi) and higher |

---

## 8. Experimental protocols — sensitivity honesty

Predicted EH dM/M at ordinary optical cavity fields is ~1e-29 to 1e-25. That is not a near-term detection.

Optomechanical cavity: dOmega/Omega = -1/2 dM/M. A 1e-29 shift is far below demonstrated thermometry. The architecture can still bound a beyond-EH contribution if reported as a limit.

Eotvos / torsion: dual cavities, mono vs thermal, equal E0. A 1e-15 eta measurement constrains non-EH spectral violations of inertial=passive mass. It does not reach the EH floor. Useful as a kill-gate on large anomalous dM_eff.

Atom interferometry: bright vs dark path measures the optical dipole potential plus any anomalous trace coupling. Standard dipole physics must be subtracted to machine precision before a vacuum-mass claim is allowed. No such subtraction is performed here.

---

## 9. Conclusions of the QED-only analysis

1. Linear SR/GR plus von Laue / Tolman wall cancellation: M = E_tot/c^2, spectrum-independent.
2. Nonlinear QED permits a configuration-dependent correction at fixed energy, controlled by <F^4> and g^(2), not by the word white.
3. The effect is real in the Standard Model and numerically negligible in laboratory CW cavities.
4. EH and the trace anomaly are one loop, not two additive mass sources.
5. Nothing in standard QED produces a coupling of size W_star ~ 0.08.

Portfolio mapping lives in WHITE_LIGHT_CFT_MAPPING.md (claim 1).

---

## References (minimum set)

- M. von Laue, Ann. Phys. 35 (1911) 524.
- R. C. Tolman, Phys. Rev. 35 (1930) 875.
- W. Heisenberg and H. Euler, Z. Phys. 98 (1936) 714.
- Trace-anomaly literature; Peskin and Schroeder for beta(e).
- R. Loudon, The Quantum Theory of Light — g^(2) conventions.

Portfolio: ware-constant-phenomenology, CFTv3.3-IQG-Unified-Framework, stress-tensor-modification, momentum-closure, coherence-drive.
