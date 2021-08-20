from src import db
from sqlalchemy.dialects.postgresql import INTEGER, VARCHAR


class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(INTEGER, primary_key=True)
    title = db.Column(VARCHAR(255))
