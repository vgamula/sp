from server.tests import BaseAsyncTestCase, unittest_run_loop


class AccountViewsTestCase(BaseAsyncTestCase):
    @unittest_run_loop
    async def test_simple_test_view(self):
        resp = await self.client.get('/test')
        assert resp.status == 200
        assert await resp.text() == 'Test response'

    @unittest_run_loop
    async def test_simple_test_view_1(self):
        resp = await self.client.get('/test')
        assert resp.status == 200
        assert await resp.text() == 'Test response'

    @unittest_run_loop
    async def test_simple_test_view_2(self):
        resp = await self.client.get('/test')
        assert resp.status == 200
        assert await resp.text() == 'Test response'

    @unittest_run_loop
    async def test_simple_test_view_3(self):
        resp = await self.client.get('/test')
        assert resp.status == 200
        assert await resp.text() == 'Test response'
