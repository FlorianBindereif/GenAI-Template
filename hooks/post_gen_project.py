def colorize(text, color_code):
    """Wraps text in ANSI color codes."""
    RESET = '\033[0m'
    return f"{color_code}{text}{RESET}"

# Constants for colors can be simplified
GREEN = '\033[92m'
YELLOW = '\033[93m'

if __name__ == "__main__":
    hr = "=" * 50
    # You can combine this with the multiline string from Option 1

    project_ready = colorize("🚀 Your project '{{ cookiecutter.project_name }}' is ready! 🚀", GREEN)
    cd_command = colorize("   cd {{ cookiecutter.project_slug }}", YELLOW)
    sync_command = colorize("   uv sync", YELLOW)
    precommit_command = colorize("   uv run pre-commit install --install-hooks", YELLOW)

    message = f"""
{hr}
{project_ready}

Next steps:
1. Navigate into your new project directory:
{cd_command}

2. (Optional) Use your IDE to 'Reopen in Container' to use the devcontainer.
   The container will set up the virtual environment and install dependencies automatically.

3. If not using a Dev Container, set up your environment and install dependencies manually:
{sync_command}
{precommit_command}

4. Happy Hacking!
{hr}
"""
    print(message)