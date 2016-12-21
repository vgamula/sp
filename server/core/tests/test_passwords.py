import pytest

from .. import passwords

params = [
    'Hello!',
    'World',
]

@pytest.mark.parametrize('password', params)
def test_generated_password(password):
    hash = passwords.generate_password(password)
    assert passwords.check_password(password, hash)
