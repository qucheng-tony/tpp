import datetime

from flask import g
from flask_restful import Resource, reqparse, abort, fields, marshal
from sqlalchemy import or_, and_

from App.apis.api_constant import HTTP_OK
from App.apis.movie_user.utils import login_check, requery_permission
from App.models.ciname_admin.ciname_hall_models import CinameHall
from App.models.ciname_admin.ciname_hall_movie_models import HallMovie
from App.models.movie_user.movie_order_models import MovieOrder, ORDER_STATUS_PAYED_NOT_GET, ORDER_STATUS_GET, \
    ORDER_STATUS_NOT_PAY
from App.models.movie_user.user_models import VIP_USER, COMMIT_USER
parse = reqparse.RequestParser()
parse.add_argument("hall_movie_id", required=True, help="请提供排挡信息")
parse.add_argument("o_seats", required=True, help="请正确选择座位")

movie_order_fields = {
    "o_price": fields.Float,
    "o_seats": fields.String,
    "o_hall_movie_id": fields.Integer
}


class MovieordersResource(Resource):
    @login_check
    def post(self):
        args = parse.parse_args()
        hall_movie_id = args.get("hall_movie_id")
        o_seats = args.get("o_seats")
        pay = MovieOrder.query.filter(MovieOrder.o_hall_movie_id == hall_movie_id).filter(or_(MovieOrder.o_status == ORDER_STATUS_PAYED_NOT_GET, MovieOrder.o_status == ORDER_STATUS_GET)).all()
        suo = MovieOrder.query.filter(MovieOrder.o_hall_movie_id == hall_movie_id).filter(and_(MovieOrder.o_status == ORDER_STATUS_NOT_PAY, MovieOrder.o_time > datetime.datetime.now())).all()
        seats = []
        for i in pay:
            sold_seats = i.o_seats.split('#')
            seats += sold_seats
        for i in suo:
            sold_seats = i.o_seats.split('#')
            seats += sold_seats
        hall_movie = HallMovie.query.get(hall_movie_id)
        hall=CinameHall.query.get(hall_movie.h_hall_id)
        all_seats = hall.seats.split('#')
        can_buy = list(set(all_seats) - set(seats))
        want_buy=o_seats.split('#')
        for item in want_buy:
            if item not in can_buy:
                abort(400,msg="锁座失败")
        user = g.user
        movie_order = MovieOrder()
        movie_order.o_hall_movie_id = hall_movie_id
        movie_order.o_seats = o_seats
        movie_order.o_user_id = user.id
        movie_order.o_time = datetime.datetime.now() + datetime.timedelta(minutes=15)

        if not movie_order.save():
            abort(400, msg="下单失败")
        data = {
            "msg": "success",
            "status": HTTP_OK,
            "data": marshal(movie_order, movie_order_fields)
        }
        return data

class MovieorderResource(Resource):
    @requery_permission(VIP_USER)
    def put(self,order_id):
        user=g.user
        return {'suecess':'ok'}