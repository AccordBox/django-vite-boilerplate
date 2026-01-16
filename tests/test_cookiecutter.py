"""
Test cookiecutter template generation with different options.

This module ensures that all combinations of style_solution and javascript_solution
can be generated without raising exceptions.
"""
import os
import shutil
import subprocess
from pathlib import Path

import pytest
from cookiecutter.exceptions import FailedHookException
from cookiecutter.main import cookiecutter


def run_npm_command(project_path: Path, command: list[str]) -> subprocess.CompletedProcess:
    """
    Run an npm command in the given project directory.

    Args:
        project_path: Path to the project directory
        command: Command list to execute (e.g., ['npm', 'install'])

    Returns:
        subprocess.CompletedProcess: The result of the command execution
    """
    result = subprocess.run(
        command,
        cwd=project_path,
        capture_output=True,
        text=True,
        timeout=300,  # 5 minute timeout
    )

    return result


class TestStyleSolutions:
    """Test all style_solution options."""

    @pytest.mark.parametrize("style", ["tailwind", "daisy", "bootstrap"])
    def test_all_style_solutions(self, template_dir, output_dir, style):
        """Test that all style solutions can be generated without errors."""
        context = {
            "project_slug": f"test_style_{style}",
            "style_solution": style,
            "javascript_solution": "valinajs",
        }

        result = cookiecutter(
            template=str(template_dir),
            output_dir=str(output_dir),
            no_input=True,
            extra_context=context,
        )

        project_path = Path(result)
        assert project_path.exists()
        assert project_path.is_dir()


class TestJavaScriptSolutions:
    """Test all javascript_solution options."""

    @pytest.mark.parametrize("js_solution", ["valinajs", "htmx_alpine", "hotwire"])
    def test_all_javascript_solutions(self, template_dir, output_dir, js_solution):
        """Test that all JavaScript solutions can be generated without errors."""
        context = {
            "project_slug": f"test_js_{js_solution}",
            "style_solution": "tailwind",
            "javascript_solution": js_solution,
        }

        result = cookiecutter(
            template=str(template_dir),
            output_dir=str(output_dir),
            no_input=True,
            extra_context=context,
        )

        project_path = Path(result)
        assert project_path.exists()
        assert project_path.is_dir()


class TestAllCombinations:
    """Test all combinations of style_solution and javascript_solution."""

    @pytest.mark.parametrize("style", ["tailwind", "daisy", "bootstrap"])
    @pytest.mark.parametrize("js_solution", ["valinajs", "htmx_alpine", "hotwire"])
    def test_all_combinations(self, template_dir, output_dir, style, js_solution):
        """
        Test all valid combinations of style and JavaScript solutions.

        This test ensures that no combination raises an exception during generation.
        """
        context = {
            "project_slug": f"test_{style}_{js_solution}",
            "style_solution": style,
            "javascript_solution": js_solution,
        }

        # This should not raise any exceptions
        result = cookiecutter(
            template=str(template_dir),
            output_dir=str(output_dir),
            no_input=True,
            extra_context=context,
        )

        project_path = Path(result)
        assert project_path.exists()
        assert project_path.is_dir()


class TestNpmBuild:
    """Test npm install and build for different combinations."""

    def test_npm_install_and_build_default(self, template_dir, output_dir, default_context):
        """Test npm install and build with default context."""
        result = cookiecutter(
            template=str(template_dir),
            output_dir=str(output_dir),
            no_input=True,
            extra_context=default_context,
        )

        project_path = Path(result)

        # Run npm install
        install_result = run_npm_command(project_path, ["npm", "install"])
        assert install_result.returncode == 0, f"npm install failed: {install_result.stderr}"

        # Run npm build
        build_result = run_npm_command(project_path, ["npm", "run", "build"])
        assert build_result.returncode == 0, f"npm run build failed: {build_result.stderr}"

        # Verify build output exists
        assert (output_dir / "public" / "static" / "assets").exists() or (output_dir / "public" / "static").exists()

    @pytest.mark.slow
    @pytest.mark.parametrize("style", ["tailwind", "daisy", "bootstrap"])
    def test_npm_install_and_build_all_styles(self, template_dir, output_dir, style):
        """Test npm install and build for all style solutions."""
        context = {
            "project_slug": f"test_build_style_{style}",
            "style_solution": style,
            "javascript_solution": "htmx_alpine",
        }

        result = cookiecutter(
            template=str(template_dir),
            output_dir=str(output_dir),
            no_input=True,
            extra_context=context,
        )

        project_path = Path(result)

        # Run npm install
        install_result = run_npm_command(project_path, ["npm", "install"])
        assert install_result.returncode == 0, f"npm install failed for {style}: {install_result.stderr}"

        # Run npm build
        build_result = run_npm_command(project_path, ["npm", "run", "build"])
        assert build_result.returncode == 0, f"npm run build failed for {style}: {build_result.stderr}"

        # Verify build output exists
        assert (output_dir / "public" / "static").exists(), f"Build output missing for {style}"

    @pytest.mark.slow
    @pytest.mark.parametrize("js_solution", ["valinajs", "htmx_alpine", "hotwire"])
    def test_npm_install_and_build_all_javascript_solutions(self, template_dir, output_dir, js_solution):
        """Test npm install and build for all JavaScript solutions."""
        context = {
            "project_slug": f"test_build_js_{js_solution}",
            "style_solution": "tailwind",
            "javascript_solution": js_solution,
        }

        result = cookiecutter(
            template=str(template_dir),
            output_dir=str(output_dir),
            no_input=True,
            extra_context=context,
        )

        project_path = Path(result)

        # Run npm install
        install_result = run_npm_command(project_path, ["npm", "install"])
        assert install_result.returncode == 0, f"npm install failed for {js_solution}: {install_result.stderr}"

        # Run npm build
        build_result = run_npm_command(project_path, ["npm", "run", "build"])
        assert build_result.returncode == 0, f"npm run build failed for {js_solution}: {build_result.stderr}"

        # Verify build output exists
        assert (output_dir / "public" / "static").exists(), f"Build output missing for {js_solution}"

    @pytest.mark.integration
    @pytest.mark.slow
    @pytest.mark.parametrize("style", ["tailwind", "daisy", "bootstrap"])
    @pytest.mark.parametrize("js_solution", ["valinajs", "htmx_alpine", "hotwire"])
    def test_npm_install_and_build_all_combinations(self, template_dir, output_dir, style, js_solution):
        """
        Test npm install and build for all combinations of style and JavaScript solutions.

        This is an integration test marked as slow because it runs npm install and build
        for all 16 combinations, which can take several minutes.
        """
        context = {
            "project_slug": f"test_build_{style}_{js_solution}",
            "style_solution": style,
            "javascript_solution": js_solution,
        }

        result = cookiecutter(
            template=str(template_dir),
            output_dir=str(output_dir),
            no_input=True,
            extra_context=context,
        )

        project_path = Path(result)

        # Run npm install
        install_result = run_npm_command(project_path, ["npm", "install"])
        assert install_result.returncode == 0, (
            f"npm install failed for {style}+{js_solution}: {install_result.stderr}\n"
            f"stdout: {install_result.stdout}"
        )

        # Run npm build
        build_result = run_npm_command(project_path, ["npm", "run", "build"])
        assert build_result.returncode == 0, (
            f"npm run build failed for {style}+{js_solution}: {build_result.stderr}\n"
            f"stdout: {build_result.stdout}"
        )

        # Verify build output exists
        dist_path = output_dir / "public" / "static"
        assert dist_path.exists(), f"Build output missing for {style}+{js_solution}"

        # Verify at least some assets were built
        assets_path = dist_path / "assets"
        if assets_path.exists():
            # Check that some files were created in assets
            asset_files = list(assets_path.rglob("*"))
            assert len(asset_files) > 0, f"No assets built for {style}+{js_solution}"
