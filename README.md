<div align="center">

# Ware Constant Phenomenology

### Runnable **numbers** for the Ware / CFT research line

[![RESEARCH](https://img.shields.io/badge/claim_≤2-7c3aed?style=for-the-badge)](https://github.com/beyond-repair/ADL-Governance)
[![Claim-0](https://img.shields.io/badge/status-RUNNABLE_SKETCH-0ea5e9?style=for-the-badge)](#quick-start-stranger-path)

</div>

---

## Status

**RUNNABLE SKETCH — NOT A COMPLETE PRODUCT (Claim-0 phenomenology).**

Offline scripts for SPARC-style scoring, kill-gates, constant-W action verify,
and white-light QED bounds. Default claim **≤2**. SPARC χ² as a pass remains
**UNSUPPORTED** (honest historical median ~9 on real SPARC; demo CSV χ² is not
a publication claim). Constants are **not** refit to fake a pass. No thrust or
energy-extraction claims.

Constant-W action freeze (2026-09-23): [`CONSTANT_W_ACTION_PRINCIPLE.md`](CONSTANT_W_ACTION_PRINCIPLE.md) — spectral source derived; local W(x) and numerical 0.08 not derived. Check: `python verify_constant_W_action.py`.

See [`CLAIM_STATUS.md`](CLAIM_STATUS.md).

---

## Quick start (stranger path)

```bash
git clone https://github.com/beyond-repair/ware-constant-phenomenology.git
cd ware-constant-phenomenology
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py                  # optional: all demos
python sparc_run.py --mode o1
python killgate_verification.py
python white_light_qed_bounds.py
python verify_constant_W_action.py
python spectral_Wstar.py
pytest -q
```

---

## Demo data disclosure

- Default `data/sparc_flat.csv` is the Lelli, McGaugh & Schombert 2016 SPARC
  mass models (175 galaxies, 3391 points). See `data/README.md`.
- `python sparc_run.py --mode o1` on that table prints median χ²_red = **9.098**
  (165 galaxies with ≥6 points; 35.8% < 5; 52.7% < 10). Constants were not
  refit. That is still **not** an O(1) pass.
- `data/sparc_flat_demo.csv` is a four-galaxy synthetic file and is not the
  default. Its χ² is not a SPARC result.
- Kill-gate `v_∞` (10^11 M_sun, W=0.08) prints **276.5 km/s** and **misses**
  the script's stated 100–250 km/s band. Pipeline W is 1/(4π) ≈ 0.079577, not 0.08.

`spectral_Wstar.py` uses an in-repo minimal `sierpinski_generator.py` (geometry
only). It still reports honestly: **no clean derivation of 0.08** from the mesh.

---

## Visual workflow

```text
 1. LOCK ANCHORS          W★ = 1/(4π) · Option A (M2 geometric only)
         │
 2. LOAD LOCAL DATA       data/sparc_flat.csv (Lelli+2016) or SPARC_CSV
         │
 3. RUN PIPELINE          sparc_run.py --mode o1
         │
 4. SCORE                 χ² / residuals (publish bad χ² too)
         │
 5. KILL-GATES            killgate_verification · white_light · verify action
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
