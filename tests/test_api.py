from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_returns_score():
    response = client.post(
        "/predict", json={"transaction_id": "abc-123", "amount": 42.5}
    )
    assert response.status_code == 200
    body = response.json()
    assert body["transaction_id"] == "abc-123"
    assert "fraud_score" in body
