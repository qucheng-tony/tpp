from App.ext import db
from App.models import Baseful
from App.models.ciname_admin import CinemaUser
from App.models.common import Movie


class CinemaMovies(Baseful):
    c_cinema_id=db.Column(db.Integer,db.ForeignKey(CinemaUser.id))
    c_movie_id=db.Column(db.Integer,db.ForeignKey(Movie.id))
