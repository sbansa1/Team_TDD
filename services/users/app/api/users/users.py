from flask import Blueprint, request
from flask_restplus import Api, Resource, fields

from app.api.users.models import User
from app.api.users import user_namespace

# Handles Validation of JSON Payload we need a model
"""First the name of the Model class and its attributes"""
user_model = user_namespace.model(
    "User",
    {
        "id": fields.Integer(readOnly=True),
        "username": fields.String(required=True),
        "email": fields.String(required=True),
        "created_date": fields.DateTime,
    },
)


class UserList(Resource):
    @user_namespace.expect(user_model, validation=True)
    def post(self):
        """Api for User Registration"""
        post_data = request.get_json()
        user_identity = User.check_user_identity(identity=post_data.get("email"))
        response_object = {}
        if user_identity:
            response_object["message"] = "Sorry. That email already exists."
            return response_object, 400
        user = User(**post_data)
        user.save()
        response_object = {"message": "{0} was added!".format(post_data.get("email"))}
        return response_object, 201

    @user_namespace.marshal_with(user_model, as_list=True)
    def get(self):
        return User.query.all(), 200


class UserByID(Resource):
    @user_namespace.marshal_with(user_model)
    def get(self, user_id):
        user = User.query.filter(id == user_id).first()
        if not user:
            user_namespace.abort(404, f"User {user_id} does not exist")
        return user, 200


user_namespace.add_resource(UserByID, "/users/<int:user_id>")
user_namespace.add_resource(UserList, "/users")