# SPARC tables (Claim-0)

## Demo (default stranger path)

`sparc_flat_demo.csv` is a **synthetic offline DEMO** with four fake galaxies
(`DEMO_A` … `DEMO_D`) and the columns expected by `sparc_o1.load`.

It is **not** the published SPARC survey. Median χ²_red from this file is a
smoke-test number only — **not** a publication claim.

The repo root `sparc_flat.csv` is an identical DEMO copy so default script
paths work without `/tmp` hacks.

## Optional full SPARC adapter

`sparc_flat.csv` in this directory (when present) is a format-adapted table
built from the public SPARC Rotmod_LTG release:

- Lelli, McGaugh & Schombert 2016, AJ 152, 157
- Zenodo: https://doi.org/10.5281/zenodo.16284118

Rebuild with:

```bash
python tools/build_sparc_flat.py /path/to/Rotmod_LTG.zip
```

Point scorers at it with `SPARC_CSV=data/sparc_flat.csv`. Historical honest
median χ²_red on real SPARC under frozen macro r0 is ~9 (UNSUPPORTED as a pass).
