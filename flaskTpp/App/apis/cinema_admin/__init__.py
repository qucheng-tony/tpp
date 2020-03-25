from flask_restful import Api

from App.apis.cinema_admin.cinema_address_api import CinemaAddressesResource, CinemaAddressResource
from App.apis.cinema_admin.cinema_hall_api import CinameHallResource
from App.apis.cinema_admin.cinema_hall_movie import CinemaMovieHallResource
from App.apis.cinema_admin.cinema_movie_buy import CinemaMovieBuyResource
from App.apis.cinema_admin.cinema_user_api import CinemaUsersResource




cinema_client_api=Api(prefix='/cinema')

cinema_client_api.add_resource(CinemaUsersResource,'/users/')

cinema_client_api.add_resource(CinemaAddressesResource,'/address/')

cinema_client_api.add_resource(CinemaAddressResource,'/address/<int:id>/')

cinema_client_api.add_resource(CinemaMovieBuyResource,'/buy/')

cinema_client_api.add_resource(CinameHallResource,'/hall/')

cinema_client_api.add_resource(CinemaMovieHallResource,'/hallmovie/')









