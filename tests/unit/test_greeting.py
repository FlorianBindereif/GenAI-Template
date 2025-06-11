from unittest.mock import MagicMock
import pytest

from app.api.schemas.greetings import Tone
from app.core.greetings_service import GreetingsService


@pytest.fixture
def mock_jinja_env(mocker):
    """
    Fixture to create a mock Jinja2 environment and template.
    This prevents actual file system access during unit tests.
    """
    mock_env = MagicMock()
    mock_template = MagicMock()

    # Configure the mock template's render method to return a predictable string
    mock_template.render.return_value = "Hey Alice! It's so great to see you. Hope you're having a wonderful day! 😄"

    # Configure the mock environment's get_template method to return our mock template
    mock_env.get_template.return_value = mock_template

    return mock_env

def test_generate_greeting(mock_jinja_env):
    """
    Tests that the generate_greeting method correctly calls the template
    rendering with the right context.
    """
    # Arrange: Initialize the service with the mocked environment
    service = GreetingsService(jinja_env=mock_jinja_env)
    test_username = "Alice"
    test_tone = Tone.FRIENDLY

    # Act: Call the method being tested
    result = service.generate_greeting(tone=test_tone, user_name=test_username)

    # Assert: Verify that the interactions with the mock were as expected
    service.jinja_env.get_template.assert_called_once_with("greeting_template.j2")
    service.jinja_env.get_template.return_value.render.assert_called_once_with(
        tone=test_tone.value,
        username=test_username
    )
    assert result == "Hey Alice! It's so great to see you. Hope you're having a wonderful day! 😄"