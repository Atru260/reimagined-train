
from schemas import AnalysisResponse

def test_analyze_schema(client):

    response_minimal = client.post("/analyze", json={"text": "oweifheoih"})

    assert response_minimal.status_code == 200
    response = response_minimal.json()

    assert AnalysisResponse.model_validate(response)



