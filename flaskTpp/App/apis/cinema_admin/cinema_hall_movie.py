from flask import g
from flask_restful import Resource, reqparse, abort, marshal, fields
from flask_restful.fields import DateTime

from App.apis.api_constant import HTTP_OK
from App.apis.cinema_admin.utils import login_check
from App.models.ciname_admin.ciname_address_models import CinemaAddress
from App.models.ciname_admin.ciname_hall_models import CinameHall
from App.models.ciname_admin.ciname_hall_movie_models import HallMovie
from App.models.ciname_admin.ciname_movie_models import CinemaMovies

parse=reqparse.RequestParser()
parse.add_argument('h_hall_id',type=int,required=True,help="请输入放映厅编号")
parse.add_argument('h_movie_id',required=True,type=int,help="请输入电影编号")
parse.add_argument('h_time',required=True,type=str,help="请输入放映时间")

hall_movie_x={
    'h_hall_id':fields.Integer,
    'h_movie_id': fields.Integer,
    'h_time': fields.DateTime,
}

class CinemaMovieHallResource(Resource):
    def get(self):
        return {'this':'ok'}
    @login_check
    def post(self):
        args=parse.parse_args()
        h_hall_id=args.get('h_hall_id')
        h_movie_id=args.get('h_movie_id')
        h_time=args.get('h_time')
        #验证movie_id是否购买
        #验证hall_id是否是自己的
        #验证时间
        #验证同一时间是否有重复的
        cinames=CinemaMovies.query.filter_by(c_cinema_id=g.user.id).all()
        cinameBuy=[cinmovie.c_movie_id for cinmovie in cinames]
        if not h_movie_id in cinameBuy:
            abort(400,msg="你不具有此电影权限")
        halls=[]
        ciname_addresses=CinemaAddress.query.filter_by(c_user_id=g.user.id).all()
        for ciname_address in ciname_addresses:
            hall=CinameHall.query.filter_by(address_id=ciname_address.id).all()
            halls.append(hall)
        ids=[]
        for ha in halls:
            for h in ha:
                ids.append(h.id)

        if not h_hall_id in ids:
            abort(400,msg="你不拥有这个放映厅")
        hall_movie=HallMovie()
        hall_movie.h_hall_id=h_hall_id
        hall_movie.h_movie_id=h_movie_id
        hall_movie.h_time=h_time

        if not hall_movie.save():
            abort(400,msg="发送不成功")

        data={
            'status':HTTP_OK,
            'msg':'ok',
            'data':marshal(hall_movie,hall_movie_x),
        }
        return data