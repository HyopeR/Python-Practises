from manage import db
from sqlalchemy.dialects.postgresql import TEXT, JSON, DATE, INTEGER, BOOLEAN, VARCHAR
from src.models.TaskCategory import TaskCategory
from datetime import datetime


class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(INTEGER, primary_key=True)
    title = db.Column(VARCHAR(255))
    content = db.Column(TEXT)
    steps = db.Column(JSON)
    created_at = db.Column(DATE, default=datetime.now())
    updated_at = db.Column(DATE, default=datetime.now(), onupdate=datetime.now())
    is_done = db.Column(BOOLEAN, default=False)
    subscriptions = db.relationship('Category', secondary=TaskCategory, backref=db.backref('tasks', lazy='dynamic'))
