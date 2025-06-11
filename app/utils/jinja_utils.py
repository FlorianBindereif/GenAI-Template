from jinja2 import Environment, FileSystemLoader
from app.config import PROMPT_DIR


def get_jinja_env() -> Environment:
    """
    Creates and returns a Jinja2 environment.
    """
    return Environment(
        loader=FileSystemLoader(PROMPT_DIR),
        trim_blocks=True,
        lstrip_blocks=True
    )