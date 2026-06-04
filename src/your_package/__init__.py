"""your_package — replace this with your project's top-level docstring.

The package version is the single source of truth read by the build backend
(see ``[tool.hatch.version]`` in ``pyproject.toml``).
"""

__version__ = "0.1.0"


def hello(name: str = "world") -> str:
    """Return a friendly greeting.

    A tiny example so the freshly cloned template imports and runs cleanly.
    Replace it with your own code.
    """
    return f"Hello, {name}!"
