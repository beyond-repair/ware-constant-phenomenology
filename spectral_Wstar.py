#!/usr/bin/env python3
"""
spectral_Wstar.py
-----------------
Route C spectral ratios on the 0.45 Sierpinski mesh + Route B toy
one-loop effective potential. Reports numbers that actually emerge.
No ratio on the finite mesh cleanly equals 0.08; 1/(4π)≈0.0796
remains the closest analytic coincidence.
"""
from __future__ import annotations
import sys
from pathlib import Path
import numpy as np

for c in [Path("/tmp/sg"), Path.cwd().parent / "sierpinski-geometry-045"]:
    if (c / "sierpinski_generator.py").exists():
        sys.path.insert(0, str(c))
        break
from sierpinski_generator import generate_asymmetric_sierpinski

def graph_laplacian(V, F):
    N = len(V)
    A = np.zeros((N, N))
    for i0, i1, i2 in F:
        for a, b in ((i0, i1), (i1, i2), (i2, i0)):
            w = 1.0 / (np.linalg.norm(V[a]-V[b]) + 1e-15)
            A[a, b] = max(A[a, b], w)
            A[b, a] = A[a, b]
    return np.diag(A.sum(axis=1)) - A

def spectral_candidates(L):
    evals = np.sort(np.real(np.linalg.eigvalsh(L)))
    evals = evals[evals > 1e-10 * evals[-1]]
    lam1, lamN = evals[0], evals[-1]
    return {
        "λ1/λN": lam1/lamN,
        "1/(4π)": 1/(4*np.pi),
        "λ1/(λ1+λN)": lam1/(lam1+lamN),
        "std/mean": np.std(evals)/np.mean(evals),
    }, evals

def one_loop_toy():
    Wc = 0.125
    best_W, best_score = 0.08, -1
    for W in np.linspace(0.01, 0.12, 50):
        phi = np.linspace(0, 3, 200)
        V = 0.5*0.1*phi**2 + 0.25*phi**4 - (W/Wc)*np.log(1+phi**2)
        i = np.argmin(V)
        score = phi[i] * abs(V[i]-V[0])
        if score > best_score:
            best_score, best_W = score, W
    return best_W

def main():
    print("=" * 60)
    print("Spectral / one-loop constraints on W_star")
    V, F = generate_asymmetric_sierpinski(0.45, 3, 1)
    cands, evals = spectral_candidates(graph_laplacian(V, F))
    print(f"Mesh: {len(V)} verts, {len(evals)} positive eigenvalues")
    for k, v in cands.items():
        mark = "  <-- near 0.08" if abs(v-0.08)<0.03 else ""
        print(f"  {k:20s} = {v:.6f}{mark}")
    print(f"Route B toy preferred W ≈ {one_loop_toy():.4f}")
    print("No clean first-principles derivation of 0.08 from this mesh.")
    print("=" * 60)

if __name__ == "__main__":
    main()
