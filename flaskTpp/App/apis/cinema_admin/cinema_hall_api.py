from flask import g
from flask_restful import Resource, reqparse, abort, fields, marshal

from App.apis.api_constant import HTTP_OK
from App.apis.cinema_admin.utils import login_check
from App.models.ciname_admin.ciname_address_models import CinemaAddress
from App.models.ciname_admin.ciname_hall_models import CinameHall

parse_hall=reqparse.RequestParser()
parse_hall.add_argument('address_id',required=True,help="请输入电影院地址")
parse_hall.add_argument('num',required=True,help="请输入放映厅编号")
parse_hall.add_argument('seats',required=True,help="请输入放映厅规模")
hall_fields={
    'address_id':fields.Integer,
    'num':fields.Integer,
    'seats':fields.String,
}

class CinameHallResource(Resource):
     @login_check
     def post(self):
         args=parse_hall.parse_args()
         address_id=args.get('address_id')
         num=args.get('num')
         seats=args.get('seats')
         addressid=[]
         cinema_address=CinemaAddress.query.filter_by(c_user_id=g.user.id).all()
         for address in cinema_address:
            addressid.append(address.id)
         if not address_id in addressid:
             abort(400,msg="不好意思，你对这个影院没有控制权")
         ciname_hall=CinameHall()
         ciname_hall.address_id=address_id
         ciname_hall.num=num
         ciname_hall.seats=seats


         if not ciname_hall.save():
             abort(400,msg="没有发送成功")
         data={
             'status':HTTP_OK,
             'msg':'ok',
             'data':marshal(ciname_hall,hall_fields)
         }

         return data