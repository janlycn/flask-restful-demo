import jwt
from hashlib import md5
from flask_restful import reqparse


def assign(obj, target_dict):
    for k, v in target_dict.items():
        if hasattr(obj, k):
            setattr(obj, k, v)


def gen_parser(target_class):
    parser = reqparse.RequestParser()
    filters = ['created_by_id', 'created_by', 'created_on',
               'updated_by_id', 'updated_by', 'updated_on', 'db', 'id']
    for key in target_class.__dict__.keys():
        if not key.startswith(('__', '_')) and not key.endswith('__') and key not in filters:
            parser.add_argument(key)
    return parser


def jwt_encode(payload, secret):
    return jwt.encode(payload, secret, algorithm='HS256').decode()


def jwt_decode(encoded, secret):
    return jwt.decode(encoded, secret, algorithms=['HS256'])


def md5_encode(text, salt):
    h = md5(salt.encode('utf-8'))
    h.update(text.encode('utf-8'))
    return h.hexdigest()
