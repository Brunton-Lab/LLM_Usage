# CLAUDE.md

Guidance for Claude Code (and humans) working in this repository.

> This file was scaffolded from a project template. After running the
> **new-project-setup** skill, replace the placeholder text below and delete this note.

## Project Overview

<!-- TODO: One or two paragraphs — what this project does, the core idea, the main
     entry points. Keep it concrete. -->

A general-purpose Python project using a `src/` layout, Hydra-managed configuration, and
`pytest`/`ruff` for testing and linting.

## Setup

```bash
conda env create -f environment.yaml   # creates the env (Python 3.12 + uv)
conda activate your_package
# --python pins uv to the active conda env (guards against a stray .venv / VIRTUAL_ENV):
uv pip install --python "$CONDA_PREFIX/bin/python" -e ".[dev]"   # package + dev tools (pytest, ruff)
```

## Running

The package exposes a Hydra entrypoint:

```bash
python -m your_package.main             # runs with configs/config.yaml
python -m your_package.main seed=123    # override any config value on the CLI
```

## Configs

Run parameters live in `configs/` and are managed by **Hydra**. Override values on the CLI;
add config groups as `configs/<group>/<option>.yaml`. Hydra writes the fully-resolved config
for each run into that run's output dir, so results are reproducible from disk.

## Testing

```bash
pytest                                  # tests live in tests/, mirroring src/
ruff check . && ruff format --check .   # lint + format check
```

## Conventions (summary)

- **Layout:** importable code under `src/your_package/`; tests under `tests/` mirroring it;
  run configs under `configs/`.
- **Imports:** absolute imports from the package (`from your_package.x import y`).
- **Units:** small, single-purpose functions/modules; split a file when it starts doing more
  than one thing.
- For anything deeper — where new code/configs/experiments should go — **load the
  `project-conventions` skill** rather than guessing.

## Available project skills (`.claude/skills/`)

Load the relevant one before doing that kind of work:

- **project-conventions** — how code, tests, and configs are organized here.
- **new-project-setup** — instantiate this template into a real project (rename, fill
  placeholders, create the env).
- **authoring-skills** — how to write a new project-local skill in this repo.
- **writing-experiments** — conventions for research/experiment code and reproducibility.

## Optional: superpowers plugin

This repo is fully self-contained. If you happen to have the **superpowers** Claude Code
plugin installed, its global skills (brainstorming, test-driven-development, writing-skills,
systematic-debugging) complement the local skills above — but nothing here requires it.
