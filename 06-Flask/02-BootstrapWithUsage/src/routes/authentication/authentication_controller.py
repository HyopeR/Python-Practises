from flask import flash
from passlib.hash import sha256_crypt
from src.helpers.mysql.MysqlService import MysqlService
from typing import Any


class AuthenticationController():

    def register(self, form) -> bool:
        name = form.name.data
        surname = form.surname.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(form.password.data)

        # Database process
        mysql_service = MysqlService.get_instance(None)
        query = "INSERT INTO users(name, surname, email, username, password) VALUES(%s, %s, %s, %s, %s)"
        result, cursor = mysql_service.raw_query(query, (name, surname, email, username, password))

        cursor.close()
        flash("You have successfully registered...", "success")

        return bool(result)

    def login(self, form) -> tuple[bool, Any]:
        username = form.username.data
        entered_password = form.password.data

        # Database process
        mysql_service = MysqlService.get_instance(None)
        query = "SELECT * FROM users WHERE username = %s"
        result, cursor = mysql_service.raw_query(query, (username,))

        login_success = False
        data = None

        if result > 0:
            data = cursor.fetchone()
            cursor.close()

            real_password = data["password"]
            if sha256_crypt.verify(entered_password, real_password):
                login_success = True
                flash("You have successfully logged in...", "success")
            else:
                login_success = False
                flash("Your password is incorrect.", "warning")

        else:
            flash("User not found.", "danger")

        return login_success, data

    def logout(self) -> bool:
        return True
