import os

from config.load import load_env

load_env()

PORT = os.environ.get('PORT', 3312)
API_KEY = os.environ.get('API_KEY', '')
YANDEX_COOKIE = os.environ.get('YANDEX_COOKIE', '')