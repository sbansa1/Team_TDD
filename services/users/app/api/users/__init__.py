from flask_restplus import Namespace

user_namespace = Namespace(name="user")
from app.api.users import users