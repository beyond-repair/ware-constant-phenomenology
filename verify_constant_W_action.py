#!/usr/bin/env python3
"""Deterministic verification of the constant-W action identities."""
from __future__ import annotations
import math
import numpy as np

def spectral_source(omega2, W, evals):
    return 0.5 * float(np.sum(evals / (omega2 - W * evals)))

def v_1loop(omega2, W, evals):
    return 0.5 * float(np.sum(np.log(omega2 - W * evals)))

def v2_1loop(omega2, W, evals):
    return -0.5 * float(np.sum(evals**2 / (omega2 - W * evals) ** 2))

def main():
    rng = np.random.default_rng(0)
    L = rng.normal(size=(12, 8))
    L = L @ L.T
    evals = np.linalg.eigvalsh(L)
    omega2 = 1.0
    W_crit = omega2 / float(evals.max())
    W = 0.4 * W_crit
    K = omega2 * np.eye(L.shape[0]) - W * L
    source_tr = 0.5 * float(np.trace(np.linalg.inv(K) @ L))
    source_spec = spectral_source(omega2, W, evals)
    assert math.isclose(source_tr, source_spec, rel_tol=1e-12, abs_tol=1e-12)
    h = 1e-6
    dV = (v_1loop(omega2, W + h, evals) - v_1loop(omega2, W - h, evals)) / (2 * h)
    d2V = (v_1loop(omega2, W + h, evals) - 2 * v_1loop(omega2, W, evals) + v_1loop(omega2, W - h, evals)) / h**2
    assert math.isclose(dV, -source_spec, rel_tol=1e-6, abs_tol=1e-8)
    assert math.isclose(d2V, v2_1loop(omega2, W, evals), rel_tol=1e-5, abs_tol=1e-6)
    assert v2_1loop(omega2, W, evals) < 0
    assert v_1loop(omega2, W_crit * (1 - 1e-8), evals) < -5.0
    print("PASS")

if __name__ == "__main__":
    main()
