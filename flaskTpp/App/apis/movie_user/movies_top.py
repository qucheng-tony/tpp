from flask_restful import Resource
from sqlalchemy import func

from App.ext import db
from App.models.ciname_admin.ciname_hall_movie_models import HallMovie
from App.models.common import Movie
from App.models.movie_user.movie_order_models import MovieOrder


class MoviesTopResource(Resource):
    def get(self):
        top=db.session.query(Movie.id,Movie.showname,func.sum(MovieOrder.o_price)).join(Movie.hall_movie).join(HallMovie.movie_order).group_by(Movie.id).order_by(-func.sum(MovieOrder.o_price)).all()
        print(top)
        return {'msg':'ok'}