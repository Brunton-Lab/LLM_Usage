---
name: new-project-setup
description: Use right after creating a repo from this template — to rename the your_package placeholder, fill in metadata, create the environment, and make the first real commit.
---

# New Project Setup

Turn a fresh copy of the template into a real project. Do these in order. The template runs
before any renaming, so you can verify each step.

## 1. Pick a package name

Choose an importable name: `lower_snake_case`, no dashes (e.g. `flywheel`, `gait_lab`). This is
the single token `your_package` used throughout the repo. Confirm the choice with the user
before mass-renaming.

## 2. Rename the `your_package` token

Rename the package directory, then replace the token everywhere it appears.

```bash
NEW=your_real_name            # <-- set this

git mv src/your_package "src/$NEW"
# Replace the token in all tracked text files (review the diff before committing):
grep -rl --exclude-dir=.git "your_package" . | xargs sed -i "s/your_package/$NEW/g"
# The console script in pyproject also uses a dash form; fix it to match:
sed -i "s/your-package/${NEW//_/-}/g" pyproject.toml README.md CLAUDE.md
```

Check nothing was missed: `grep -rn --exclude-dir=.git "your_package\|your-package" .` should
return nothing.

## 3. Fill in placeholders

Search for `TODO` and replace:

- `pyproject.toml` — `description`, `authors`.
- `CLAUDE.md` — the **Project Overview** paragraph; delete the "scaffolded from template" note.
- `README.md` — replace everything below the `---` with the real project README; update the
  title.

## 4. Create the environment and verify

```bash
conda env create -f environment.yaml      # env name now matches your package
conda activate <your_package>
# --python pins uv to the active conda env (not a stray .venv / VIRTUAL_ENV):
uv pip install --python "$CONDA_PREFIX/bin/python" -e ".[dev]"

python -c "import <your_package>; print(<your_package>.__version__)"   # -> 0.1.0
python -m <your_package>.main seed=123                                  # prints resolved config
ruff check . && ruff format --check .
```

## 5. (Optional) scaffold the parts not shipped by default

Create these only when you need them:

- `tests/` with a first smoke test (e.g. assert `hello()` works) — then `pytest`.
- `docs/` already ships `bash-safety.md` (keep it); add your project docs alongside it.
- A `LICENSE` file (ask the user which license).

## 6. First commit

```bash
git add -A
git commit -m "Initialize <your_package> from template"
```

Then start building — load the `project-conventions` skill when adding code.
