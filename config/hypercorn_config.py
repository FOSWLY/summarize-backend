import logging

from config.load import load_cfg
from settings import PORT

logs = load_cfg()['logging']


accesslog = logging.getLogger('server')
errorlog = logging.getLogger('server')
loglevel = logging.getLevelName(logs['level'])
bind = f'0.0.0.0:{PORT}'