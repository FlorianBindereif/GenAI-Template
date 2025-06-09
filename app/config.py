import pathlib

from pydantic_settings import BaseSettings, SettingsConfigDict

# Project root directory
ROOT_DIR = pathlib.Path(__file__).resolve().parent.parent

# Project prompt directory
PROMPT_DIR: pathlib.Path = ROOT_DIR / "app" / "prompts"


class Settings(BaseSettings):
    """Application settings."""

    # --- Logging ---
    LOG_LEVEL: str = "INFO"

    # --- AI Model Core Settings ---
    OPENAI_API_KEY: str | None = None
    OPENAI_BASE_URL: str = "https://api.openai.com/v1"

    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        extra="ignore",
    )


settings = Settings()
