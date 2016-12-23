from aiohttp import web
from aiohttp_jinja2 import template

from .forms import RegistrationForm


@template('accounts/signup.jinja2')
async def signup(request: web.Request):
    data = await request.post()
    form = RegistrationForm(data)
    form_valid = await form.is_valid()
    import ipdb; ipdb.set_trace()
    return {'form': form}


@template('accounts/login.jinja2')
def login(request: web.Request):
    return {
        'a': '1',
        'b': '2'
    }
