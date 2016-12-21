import os
from pathlib import Path

get = os.environ.get

DEBUG = False
ENVIRONMENT = get('ENV', 'production')  # development, testing
DATABASE_URL = get('DATABASE_URL', 'mongodb://localhost:27017')
SECRET_KEY = get('SECRET_KEY', '109la0m3tK8ErcOJGJNqkQTU-KdvEqw8oEnfKZ556LQ=')

try:
    from .local_settings import *
except ImportError:
    pass

WEBPACK_CONFIG = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'STATS_FILE': str(Path(__file__).parent.parent / 'static' / 'dist' / 'stats.json')
    },
    'VENDOR': {
        'CACHE': not DEBUG,
        'STATS_FILE': str(Path(__file__).parent.parent / 'static' / 'dist' / 'vendor-stats.json')
    }
}
