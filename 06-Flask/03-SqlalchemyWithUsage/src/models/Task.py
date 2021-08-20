from src import db
from sqlalchemy.dialects.postgresql import TEXT, JSON, DATE, INTEGER, VARCHAR
from src.models.TaskCategory import TaskCategory
from datetime import datetime


class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(INTEGER, primary_key=True)
    content = db.Column(TEXT)
    steps = db.Column(JSON)
    created_at = db.Column(DATE, default=datetime.now())
    updated_at = db.Column(DATE, default=datetime.now(), onupdate=datetime.now())
    subscriptions = db.relationship('Category', secondary=TaskCategory, backref=db.backref('tasks', lazy='dynamic'))
