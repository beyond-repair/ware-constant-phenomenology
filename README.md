# Ware Constant Phenomenology

**Status (2026-08-17):** Canonical math + executable pipelines for the Ware / CFT stack.

**Locked baseline**

- \(W_\star = 1/(4\pi) \approx 0.079577\) (tree-level matching)
- Option A: M2 is geometric only
- Macro \(r_0(M_b)\) verified; local SPARC median \(\chi^2_{\rm red}\sim 9\) (not O(1))

## SPARC entrypoint

```bash
# recommended
python sparc_run.py --mode o1

# legacy
python sparc_run.py --mode grid   # sparc_local_tune
python sparc_run.py --mode chi2   # sparc_chi2
```

| Script | Role |
|--------|------|
| **sparc_run.py** | **Canonical entrypoint** |
| sparc_o1.py | Continuous local optimizer (default backend) |
| sparc_local_tune.py | Legacy grid tuner |
| sparc_chi2.py | Legacy transparent χ² |

## Other pipelines

```bash
python killgate_verification.py
python multiplane_lensing.py
python bullet_alt_lag.py
python bulk_boundary_reduction.py
```

## Docs

Math.md · CONSISTENCY (in CFTv3.3-IQG-Unified-Framework) · WSTAR_* · BULK_PROCA_REDUCTION.md

## Open physics

Bullet Model D · local SPARC → O(1) · bulk \(c_\star\) · \(\lambda_A\)/δ_sat
