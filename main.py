import asyncio
from hypercorn.asyncio import serve

from server import start

if __name__ == '__main__':
    config, app = asyncio.run(start())
    asyncio.run(serve(app, config)) # type: ignore