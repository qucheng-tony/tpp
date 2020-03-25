import datetime

from flask_restful import Resource, reqparse, marshal, fields
from sqlalchemy import or_, and_

from App.apis.api_constant import HTTP_OK
from App.apis.movie_user.utils import login_check
from App.models.ciname_admin.ciname_address_models import CinemaAddress
from App.models.ciname_admin.ciname_hall_models import CinameHall
from App.models.ciname_admin.ciname_hall_movie_models import HallMovie
from App.models.movie_user.movie_order_models import MovieOrder, ORDER_STATUS_PAYED_NOT_GET, ORDER_STATUS_GET, \
    ORDER_STATUS_NOT_PAY

parse=reqparse.RequestParser()
parse.add_argument('address_id')
parse.add_argument('movie_id')
parse.add_argument('district')

hall_movie_hall={
    'id':fields.Integer,
    'h_hall_id':fields.Integer,
    'h_movie_id':fields.Integer,
    'h_time':fields.DateTime,
}
muite_hall_movie_hall={
    'status':fields.Integer,
    'msg':fields.String,
    'data':fields.List(fields.Nested(hall_movie_hall))
}
class UserMovieHallsResource(Resource):
    def get(self):
        args=parse.parse_args()
        movie_id=args.get('movie_id')
        address_id=args.get('address_id')
        district=args.get('district')
        hall_movies=[]
        cinema_address=CinemaAddress.query.filter(CinemaAddress.district==district).filter(CinemaAddress.id==address_id).first()
        halls=CinameHall.query.filter_by(address_id=cinema_address.id)
        for hall in halls:
            hall_movie=HallMovie.query.filter_by(h_hall_id=hall.id).filter_by(h_movie_id=movie_id).all()
            hall_movies += hall_movie
        data={
            'status':HTTP_OK,
            'msg':'ok',
            'data':hall_movies
        }
        return marshal(data,muite_hall_movie_hall)
hall_se={
    'address_id':fields.Integer,
    'num':fields.Integer,
    'seats':fields.String,
}
class UserMovieHallResource(Resource):
    @login_check
    def get(self,id):
        hallmovie=HallMovie.query.get(id)
        hall=CinameHall.query.get(hallmovie.h_hall_id)
        pay=MovieOrder.query.filter(MovieOrder.o_hall_movie_id==id).filter(or_(MovieOrder.o_status==ORDER_STATUS_PAYED_NOT_GET,MovieOrder.o_status==ORDER_STATUS_GET)).all()
        suo=MovieOrder.query.filter(MovieOrder.o_hall_movie_id==id).filter(and_(MovieOrder.o_status==ORDER_STATUS_NOT_PAY,MovieOrder.o_time>datetime.datetime.now())).all()
        seats=[]
        for i in pay:
            sold_seats=i.o_seats.split('#')
            seats += sold_seats
        for i in suo:
            sold_seats=i.o_seats.split('#')
            seats += sold_seats
        all_seats=hall.seats.split('#')
        can_buy=set(all_seats)-set(seats)
        can_buy='#'.join(can_buy)
        hall.seats=can_buy
        data={
            'status':HTTP_OK,
            'msg':'ok',
            'data':marshal(hall,hall_se)
        }
        return data
