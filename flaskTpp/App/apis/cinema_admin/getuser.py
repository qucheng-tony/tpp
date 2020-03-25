

#这个函数用来获取user
from App.models.ciname_admin.ciname_user_models import CinemaUser


def get_cinema_user(user_data):
    if not user_data:
        return None

    user=CinemaUser.query.filter(CinemaUser.name == user_data).first()
    if user:
        return user

    user=CinemaUser.query.get(user_data)
    if user:
        return user

    user=CinemaUser.query.filter(CinemaUser.phone == user_data).first()
    if user:
        return user

    return None