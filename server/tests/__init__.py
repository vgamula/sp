from aiohttp.test_utils import AioHTTPTestCase, unittest_run_loop

from server.main import make_app


class BaseAsyncTestCase(AioHTTPTestCase):
    async def get_application(self):
        return make_app()


__all__ = ['unittest_run_loop', 'BaseAsyncTestCase']
