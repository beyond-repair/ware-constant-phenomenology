---
# Mathematical & Numerical Framework: Ware Constant Phenomenology (v0.4.0)

**Last update:** 2026-08-15 (three-front pass)

## Locked Baseline

\(W_\star=1/(4\pi)\approx0.079577\) · Option A · Macro \(r_0\propto M_b^{0.40}\) verified

## Sector Status

| Sector | Status |
|--------|--------|
| Macro SPARC | **Pass** |
| Local SPARC | Median χ²_red **~9.1** (single-digit; not O(1)) |
| Lensing ×2.2 | Multiplicative + δ_sat (semi-derived via \|A\|^4 structure) |
| Bullet lag | Simple r0/c **FAIL**; Model D (cluster ξ~800) open candidate |
| Bulk c_star=1 | Matching convention; non-minimal bulk open |

## Core Equations

\[
a_{\rm tot}=\frac{GM_b}{r^2}+\frac{W_\star GM_b}{r_0 r},\quad
v_\infty^2=\frac{W_\star GM_b}{r_0}
\]

\[
\theta_E=\theta_{E,{\rm GR}}(1+\delta_{\rm eff}),\quad
\delta_{\rm eff}=\frac{\delta_{\rm raw}}{1+\delta_{\rm raw}/\delta_{\rm sat}}
\]

## Open Problems

1. Cluster collective scale ξ for Bullet (Model D) from first principles
2. Local χ² → O(1)
3. Non-minimal bulk confirmation of c_star
4. λ_A from bulk → numerical δ_sat

Scripts: sparc_o1.py · bullet_alt_lag.py · bulk_boundary_reduction.py · delta_sat_from_A4.py
