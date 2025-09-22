from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_add_numbers():
    response = client.get("/add/3/5")
    assert response.status_code == 200
    assert response.json() == {"result": 8}
