from manage import db
from sqlalchemy.dialects.postgresql import INTEGER, VARCHAR, TIMESTAMP, BOOLEAN
from datetime import datetime
from flask_sqlalchemy import BaseQuery


class User(db.Model):
    __tablename__ = 'users'
    query: BaseQuery

    id = db.Column(INTEGER, primary_key=True)
    name = db.Column(VARCHAR(255), nullable=False)
    surname = db.Column(VARCHAR(255), nullable=True)
    email = db.Column(VARCHAR(255), nullable=False, unique=True)
    password = db.Column(VARCHAR(255), nullable=False)
    active = db.Column(BOOLEAN, default=True)
    created_at = db.Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = db.Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)
    tasks = db.relationship('Task', cascade="all, delete")

    def __init__(self, name, email, password, surname=None, active=True):
        self.name = name
        self.email = email
        self.password = password
        self.surname = surname
        self.active = active
