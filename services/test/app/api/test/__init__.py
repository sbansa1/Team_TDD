from flask_restplus import Namespace

test_namespace = Namespace("test")

from app.api.test import test_api