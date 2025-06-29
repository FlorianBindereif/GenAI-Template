# ANSI color codes
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'
HR = "=" * 50 # Horizontal Rule

if __name__ == "__main__":
    message = f"""
{HR}
{GREEN}🚀 Your project '{{ cookiecutter.project_name }}' is ready! 🚀{RESET}

Next steps:
1. Navigate into your new project directory:
{YELLOW}   cd {{ cookiecutter.project_slug }}{RESET}

2. (Optional) If using VS Code and Dev Containers, you can now 'Reopen in Container'.
   The container will set up the virtual environment and install dependencies automatically.

3. If not using a Dev Container, set up your environment and install dependencies manually:
{YELLOW}   uv venv .venv{RESET}
{YELLOW}   uv sync{RESET}
{YELLOW}   uv run pre-commit install --install-hooks{RESET}
{HR}
"""
    print(message)