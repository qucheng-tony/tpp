from flask_restful import Resource, fields, marshal, reqparse, abort
from flask_restful.fields import Nested

from App.apis.admin.utils import login_check
from App.apis.api_constant import HTTP_OK
from App.models.ciname_admin import CinemaUser
parse=reqparse.RequestParser()
parse.add_argument('is_verify',type=bool,required=True,help="请提供操作")
ciname_user_fileds={
    'id':fields.Integer,
    'name':fields.String,
    '_password':fields.String,
    'phone':fields.String,
    'is_verify':fields.Boolean,
}
list_cinema_user_fileds={
    'msg':fields.String,
    'status':fields.Integer,
    'data':fields.List(Nested(ciname_user_fileds))
}
single_cinema_user_fileds={
    'msg':fields.String,
    'status':fields.Integer,
    'data':fields.Nested(ciname_user_fileds)
}


class AdminCinemaUsersResource(Resource):
    @login_check
    def get(self):
        ciname_user=CinemaUser.query.all()
        data={
            'status':HTTP_OK,
            'msg':'ok',
            'data':ciname_user,
        }
        return marshal(data,list_cinema_user_fileds)


class AdminCinemaUserResource(Resource):
    @login_check
    def patch(self,id):
        args=parse.parse_args()

        ciname_auth = args.get('is_verify')
        ciname_user=CinemaUser.query.get(id)
        ciname_user.is_verify=ciname_auth
        if not ciname_user.save():
            abort(400,msg="没有发送成功")
        data = {
            'status': HTTP_OK,
            'msg': 'ok',
            'data': ciname_user,
        }
        return marshal(data, single_cinema_user_fileds)



