from modules import db
from lib.mixins import CommonModelMixin


class User(CommonModelMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=True, nullable=False)
    nickname = db.Column(db.String(80), unique=True, nullable=False)

    # 提供给增删改使用
    db = db
