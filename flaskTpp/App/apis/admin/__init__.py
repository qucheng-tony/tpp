from flask_restful import Api

from App.apis.admin.admin_auth_api import AdminCinemaUsersResource, AdminCinemaUserResource
from App.apis.admin.admin_user_api import AdminResource

movie_admin_api=Api(prefix='/admin')

movie_admin_api.add_resource(AdminResource, '/users/')

movie_admin_api.add_resource(AdminCinemaUsersResource,'/auth/')

movie_admin_api.add_resource(AdminCinemaUserResource,'/auth/<int:id>/')



