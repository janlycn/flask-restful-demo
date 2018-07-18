import datetime
from flask import g
from sqlalchemy import Column, Integer, VARCHAR, DateTime
from sqlalchemy.ext.declarative import declared_attr
from lib.utils import assign


class CommonModelMixin(object):

    created_on = Column(
        DateTime, default=datetime.datetime.now, nullable=False)
    updated_on = Column(DateTime, default=datetime.datetime.now,
                        onupdate=datetime.datetime.now, nullable=False)

    @declared_attr
    def created_by_id(self):
        return Column(Integer, default=self.get_user_id)

    @declared_attr
    def created_by(self):
        return Column(VARCHAR(80), default=self.get_user_name)

    @declared_attr
    def updated_by_id(self):
        return Column(Integer, default=self.get_user_id, onupdate=self.get_user_id)

    @declared_attr
    def updated_by(self):
        return Column(VARCHAR(80), default=self.get_user_name, onupdate=self.get_user_name)

    @classmethod
    def get_user_id(cls):
        try:
            return g.user['id']
        except Exception as e:
            return None

    @classmethod
    def get_user_name(cls):
        try:
            return g.user['nickname']
        except Exception as e:
            return None

    @classmethod
    def add(cls, model):
        model.db.session.add(model)
        model.db.session.commit()
        return model.id

    @classmethod
    def delete(cls, pk):
        model = cls.query.get(pk)
        model.db.session.delete(model)
        model.db.session.commit()
        return model.id

    @classmethod
    def update(cls, pk, **args):
        model = cls.query.get(pk)
        assign(model, args)
        model.db.session.commit()
        return model
