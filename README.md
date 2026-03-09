

```markdown
# Ware Constant Phenomenology

**Phenomenological study of the Ware Constant (W ≈ 0.08) as a universal dimensionless coupling across subatomic, galactic, and cosmological anomalies.**

This repository documents an independent theoretical framework that resolves major gravitational anomalies traditionally attributed to non-baryonic dark matter using a single screened modification to general relativity parameterized by one derived constant:

**W ≈ 0.08**  
(the Ware Constant — vacuum coherence backreaction / informational efficiency loss)

### Core Kill-Gates (Four Independent Validations)
The same value W ≈ 0.08 reproduces four key observations spanning 15+ orders of magnitude:

- **Muonic hydrogen proton-radius puzzle** → Δr ≈ 0.070 fm shift (matches observed ~0.075 ± 0.007 fm)  
- **SPARC/BTFR galactic rotation curves** → asymptotic v_∞ = √(W G M_b / r_0) in 150–250 km/s range  
- **Bullet Cluster lensing offset** → ~3× amplification via screening failure in chaotic plasma  
- **LRG 3-757 / Cosmic Horseshoe strong lensing** → θ_E ≈ 5.2″ reproduced with ~2.8× baryonic boost

All four use the same W with density-dependent screening (S=1 in virialized systems, S=0 in high-density/chaotic regimes).

### Theoretical Foundation
W is not fitted — it is derived from:
- Classical entropy Poisson equation → W = 1/(4π) ≈ 0.0796  
- Quantum logarithmic corrections (LQG-inspired) → cubic equation δ³ – δ² – β = 0 with small β ≈ –0.005888 → physical root ≈ 0.080

Embedded in a screened scalar-tensor / informational flux picture (modified EFE: G_μν = 8πG (T_μν + W T_μν^info)).

### Repository Contents (March 2026)

| File                                      | Description                                                                 | Format     | Status              |
|-------------------------------------------|-----------------------------------------------------------------------------|------------|---------------------|
| `ware-constant-phenomenology.tex`         | Capstone white paper: derivation of W, equations, kill-gates, falsifiability | LaTeX      | Primary document    |
| `Schwarzschild-Ware-metric.tex`           | Modified Schwarzschild solution, weak-field limit, η ≈ 4.8×10⁻¹¹, LRG validation | LaTeX      | Core derivation     |
| `PROVISIONAL_DERIVATIONS.tex`             | Provisional SVT-hybrid Lagrangian, acceleration law, transition radius plot | LaTeX      | Work-in-progress    |
| `ware-constant-phenomenology.md`          | GitHub-friendly summary of main phenomenology                              | Markdown   | Quick preview       |
| `Math.md`                                 | Numerical checks: rotation curves, lensing, Bullet Cluster boost, caveats   | Markdown   | Validation notebook |
| `LICENSE`                                 | All rights reserved (contact for permissions)                               | Text       | Proprietary         |

### Quick Start
1. Clone:  
   ```bash
   git clone https://github.com/beyond-repair/ware-constant-phenomenology.git
   ```

2. Compile main paper:  
   ```bash
   pdflatex ware-constant-phenomenology.tex
   ```

3. Read quick summary: open `ware-constant-phenomenology.md` in browser

### Key Equations
- Modified EFE:  
  $$ G_{\mu\nu} = 8\pi G (T_{\mu\nu} + W T_{\mu\nu}^{\rm info}) $$

- Schwarzschild-Ware potentials:  
  $$ B(r) = 1 - \frac{2GM}{rc^2} + 2W \frac{GM}{r_0 c^2} \ln(r/\lambda) $$

- Screened acceleration (weak-field):  
  $$ a_{\rm total} = -\frac{GM}{r^2} + W \frac{GM}{r_0 r} \quad (S=1) $$

- Asymptotic rotation velocity:  
  $$ v_\infty = \sqrt{W \frac{GM}{r_0}} $$

### Falsifiability Highlights
- Muonic Lamb-shift series: within ±10–15% of W-scaled prediction  
- Weak-lensing γ ≈ 0.96 (unscreened voids) — Euclid/DESI test  
- SPARC χ² comparable or better than MOND/ΛCDM (no halo parameters)  
- Bullet Cluster ratio ≈ 3× (screening failure)  
- Informational Fork Protocol: T_Red > T_CIS × 10³ threshold

### Related Repositories
- [CFT-v3.1](https://github.com/beyond-repair/CFT-v3.1) — Coherence Field Theory kill-gates  
- [CFTv3.3-IQG-Unified-Framework](https://github.com/beyond-repair/CFTv3.3-IQG-Unified-Framework) — Informational quantum gravity unification  
- [-text-informational-fork-protocol-](https://github.com/beyond-repair/-text-informational-fork-protocol-) — Non-locality test

### License & Contact
© 2026 William B. Ware (Atomic Dream Labs) — All rights reserved.  
No reproduction, modification, or distribution without written permission.  
For collaboration, review, or permissions: open an issue or contact via X @AtomicDreamlabs.

If this work is useful, consider starring the repo or sharing feedback — it helps independent research move forward.
```
