from flask import g
from flask_restful import Resource, reqparse, fields, abort, marshal

from App.apis.api_constant import HTTP_OK
from App.apis.cinema_admin.utils import requery_permission
from App.models.ciname_admin.ciname_address_models import CinemaAddress
from App.models.ciname_admin.ciname_permission import PERMISSION_WRITE

parse = reqparse.RequestParser()
parse.add_argument("name", required=True, help="请提供影院名字")
parse.add_argument("phone", required=True, help="请提供联系方式")
parse.add_argument("city", required=True, help="请提供城市")
parse.add_argument("district", required=True, help="请提供所在区")
parse.add_argument("address", required=True, help="请提供详细地址")


cinema_fields = {
    "c_user_id": fields.Integer,
    "name": fields.String,
    "city": fields.String,
    "district": fields.String,
    "address": fields.String,
    "phone": fields.String,
    "score": fields.Float,
    "servicecharge": fields.Float,
    "astrict": fields.Float,
    "hallnum": fields.Integer,
}

class CinemaAddressesResource(Resource):
    def get(self):
        return {'get':'ok'}

    @requery_permission(PERMISSION_WRITE)
    def post(self):
        par=parse.parse_args()
        name=par.get('name')
        phone=par.get('phone')
        city=par.get('city')
        district=par.get('district')
        address=par.get('address')
        cinema_address=CinemaAddress()
        cinema_address.c_user_id=g.user.id
        cinema_address.name=name
        cinema_address.phone=phone
        cinema_address.city=city
        cinema_address.district=district
        cinema_address.address=address
        if not cinema_address.save():
            abort(400,msg="没有发送")
        data={
            'msg':'发送成功',
            'status':HTTP_OK,
            'data':marshal(cinema_address,cinema_fields),
        }

        return data

class CinemaAddressResource(Resource):
    def get(self,id):
        pass
    def put(self,id):
        pass
    def patch(self,id):
        pass
    def delete(self,id):
        pass