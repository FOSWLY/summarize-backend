import re
import os
import json
import toml
from dotenv import load_dotenv

JSON_FILE = re.compile(".*.json")

def load_cfg():
    """Загружает конфиг файл"""
    cfg = toml.load('./config/config.cfg')
    return cfg

def load_json(file: str):
    """Загружает выбранный json файл из папки с конфигами

    Args:
        file (str): Файл, который нужно загрузить

    Returns:
        json: Загруженный json файл
    """
    if JSON_FILE.fullmatch(file):
        with open('./config/' + file, 'r') as f:
            data = json.load(f)
    else:
        data = False
    return data

def load_env():
    """Загружает .env файл"""
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')

    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
        return True
    return False