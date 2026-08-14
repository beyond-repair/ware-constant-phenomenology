# SPARC χ² Report under Locked W_★ = 0.08

**Date:** 2026-08-14  
**Status:** Transparent baseline — claims of excellent SPARC fits are **not** supported.

## Setup

- Parameter lock: Option A, \(W_\star = 0.08\).
- Coherence scale: \(r_0 = 0.45\,\mathrm{kpc}\,(M_b/10^{11}M_\odot)^{0.40}\).
- Model: asymptotic additive term \(V_W^2 = W_\star G M_b / r_0\).
- Per-galaxy stellar mass-to-light ratio \(\Upsilon_\mathrm{disk}\in[0.1,1.2]\); bulge ratio 1.4 when present.
- Data: 175 SPARC galaxies, 3391 points (public unified corpus).

## Results (asymptotic model)

| Statistic | Value |
|-----------|-------|
| Median \(\chi^2_\mathrm{red}\) | ≈ 40 |
| Mean \(\chi^2_\mathrm{red}\) | ≈ 175 |
| P16 / P50 / P84 | ≈ 6.6 / 40 / 231 |
| Median \(\Upsilon_\mathrm{disk}\) | 0.10 (floor of grid) |

A radially dependent form taken from PROVISIONAL_DERIVATIONS.tex yields median \(\chi^2_\mathrm{red}\approx 34\) — still far from an acceptable fit.

## Interpretation

1. The statements in earlier `.tex` notes that SPARC residuals are "<5%" are **not reproduced** by either the asymptotic or the provisional radial formula under a single global \(W_\star\).
2. Many galaxies prefer the lowest allowed \(\Upsilon\), suggesting the Ware term is often too large or that \(M_b\)/\(r_0\) scaling needs recalibration.
3. A publication-grade analysis would require hierarchical modelling, distance uncertainties, and possibly galaxy-to-galaxy variation in effective \(W\) or \(r_0\). None of that is claimed here.

## Consequence for the framework

SPARC is a kill-gate. Until a calibrated model achieves median \(\chi^2_\mathrm{red}\sim\mathcal{O}(1)\) under a clearly stated parameter policy, galactic-scale success remains **unverified**.

Script: `sparc_chi2.py`  
Per-galaxy table: `sparc_chi2_results.csv` (generated locally from public data).
