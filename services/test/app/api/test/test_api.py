from app.api.test import test_namespace
from flask_restplus import Resource


class TestAPI(Resource):

    def get(self):
        return {"message": "Test Api"},200


test_namespace.add_resource(TestAPI,"/test")