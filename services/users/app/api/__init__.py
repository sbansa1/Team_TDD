from flask_restplus import Api

api = Api(version='1.0',description="All the endpoints for the Flask TDD Api",title="TDD Api", doc="/doc")


from app.api.ping import ping_namespace
api.add_namespace(ping_namespace)
from app.api.users import user_namespace
api.add_namespace(user_namespace)


