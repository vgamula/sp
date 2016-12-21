from passlib.hash import pbkdf2_sha256


def generate_password(password: str) -> str:
    return pbkdf2_sha256.hash(password)


def check_password(password: str, hash: str) -> bool:
    return pbkdf2_sha256.verify(password, hash)
