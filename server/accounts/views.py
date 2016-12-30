from aiohttp import web
from aiohttp_jinja2 import template

from .forms import RegistrationForm


@template('accounts/signup.jinja2')
async def signup(request: web.Request):
    if request.method == 'POST':
        data = await request.post()
        form = RegistrationForm(data, db=request.app['db'])
        if await form.is_valid():
            user = await form.save()
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
