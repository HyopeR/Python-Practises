from flask import flash, session
from src.helpers.mysql.MysqlService import MysqlService
from typing import Any, Tuple
from src.services.forms.ArticleForm import ArticleForm


class ArticleController():
    def articles(self) -> Tuple[bool, Any]:
        mysql_service = MysqlService.get_instance(None)
        query = "SELECT * FROM articles"

        result, cursor = mysql_service.raw_query(query)
        data = cursor.fetchall()
        cursor.close()

        return bool(result), data

    def one_article(self, id) -> Tuple[bool, Any]:
        mysql_service = MysqlService.get_instance(None)
        query = "SELECT * FROM articles WHERE id = %s"

        result, cursor = mysql_service.raw_query(query, (id,))
        data = cursor.fetchone()
        cursor.close()

        return bool(result), data

    def add_article(self, form) -> bool:
        title = form.title.data
        content = form.content.data

        mysql_service = MysqlService.get_instance(None)
        query = "INSERT INTO articles(title, author, content) VALUES(%s, %s, %s)"
        result, cursor = mysql_service.raw_query(query, (title, session["username"], content))
        cursor.close()

        flash("Article added successfully.", "success")

        return bool(result)

    def delete_article(self, id) -> bool:
        mysql_service = MysqlService.get_instance(None)
        query = "SELECT * FROM articles WHERE author = %s and id = %s"
        result, cursor = mysql_service.raw_query(query, (session["username"], id))

        if bool(result):
            query2 = "DELETE FROM articles WHERE id = %s"
            cursor.execute(query2, (id,))
            mysql_service.commit()
            flash("Article deleted successfully.", "success")
        else:
            flash("This article is not yours!", "danger")

        cursor.close()
        return bool(result)

    def update_article(self, id, form) -> Tuple[bool, Any]:
        mysql_service = MysqlService.get_instance(None)

        query = "SELECT * FROM articles WHERE author = %s and id = %s"
        result, cursor = mysql_service.raw_query(query, (session["username"], id))

        data = None
        if bool(result):
            if form is not None:
                title = form.title.data
                content = form.content.data

                query2 = "UPDATE articles SET title = %s, content = %s WHERE id = %s"
                cursor.execute(query2, (title, content, id))
                mysql_service.commit()
                flash("Article updated successfully.", "success")

            else:
                db_article = cursor.fetchone()
                data = db_article

        else:
            flash("This article is not yours!", "danger")

        cursor.close()
        return bool(result), data

    def search_article(self, keyword) -> Tuple[bool, Any]:
        mysql_service = MysqlService.get_instance(None)

        like = "%" + keyword.strip() + "%"
        query = """SELECT * FROM articles WHERE title LIKE %s"""

        result, cursor = mysql_service.raw_query(query, (like,))

        if bool(result) is False:
            flash("No article found matching your search term.", "warning")

        data = cursor.fetchall()
        cursor.close()

        return bool(result), data
