import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    return TestClient(app)

# @pytest.fixture
# def response_minimal(client):
#     return client.post("/analyze", json={"text": "oweifheoih"})
