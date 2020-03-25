from werkzeug.security import check_password_hash, generate_password_hash

from App.ext import db
from App.models import Baseful

PERMISSION_NONE=0
PERMISSION_MAN=1

class AdminUser(Baseful):

    name=db.Column(db.String(32),unique=True)
    _password=db.Column(db.String(256))

    is_delete=db.Column(db.Boolean(),default=False)
    is_super=db.Column(db.Boolean(),default=False)
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

        return self.is_super or self.permission & permission_s == permission_s

