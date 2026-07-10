
def test_empty(client):
    assert client.post("/analyze", json={}).status_code == 422