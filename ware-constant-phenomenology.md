# The Schwarzschild-Ware Metric (historical note + lock)

**William B. Ware** · Atomic Dream Labs  
GitHub: [beyond-repair/ware-constant-phenomenology](https://github.com/beyond-repair/ware-constant-phenomenology)

> **Sweep-159f lock.** This file is a historical narrative. Authoritative symbols and
> claim flags live in [CLAIM_STATUS.md](CLAIM_STATUS.md),
> [AUDIT_2026-09-22.md](AUDIT_2026-09-22.md), and
> [DERIVATION_INVENTORY.md](DERIVATION_INVENTORY.md).
> Stage 1 freeze is not modified here.

## Symbols (Option A)

$$
W_\star = \frac{1}{4\pi}\approx 0.079577
\qquad
W(n)=0.08\,e^{0.23(n-3)}
$$

Do not interchange them. Deprecated indexing \(W(n)=0.08 e^{0.23(n-1)}\) is out of scope.

## 1. Modified Einstein equation (as written)

$$
G_{\mu\nu} = 8\pi G \left( T_{\mu\nu} + W_\star T_{\mu\nu}^{\rm info} \right)
$$

\(T^{\rm info}\) is not derived from a completed variation in this tree.

## 2. Metric ansatz (not an integrated Proca solution)

$$
B(r) = 1 - \frac{2GM}{r c^2} + \frac{2W_\star GM}{r_0 c^2} \ln\left(\frac{r}{\lambda}\right), \quad A(r) = B(r)^{-1}
$$

Geodesic identity from this ansatz only:

$$
v_c^2 \approx \frac{GM}{r} + \frac{W_\star GM}{r_0}.
$$

A different Yukawa-shaped law still exists in `Ware-Full-Action.tex`. That conflict is open.

## 3. Engineering ratios (Sweep-137)

| Model | \(F(2):F(3):F(4)\) |
|-------|---------------------|
| A (\(W\)-only) | \(0.795:1:1.259\) |
| B (\(W(3\alpha)^n\)) | \(0.589:1:1.699\) |
| Hybrid \(0.795:1:1.993\) | **rejected** |

\(3\times10^{-8}\,\mathrm{N/W}\) is a design target. It does not define \(W\) or \(\kappa\).
Photon Class B cannot reach it (\(1/c\approx 3.34\times10^{-9}\,\mathrm{N/W}\)).

## 4. Observational status (honest)

- SPARC median \(\chi^2_{\rm red}\sim 9.1\): not \(\mathcal{O}(1)\), not a pass.
- Lensing \(\delta_{\rm sat}=1.2\): phenomenological cap.
- Bullet \(r_0/c\): simple model fail.
- Ghost-free \(W<0.125\): model-internal bound.

```
experimental_validation     = false
thrust_validated            = false
energy_extraction_validated = false
```
