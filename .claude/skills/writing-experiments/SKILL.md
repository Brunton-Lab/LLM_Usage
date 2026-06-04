---
name: writing-experiments
description: Use when writing research/experiment or analysis code — training runs, sweeps, notebooks, figures — to keep it reproducible and separate from the importable package.
---

# Writing Experiments

Conventions for research/experiment code: runs, analyses, notebooks, and figures. The goal is
that any result can be traced back to the exact code and config that produced it.

## Library vs. experiment code

- **Reusable logic** (models, data loaders, metrics) belongs in `src/your_package/` and gets
  tested. Import it from experiments.
- **Experiment code** (a specific run, sweep, or analysis) stays **out of `src/`** — in
  `scripts/`, `experiments/`, or `notebooks/`. It can be messier, but it should call into the
  package rather than reimplementing logic.

Rule of thumb: if you'd want to reuse it next week, it goes in the package; if it's "the thing I
ran on Tuesday," it's experiment code.

## Configs drive runs (Hydra)

- Every run is defined by a config in `configs/`, not by editing code. Override on the CLI:
  `python -m your_package.main lr=1e-3 seed=7`.
- Hydra automatically writes the **fully-resolved config and the CLI overrides** into each run's
  output directory (`outputs/<date>/<time>/.hydra/`). That snapshot is your reproducibility
  record — don't reconstruct it by hand.
- Sweeps: use `--multirun` (`python -m your_package.main --multirun seed=1,2,3`); outputs land
  under `multirun/`.

## Reproducibility checklist

- **Seed everything** and put the seed in the config (`seed:` is in `config.yaml`). Seed
  Python/NumPy/your framework's RNGs from `cfg.seed`.
- **Record the code version** — commit before a real run, or log `git rev-parse HEAD` into the
  run dir. Don't run experiments on a dirty tree you can't recover.
- **Pin the environment** for results you'll report (`uv pip freeze` / export the conda env).

## Outputs and artifacts

- Hydra run dirs (`outputs/`, `multirun/`) are git-ignored — they're regenerable, not source.
- Save figures/tables to the run's output dir (or a `results/` dir), not next to the code.
- Reference large/raw data by path or config; don't commit it.

## Notebooks

- Keep notebooks thin: import from the package, don't grow reusable logic inside a cell.
- When notebook code matures, promote it into `src/your_package/` with a test.
- Clear outputs before committing (notebooks with embedded outputs bloat diffs).
