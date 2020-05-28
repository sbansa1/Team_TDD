from flask_restplus import Namespace

ping_namespace = Namespace('ping',description="Testing...")

from app.api.ping import ping