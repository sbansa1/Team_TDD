import json
from app.api.models import User


def test_add_user(test_app, test_database):
    """Tests the users"""

    data = dict(username="Saurabh.bnss0123", email="Saurabh.bnss0123@gmail.com")

    client = test_app.test_client()
    response = client.post(
        "/users", data=json.dumps(data), content_type="application/json"
    )
    data = json.loads(response.data.decode())
    assert response.status_code == 201
    assert "Saurabh.bnss0123@gmail.com was added!" in data.get("message")


def test_user_already_exists(test_app, test_database):
    """Duplicate User"""

    user_data = dict(username="Saurabh", email="Saurabh.bnss0123@gmail.com")

    client = test_app.test_client()

    client.post("/users", data=user_data, content_type="application/json")

    response = client.post(
        "/users", data=json.dumps(user_data), content_type="application/json"
    )
    data = json.loads(response.data.decode())
    assert response.status_code == 400
    assert "Sorry. That email already exists." in data["message"]


""""
def test_single_user(test_app, test_database, add_user):
    user = add_user("saurabh", "Saurabh.bnss0123@gmail.com")
    client = test_app.test_client()
    respone = client.get("/users/{0}".format(user.id))
    data = json.loads(respone.data.decode())
    assert respone.status_code == 404
    assert "saurabh" in data.get("username")
    assert "Saurabh.bnss0123@gmail.com" in data.get("email")
"""

"""
def test_single_user_incorrect_id(test_app, test_database):

    client = test_app.test_client()
    resp = client.get("/users/{0}".format(int(999)))
    data = json.loads(resp.data.decode())
    assert resp.status_code == 404
    assert "User 999 does not exist" in data.get("message")
"""


def test_all_users(test_app, test_database, add_user):

    test_database.session.query(User).delete()
    add_user("madbala", "madhubala.gadodia@gmail.com")
    add_user("micheal", "micheal@he.com")
    client = test_app.test_client()
    resp = client.get("/users")
    data = json.loads(resp.data.decode())
    assert len(data) == 2
    assert "madhubala.gadodia@gmail.com" in data[0]["email"]
    assert "madbala" in data[0]["username"]
    assert "micheal" in data[1]["username"]
    assert "micheal@he.com" in data[1]["email"]