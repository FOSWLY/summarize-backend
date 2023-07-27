import os

from config.load import load_env

load_env()

PORT = os.environ.get('PORT') or 3312
API_KEY = os.environ.get('API_KEY') or ''
YANDEX_COOKIE = os.environ.get('YANDEX_COOKIE') or ''