import os
from pathlib import Path

get = os.environ.get


DEBUG = True
ENVIRONMENT = get('ENV', 'production')  # development, testing
DATABASE_URL = get('DATABASE_URL', 'mongodb://localhost:27017')
SECRET_KEY = get('SECRET_KEY', '109la0m3tK8ErcOJGJNqkQTU-KdvEqw8oEnfKZ556LQ=')

WEBPACK_CONFIG = {
    'DEFAULT': {
        'CACHE': False,
        'STATS_FILE': str(Path(__file__).parent.parent / 'static' / 'dist' / 'stats.json')
    },
    'VENDOR': {
        'CACHE': False,
        'STATS_FILE': str(Path(__file__).parent.parent / 'static' / 'dist' / 'vendor-stats.json')
    }
}


try:
    from .local_settings import *
except ImportError:
    pass

if not DEBUG:
    WEBPACK_CONFIG = {
        'DEFAULT': {
            'CACHE': True,
            'STATS_FILE': str(Path(__file__).parent.parent / 'static' / 'dist' / 'stats.json')
        },
        'VENDOR': {
            'CACHE': True,
            'STATS_FILE': str(Path(__file__).parent.parent / 'static' / 'dist' / 'vendor-stats.json')
        }
    }
