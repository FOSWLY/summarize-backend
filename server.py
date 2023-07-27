from core.app import app
from hypercorn.config import Config
from core.logger.main import init_logging
from routes import api_router


app.include_router(api_router)

async def start():
    config = Config().from_pyfile('config/hypercorn_config.py')
    init_logging()
    return config