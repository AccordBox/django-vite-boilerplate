import os
import os.path
import shutil

TERMINATOR = "\x1b[0m"
WARNING = "\x1b[1;33m [WARNING]: "
INFO = "\x1b[1;33m [INFO]: "
HINT = "\x1b[3;33m"
SUCCESS = "\x1b[1;32m [SUCCESS]: "

DENY_LIST = [".gitignore"]
ALLOW_LIST = ["package.json", "vite_django_config.json", "vite.config.js"]


def print_success_msg(msg):
    print(SUCCESS + msg + TERMINATOR)


def get_frontend_config_files():
    frontend_path = os.getcwd()

    for f in os.listdir(frontend_path):
        if f.startswith(".") and f not in DENY_LIST:
            full_path = os.path.join(frontend_path, f)
            yield os.path.dirname(full_path), os.path.basename(full_path)

    for f in ALLOW_LIST:
        full_path = os.path.join(frontend_path, f)
        yield os.path.dirname(full_path), os.path.basename(full_path)


def copy_frontend_config_files():
    """
    Move frontend config files from frontend dir to the root directory
    """
    for dirname, filename in get_frontend_config_files():
        old_full_path = os.path.join(dirname, filename)
        root_dir = os.path.dirname(dirname)
        new_full_path = os.path.join(root_dir, filename)
        try:
            shutil.copyfile(old_full_path, new_full_path)
            os.remove(old_full_path)
        except (OSError, IOError) as e:
            print(f"{WARNING}Failed to copy {filename}: {e}{TERMINATOR}")
            print(f"{HINT}Source: {old_full_path}{TERMINATOR}")
            print(f"{HINT}Destination: {new_full_path}{TERMINATOR}")
            raise


def cleanup_unnecessary_files():
    """
    Remove unnecessary files based on template choices.
    """
    frontend_path = os.getcwd()

    # Remove app.scss if style_solution is 'bootstrap', otherwise remove app.css
    if "{{ cookiecutter.style_solution }}" == "bootstrap":
        app_css_path = os.path.join(frontend_path, "application", "app.css")
        if os.path.exists(app_css_path):
            os.remove(app_css_path)
    else:
        app_scss_path = os.path.join(frontend_path, "application", "app.scss")
        if os.path.exists(app_scss_path):
            os.remove(app_scss_path)


def main():
    copy_frontend_config_files()
    cleanup_unnecessary_files()

    print_success_msg(
        f"Frontend app '{{ cookiecutter.project_slug }}' "
        f"has been created. "
    )


if __name__ == "__main__":
    main()
