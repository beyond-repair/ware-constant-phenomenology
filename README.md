<div align="center">

# Ware Constant Phenomenology

### The **numbers and pipelines** behind the Ware / CFT research line

[![RESEARCH](https://img.shields.io/badge/classification-RESEARCH-f59e0b?style=for-the-badge)](https://github.com/beyond-repair/ADL-Governance)
[![Claim](https://img.shields.io/badge/claim_≤_2-7c3aed?style=for-the-badge)](https://github.com/beyond-repair/ADL-Governance/blob/main/docs/CLAIM_VALIDATION.md)

</div>

---

## Why this exists

If the Ware idea is only prose, it cannot be attacked or improved.  
This repo is where **equations meet runnable checks**: SPARC-style curves, kill-gate scripts, lensing helpers — so claims stay **phenomenology (≤2)**, not marketing.

## Why you need it

| You are… | You open this repo to… |
|----------|-------------------------|
| Reviewing CFT / Ware | Run the **same scripts** the ledger points at |
| Building Stage-2 numerics | Keep **\(W_\star\)** separate from recursive **\(W(n)\)** |
| Auditing honesty | See open physics (SPARC not O(1), Bullet still open) |

**You do not need it** for a shipping product. It is not an engine and does not raise thrust claims.

## How it works

1. **Anchor** — tree-level \(W_\star = 1/(4\pi) \approx 0.079577\) for galactic-style phenomenology.  
2. **Option A** — M2 / recursion factors are **geometric / LDOS-side only**; they do not silently rescale Einstein coupling.  
3. **Pipelines** — local Python entrypoints fit or score model curves against data files you provide offline.  
4. **Honest scoreboard** — local SPARC median \(\chi^2_{\rm red}\sim 9\) is **not** O(1); that gap is documented, not hidden.

```bash
python sparc_run.py --mode o1          # recommended
python killgate_verification.py
python multiplane_lensing.py
```

| Script | Role |
|--------|------|
| `sparc_run.py` | Canonical SPARC entry |
| `sparc_o1.py` | Continuous local optimizer |
| `killgate_verification.py` | Multi-scale check harness |

## What it is not

- Not proof of dark-matter replacement  
- Not laboratory thrust  
- Not energy extraction  

Theory freeze / residual-force stages: [coherence-drive/docs/MATH_THEORY_CLOSURE.md](https://github.com/beyond-repair/coherence-drive/blob/main/docs/MATH_THEORY_CLOSURE.md)

## Open physics

Bullet Model D · local SPARC → O(1) · bulk \(c_\star\) · \(\lambda_A\)/δ_sat

---

**Atomic Dream Labs** · Index: [coherence-drive](https://github.com/beyond-repair/coherence-drive) · Governance: [ADL-Governance](https://github.com/beyond-repair/ADL-Governance)
