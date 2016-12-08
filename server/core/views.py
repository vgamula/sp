from aiohttp import web
from aiohttp_jinja2 import template


@template('core/403.jinja2')
async def handle_403(request: web.Request):
    return {}


@template('core/404.jinja2')
async def handle_404(request: web.Request):
    return {}

@template('app.jinja2')
async def application(request: web.Request):
    return {}
