# -- Path setup --------------------------------------------------------------

import datetime
import sys
import tomllib
from pathlib import Path

here = Path(__file__).parent.resolve()
sys.path.insert(0, str(here / ".." / ".."))


# -- Project information -----------------------------------------------------

project = "django-vite-boilerplate"
copyright = f"{datetime.datetime.now().year}, Your Name"
author = "Your Name"


def _get_version() -> str:
    with (here / ".." / ".." / "pyproject.toml").open("rb") as fp:
        data = tomllib.load(fp)
    version: str = data["tool"]["poetry"]["version"]
    return version


version = _get_version()
release = version


# -- General configuration ---------------------------------------------------

extensions = ["sphinx.ext.autodoc", "autoapi.extension", "myst_parser"]

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "markdown",
    ".md": "markdown",
}

autoapi_type = "python"
autoapi_dirs = ["../.."]
autoapi_ignore = ["*/tests/*.py", "*/venv/*"]
autodoc_typehints = "description"

templates_path = ["_templates"]

exclude_patterns = []

pygments_style = "sphinx"


# -- Options for HTML output -------------------------------------------------

html_theme = "furo"

html_theme_options = {
    "announcement": '🚀 Follow <a href="https://x.com/michaelyinplus" rel="nofollow" target="_blank">@michaelyinplus</a> on X for daily insights on Django and Modern Frontend development.',
}