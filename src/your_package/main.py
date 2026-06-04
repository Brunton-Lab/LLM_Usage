"""Example Hydra entrypoint.

Run it with:
    python -m your_package.main
    python -m your_package.main seed=123 name=ada   # override any config value

Hydra loads ``configs/config.yaml`` (relative to this file), merges any CLI
overrides, and writes the fully-resolved config + overrides into the run's
output directory under ``outputs/`` — so every run is reproducible from disk.
"""

import hydra
from omegaconf import DictConfig, OmegaConf

from your_package import hello


@hydra.main(version_base=None, config_path="../../configs", config_name="config")
def main(cfg: DictConfig) -> None:
    """Print the resolved config and a greeting built from it."""
    print(OmegaConf.to_yaml(cfg))
    print(hello(cfg.name))


if __name__ == "__main__":
    main()
