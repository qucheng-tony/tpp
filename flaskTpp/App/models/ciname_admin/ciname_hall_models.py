from App.ext import db
from App.models import Baseful
from App.models.ciname_admin.ciname_address_models import CinemaAddress


class CinameHall(Baseful):
    address_id=db.Column(db.Integer,db.ForeignKey(CinemaAddress.id))
    num=db.Column(db.Integer,default=1)
    seats=db.Column(db.String(128))

