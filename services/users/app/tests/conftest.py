import pytest

from services.app import create_app
from services.users import User
from services.app import db


@pytest.fixture(scope="module")
def test_app():
    app = create_app()
    app.config.from_object("app.config.TestingConfig")
    with app.app_context():
        yield app  # this is where the testing begins


@pytest.fixture(scope="module")
def test_database():
    db.create_all()
    yield db  # this is where the fixture becomes available.
    db.session.remove()
    db.drop_all()  # Tear down after the fixture is done


@pytest.fixture(scope="function")
def add_user():
    def _add_user(username, email):
        """Fixture for User"""
        user = User(username=username, email=email)
        user.save()
        return user

    return _add_user
