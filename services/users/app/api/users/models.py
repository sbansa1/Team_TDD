from sqlalchemy import or_
from app import db
from app.utils.db_resource import ResourceMixin


class User(db.Model, ResourceMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    @classmethod
    def check_user_identity(cls, identity):
        """Checks the User Identity"""
        return User.query.filter(
            or_(User.email == identity, User.username == identity)
        ).first()
