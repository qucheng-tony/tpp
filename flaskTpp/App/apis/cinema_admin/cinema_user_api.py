
from flask_restful import Resource, reqparse, fields, marshal, abort

from App.apis.api_constant import HTTP_CREAT_OK, USER_REGISTER, USER_LOGIN, HTTP_OK
from App.apis.cinema_admin.getuser import get_cinema_user
from App.ext import cache
from App.models.ciname_admin import CinemaUser

from App.utils import  generate_ciname_user_token

parse_base=reqparse.RequestParser()
parse_base.add_argument('password', type=str, required=True, help="请输入密码")
parse_base.add_argument('action', type=str, required=True, help="请输入登陆或注册")


parse_regist=parse_base.copy()
parse_regist.add_argument('phone', type=str, required=True, help="请输入手机")
parse_regist.add_argument('name', type=str, required=True, help="请输入姓名")

parse_login=parse_base.copy()
parse_login.add_argument('phone', type=str, help="请输入手机")
parse_login.add_argument('name', type=str, help="请输入姓名")


#序列化
ciname_user_fileds={
    'name':fields.String,
    '_password':fields.String,
    'phone':fields.String,
    'is_verify':fields.Boolean,
}
single_cinema_user_fileds={
    'msg':fields.String,
    'status':fields.Integer,
    'data':fields.Nested(ciname_user_fileds)
}

class CinemaUsersResource(Resource):
    def post(self):
        args=parse_base.parse_args()
        password=args.get('password')
        action=args.get('action').lower()
        if action==USER_REGISTER:
            args_registe=parse_regist.parse_args()
            name = args_registe.get('name')
            phone = args_registe.get('phone')
            cinema_user=CinemaUser()
            cinema_user.name=name
            cinema_user.phone=phone
            cinema_user.password=password
            if not cinema_user.save():
                abort(400,msg="create fail")
            data={
                'msg':"创建成功",
                'status':HTTP_CREAT_OK,
                'data':cinema_user,
            }

            return marshal(data, single_cinema_user_fileds)
        elif action==USER_LOGIN:
            args_login = parse_login.parse_args()
            name = args_login.get('name')
            phone = args_login.get('phone')
            cinema_user= get_cinema_user(phone) or get_cinema_user(name)
            if not cinema_user:
                abort(400,msg="请输入用户名")
            if not cinema_user.check_password(password):
                abort(400,msg="密码错误")
            if cinema_user.is_delete:
                abort(400,msg="用户不存在")
            token=generate_ciname_user_token()
            cache.set(token, cinema_user.id, timeout=60 * 60 * 24 * 7)
            data={
                'status':HTTP_OK,
                'msg':'http_ok',
                'token':token,
            }
            return data

        else:
            abort(400,msg="请提供正确的参数")