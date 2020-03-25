from flask import g
from flask_restful import Resource, reqparse, abort, marshal

from App.apis.api_constant import HTTP_OK
from App.apis.cinema_admin.utils import login_check
from App.apis.common.movie_api import movie_list
from App.models.ciname_admin.ciname_movie_models import CinemaMovies
from App.models.common import Movie

pares=reqparse.RequestParser()
pares.add_argument('movies_id',type=int,required=True,help="请输入要购买的电影")


class CinemaMovieBuyResource(Resource):
    @login_check
    def get(self):
        user_id=g.user.id
        cinema_movie=CinemaMovies.query.filter(CinemaMovies.c_cinema_id==user_id).all()
        movies=[]
        for cinema in cinema_movie:
            movies.append(Movie.query.get(cinema.c_movie_id))
        data={
            'msg':'ok',
            'status':HTTP_OK,
            'data':movies,
        }
        return marshal(data,movie_list)
    @login_check
    def post(self):
        user_id=g.user.id
        args=pares.parse_args()
        movie_id=args.get('movies_id')
        cinema_movies=CinemaMovies.query.filter(CinemaMovies.c_cinema_id==user_id).filter(CinemaMovies.c_movie_id==movie_id).all()
        if cinema_movies:
            abort(400,msg="你已经购买，不需要再次购买")
        cinemamovies=CinemaMovies()
        cinemamovies.c_movie_id=movie_id
        cinemamovies.c_cinema_id=user_id
        if not cinemamovies.save():
            abort(400,msg="发送失败")
        data={
            'status':200,
            'msg':"购买成功",
        }
        return data