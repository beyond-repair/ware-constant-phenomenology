# SPARC Evaluation Report under Locked W_★ = 0.08

**Date:** 2026-08-14 (local-tuning update)  
**Status:** Macro-scaling verified; local residuals improved but not O(1).

## Macro vs Local

| Test | Status |
|------|--------|
| Macro \(r_0(M_b)\propto M_b^{0.40}\) | **Verified** (ontological-fit figure) |
| Local \(V(r)\) χ² (untuned) | median χ²_red ~35–40 |
| Local \(V(r)\) χ² (tuned Υ, β; macro frozen) | median χ²_red ~14; 22% of galaxies < 5; 41% < 10 |

## Local Tuning Result

- Macro relation never varied.
- Free parameters per galaxy: Υ_disk ∈ [0.1, 1.5], β ∈ [0.0, 1.5].
- Median χ²_red improved from ~40 → ~14.
- Still short of median O(1). Outliers (e.g. DDO154, NGC2403) remain severe.
- Median β ≈ 0 (prefers flatter Ware contribution).

Script: `sparc_local_tune.py`

## Consequence

Macro scale dependence is supported. Detailed curve fidelity under a single global W with only Υ/β freedom is improved but not solved. Further radial-structure work or limited galaxy-to-galaxy coupling variation may be required.
