from aiohttp import web
from . import views


def error_pages():
    overrides = {
        403: views.handle_403,
        404: views.handle_404,
    }
    async def middleware(app, handler):
        async def middleware_handler(request):
            is_api_request = request.headers.get('API-Request')
            try:
                # import ipdb; ipdb.set_trace()
                response = await handler(request)
                override = overrides.get(response.status)
                if override is not None and not is_api_request:
                    return await override(request, response)
                else:
                    return response
            except web.HTTPException as ex:
                # import ipdb; ipdb.set_trace()
                override = overrides.get(ex.status)
                if override is not None and not is_api_request:
                    return await override(request)
                else:
                    raise ex
        return middleware_handler
    return middleware
