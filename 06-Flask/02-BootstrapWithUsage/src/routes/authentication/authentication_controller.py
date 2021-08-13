from passlib.hash import sha256_crypt

from src.helpers.mysql.mysql_service import ServiceMysql


class AuthenticationController():
    def __init__(self, form):
        self.form = form

    def register(self):
        name = self.form.name.data
        surname = self.form.surname.data
        email = self.form.email.data
        username = self.form.username.data
        password = sha256_crypt.encrypt(self.form.password.data)

        mysql = ServiceMysql.get_instance(None)
        print('CONTROLLER', mysql)