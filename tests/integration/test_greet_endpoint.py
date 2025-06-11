from fastapi import status

def test_greet_endpoint_integration(test_client):
    # Arrange: Define the request payload
    request_payload = {"username": "Alice", "tone": "friendly"}

    # Act: Make a POST request to the endpoint using the TestClient
    response = test_client.post("/api/v1/greet", json=request_payload)

    # Assert: Check the HTTP status and the content of the response
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"greeting": "Hey Alice! It's so great to see you. Hope you're having a wonderful day! 😄"}