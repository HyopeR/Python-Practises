from passlib.hash import sha256_crypt
from src.helpers.mysql.MysqlService import MysqlService
import attr

class AuthenticationController():

    def register(self, form):
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(form.password.data)

        mysql = MysqlService.get_instance(None)
        mysql.get_cursor()
        print('CONTROLLER', mysql)

    def login(self, form):
        username = form.username.data
        password = sha256_crypt.encrypt(form.password.data)

        mysql = MysqlService.get_instance(None)
        mysql.get_cursor()
        print('CONTROLLER', mysql)