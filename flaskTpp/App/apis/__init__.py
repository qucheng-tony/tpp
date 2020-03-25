from flask_restful import Api, Resource

from App.apis.admin import movie_admin_api
from App.apis.common import common_api
from App.apis.cinema_admin import cinema_client_api
from App.apis.movie_user import client_api
from App.apis.movie_user.movie_user_api import MovieUsersResource


def init_api(app):
    client_api.init_app(app)
    cinema_client_api.init_app(app)
    movie_admin_api.init_app(app)
    common_api.init_app(app)


