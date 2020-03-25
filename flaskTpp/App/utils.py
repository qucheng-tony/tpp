import uuid

MOVIE_USER='movie_user'
CINAME_USER='ciname_user'
ADMIN_USER='admin_user'

def generate_token(prefix=None):
    return prefix+uuid.uuid4().hex

def generate_movie_user_token():
    return generate_token(prefix=MOVIE_USER)

def generate_ciname_user_token():
    return generate_token(prefix=CINAME_USER)

def generate_admin_user_token():
    return generate_token(prefix=ADMIN_USER)