from aiohttp import web
from aiohttp_jinja2 import template


@template('accounts/signup.jinja2')
def signup(request: web.Request):
    return {
        'a': '1',
        'b': '2'
    }


@template('accounts/login.jinja2')
def login(request: web.Request):
    return {
        'a': '1',
        'b': '2'
    }
