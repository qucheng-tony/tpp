from flask import request, g
from flask_restful import abort
from App.apis.admin.getuser import get_admin_user
from App.ext import cache
from App.utils import ADMIN_USER


def _v():
    token = request.args.get('token')
    print(token)
    if not token:
        abort(401, msg="用户未登陆")
    if not token.startswith(ADMIN_USER):
        abort(401,msg="登错借口了")
    user_id = cache.get(token)
    if not token:
        abort(401, msg="密令不可用")
    user = get_admin_user(user_id)
    if not user:
        abort(401, msg="用户id不可用")
    g.user = user
    g.token=token

#工具箱
def login_check(fun):

    def war(*args,**kwargs):
        _v()
        return fun(*args,**kwargs)
    return war

def requery_permission(permmision):
    def requery(fun):
        def war(*args, **kwargs):
            _v()
            if not g.user.check_permission(permmision):
                abort(403,msg="你没有的权限")
            return fun(*args, **kwargs)
        return  war
    return requery



