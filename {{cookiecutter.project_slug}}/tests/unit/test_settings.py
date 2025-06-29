from pathlib import Path

import pytest
from pydantic import ValidationError

from app.config import Settings


def test_settings_override_with_env_vars(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Tests that settings can be overridden with environment variables.
    """
    # Arrange: Set custom environment variables
    monkeypatch.setenv("APP_NAME", "My Awesome Test App")
    monkeypatch.setenv("LOG_LEVEL", "DEBUG")

    # Act: initialize Instance of setting object
    settings = Settings()

    # Assert: verify expected behavior
    assert settings.APP_NAME == "My Awesome Test App"
    assert settings.LOG_LEVEL == "DEBUG"


def test_settings_loading_from_env_file(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Tests that settings are correctly loaded from a .env file.
    """

    # Arrange: Set custom environment dotfile
    env_content = "OPENAI_API_KEY='test_api_key_from_dotenv'"
    env_file = tmp_path / ".env"
    env_file.write_text(env_content)
    monkeypatch.setitem(Settings.model_config, "env_file", env_file)

    # Act: initialize Instance of setting object
    settings = Settings()

    # Assert: verify expected behavior
    assert settings.OPENAI_API_KEY == "test_api_key_from_dotenv"
    assert settings.LOG_LEVEL == "INFO"


def test_settings_invalid_base_url(monkeypatch: pytest.MonkeyPatch) -> None:
    """
    Tests that settings can be overridden with environment variables.
    """

    # Arrange: Set custom environment dotfile
    invalid_url = "https//api.openai.com/v1"
    monkeypatch.setenv("OPENAI_BASE_URL", invalid_url)

    # Act / Assert: verify expected behavior
    with pytest.raises(ValidationError):
        Settings()
