from flask import g, request
from lib import utils
from config import config


def init(app):
    @app.before_request
    def before_request():
        if 'Authorization' in request.headers:
            try:
                token = request.headers['Authorization'].split(None, 1)[1]
                g.user = utils.jwt_decode(token, config.TOKEN_SECRET)
            except Exception as e:
                pass
