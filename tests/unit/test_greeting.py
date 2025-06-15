from unittest.mock import MagicMock

import pytest
from pytest_mock import MockerFixture

from app.api.schemas.greetings import Tone
from app.core.greetings_service import GreetingsService


@pytest.fixture
def mock_template(mocker: MockerFixture) -> MagicMock:
    """
    Mocked Jinja2 template object.
    """
    return mocker.MagicMock()


@pytest.fixture
def mock_jinja_env(mocker: MockerFixture, mock_template: MagicMock) -> MagicMock:
    """
    Fixture that provides a mocked Jinja2 environment that returns our mock_template.
    """
    mock_env = mocker.MagicMock()
    mock_env.get_template.return_value = mock_template
    return mock_env


@pytest.mark.parametrize(
    ("tone", "username", "expected_output"),
    [
        (Tone.FRIENDLY, "Alice", "Hey Alice! It's so great to see you. Hope you're having a wonderful day! 😄"),
        (Tone.ANGRY, "Bob", "What do you want, Bob?! Don't waste my time. 😡"),
        (Tone.NEUTRAL, "Charlie", "Hello, Charlie."),
    ],
)
def test_generate_greeting(
    mock_jinja_env: MagicMock,
    mock_template: MagicMock,
    tone: Tone,
    username: str,
    expected_output: str,
) -> None:
    """
    Tests the generate_greeting method with various tones and usernames.
    """
    # Arrange: Set the return value of the mocked render method to our expected output.
    mock_template.render.return_value = expected_output
    service = GreetingsService(jinja_env=mock_jinja_env)

    # Act: Generate greeting
    result: str = service.generate_greeting(tone=tone, user_name=username)

    # Assert: Verify that the templating functionality works as expected
    mock_jinja_env.get_template.assert_called_once_with("greeting_template.j2")
    mock_template.render.assert_called_once_with(
        tone=tone.value,
        username=username,
    )
    # Assert: Verify that the method returns the correctly rendered string.
    assert result == expected_output
