import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_create_task():
    response = client.post("/tasks", json={"title": "Test task"})
    assert response.status_code == 201
    assert response.json()["title"] == "Test task"
    assert response.json()["done"] == False
    assert response.json()["id"] is not None


def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_task_not_found():
    response = client.get("/tasks/99999")
    assert response.status_code == 404


def test_delete_task():
    # Create first
    create = client.post("/tasks", json={"title": "To delete"})
    task_id = create.json()["id"]
    # Then delete
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204
