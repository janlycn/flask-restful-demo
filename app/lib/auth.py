from functools import wraps
from flask import g
from flask_restful import abort


def authenticate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not getattr(func, 'authenticated', True):
            return func(*args, **kwargs)

        acct = basic_authentication()

        if acct:
            return func(*args, **kwargs)

        abort(401)
    return wrapper


def basic_authentication():
    return g.user and g.user['id']
