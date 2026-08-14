---
# Mathematical & Numerical Framework: Ware Constant Phenomenology (v0.3.8)

**Last update:** 2026-08-14 (tree-wide audit pass)

## Locked Baseline

- \(W_\star = 1/(4\pi)\approx 0.079577\) (tree-level monopole matching, \(c_\star=1\))
- Macro: \(r_0 = 0.45\,\mathrm{kpc}\,(M_b/10^{11}M_\odot)^{0.40}\) — **verified**
- Option A: M2 geometric only

## Status Summary

| Item | Status |
|------|--------|
| Macro SPARC \(r_0(M_b)\) | Verified |
| Local SPARC χ² | Median ~11.9 (not O(1)) |
| Lensing factor 2.2 | Multiplicative + δ_sat=1.2 (phenomenological saturation scale) |
| δ_sat from additive geodesics | **Fails** |
| δ_sat from lens-plane ξ | Structural multiplicative form; ξ_cap matched |
| Bulk c_star=1 | Matching convention; full non-minimal bulk open |
| Bullet Cluster r0/c lag | **Fails** observed offsets (potential falsifier of minimal lag) |

## Priority Open

1. Full non-minimal bulk → boundary reduction
2. Local χ² → O(1)
3. |A|^4 derivation of ξ_cap / δ_sat
4. Viable Bullet lag mechanism or model revision

Scripts: bulk_boundary_reduction.py · lens_plane_projection.py · bullet_cluster_lag.py · sparc_local_tune.py · multiplane_lensing.py
