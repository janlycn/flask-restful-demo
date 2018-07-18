from flask import Blueprint
from flask_restful import Api, url_for
from config import config
from . import resource

# 蓝图
api_bp = Blueprint('user', __name__)
# api
api = Api(api_bp)
# 路由
api.add_resource(resource.UserApi, '/users/<int:pk>')
api.add_resource(resource.UserListApi, '/users')
api.add_resource(resource.AuthApi, '/auth')


def init(app):
    '''初始化蓝图
    '''
    app.register_blueprint(api_bp, url_prefix=config.URL_PREFIX)
