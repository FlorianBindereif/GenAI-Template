# 🚀 Python Generative AI Starter Template

A standardized template for bootstrapping Generative AI applications. 
This template provides a solid foundation with a pre-configured development environment, modern tooling, and a logical project structure.

## ✨ Features

This template is packed with modern tools to ensure a smooth, efficient, and high-quality development experience.

  * **📦 Development Environment**:

      * [**Dev Containers**](https://containers.dev/): Fully configured, consistent, and reproducible development environment using Docker.
      * [**uv**](https://github.com/astral-sh/uv): Extremely fast Python package installer and resolver. Used for dependency management and running tasks, it's a significant speed upgrade over `pip`.

  * **✅ Code Quality & Automation**:

      * [**Pre-commit Hooks**](https://pre-commit.com/): Framework for managing and maintaining pre-commit hooks. Ensures code quality checks are run automatically before any code is checked in.
      * [**Ruff**](https://docs.astral.sh/ruff/): Extremely fast Python linter and code formatter. Replaces `black`, `isort`, `flake8`, and many other tools.
      * [**basedpyright**](https://github.com/detachhead/basedpyright): Powerful and performant static type checker based on Microsoft's `pyright`.
      * [**deptry**](https://deptry.com/): Command-line utility to check for obsolete, missing, and unused dependencies.
      * [**Conventional Commits**](https://github.com/compilerla/conventional-pre-commit): Enforces a standardized commit message format to create an explicit and readable commit history.

  * **🔧 Application & API**:

      * [**FastAPI**](https://fastapi.tiangolo.com/): Modern, high-performance web framework for building APIs with Python.
      * [**Pydantic**](https://www.google.com/search?q=https://docs.pydantic.dev/): Data validation and settings management using Python type annotations.
      * [**Jinja2**](https://jinja.palletsprojects.com/): Modern and designer-friendly templating engine, perfect for managing and versioning prompts.

  * **🧪 Testing**:

      * [**Pytest**](https://docs.pytest.org/): Mature, full-featured Python testing tool that makes it easy to write simple, scalable tests.

-----

## 📂 Project Structure

The project follows a standard layout for scalability and maintainability.

```
└── ./
    ├── .devcontainer/     # Dev Container configuration (Dockerfile, etc.)
    ├── app/               # Main application source code
    │   ├── core/          # Core business logic (services)
    │   ├── models/        # Pydantic models (data structures)
    │   ├── prompts/       # Jinja2 prompt templates
    │   ├── routers/       # FastAPI endpoints (controllers)
    │   ├── utils/         # Utility functions
    │   ├── config.py      # Application settings
    │   └── main.py        # Application entrypoint
    ├── data/              # For storing data files (e.g., CSV, JSON)
    ├── notebooks/         # Jupyter notebooks for experimentation
    ├── tests/             # Tests
    │   ├── component/
    │   ├── integration/
    │   └── unit/
    ├── .gitignore
    ├── .pre-commit-config.yaml # Configuration for pre-commit hooks
    ├── pyproject.toml     # Project metadata and dependencies (for uv)
    └── uv.lock            # Pinned versions of all dependencies
```

-----

## 🏁 Getting Started

Follow these steps to bootstrap your new project. You can choose to use the pre-configured Dev Container or set it up locally.

### 🐳 Option 1: Using the Dev Container (Recommended)

This is the easiest way to get started, as it provides a consistent and fully-equipped environment out of the box.

**Prerequisites**:

  * [Docker Desktop](https://www.docker.com/products/docker-desktop/)

**Steps**:

1.  **Create from Template**: Click "**Use this template**" at the top of the repository page to create your new project.
2.  **Clone the Repository**: Clone your newly created repository to your local machine.
3.  **Open in Pycharm /VS Code**: Open the cloned repository folder in Pycharm / VS Code.
4.  **Reopen in Container**: Pycharm / VS Code will detect the `.devcontainer` and prompt you to reopen the project in a container. Click "**Reopen in Container**".

That's it\! The container will build, create a virtual environment, install all dependencies, and set up pre-commit hooks automatically.
-----

### 💻 Option 2: Running Locally

If you prefer not to use a Dev Container, you can set up the project locally.

**Prerequisites**:

  * **Python `~=3.13`**
  * **uv**: You'll need to install `uv`. You can do this with methods described in the [uv installation guide](https://docs.astral.sh/uv/getting-started/installation/).
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

**Steps**:

1.  **Create from Template & Clone**: Create your repository using the template and clone it locally.
2.  **Create Virtual Environment**: Navigate to the project's root directory, create a virtual environment.
    ```bash
    uv venv
    ```
3.  **Activate Virtual Environment**:
      * **macOS/Linux (bash/zsh)**: `source .venv/bin/activate`
4.  **Install Dependencies**: Sync your environment with the locked dependencies.
    ```bash
    uv sync
    ```
5.  **Install Pre-commit Hooks**: Set up the git hooks in your local repository.
    ```bash
    uv run pre-commit install --install-hooks
    ```

Your local environment is now set up and ready for development.

-----

## 🛠️ Development Workflow

### Dependency Management with `uv`

  * **To add a new dependency**:

    ```bash
    uv add <package-name>
    ```

    This will add it to your `pyproject.toml` and update `uv.lock`.

  * **To install all dependencies** from `pyproject.toml` (e.g., after pulling changes):

    ```bash
    uv sync
    ```

### Running Tests

  * To run the entire test suite (unit and component tests), use the following command:
    ```bash
    uv run pytest
    ```

### Code Quality and Formatting

The pre-commit hooks will automatically run `ruff` to format and lint your code on every commit. You can also run it manually:

  * **Format code**:
    ```bash
    uv run ruff format
    ```
  * **Lint and auto-fix code**:
    ```bash
    uv run ruff check
    ```

-----

## 🏃 Running the Example Application

This template includes a simple "Greeting" API to demonstrate its functionality.

1.  **Activate the Virtual Environment**: The dev container automatically uses the project's virtual environment, so you don't need to activate it manually.

2.  **Start the API Server**: Run the following command in the VS Code terminal:

    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```

3.  **Access the API**:

      * The dev container forwards port `8000`, so you can access the API from your local browser.
      * **Swagger UI (Interactive Docs)**: [http://localhost:8000/docs](https://www.google.com/search?q=http://localhost:8000/docs)
      * **Root Endpoint**: [http://localhost:8000/](https://www.google.com/search?q=http://localhost:8000/)

4.  **Send a Request**: Use `curl` or the Swagger UI to interact with the `/greet` endpoint.

    ```bash
    curl -X 'POST' \
      'http://localhost:8000/api/v1/greet' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
        "username": "developer",
        "tone": "friendly"
      }'
    ```

    You should receive a friendly greeting in response\! 🎉

    ```json
    {
      "greeting": "Hey developer! It's so great to see you. Hope you're having a wonderful day! 😄"
    }
    ```
-----

### Configuration

Application settings are managed in `app/config.py` using **Pydantic's `BaseSettings`**. You can create a `.env` file in the project root to override default settings (e.g., for API keys). A `.gitignore` entry is already in place to prevent committing this file.

```dotenv
# .env file
OPENAI_API_KEY="your-secret-key-here"
LOG_LEVEL="DEBUG"
```