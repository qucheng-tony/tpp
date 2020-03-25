from werkzeug.security import generate_password_hash,check_password_hash

from App.ext import db
from App.models import Baseful
from App.models.movie_user.models_constant import PERMISSION_NONE
BLAK_USER=1
COMMIT_USER=0
VIP_USER=2

class MovieUser(Baseful):

    name=db.Column(db.String(32),unique=True)
    _password=db.Column(db.String(256))
    phone=db.Column(db.String(32),unique=True)
    is_delete=db.Column(db.Boolean(),default=False)
    permission=db.Column(db.Integer,default=PERMISSION_NONE)

    @property
    def password(self):
        raise Exception('不准查看')

    @password.setter
    def password(self,password_value):
        self._password=generate_password_hash(password_value)

    def check_password(self, user_password):
        return check_password_hash(self._password,user_password)

    def check_permission(self,permission_s):

        if BLAK_USER & permission_s ==BLAK_USER:
            return False
        else:
            return self.permission & permission_s == permission_s

