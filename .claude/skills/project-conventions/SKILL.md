---
name: project-conventions
description: Use when structuring code in this repo — adding a module, test, script, or config, deciding where a file belongs, or naming things — to follow the project's layout and style.
---

# Project Conventions

How code, tests, and configs are organized here. Follow these so the repo stays navigable and
predictable. When in doubt, match the nearest existing example over inventing a new pattern.

## Layout

```
src/your_package/   importable library code — the only thing that gets packaged
configs/            Hydra configs (run parameters), see "Configs" below
tests/              pytest tests, mirroring the src/ tree
scripts/            optional one-off / CLI scripts that are NOT part of the library
docs/               optional longer-form docs
```

- **Importable code lives in `src/your_package/`.** Nothing outside `src/` is importable as the
  package. This keeps "what ships" unambiguous and avoids accidental imports from the repo root.
- **Tests mirror the source.** `src/your_package/foo/bar.py` → `tests/foo/test_bar.py`.
- **Experiment/analysis code is not library code.** Keep it out of `src/` (see the
  `writing-experiments` skill).

## Naming

- Modules and packages: `lower_snake_case`.
- Classes: `CapWords`. Functions/variables: `lower_snake_case`. Constants: `UPPER_SNAKE_CASE`.
- Test files: `test_*.py`; test functions: `test_*`.

## Imports

- Use **absolute imports** from the package: `from your_package.models import Encoder`.
- No imports from the repo root or relative `..` climbing across subpackages.
- Group/sort imports stdlib → third-party → first-party (ruff's isort rule `I` enforces this;
  run `ruff check --fix .`).

## Configs (Hydra)

- Run parameters live in `configs/`. The root is `configs/config.yaml`.
- Group related options as `configs/<group>/<option>.yaml` and select them via the `defaults:`
  list. Example: `configs/model/small.yaml`, `configs/model/large.yaml`, chosen with
  `defaults: [_self_, model: small]`.
- Override on the CLI rather than editing files for one-off runs:
  `python -m your_package.main model=large seed=7`.
- Don't read environment variables or hard-code paths in code that a config value could carry.
- **Paths:** the `paths` group (`configs/paths/`) holds output/data locations. The portable
  `default.yaml` keeps runs under the git-ignored `outputs/`; add a machine-specific
  `configs/paths/<machine>.yaml` (copy `template.yaml`) and pick it with `paths=<machine>`.
- **Custom resolvers:** project-specific OmegaConf resolvers (e.g. `multirun_save_dir`) live in
  `src/your_package/utils/path_utils.py` and register on import — so `main.py` imports the
  package before Hydra composes a config.

## Functions, files, and size

- Prefer **small, single-purpose** functions and modules. If you can't summarize a function in
  one sentence, split it.
- When a file grows past a few hundred lines or mixes unrelated responsibilities, that's the
  signal to break it into focused modules.
- Public functions/classes get a short docstring: what it does, args, returns.

## Efficiency & accuracy

- **Prioritize computational efficiency (speed and memory) and numerical accuracy** when
  choosing algorithms and data structures — this applies to library code and
  experiment/analysis code alike.
- Prefer vectorized/batched operations over unnecessary Python-level loops on numerical data;
  avoid needless copies of large arrays/tensors.
- Watch for numerical-correctness pitfalls: precision loss, unstable computations, silent
  dtype casts, off-by-one/edge-case errors in math-heavy code.
- This doesn't license extra complexity: don't add caching, manual memory tricks, or
  low-level rewrites without a known bottleneck. The simplest correct approach still wins by
  default — reach for efficiency only when the algorithm/data-structure choice actually
  matters.

## Style & tooling

- `ruff format` for formatting; `ruff check` for linting (config in `pyproject.toml`,
  line length 100). Run both before committing.
- Type-hint public function signatures.

## Adding something new — quick reference

| Adding… | Put it in… | Also do |
|---|---|---|
| Library code | `src/your_package/...` | add a mirrored test in `tests/` |
| A test | `tests/...` mirroring src | name it `test_*.py` |
| A run parameter | `configs/` (root or a group) | reference it via `cfg`, not a literal |
| A CLI / one-off script | `scripts/` | keep it thin; import logic from the package |
| An experiment / analysis | see `writing-experiments` | keep out of `src/` |
