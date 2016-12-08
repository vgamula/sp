from aiohttp.web import Application

from server.accounts import views as accounts_views


def make_routes(app: Application, directory_root: str):
    app.router.add_route('*', '/signup', accounts_views.signup)
    app.router.add_route('*', '/login', accounts_views.login)
    app.router.add_static('/static', directory_root)
