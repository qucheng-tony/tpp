import uuid

from flask_restful import Resource, reqparse, fields, marshal, marshal_with, abort

from App.apis.admin.getuser import get_admin_user
from App.apis.api_constant import HTTP_CREAT_OK, USER_REGISTER, USER_LOGIN, HTTP_OK
from App.ext import cache
from App.models.admin.admin_user_models import AdminUser
from App.settings import ADMIN
from App.utils import generate_admin_user_token

parse_base=reqparse.RequestParser()
parse_base.add_argument('password', type=str, required=True, help="请输入密码")
parse_base.add_argument('action', type=str, required=True, help="请输入登陆或注册")
parse_base.add_argument('name', type=str, required=True, help="请输入姓名")



#序列化
movie_user_fileds={
    'name':fields.String,
    '_password':fields.String,
    'phone':fields.String,
}
single_movie_user_fileds={
    'msg':fields.String,
    'status':fields.Integer,
    'data':fields.Nested(movie_user_fileds)
}

class AdminResource(Resource):
    def post(self):
        args=parse_base.parse_args()
        password=args.get('password')
        action=args.get('action').lower()
        if action==USER_REGISTER:
            args_registe=parse_base.parse_args()
            name = args_registe.get('name')
            user=AdminUser()
            user.name=name
            user.password=password
            if name in ADMIN:
                user.is_super=True
            if not user.save():
                abort(400,msg="create fail")
            data={
                'msg':"创建成功",
                'status':HTTP_CREAT_OK,
                'data':user,
            }

            return marshal(data,single_movie_user_fileds)
        elif action==USER_LOGIN:
            args_login = parse_base.parse_args()
            name = args_login.get('name')
            user=get_admin_user(name)
            if not user:
                abort(400,msg="请输入用户名")
            if not user.check_password(password):
                abort(400,msg="密码错误")
            if user.is_delete:
                abort(400,msg="用户不存在")
            token=generate_admin_user_token()
            cache.set(token,user.id,timeout=60*60*24*7)
            data={
                'status':HTTP_OK,
                'msg':'http_ok',
                'token':token,
            }
            return data

        else:
            abort(400,msg="请提供正确的参数")