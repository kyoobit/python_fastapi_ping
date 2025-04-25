import logging

from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_404_handler(caplog):
    """Test a non-existent route for default behavior"""
    caplog.log_level = logging.DEBUG
    response = client.get("/non-existent-route")
    assert response.status_code == 204
    assert response.headers.get("x-powered-by") == "^c+^p"
