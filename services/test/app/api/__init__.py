from flask_restplus import Api

api = Api(version='1.0',description="All the endpoints for the Flask TDD Api",title="TDD Api", doc="/doc")

from app.api.test import test_namespace
api.add_namespace(test_namespace)