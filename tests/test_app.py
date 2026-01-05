import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "<!DOCTYPE html>" in response.text
    assert "<html" in response.text


def test_invalid_route():
    response = client.get("/invalid")
    assert response.status_code == 404