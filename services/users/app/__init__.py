# app/__init__.py

from flask import Flask
import os
from app.extensions import db
from app.api import api

from flask_cors import CORS

cors = CORS()

def create_app(script_info=None):
    app = Flask(__name__)
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)
    extensions(app)
    # used to register the app and db to the shell
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app


def extensions(app):

    db.init_app(app)
    cors.init_app(app,resources={r"*": {"origins": "*"}})
    api.init_app(app)
