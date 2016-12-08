import asyncio
import pathlib

import uvloop
import jinja2
from aiohttp import web
from aiohttp_session import setup as session_setup
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from aiohttp_jinja2 import setup as jinja2_setup
from motor.motor_asyncio import AsyncIOMotorClient

from . import settings
from .routes import make_routes

PROJECT_ROOT = pathlib.Path(__file__).parent.parent
SERVER_ROOT = PROJECT_ROOT / 'server'


async def handle(request: web.Request):
    return web.Response(text='Hello, World!')


def make_app(loop: asyncio.AbstractEventLoop) -> web.Application:
    middlewares = []
    app = web.Application(loop=loop, middlewares=middlewares, debug=settings.DEBUG)

    # Session setup
    session_setup(app, EncryptedCookieStorage(settings.SECRET_KEY))

    # DB setup
    client = AsyncIOMotorClient(settings.DATABASE_URL)
    app['db'] = client.sp

    # Templates setup
    jinja2_setup(app, loader=jinja2.FileSystemLoader(str(SERVER_ROOT / 'templates')))

    make_routes(app, str(SERVER_ROOT / 'static'))
    app.router.add_get('/', handle)
    return app


if __name__ == '__main__':
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = asyncio.get_event_loop()
    app = make_app(loop=loop)
    web.run_app(app, port=8888)
