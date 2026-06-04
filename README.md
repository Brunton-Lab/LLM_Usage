# Python Project Template

A GitHub **template repository** for starting new general-purpose Python projects that come
pre-wired for [Claude Code](https://claude.com/claude-code): a `src/` layout, Hydra config
management, `pytest`/`ruff`, and a `.claude/` folder of conventions and starter skills.

## Use this template

1. Click **"Use this template" → "Create a new repository"** on GitHub (or copy this repo).
2. Open the new repo in Claude Code and run the **new-project-setup** skill — it renames the
   `your_package` placeholder, fills in metadata, and creates the environment. To do it by
   hand, follow `.claude/skills/new-project-setup/SKILL.md`.
3. Replace this README's content (below) with your project's real description.

## What you get

```
.claude/skills/   project-conventions, new-project-setup, authoring-skills, writing-experiments
configs/          Hydra config (configs/config.yaml)
src/your_package/ the importable package (rename this) + example Hydra entrypoint
pyproject.toml    metadata, deps (hydra-core), ruff + pytest config
environment.yaml  conda env (Python 3.12 + uv); uv installs the package
CLAUDE.md         always-on guidance + an index of the skills above
```

The template runs out of the box before you rename anything:

```bash
conda env create -f environment.yaml && conda activate your_package
uv pip install --python "$CONDA_PREFIX/bin/python" -e ".[dev]"   # installs into the conda env
python -m your_package.main          # prints the resolved config + a greeting
```

> The local skills are self-contained and do **not** require the superpowers plugin. If you
> have it installed, its global skills complement these.

---

<!-- TODO: Replace everything below with your project's real README. -->

## Your Project

A short description of what your project does.
