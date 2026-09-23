<div align="center">

# Ware Constant Phenomenology

### Runnable **numbers** for the Ware / CFT research line

[![RESEARCH](https://img.shields.io/badge/claim_≤2-7c3aed?style=for-the-badge)](https://github.com/beyond-repair/ADL-Governance)

</div>

---

## Why unique

Not a whitepaper-only repo — **scripts you can run offline** so fits and kill-gates are attackable. Default claim **≤2** (phenomenology, not proven ontology).

Constant-W action freeze (2026-09-23): [`CONSTANT_W_ACTION_PRINCIPLE.md`](CONSTANT_W_ACTION_PRINCIPLE.md) — spectral source derived; local W(x) and numerical 0.08 not derived. Check: `python verify_constant_W_action.py`.

---

## Visual workflow

```text
 1. LOCK ANCHORS          W★ = 1/(4π) · Option A (M2 geometric only)
         │
 2. LOAD LOCAL DATA       SPARC-style curves (no network)
         │
 3. RUN PIPELINE          sparc_run.py --mode o1
         │
 4. SCORE                 χ² / residuals (honest: local median ~9, not O(1))
         │
 5. KILL-GATES            killgate_verification · lensing helpers
         │
 6. FEED LEDGER           results inform CFTv3.3 registry — do not invent thrust
```

| Step | How | Why |
|-----:|-----|-----|
| 1 | Fix W_star, Option A | Stop silent double-use of W |
| 2 | Local files only | Reproducible, offline |
| 3 | `sparc_run.py` | One entrypoint |
| 4 | Publish bad χ² too | Honesty > marketing |
| 5 | Multi-scale checks | Stress the model |
| 6 | Point to synthesis | Conjunction with index |

```bash
python sparc_run.py --mode o1
python killgate_verification.py
python white_light_qed_bounds.py
python verify_constant_W_action.py
```

**Conjunction:** geometry/stress live elsewhere; this repo is **galactic-style scoring**. Theory freeze: [coherence-drive](https://github.com/beyond-repair/coherence-drive).

**White-Light companion (2026-09-19, claim 1):** `WHITE_LIGHT_MASS_HYPOTHESIS.md`, mapping `WHITE_LIGHT_CFT_MAPPING.md`. Does **not** derive W_star and does **not** raise experimental_validation.
