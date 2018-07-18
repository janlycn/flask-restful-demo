import click
from .extensions import db
from modules.user.models import User


def init(app):
    @app.cli.command()
    def initdb():
        db.drop_all()
        db.create_all()
