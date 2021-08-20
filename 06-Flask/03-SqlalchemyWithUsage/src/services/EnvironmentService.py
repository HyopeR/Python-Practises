from flask import Config
from src.core.metaclass.Singleton import Singleton


class EnvironmentService(metaclass=Singleton):
    __env: Config = None

    def initialize(self, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = app.config.get("POSTGRES_URI")
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

        self.__env = app.config
        return EnvironmentService()

    def get_all(self):
        return self.__env.copy()

    def get_one(self, key):
        item = self.__env.get(key)

        if isinstance(item, property):
            return item.fget()

        return self.__env.get(key)