from App.models.admin.admin_user_models import AdminUser

#这个函数用来获取user
def get_admin_user(user_data):

    if not user_data:
        return None
    user=AdminUser.query.filter(AdminUser.name==user_data).first()
    if user:
        return user
    user=AdminUser.query.get(user_data)
    if user:
        return user

    return None