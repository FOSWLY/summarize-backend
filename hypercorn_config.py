import logging

from core.settings import get_settings

settings = get_settings()

accesslog = logging.getLogger('server')
errorlog = logging.getLogger('server')
loglevel = logging.getLevelName(settings.log_level)
bind = f'{settings.address}:{settings.port}'