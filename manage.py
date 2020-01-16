#manage.py
#It is your tool for executing many Django-specific tasks
# -- starting a new app within a project,
# running the development server, running your tests...

from flask.cli import FlaskGroup
from app import create_app
from app.api.models import User
from app.extensions import db

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command('seed_db')
def seed_db():
    db.session.add(User( username='Saurabh', email="Saurabh.bnss0123@gmail.com" ) )
    db.session.add(User( username='Madubala', email="Madhubala@gmail.com" ) )
    db.session.commit()


if __name__=='__main__':
    cli()