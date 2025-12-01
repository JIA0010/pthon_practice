import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_greet_with_name():
    response = client.get("/greet?name=John")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, John!"}

def test_greet_without_name():
    response = client.get("/greet")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, anonymous!"}

def test_create_todo():
    todo = {"title": "Buy milk", "done": False}
    response = client.post("/todos", json=todo)
    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "Buy milk", "done": False}