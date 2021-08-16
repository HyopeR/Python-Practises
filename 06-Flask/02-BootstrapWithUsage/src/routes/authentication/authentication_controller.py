from passlib.hash import sha256_crypt
from src.helpers.mysql.MysqlService import MysqlService


class AuthenticationController():

    def register(self, form):
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(form.password.data)

        try:

            mysql_service = MysqlService.get_instance(None)
            cursor = mysql_service.cursor()

            query = "INSERT INTO users(name, surname, email, username, password) VALUES(%s, %s, %s, %s, %s)"
            cursor.execute(query, (name, surname, email, username, password))
            mysql_service.commit()
            cursor.close()

        except Exception as err:
            print('ERRORS', err)


    def login(self, form):
        username = form.username.data
        password = sha256_crypt.encrypt(form.password.data)

        mysql_service = MysqlService.get_instance(None)
        cursor = mysql_service.get_cursor()