# tests/test_main.py
import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "app"))

import main
app = main.app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_home_returns_html(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.content_type.startswith("text/html")
    assert b"My App" in res.data


def test_api_home(client):
    res = client.get("/api")
    assert res.status_code == 200
    assert "message" in res.json


def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json["status"] == "ok"