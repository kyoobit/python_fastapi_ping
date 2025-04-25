import logging

from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_handlers_ping_get(caplog):
    caplog.log_level = logging.DEBUG
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.headers.get("x-powered-by") == "^c+^p"
    assert response.content == b"pong"


def test_handlers_ping_post(caplog):
    caplog.log_level = logging.DEBUG
    response = client.post("/ping", json={"message": "hello"})
    assert response.status_code == 204
    assert response.headers.get("x-powered-by") == "^c+^p"


def test_handlers_ping_post_malformed(caplog):
    caplog.log_level = logging.DEBUG
    response = client.post("/ping", content="{message: malformed}")
    assert response.status_code == 204
    assert response.headers.get("x-powered-by") == "^c+^p"
