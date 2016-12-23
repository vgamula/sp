import trafaret as t

from server.core.forms import TrafaretForm, TrafaretError


class RegistrationForm(TrafaretForm):
    checker = t.Dict({
        t.Key('email'): t.Email(),
        t.Key('password'): t.String(max_length=255),
        t.Key('confirm'): t.String(max_length=255),
        t.Key('accept_tos'): t.StrBool(),
    })

    async def extra_validation(self):
        errors = {}
        if self.data['confirm'] != self.data['password']:
            errors['confirm'] = 'Passwords should match.'
        # TODO: Add email existing checking.
        if errors:
            raise TrafaretError(errors)
        return None
