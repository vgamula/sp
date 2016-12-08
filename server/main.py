import asyncio
import pathlib

import uvloop
from aiohttp import web

from server import settings
from server.routes import make_routes


PROJECT_ROOT = pathlib.Path(__file__).parent.parent
SERVER_ROOT = PROJECT_ROOT / 'server'


async def handle(request: web.Request):
    return web.Response(text='Hello, World!')


def make_app(loop: asyncio.AbstractEventLoop) -> web.Application:
    app = web.Application(loop=loop)
    make_routes(app, str(SERVER_ROOT / 'static'))
    app.router.add_get('/', handle)
    return app


if __name__ == '__main__':
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = asyncio.get_event_loop()
    app = make_app(loop=loop)
    web.run_app(app, port=8888)
