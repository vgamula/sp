from aiohttp.web_exceptions import HTTPNotFound, HTTPForbidden


class NotFoundException(HTTPNotFound):
    pass


class Forbidden(HTTPForbidden):
    pass
