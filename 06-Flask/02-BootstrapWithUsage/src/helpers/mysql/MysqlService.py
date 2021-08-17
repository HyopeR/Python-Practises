import MySQLdb.cursors
from flask_mysqldb import MySQL
from typing import Any, Tuple


class SkeletonMysqlService:
    def __init__(self):
        self.mysql: MySQL

    def cursor(self):
        pass

    def commit(self):
        pass

    def raw_query(self, query, values=None) -> Tuple[Any, MySQLdb.cursors.DictCursor]:
        pass


class MysqlService:
    __instance = None

    @staticmethod
    def get_instance(app) -> SkeletonMysqlService:
        """ Static access method. """
        if MysqlService.__instance is None:
            MysqlService(app)

        return MysqlService.__instance

    def __init__(self, app):
        if MysqlService.__instance is None:
            try:
                self.__host = "127.0.0.1"
                self.__port = 3306
                self.__user = "root"
                self.__password = "123123aa"
                self.__db = "ybblog"
                self.__cursor_class = "DictCursor"
                self.mysql: MySQL

                app.config["MYSQL_HOST"] = self.__host
                app.config["MYSQL_PORT"] = self.__port
                app.config["MYSQL_USER"] = self.__user
                app.config["MYSQL_PASSWORD"] = self.__password
                app.config["MYSQL_DB"] = self.__db
                app.config["MYSQL_CURSORCLASS"] = self.__cursor_class

                self.mysql = MySQL(app)
                MysqlService.__instance = self

            except Exception as error:
                raise print(repr(error))
        else:
            raise Exception("This class is a singleton!")

    def cursor(self):
        return self.mysql.connection.cursor()

    def commit(self):
        self.mysql.connection.commit()

    def raw_query(self, query, values=None) -> Tuple[Any, MySQLdb.cursors.DictCursor]:
        try:
            cursor = self.cursor()
            result = cursor.execute(query, values)
            self.commit()

            return result, cursor

        except Exception as err:
            print(err)
