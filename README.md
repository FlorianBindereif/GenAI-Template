# GenAI Project Template

A modern, best-practices cookiecutter template for creating Generative AI applications in Python. This template sets up a robust project structure with `uv`, `FastAPI`, `pre-commit` hooks, and `devcontainer` support out of the box.

## Features

-   **⚡ Ultra-Fast Tooling**: Uses [**uv**](https://github.com/astral-sh/uv) for lightning-fast package installation and virtual environment management.
-   **🐳 Containerized Development**: Comes with a pre-configured [**Dev Container**](https://containers.dev/) for a consistent and reproducible development environment in VS Code and other supported IDEs.
-   **✅ Code Quality**: Integrated **pre-commit** hooks with `ruff` for formatting and linting, `deptry` for dependency checking, and `basedpyright` for static type analysis.
-   **🚀 API-Ready**: Includes a basic **FastAPI** application structure.
-   **🧪 Testing Framework**: Configured with `pytest` for unit, integration, and component testing.

## Prerequisites

Before you begin, you need to install [**uv**](https://github.com/astral-sh/uv).

#### macOS & Linux

```bash
curl -LsSf [https://astral.sh/uv/install.sh](https://astral.sh/uv/install.sh) | sh
```

## Usage

To generate a new project from this template, run the following command. 
It uses uvx to temporarily install and run cookiecutter without polluting your global environment.

```bash
uvx cookiecutter https://github.com/FlorianBindereif/GenAI-Template --checkout cookiecutter_implementation
```

You will be prompted to enter the following information:

-   **project_name**: The human-readable name of your project (e.g., "My Awesome Chatbot").

-   **project_slug**: The directory name for your project (derived automatically from the project name).

-   **project_description**: A short description of your project.

-   **author_name**: Your name.

-   **project_email**: Your email address.

After you provide the details, Cookiecutter will generate the project structure in your current directory.

## Next Steps

Once your project is generated, navigate into the new directory and follow the instructions in its README.md file to set up your development environment and start coding!