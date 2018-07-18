from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init(app):
    db.init_app(app)
