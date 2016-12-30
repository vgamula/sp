USER_ID_SESSION_KEY = 'user_id'


def login_user(session, user_id):
    session[USER_ID_SESSION_KEY] = str(user_id)


def logout_user(session):
    return session.pop(USER_ID_SESSION_KEY)
