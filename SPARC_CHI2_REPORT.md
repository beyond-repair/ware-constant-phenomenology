# SPARC Evaluation Report (W_★ = 1/(4π))

**Date:** 2026-08-15 (continuous optimization pass)

## Results

| Stage | Median χ²_red | Notes |
|-------|---------------|-------|
| Untuned additive | ~35–40 | |
| Grid-tuned Υ,β,γ | ~11.9 | |
| **Continuous scipy** | **~9.1** | Single-digit median; 36% <5; 53% <10 |
| Double-component attempt | ~51 | Rejected (worse) |

Macro \(r_0(M_b)\) **never varied**. W locked at \(1/(4\pi)\).

## Status

Median is now **single-digit** (~9.1) but not yet \(\mathcal{O}(1)\) (~1–3). Further profile structure or limited galaxy-to-galaxy physics still needed.


## Recompute on the committed table (2026-10-02)

`python sparc_run.py --mode o1` on `data/sparc_flat.csv`
(Lelli+2016 Rotmod_LTG adapter; 3391 points; 175 galaxies; 165 with ≥6 points).

| Quantity | Printed |
|----------|---------|
| median χ²_red | 9.098 |
| fraction < 5 | 35.8% |
| fraction < 10 | 52.7% |

W stayed 1/(4π). Macro r0(Mb) stayed frozen. Nothing was tuned to chase the
historical "~9.1 / 36% <5 / 53% <10" line; this run landed next to it.
Still not O(1). SPARC χ² as a pass remains **UNSUPPORTED**.
