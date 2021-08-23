from manage import db
from sqlalchemy.dialects.postgresql import INTEGER, VARCHAR
from flask_sqlalchemy import BaseQuery


class Category(db.Model):
    __tablename__ = 'category'
    query: BaseQuery

    id = db.Column(INTEGER, primary_key=True)
    title = db.Column(VARCHAR(255))
