import trafaret as t

from server.core.passwords import generate_password, check_password
from server.core.forms import TrafaretForm, TrafaretError


class RegistrationForm(TrafaretForm):
    fields = t.Dict({
        t.Key('email'): t.Email(),
        t.Key('password'): t.String(max_length=255),
        t.Key('confirm'): t.String(max_length=255),
        t.Key('accept_tos'): t.StrBool(),
    })

    async def extra_validation(self):
        errors = {}
        if self.data['confirm'] != self.data['password']:
            errors['confirm'] = 'Passwords should match.'

        if await self.db.users.find_one({'email': self.data['email']}):
            errors['email'] = 'User with this email is already registered.'

        if errors:
            raise TrafaretError(errors)

    async def save(self):
        data = self.data
        data_to_save = {
            'email': data['email'],
            'password': generate_password(data['password']),
        }
        result = await self.db.users.insert_one(data_to_save)
        data_to_save['_id'] = result.inserted_id
        return data_to_save


class LoginForm(TrafaretForm):
    user = None

    fields = t.Dict({
        t.Key('email'): t.Email(),
        t.Key('password'): t.String(max_length=255),
    })

    async def extra_validation(self):
        errors = {}
        user = await self.db.users.find_one({'email': self.data['email']})
        if not user:
            errors['email'] = 'User not found'
        else:
            if not check_password(self.data['password'], user.password):
                errors['password'] = 'Password is not correct'
            self.user = user
        if errors:
            raise TrafaretError(errors)

    def get_user(self):
        return self.user
