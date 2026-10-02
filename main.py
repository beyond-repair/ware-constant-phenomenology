#!/usr/bin/env python3
"""
Claim-0 demo entrypoint for Ware Constant Phenomenology.

Runs the four README demos plus spectral_Wstar offline. Does not refit
constants and does not invent thrust/energy claims.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCRIPTS = [
    ("verify_constant_W_action.py", []),
    ("killgate_verification.py", []),
    ("white_light_qed_bounds.py", []),
    ("sparc_run.py", ["--mode", "o1"]),
    ("spectral_Wstar.py", []),
]


def main() -> int:
    def out(*args, **kwargs):
        kwargs.setdefault("flush", True)
        print(*args, **kwargs)

    out("Ware Constant Phenomenology — Claim-0 offline demo")
    out("=" * 60)
    failed = 0
    for script, args in SCRIPTS:
        out(f"\n>>> python {script} {' '.join(args)}".rstrip())
        proc = subprocess.run(
            [sys.executable, "-u", str(ROOT / script), *args],
            cwd=str(ROOT),
        )
        if proc.returncode != 0:
            out(f"FAILED: {script} exit={proc.returncode}")
            failed += 1
    out("\n" + "=" * 60)
    if failed:
        out(f"Demo finished with {failed} failure(s).")
        return 1
    out("All Claim-0 demos completed.")
    out("SPARC χ² pass remains UNSUPPORTED (see CLAIM_STATUS.md).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
