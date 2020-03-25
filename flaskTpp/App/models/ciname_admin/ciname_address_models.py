from App.ext import db
from App.models import Baseful
from App.models.ciname_admin import CinemaUser

"""
insert into cinemas(name,city,district,address,phone,score,hallnum,servicecharge,astrict,flag,isdelete)
 values("深圳戏院影城","深圳","罗湖","罗湖区新园路1号东门步行街西口","0755-82175808",9.7,9,1.2,20,1,0);

"""


class CinemaAddress(Baseful):
    c_user_id = db.Column(db.Integer, db.ForeignKey(CinemaUser.id))
    name = db.Column(db.String(64))
    city = db.Column(db.String(16))
    district = db.Column(db.String(16))
    address = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    score = db.Column(db.Float, default=10)
    hallnum = db.Column(db.Integer, default=1)
    servicecharge = db.Column(db.Float, default=10)
    astrict = db.Column(db.Float, default=10)
    flag = db.Column(db.Boolean, default=False)
    is_delete = db.Column(db.Boolean, default=False)