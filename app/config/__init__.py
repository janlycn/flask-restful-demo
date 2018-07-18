import os
from . import development, production

config = {
    'development': development,
    'production': production,
}[os.getenv('FLASK_ENV') or 'production']
