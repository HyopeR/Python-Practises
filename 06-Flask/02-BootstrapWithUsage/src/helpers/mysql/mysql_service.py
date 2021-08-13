from flask_mysqldb import MySQL


class ServiceMysql:
    __instance = None

    @staticmethod
    def get_instance(app):
        """ Static access method. """
        if ServiceMysql.__instance is None:
            ServiceMysql(app)
        return ServiceMysql.__instance

    def __init__(self, app):
        if ServiceMysql.__instance is None:
            print(app)

            try:
                self.__host = ' 192.168.1.210'
                self.__port = '3306'
                self.__user = 'root'
                self.__password = '123123aa'
                self.__db = 'ybblog'
                self.__cursor_class = 'DictCursor'
                self.__mysql = None

                app.config["MYSQL_HOST"] = self.__host
                app.config["MYSQL_PORT"] = self.__port
                app.config["MYSQL_USER"] = self.__user
                app.config["MYSQL_PASSWORD"] = self.__password
                app.config["MYSQL_DB"] = self.__db
                app.config["MYSQL_CURSORCLASS"] = self.__cursor_class

                self.__mysql = MySQL(app)
                ServiceMysql.__instance = self

            except Exception as error:
                raise print(repr(error))
        else:
            raise Exception("This class is a singleton!")

    def get_cursor(self):
        return self.__instance.__mysql.cursor()
