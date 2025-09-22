from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Welcome to Todo API"}

def test_create_todo():
    todo_data = {"id": 1, "name": "Shopping", "des": "Buy groceries"}
    response = client.post("/todos", json=todo_data)
    assert response.status_code == 200
    assert response.json() == todo_data

def test_get_todo():
    response = client.get("/todos/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "name": "Shopping", "des": "Buy groceries"}

def test_update_todo():
    updated_data = {"id": 1, "name": "Shopping Updated", "des": "Buy groceries updated"}
    response = client.put("/todos/1", json=updated_data)
    assert response.status_code == 200
    assert response.json() == updated_data

def test_delete_todo():
    response = client.delete("/todos/1")
    assert response.status_code == 200
    assert response.json() == {"msg": "Todo 1 deleted"}
    response = client.get("/todos/1")