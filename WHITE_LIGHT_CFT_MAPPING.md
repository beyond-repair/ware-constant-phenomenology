# White-Light Mass Hypothesis — Portfolio Fit and Findings

**Date:** 2026-09-19
**Status:** RESEARCH synthesis. Claim level 1.
**Inputs:** WHITE_LIGHT_MASS_HYPOTHESIS.md; locked Ware / CFT artifacts in this repo and siblings.
**Does not:** raise claim level, derive W_star, or certify thrust.

---

## 1. Where the note sits

```text
PIF / Quantules (CFT ontology, A4)
        |
        v
W_star T_info  -- modified EFE -- Schwarzschild-Ware metric
        |
        +-- galactic scoring          ware-constant-phenomenology (this repo)
        +-- consistency ledger        CFTv3.3-IQG-Unified-Framework
        +-- Maxwell surface integrals stress-tensor-modification
        +-- closed-box flux           momentum-closure
        +-- engineering index         coherence-drive (Stage 1 frozen)
                |
                v
        White-Light note  <- laboratory EM configuration at fixed E
```

The White-Light note is a laboratory-side probe design, not a new cosmological parameter. It asks whether two confined EM states with the same E_tot can differ in effective mass. The portfolio already asks a related question: whether an informational stress W T_info can make the Maxwell surface integral configuration-dependent.

Those are not the same claim. Conflating them is a registered failure mode.

| Claim | Content | Status |
|-------|---------|--------|
| L0 | Linear confined light has M=E/c^2 after von Laue walls | Standard physics (A3). Accepted. |
| L1 | EH / g^(2) give a tiny extra dM at fixed E | Standard QED (A3). Accepted as order-of-magnitude. |
| L2 | Ware injection into Maxwell T_ij yields net laboratory force | RESEARCH, claim <=2, experimental_validation=false. Unchanged. |
| L3 | Spectral statistics source a piece of T_info | New hypothesis (this document). Unverified. |
| L4 | EH explains W_star ~ 0.08 | Rejected. Magnitude mismatch. |

---

## 2. Symbol alignment (one definition each)

| Symbol | Active definition | Do not reuse as |
|--------|-------------------|-----------------|
| W_star | Phenomenological / galactic / muonic anchor ~ 0.08; preferred analytic candidate 1/(4 pi) | EH prefactor alpha/(45 pi) |
| W(n) | Engineering recursion 0.08 exp(0.23(n-1)) (provisional; conflicts with ghost-free bound W<0.125 at large n) | Spectral shape factor |
| T_info | Informational stress in the modified EFE | Euler-Heisenberg effective Maxwell tensor |
| S(rho) / SVC | Screened vacuum coherence / MDS screening | Optical g^(2) |
| E_c | Schwinger field ~ 1.3e18 V/m | Critical Ware field |

If L3 is ever promoted, use a new symbol (proposal: T_coh or C_mu nu[g^(2), <F^4>]) rather than overloading T_info.

---

## 3. Fit, domain by domain

### 3.1 Von Laue / walls <-> stress-tensor-modification + momentum-closure

Exact structural rhyme. Both say: integral T_ij over fields alone is not a four-vector; walls or complementary flux must cancel it; a leftover is either bookkeeping error or new physics.

Fit quality: strong (same theorem). New linear content: none.
Risk: treating a numerical mesh residual on the 0.45 Sierpinski surface as dM_eff. Forbidden without Class B dual-surface closure (already documented as not implemented).

### 3.2 Tolman M_act <-> modified EFE

CFT writes G_mu nu = 8 pi G (T_mu nu + W T_info). After the sign fix, radiation contributes rho+3p = 2 rho and walls cancel the extra rho.

If T_info were sourced by field statistics rather than baryonic density rho_b^alpha, then two cavities with identical E_tot and different g^(2) would have different active mass. That would be a laboratory WEP / torsion kill-gate on L3.

Current CFT sourcing is baryonic density + fractal boundary modes (Ware-Full-Action.tex), not optical g^(2). L3 is an extension, not a theorem of the existing action.

### 3.3 Euler-Heisenberg <-> |A|^4 saturation

Portfolio saturation lambda_A (A_mu A^mu)^2 is quartic in the Proca informational potential. EH is quartic in the Maxwell field. Same polynomial degree, different field.

Legitimate analogy: both break linear superposition and both can enhance under peaky fields.
Illegitimate identification: lambda_A <-> alpha/(45 pi E_c^2).

### 3.4 Trace anomaly <-> conformal breaking already present in CFT

CFT puts a traceful informational stress in by hand. QED generates a traceful Maxwell effective tensor from beta(e).

Finding (conceptual, Weak to Moderate): the anomaly is the Standard Model object that most closely resembles the job T_info is asked to do — break T^mu_mu = 0 without adding baryons.

Finding (numeric, Deterministic mismatch):

    alpha/(45 pi) ~ 5.16e-5
    alpha/pi      ~ 2.32e-3
    W_star        ~ 0.08
    1/(4 pi)      ~ 0.0796

W_star is ~35x larger than alpha/pi and ~1.5e3 larger than the EH electric prefactor, before (E/E_c)^2 suppression. You cannot promote the anomaly to W_star without a new amplification axiom (LDOS / fractal recursion / M2). That amplifier is the unvalidated engineering claim already capped in coherence-drive.

### 3.5 g^(2) <-> Screened Vacuum Coherence

SVC / MDS is written as a density-and-order screen. Optical physics already has a laboratory order parameter g^(2)(0):
- laser: ordered, g^(2)=1
- thermal white: bunched, g^(2)=2
- squeezed / antibunched: g^(2)<1

New finding (Hypothesis): g^(2) is the cleanest existing laboratory dial that could be identified with a slice of SVC without inventing new hardware. A null result (thermal vs coherent cavities, equal energy, no dM down to some eta) would bound that identification. It would not bound galactic W_star.

This is the only genuinely new experimental handle the White-Light note adds to the portfolio.

### 3.6 "Spectral" language <-> spectral_Wstar.py

That script computes Laplacian eigenvalue ratios on the 0.45 mesh. It is graph-spectral, not optical-spectral. Keep "optical spectrum d omega" and "mesh spectrum lambda_i" in different sentences. No ratio in that script equals a white-light mass shift.

---

## 4. Findings register

### Accepted (high precedence)

F1. Linear confined EM mass is spectrum-independent after walls.
F2. EH supplies a real, tiny, <F^4>-dependent correction.
F3. Thermal vs coherent multiplies the quartic piece by g^(2).
F4. EH + anomaly are one loop. Stacking them is invalid.
F5. EH cannot source W_star.

### New, claim-1 only

N1. Invariant restatement. Internal ledgers should treat this as configuration-dependent vacuum mass at fixed E, with control variables <F^4> and g^(2). "White light" is a slogan, not an invariant.
N2. SVC optical proxy. Identify or kill a slice of SVC with g^(2) using equal-energy thermal vs coherent cavities. New kill-gate, not a detection claim.
N3. Trace-anomaly as SM analog of T_info. Conceptual rhyme only. Requires an explicit map T_info contains c_an <T^mu_mu>_QED with a measured c_an. Default prior: c_an = 0 extra beyond EH.
N4. Pulse vs white. A phase-locked comb can beat thermal <F^4> via duty cycle. If any future lab claims a white-light mass excess, first check whether the source was pulsed.
N5. No portfolio parameter moves. Do not retune W_star, alpha=0.45, M2, or F/P targets from this note.

### Rejected

R1. Draft Tolman statement that unconfined radiation has zero active mass.
R2. Draft formula dM/M ~ 1e-32 (E/E_crit)^2 as a derived law.
R3. More modes => more mass at fixed energy.
R4. Additive EH + anomaly mass.
R5. Near-term optomechanics / torsion detection of standard EH dM. Bounds only.
R6. This note as a first-principles derivation of W_star (that job remains WSTAR_ENTROPIC_DERIVATION.md under axioms E1-E4, plus the incomplete Proca bridge).

---

## 5. What would count as a real new finding later

Promotion of N2 or N3 above claim 1 requires:
1. A Lagrangian term written in the same field variables as Ware-Full-Action.tex, with a new symbol, not a silent reuse of W.
2. A predicted dM/M or dOmega/Omega number from that term for a named cavity.
3. An experimental bound or detection at that number.
4. Compatibility report against ghost-free bound, solar-system eta, and Stage-1 coherence-drive freeze.

Until those exist, the White-Light note is a cleaned QED review plus a proposed kill-gate.

---

## 6. Open questions

Q1. Write C_mu nu[g^(2), <F^4>] explicitly and vary it.
Q2. Does Schwarzschild-Ware B(r) produce an observably different Tolman-Ehrenfest tilt than GR inside a laboratory-scale cavity? Expected: no. Confirm with numbers.
Q3. Can M2 / LDOS amplification be defined as a multiplier of EH without destroying the electron-loop interpretation?
Q4. Keep optical spectrum and mesh spectrum vocabularies segregated in CLAIM_STATUS and Nexus Layer 7.
