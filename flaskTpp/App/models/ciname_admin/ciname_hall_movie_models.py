

from App.ext import db
from App.models import Baseful
from App.models.ciname_admin.ciname_hall_models import CinameHall
from App.models.common import Movie


class HallMovie(Baseful):
    h_hall_id=db.Column(db.Integer,db.ForeignKey(CinameHall.id))
    h_movie_id=db.Column(db.Integer,db.ForeignKey(Movie.id))
    h_time=db.Column(db.DateTime)

    movie_order=db.relationship('MovieOrder',backref='HallMovie',lazy=True)