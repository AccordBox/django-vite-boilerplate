"""
Pytest configuration and fixtures for cookiecutter tests.
"""
import os
import shutil
import tempfile
from pathlib import Path

import pytest
from cookiecutter.main import cookiecutter


@pytest.fixture
def template_dir():
    """Return the cookiecutter template directory."""
    return Path(__file__).parent.parent / "django_vite_boilerplate" / "frontend_template"


@pytest.fixture
def output_dir(tmp_path):
    """Create a temporary directory for cookiecutter output."""
    output_dir = tmp_path / "output"
    output_dir.mkdir()
    return output_dir


@pytest.fixture
def context_generator():
    """
    Generate all valid combinations of cookiecutter context.

    Returns a list of dictionaries with different template configurations.
    """
    style_solutions = ["tailwind", "daisy", "bootstrap"]
    javascript_solutions = ["valinajs", "htmx_alpine", "hotwire"]

    contexts = []
    for style in style_solutions:
        for js in javascript_solutions:
            contexts.append({
                "project_slug": f"test_{style}_{js}",
                "style_solution": style,
                "javascript_solution": js,
            })

    return contexts


@pytest.fixture
def default_context():
    """Return a default cookiecutter context."""
    return {
        "project_slug": "test_frontend",
        "style_solution": "tailwind",
        "javascript_solution": "htmx_alpine",
    }
