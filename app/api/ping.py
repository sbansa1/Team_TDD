from flask_restplus import Resource

from app.api import api_ping_blueprint


class Ping(Resource):
    """Restful Paths"""

    def get(self):
        """Get Endpoint for Get Request"""

        return {"status": "success", "message": "pong"}


api_ping_blueprint.add_resource(Ping, "/ping")
