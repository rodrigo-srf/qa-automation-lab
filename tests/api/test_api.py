from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_existing_user_contract():
    response = client.get("/api/users/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Rodrigo", "role": "qa-devops"}


def test_missing_user_returns_404():
    response = client.get("/api/users/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


def test_valid_login():
    response = client.post("/api/login", json={"username": "tester", "password": "qa1234"})
    assert response.status_code == 200
    assert response.json()["authenticated"] is True
    assert response.json()["token"]


def test_invalid_login():
    response = client.post("/api/login", json={"username": "tester", "password": "wrong"})
    assert response.status_code == 401


def test_login_schema_validation():
    response = client.post("/api/login", json={"username": "x", "password": "1"})
    assert response.status_code == 422
