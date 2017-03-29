from aiohttp import web
from aiohttp_jinja2 import template
from aiohttp_session import get_session

from .forms import RegistrationForm
from . import auth


@template('accounts/signup.jinja2')
async def signup(request: web.Request):
    if request.method == 'POST':
        data = await request.post()
        form = RegistrationForm(data, db=request.app['db'])
        if await form.is_valid():
            user = await form.save()
            session = await get_session(request)
            auth.login_user(session, user['_id'])
            return {'form': form, 'message': 'User has been registered'}
    else:
        form = RegistrationForm()
    return {'form': form}


@template('accounts/login.jinja2')
def login(request: web.Request):
    return {
        'a': '1',
        'b': '2'
    }


async def logout(request: web.Request):
    session = await get_session(request)
    auth.logout_user(session)
    return web.HTTPFound('/')


async def simple_test_view(request: web.Request):
    return web.Response(body='Test response')
