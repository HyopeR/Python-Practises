from flask import session
from src.helpers.mysql.MysqlService import MysqlService
from typing import Any, Tuple


class MainController():
    def index(self) -> bool:
        return True

    def about(self) -> bool:
        return True

    def dashboard(self) -> Tuple[bool, Any]:
        mysql_service = MysqlService.get_instance(None)
        query = "SELECT * FROM articles WHERE author = %s"

        result, cursor = mysql_service.raw_query(query, (session["username"],))
        data = cursor.fetchall()
        cursor.close()

        return bool(result), data

    def example(self) -> bool:
        return True