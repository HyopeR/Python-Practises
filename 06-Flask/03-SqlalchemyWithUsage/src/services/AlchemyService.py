from src.core.metaclass.Singleton import Singleton
from flask_sqlalchemy import SQLAlchemy


class AlchemyService(metaclass=Singleton):
    db: SQLAlchemy = None

    def initialize(self, app):
        self.db = SQLAlchemy(app)

        return AlchemyService()