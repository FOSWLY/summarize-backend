import asyncio
from hypercorn.asyncio import serve

from server import start, app

if __name__ == '__main__':
    config = asyncio.run(start())
    asyncio.run(serve(app, config))