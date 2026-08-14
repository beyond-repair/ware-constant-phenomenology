# Working Note: First-Principles Paths to W_★ ≈ 0.08

**Date:** 2026-08-14 (spectral pass)  
**Status:** No completed derivation. Spectral and toy one-loop results recorded.

## Spectral (Route C) on Finite 0.45 Mesh

| Ratio | Value |
|-------|-------|
| λ₁/λ_N | 0.029 |
| 1/(4π) | **0.0796** |
| λ₁/(λ₁+λ_N) | 0.028 |
| std/mean | 0.56 |

No mesh spectral ratio cleanly equals 0.08. The analytic value 1/(4π) remains the closest coincidence.

## One-Loop Toy (Route B)

Schematic effective potential with ghost-critical W_c = 0.125 prefers W near the upper end of the scan (~0.12), sensitive to parameter choices. Not a controlled derivation.

## Status of Routes

| Route | Status |
|-------|--------|
| A Entropic / 1/(4π) | Best numerical coincidence; no derivation |
| B Ghost-bound attractor | Toy model only |
| C Spectral LDOS | Finite-mesh ratios do not yield 0.08 |
| D IR cutoff hierarchy | Not pursued this pass |
| E Anomaly coefficient | Same 1/(4π) coincidence |

## Required for Closure

Controlled continuum spectral calculation on the infinite lattice, or a derived one-loop effective potential from the actual Proca + Einstein action, with all coefficients fixed by the Lagrangian.

Script: `spectral_Wstar.py`
