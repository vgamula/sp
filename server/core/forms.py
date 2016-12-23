import asyncio

import trafaret


class TrafaretError(Exception):
    def __init__(self, errors, *args, **kwargs):
        self.errors = errors


class TrafaretForm:
    checker = None
    result = None
    errors = None

    def __init__(self, data):
        self.data = data
        errors = {}

    async def extra_validation(self):
        pass

    async def is_valid(self):
        try:
            self.result = self.checker.check(self.data)
            await self.extra_validation()
            return True
        except trafaret.DataError:
            self.errors = trafaret.extract_error(self.checker, self.data)
            return False
        except TrafaretError as e:
            self.errors = e.errors
            return False
