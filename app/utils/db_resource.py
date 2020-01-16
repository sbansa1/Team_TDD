from app.extensions import db


class ResourceMixin(object):
    def save(self):
        """Generic Method for saving an object to the db"""
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.remove(self)
        return db.session.commit()

    def update(self):
        """Generic Method for Updating the object"""
        db.session.update(self)
        db.session.commit()
        return self
