# masw_fwi

Repository scaffold for a Python application workflow with:
- source code under `src/`
- tests under `tests/`
- scripts under `scripts/`
- local-only data folders for `raw` and `processed` data
- GitHub Actions CI for linting and tests

> `data/`, `notebooks/`, and generated outputs (`results/`, `output/`, `outputs/`, `figures/`, `plots/`) are ignored by Git and not shared.

## Project structure

```text
masw_fwi/
├─ .github/workflows/
├─ data/
│  ├─ raw/
│  └─ processed/
├─ docs/
├─ notebooks/
├─ scripts/
├─ src/masw_fwi/
└─ tests/
```

## Quick start

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements-dev.txt
```

3. Run tests:

```bash
pytest -q
```
