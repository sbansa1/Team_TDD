import os


def test_development_config(test_app):
    """Tests the configuration of the Development"""
    test_app.config.from_object("app.config.DevelopmentConfig")
    assert test_app.config["SECRET_KEY"] == "my_precious"
    assert test_app.config.get("SQLALCHEMY_DATABASE_URI") == os.environ.get(
        "DATABASE_URL"
    )
    assert not test_app.config.get("TESTING")


def test_testing_config(test_app):
    """Tests the config of the tests"""

    test_app.config.from_object("app.config.TestingConfig")
    assert test_app.config["SECRET_KEY"] == "my_precious"
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get(
        "DATABASE_TEST_URL"
    )
    assert not test_app.config.get("DEVELOPMENT")


def test_production_config(test_app):
    """Tests the config of the Production"""

    test_app.config.from_object("app.config.ProductionConfig")
    assert test_app.config["SECRET_KEY"] == "my_precious"
    assert test_app.config.get("SQLALCHEMY_DATABASE_URI") == os.environ.get(
        "DATABASE_URL"
    )
    assert not test_app.config.get("TESTING")