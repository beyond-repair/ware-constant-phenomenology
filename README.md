# Ware Constant Phenomenology (CFT v4.0)

**Phenomenological evidence ledger for the Ware Constant as a universal dimensionless coupling across subatomic, galactic, cosmological, and vacuum-engineering regimes.**

**Status (2026-08-14):** Consistency repair applied. This repository remains the canonical source for mathematics, kill-gates, and the Symbol Registry of the broader framework.

---

## Core Invariant

\[
W_\star \approx 0.08
\]

- **Role:** Primary empirical / phenomenological anchor.
- **Status:** Locked for all galactic, muonic, and lensing formulae in this repository.
- **Derivation status:** Open. First-principles derivation is the responsibility of the derivation repository; this ledger treats \(W_\star\) as an empirical invariant whose recurrence across scales is the phenomenon under study.

---

## Theoretical Foundation

Screened modification of general relativity via a Proca informational vector field. Effective stress-energy:

\[
T_{\mu\nu}^{\rm eff} = T_{\mu\nu} + W\, T_{\mu\nu}^{\rm info}
\]

where the informational contribution arises from non-minimal fermionic coupling and fractal vacuum-expectation-value (VEV) sourcing. Screening function \(S(\rho)\) suppresses the effect in high-density / high-entropy regions and activates it in virialized systems.

Associated geometric transducer for the engineering sector: 0.45-scaled asymmetric Sierpinski LDOS structure.

---

## Kill-Gates (Current Best Statement)

| Sector | Claim | Notes |
|--------|-------|-------|
| Subatomic | Muonic proton-radius shift via informational screening | Uses \(W_\star\) |
| Galactic | SPARC/BTFR flat rotation curves from \(a_{\rm info}\) | \(r_0 \propto M_b^{0.40}\), \(\alpha=0.45\) lock |
| Cluster lensing | ~2.2× baryonic amplification (LRG 3-757) | |A|^4 saturation |
| Solar System | PPN parameter \(\eta \approx 4.8 \times 10^{-11}\) | Screening protects local tests |
| Engineering | Target \(F/P = 3 \times 10^{-8}\) N/W | See Coherence Drive family |

---

## M2 Renormalization (Provisional)

\[
W(n) = W_\star \, e^{0.23(n-1)}
\]

**Important:** The tabulated values that appear in the engineering sub-repositories (W(3) ≈ 0.1267, W(4) ≈ 0.159) exceed the previously stated ghost-free bound \(W < 0.125\). Until this tension is resolved, the M2 law is classified as a **phenomenological scaling ansatz**, not a completed renormalization-group result. All stability claims that assume the bound must be revisited.

---

## Repository Contents

- `Math.md` — Consolidated constants, internal consistency ledger, open problems
- `PROVISIONAL_DERIVATIONS.tex` — Proca action, stability analysis, r_0 derivation
- `Ware-Full-Action.tex` — Unified action and metric
- `Schwarzschild-Ware-metric.tex` — Geodesics, lensing, saturation
- `ware-constant-phenomenology.md` — Observational summary

---

## Cross-Repository Map

| Component | Repository |
|-----------|------------|
| Synthesis & ontology (PIF / Quantules) | [CFTv3.3-IQG-Unified-Framework](https://github.com/beyond-repair/CFTv3.3-IQG-Unified-Framework) |
| Derivation attempt | [-ware-constant-derivation](https://github.com/beyond-repair/-ware-constant-derivation) |
| M2 law | [m2-renormalization-law](https://github.com/beyond-repair/m2-renormalization-law) |
| Stress-tensor evaluator fragment | [stress-tensor-modification](https://github.com/beyond-repair/stress-tensor-modification) |
| Momentum closure | [momentum-closure](https://github.com/beyond-repair/momentum-closure) |
| Topological pinch | [topological-pinch](https://github.com/beyond-repair/topological-pinch) |
| Geometry | [sierpinski-geometry-045](https://github.com/beyond-repair/sierpinski-geometry-045) |
| Integration pointer | [coherence-drive](https://github.com/beyond-repair/coherence-drive) |

---

## Quick Start

```bash
git clone https://github.com/beyond-repair/ware-constant-phenomenology.git
cd ware-constant-phenomenology
pdflatex PROVISIONAL_DERIVATIONS.tex
pdflatex Ware-Full-Action.tex
pdflatex Schwarzschild-Ware-metric.tex
```

---

© 2026 William B. Ware / Atomic Dream Labs — All rights reserved.
