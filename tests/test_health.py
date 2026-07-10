
def test_health(client):
    health = client.get("/health").json()
    assert health["status"] == "ok"