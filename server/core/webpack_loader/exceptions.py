from aiohttp.web import HTTPException


class WebpackException(HTTPException):
    def __init__(self, message):
        self.message = message
