import pytest
from fastapi import status
from fastapi.testclient import TestClient

from app.config import settings
from app.models.greetings import Tone


@pytest.mark.parametrize(
    ("username", "tone", "expected_greeting"),
    [
        ("Alice", Tone.FRIENDLY, "Hey Alice! It's so great to see you. Hope you're having a wonderful day! 😄"),
        ("Bob", Tone.ANGRY, "What do you want, Bob?! Don't waste my time. 😡"),
        ("Charlie", Tone.NEUTRAL, "Hello, Charlie."),
    ],
)
def test_greet_endpoint(
    test_client: TestClient,
    username: str,
    tone: Tone,
    expected_greeting: str,
) -> None:
    """
    Tests the /greet endpoint for all tones via the TestClient.
    """
    # Arrange: Define the request payload from the parameterized inputs
    request_payload = {"username": username, "tone": tone.value}

    # Act: Make a POST request to the endpoint
    endpoint_url = f"{settings.API_PREFIX}/greet"
    response = test_client.post(endpoint_url, json=request_payload)

    # Assert: Check the HTTP status and the content of the response
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"greeting": expected_greeting}
