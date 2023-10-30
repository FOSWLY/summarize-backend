import logging

from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # - server section -
    port: int = 3312
    address: str = '0.0.0.0'

    # - yandex section -
    api_key: str = '' # ! DO NOT CHANGE THESE FIELDS. You need to change the values in .env
    yandex_cookie: str = '' # ! DO NOT CHANGE THESE FIELDS. You need to change the values in .env

    # - logging section -
    log_level: int = logging.INFO # level of logs (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    log_save: bool = True # save logs to file
    log_rich_formatter: bool = True # format logs with rich lib

    # - app section -
    app_name: str = '[FOSWLY] Summarize'
    app_desc: str = '[FOSWLY] Summarize is Free Yandex Summarize API without any authorization or restrictions.'
    app_version: str = '1.2.0'
    app_license: str = 'MIT'
    app_developer_url: str = 'https://github.com/FOSWLY/summarize-backend'
    app_developer_email: str = 'toil.contact@yandex.com'

    model_config = SettingsConfigDict(env_file='.env')

@lru_cache
def get_settings() -> Settings:
    return Settings()