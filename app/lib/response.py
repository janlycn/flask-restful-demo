from functools import wraps
from flask_restful.utils import unpack
from flask_restful import marshal, fields

class marshal_with(object):

    def __init__(self, fields=None, envelope=None):
        self.fields = fields
        self.envelope = envelope

    def __call__(self, f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            resp = f(*args, **kwargs)
            if(self.fields):
                if isinstance(resp, tuple):
                    data, code, headers = unpack(resp)
                    marshal_data = marshal(data, self.fields, self.envelope), code, headers
                else:
                    marshal_data = marshal(resp, self.fields, self.envelope)
            else:
                marshal_data = resp

            return {
                'success': True,
                'data': marshal_data,
            }
        return wrapper
