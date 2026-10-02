# SPARC tables

## `sparc_flat.csv` — default

Flat table built from the public SPARC Newtonian mass models
(Lelli, McGaugh & Schombert 2016, AJ 152, 157; Zenodo
[10.5281/zenodo.16284118](https://doi.org/10.5281/zenodo.16284118),
file `Rotmod_LTG.zip`, 175 galaxies, 3391 points).

Columns: `survey`, `galaxy`, `Rad`, `Vobs`, `errV`, `Vgas`, `Vdisk`, `Vbul`.
Surface brightness is omitted. No velocities were rescaled and no galaxies
were dropped.

sha256: `84723347aa1b0ce7c6cf55b0d53016f2216723379058b9926d95fd434accf07a`

Rebuild from a local zip (no network at runtime):

```bash
python tools/build_sparc_flat.py /path/to/Rotmod_LTG.zip
```

Continuous fit on this file, constants not refit: median χ²_red = 9.098
(165 galaxies with ≥6 points; 35.8% < 5; 52.7% < 10). Not an O(1) pass.

## `sparc_flat_demo.csv` — not the default

Four synthetic galaxies. Set `SPARC_CSV=data/sparc_flat_demo.csv` to use it.
Its χ² is not a SPARC result.
