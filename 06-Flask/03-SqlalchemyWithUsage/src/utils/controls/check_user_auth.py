from flask import request


# Bu fonksiyon kullanıcının kendi haricidenki kayıtları değiştirmesini önler.

def check_user_auth(other_user_id):
    your_user_id = request.user_id

    if your_user_id == other_user_id:
        return True
    else:
        raise Exception(
            'Your id number is {}. But you are trying to change the data of a user with id number {}.'.format(
                your_user_id, other_user_id))
