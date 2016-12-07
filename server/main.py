import asyncio
import uvloop
from aiohttp import web


async def handle(request: web.Request):
    return web.Response(text='Hello, World!')


def make_app(loop: asyncio.AbstractEventLoop) -> web.Application:
    app = web.Application(loop=loop)
    app.router.add_get('/', handle)
    return app


if __name__ == '__main__':
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = asyncio.get_event_loop()
    app = make_app(loop=loop)
    web.run_app(app, port=8888)
