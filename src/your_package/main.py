"""Example Hydra entrypoint.

Run it with:
    python -m your_package.main
    python -m your_package.main seed=123 name=ada      # override any config value
    python -m your_package.main run_id=exp1 version=v2  # name the run / group of runs
    python -m your_package.main paths=template          # pick a configs/paths/<machine>.yaml

Hydra loads ``configs/config.yaml`` (relative to this file), merges any CLI
overrides, and changes the working directory to the run's output dir
(``${paths.base_dir}/${run_id}`` — under the git-ignored ``outputs/`` by
default). The custom path resolvers are registered by importing
``your_package.utils`` below, so configs that interpolate them compose correctly.
"""

import hydra
from omegaconf import DictConfig, OmegaConf

from your_package import hello

# Importing utils registers the custom OmegaConf resolvers (multirun_save_dir, …).
from your_package.utils import convert_dict_to_path, save_config


@hydra.main(version_base=None, config_path="../../configs", config_name="config")
def main(cfg: DictConfig) -> None:
    """Print the config, materialize the run's directories, and save the config."""
    print(OmegaConf.to_yaml(cfg))
    print(hello(cfg.name))

    # Resolve the `paths` group to concrete directories and create them.
    paths = convert_dict_to_path(OmegaConf.to_container(cfg.paths, resolve=True))
    print(f"[paths] save_dir = {paths['save_dir']}")

    # Save a fully-resolved copy of the config for reproducibility.
    save_config(cfg, paths["save_dir"] / "config.yaml")


if __name__ == "__main__":
    main()
