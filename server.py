from hypercorn.config import Config

from core.app import app
from core.logger import init_logging
from routes import api_router


async def start():
    app.include_router(api_router)
    config = Config().from_pyfile('hypercorn_config.py')
    init_logging()
    return config, app