import os

get = os.environ.get


ENVIRONMENT = get('ENV', 'production')  # development, testing
DATABASE_URL = get('DATABASE_URL', 'mongodb://localhost:27017')
SECRET_KEY = get('SECRET_KEY', '109la0m3tK8ErcOJGJNqkQTU-KdvEqw8oEnfKZ556LQ=')


try:
    from .local_settings import *
except ImportError:
    pass
