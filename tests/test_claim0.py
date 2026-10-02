"""Claim-0 offline smoke tests for ware-constant-phenomenology."""
from __future__ import annotations

import math
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def _run(script: str, *extra: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(ROOT / script), *extra],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
        check=False,
    )


def test_verify_constant_W_action_pass():
    proc = _run("verify_constant_W_action.py")
    assert proc.returncode == 0, proc.stderr
    assert "PASS" in proc.stdout


def test_killgate_runs():
    proc = _run("killgate_verification.py")
    assert proc.returncode == 0, proc.stderr
    assert "Kill-gate verification" in proc.stdout
    assert "W_star" in proc.stdout


def test_white_light_runs():
    proc = _run("white_light_qed_bounds.py")
    assert proc.returncode == 0, proc.stderr
    assert "White-Light" in proc.stdout
    assert "EH does not produce W_star" in proc.stdout


def test_sparc_run_o1_demo_finite_median():
    import sparc_o1

    path = sparc_o1.resolve_sparc_csv()
    assert path.exists()
    tab = sparc_o1.main()
    assert len(tab) >= 1
    med = float(tab.chi2_red.median())
    assert math.isfinite(med)
    assert med > 0


def test_spectral_Wstar_offline():
    proc = _run("spectral_Wstar.py")
    assert proc.returncode == 0, proc.stderr
    assert "No clean first-principles derivation of 0.08" in proc.stdout
    assert "Mesh:" in proc.stdout


def test_sierpinski_generator_local():
    from sierpinski_generator import generate_asymmetric_sierpinski

    V, F = generate_asymmetric_sierpinski(0.45, 2, 1)
    assert V.ndim == 2 and V.shape[1] == 3
    assert F.ndim == 2 and F.shape[1] == 3
    assert len(V) > 4
    assert len(F) > 0


def test_demo_csv_columns():
    import pandas as pd

    demo = ROOT / "data" / "sparc_flat_demo.csv"
    assert demo.exists()
    df = pd.read_csv(demo)
    for col in ("survey", "errV", "galaxy", "Rad", "Vgas", "Vdisk", "Vbul", "Vobs"):
        assert col in df.columns
    assert (df.survey == "SPARC").all()
    assert df.galaxy.nunique() >= 3


def test_main_demo_entrypoint():
    proc = _run("main.py")
    assert proc.returncode == 0, proc.stderr + proc.stdout
    assert "All Claim-0 demos completed" in proc.stdout
