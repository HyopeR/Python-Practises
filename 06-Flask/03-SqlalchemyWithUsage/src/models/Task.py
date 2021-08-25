from manage import db
from sqlalchemy.dialects.postgresql import TEXT, JSON, DATE, INTEGER, BOOLEAN, VARCHAR, TIMESTAMP
from src.models.TaskCategory import TaskCategory
from datetime import datetime
from flask_sqlalchemy import BaseQuery


class Task(db.Model):
    __tablename__ = 'task'
    query: BaseQuery

    id = db.Column(INTEGER, primary_key=True)
    user_id = db.Column(INTEGER, db.ForeignKey('users.id'), nullable=False)
    title = db.Column(VARCHAR(255), nullable=False)
    content = db.Column(TEXT, nullable=True)
    steps = db.Column(JSON, nullable=True)
    created_at = db.Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = db.Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    is_done = db.Column(BOOLEAN, default=False)
    categories = db.relationship('Category', secondary=TaskCategory, backref=db.backref('categories', lazy='dynamic'), cascade="all, delete")

    def __init__(self, user_id, title, content=None, steps=None, is_done=False):
        self.user_id = user_id
        self.title = title
        self.content = content
        self.steps = steps
        self.is_done = is_done
