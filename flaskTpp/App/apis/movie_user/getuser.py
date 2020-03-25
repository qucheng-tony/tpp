

#这个函数用来获取user
from App.models.movie_user.user_models import MovieUser


def get_user(user_data):
    if not user_data:
        return None
    user=MovieUser.query.filter(MovieUser.name == user_data).first()
    if user:
        return user

    user=MovieUser.query.get(user_data)
    if user:
        return user

    user=MovieUser.query.filter(MovieUser.phone == user_data).first()
    if user:
        return user

    return None