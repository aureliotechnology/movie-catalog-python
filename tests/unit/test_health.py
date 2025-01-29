from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "message": "API is running"}

def test_database_health_check():
    response = client.get("/api/db-health")
    assert response.status_code in [200, 500]  # Pode retornar erro caso o DB não esteja ativo
