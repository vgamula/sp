from aiohttp.web import Application

from .accounts import views as accounts_views
from .core import views as core_views


def make_routes(app: Application, directory_root: str):
    app.router.add_route('*', '/test', accounts_views.simple_test_view, name='view_for_test')
    app.router.add_route('*', '/signup', accounts_views.signup, name='signup')
    app.router.add_route('*', '/login', accounts_views.login)
    app.router.add_route('GET', '/app', core_views.application)

    if app.debug:  # In production mode it will be handled by web-server
        app.router.add_static('/static', directory_root)
