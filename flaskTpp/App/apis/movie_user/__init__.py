from flask_restful import Api

from App.apis.movie_user.movie_hall_api import UserMovieHallsResource, UserMovieHallResource
from App.apis.movie_user.movie_order import MovieordersResource, MovieorderResource
from App.apis.movie_user.movie_order_pay import MovieOrderPayResource
from App.apis.movie_user.movie_user_api import MovieUsersResource
from App.apis.movie_user.movies_top import MoviesTopResource

client_api=Api(prefix='/user')
client_api.add_resource(MovieUsersResource, '/moviesresource/')

client_api.add_resource(MovieordersResource, '/movieorder/')

client_api.add_resource(MovieorderResource, '/movieorder/<int:order_id>/')
client_api.add_resource(UserMovieHallsResource, '/moviehalls/')

client_api.add_resource(UserMovieHallResource, '/moviehalls/<int:id>/')

client_api.add_resource(MovieOrderPayResource, '/pay/<int:order_id>/')

client_api.add_resource(MoviesTopResource, '/moviestop/')



