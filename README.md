# Ware Constant Phenomenology (CFT v3.1)

**Phenomenological study of the Ware Constant (W ≈ 0.08) as a universal dimensionless coupling across subatomic, galactic, and cosmological anomalies.**

This repository presents an independent theoretical framework that resolves major gravitational anomalies traditionally attributed to non-baryonic dark matter using a single screened modification to general relativity parameterized by one derived constant:  
**W ≈ 0.08**  
(the Ware Constant — vacuum coherence backreaction / informational efficiency loss)

### Core Kill-Gates (Four Independent Validations)
The same value \( W \approx 0.08 \) reproduces four key observations spanning 15+ orders of magnitude:

- **Muonic hydrogen proton-radius puzzle** → Δr ≈ 0.070 fm shift (matches observed ~0.075 ± 0.007 fm)
- **SPARC/BTFR galactic rotation curves** → asymptotic \( v_\infty = \sqrt{W G M_b / r_0} \) in the 150–250 km/s range
- **Bullet Cluster lensing offset** → ~3× amplification via screening failure in chaotic plasma
- **LRG 3-757 / Cosmic Horseshoe strong lensing** → θ_E reproduced with ~2.2–2.8× baryonic boost

All four use the same fixed W with density-dependent screening (S=1 in virialized low-density systems, S=0 in high-density/chaotic regimes).

### Theoretical Foundation
W is not fitted — it is derived from first principles:

- Classical entropy Poisson equation → \( W = 1/(4\pi) \approx 0.0796 \)
- Quantum logarithmic corrections (LQG-inspired, c ≈ -3/2) → cubic equation \( \delta^3 - \delta^2 - \beta = 0 \) with β ≈ -0.005888 → physical root ≈ 0.080

The framework is embedded in a screened Proca-type informational vector field that modifies the Einstein equations:
\[
G_{\mu\nu} = 8\pi G (T_{\mu\nu} + W T_{\mu\nu}^{\rm info})
\]

The acceleration law \( a_{\rm info} = W G M_b / (r_0 r) \) is now **explicitly derived** from variation of the action (see PROVISIONAL_DERIVATIONS.tex).

### Repository Contents (April 2026)

| File                                | Description                                                              | Format   | Status          |
|-------------------------------------|--------------------------------------------------------------------------|----------|-----------------|
| `ware-constant-phenomenology.tex`   | Capstone white paper: full derivation of W, equations, kill-gates        | LaTeX    | Primary document |
| `Schwarzschild-Ware-metric.tex`     | Modified Schwarzschild solution, explicit integration, corrected lensing | LaTeX    | Core derivation |
| `PROVISIONAL_DERIVATIONS.tex`       | Proca Lagrangian, explicit action variation, acceleration law derivation | LaTeX    | Complete        |
| `ware-constant-phenomenology.md`    | GitHub-friendly summary                                                  | Markdown | Quick preview   |
| `Math.md`                           | Numerical checks: rotation curves, lensing, Bullet Cluster               | Markdown | Validation      |
| `LICENSE`                           | All rights reserved                                                      | Text     | Proprietary     |

### Quick Start

```bash
git clone https://github.com/beyond-repair/ware-constant-phenomenology.git
cd ware-constant-phenomenology
pdflatex ware-constant-phenomenology.tex
pdflatex ware-constant-phenomenology.tex
