from flask import Flask
from app.api import api


def create_app(script_info=None):
    """Creates an app instance"""

    app = Flask(__name__)
    api.init_app(app)
    return app