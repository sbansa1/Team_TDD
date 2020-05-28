from flask_restplus import Resource
from app.api.ping import ping_namespace

class Ping(Resource):
    """Restful Paths"""

    def get(self):
        """Get Endpoint for Get Request"""

        return {"status": "success", "message": "pong"}


ping_namespace.add_resource(Ping, "/ping")