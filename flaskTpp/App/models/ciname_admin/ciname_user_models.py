from werkzeug.security import generate_password_hash, check_password_hash

from App.ext import db
from App.models import Baseful
from App.models.movie_user.models_constant import PERMISSION_NONE
BLAK_USER=1
COMMIT_USER=0
VIP_USER=2

class CinemaUser(Baseful):

    name=db.Column(db.String(32),unique=True)
    _password=db.Column(db.String(256))
    phone=db.Column(db.String(32),unique=True)
    is_delete=db.Column(db.Boolean(),default=False)
    is_verify = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise Exception('不准查看')

    @password.setter
    def password(self,password_value):
        self._password=generate_password_hash(password_value)

    def check_password(self, user_password):
        return check_password_hash(self._password,user_password)

    def check_permission(self,permission):
        if not self.is_verify:
            return False
        pers=CinemaUserPermission.query.filter_by(c_user_id=self.id)
        for per in pers:
            if permission==Permissions.query.get(per.c_perssion_id).p_name:
                return True
        return False

class Permissions(Baseful):
    p_name=db.Column(db.String(64),unique=True)

class CinemaUserPermission(Baseful):
    c_user_id=db.Column(db.Integer,db.ForeignKey(CinemaUser.id))
    c_perssion_id=db.Column(db.Integer,db.ForeignKey(Permissions.id))

