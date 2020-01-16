from flask import Blueprint
from flask_restplus import Api

ping_blueprint = Blueprint("ping_blueprint", __name__)
api_ping_blueprint = Api(ping_blueprint)

from app.api import ping
