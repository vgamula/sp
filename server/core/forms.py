import asyncio
from motor.motor_asyncio import AsyncIOMotorDatabase

import trafaret


class TrafaretError(Exception):
    def __init__(self, errors, *args, **kwargs):
        self.errors = errors


class TrafaretForm:
    fields = None
    result = None
    errors = None

    def __init__(self, data: dict=None, db: AsyncIOMotorDatabase=None):
        self.db = db
        self.errors = {}
        if data:
            self.data = data
        else:
            self.data = {}

    async def extra_validation(self):
        pass

    async def is_valid(self):
        try:
            self.result = self.fields.check(self.data)
            await self.extra_validation()
            return True
        except trafaret.DataError:
            self.errors = trafaret.extract_error(self.fields, self.data)
            return False
        except TrafaretError as e:
            self.errors = e.errors
            return False

    async def save(self):
        pass
