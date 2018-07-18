from flask import g
from flask_restful import Resource, fields
from lib.response import marshal_with
from lib.utils import gen_parser, jwt_encode, md5_encode
from lib.auth import authenticate
from config import config
from .models import User


user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'nickname': fields.String,
}

parser = gen_parser(User)


class UserApi(Resource):
    method_decorators = [authenticate]

    @marshal_with(user_fields)
    def get(self, pk):
        return User.query.get(pk)

    @marshal_with()
    def delete(self, pk):
        User.delete(pk)
        return pk

    @marshal_with(user_fields)
    def put(self, pk):
        parser.remove_argument('password')
        return User.update(pk, **parser.parse_args())


class UserListApi(Resource):
    method_decorators = [authenticate]

    @marshal_with(user_fields)
    def get(self):
        return User.query.all()

    @marshal_with()
    def post(self):
        user = User(**parser.parse_args())
        user.password = md5_encode(user.password, config.PASSWORD_SALT)
        return User.add(user)


class AuthApi(Resource):
    @marshal_with()
    def get(self):
        user = User.query.get(g.user['id'])
        result = {}
        if user:
            result['userid'] = user.id
            result['name'] = user.nickname
            result['avatar'] = 'https://gw.alipayobjects.com/zos/rmsportal/BiazfanxmamNRoxxVxka.png'
            result['notifyCount'] = 12
        return result

    @marshal_with()
    def post(self):
        args = parser.parse_args()
        user = User.query.filter_by(username=args.username).first()
        result = {
            'type': 'account'
        }
        if not user:
            result['status'] = 'error'

        md5_password = md5_encode(args.password, config.PASSWORD_SALT)
        if user.password != md5_password:
            result['status'] = 'error'

        token_user = {
            'id': user.id,
            'username': user.username,
            'nickname': user.nickname,
        }

        result['currentAuthority'] = 'admin'
        result['token'] = jwt_encode(token_user, config.TOKEN_SECRET)
        result['status'] = 'ok'

        return result
