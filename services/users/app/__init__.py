# app/__init__.py

from flask import Flask
import os
from services.app import db


def create_app(script_info=None):
    app = Flask(__name__)
    app_settings = os.getenv("APP_SETTINGS")
    app.config.from_object(app_settings)
    extensions(app)

    # Register Blueprint(Prevents Circular Imports)
    from services.users import ping_blueprint

    app.register_blueprint(ping_blueprint)
    from services.users import user_blueprint

    app.register_blueprint(user_blueprint)

    # used to register the app and db to the shell
    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}

    return app


def extensions(app):

    db.init_app(app)
