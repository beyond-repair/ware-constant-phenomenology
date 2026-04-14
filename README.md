# Ware Constant Phenomenology (CFT v3.1)

**Phenomenological study of the Ware Constant (W ≈ 0.08) as a universal dimensionless coupling across subatomic, galactic, and cosmological anomalies.**

This repository presents a screened modification to general relativity based on a single derived constant \( W \approx 0.08 \), interpreted as vacuum coherence backreaction.

### Core Validations (Kill-Gates)
- **Subatomic**: Muonic hydrogen proton radius shift (~0.07 fm) via informational screening.
- **Galactic**: Flat rotation curves from the derived acceleration law \( a_{\rm info} = W G M_b / (r_0 r) \) (see PROVISIONAL_DERIVATIONS.tex).
- **Cluster Lensing**: ~2.2× amplification in strong lensing systems using the corrected Einstein radius (see Schwarzschild-Ware-metric.tex).
- **Solar System**: Passes PPN tests with screening (\( \eta \approx 4.8 \times 10^{-11} \)).

### Theoretical Foundation
W is derived from entropy extremization (\( W = 1/(4\pi) \)) refined by quantum logarithmic corrections. The framework uses a Proca-type informational vector field whose variation yields the acceleration law and the Schwarzschild-Ware metric.

### Repository Files
- `ware-constant-phenomenology.tex` — Main white paper
- `PROVISIONAL_DERIVATIONS.tex` — Proca Lagrangian and explicit derivation of the acceleration law
- `Schwarzschild-Ware-metric.tex` — Modified metric and corrected lensing formula
- `Math.md` — Numerical checks and validations
- `ware-constant-phenomenology.md` — GitHub summary

### Quick Start
```bash
git clone https://github.com/beyond-repair/ware-constant-phenomenology.git
cd ware-constant-phenomenology
pdflatex ware-constant-phenomenology.tex
