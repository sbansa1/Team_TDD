import json


def test_ping(test_app):
    """Functional Tests for checking the response"""
    test_client = test_app.test_client()
    resp = test_client.get("ping")
    assert resp.status_code == 200
    data = json.loads(resp.data.decode())
    assert "pong" in data["message"]
    assert "success" in data["status"]
