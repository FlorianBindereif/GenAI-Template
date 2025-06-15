import pytest
from fastapi.testclient import TestClient

from app.api.main import app


@pytest.fixture(scope="module")
def test_client() -> TestClient:
    """
    Provides a FastAPI TestClient for making requests to the application during tests.
    """
    return TestClient(app)
