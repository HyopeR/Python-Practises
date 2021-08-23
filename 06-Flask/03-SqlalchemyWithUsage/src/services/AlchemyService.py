from src.core.metaclass.Singleton import Singleton
from flask_sqlalchemy import SQLAlchemy, BaseQuery


class AlchemyService(metaclass=Singleton):
    db: SQLAlchemy = None

    def initialize(self, app):
        self.db: SQLAlchemy = SQLAlchemy(app, query_class=BaseQuery)

        return AlchemyService()


def serve_db() -> SQLAlchemy:
    return AlchemyService().db


def serve_alchemy() -> AlchemyService:
    return AlchemyService()
