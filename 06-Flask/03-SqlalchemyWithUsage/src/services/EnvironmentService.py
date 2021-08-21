import os
from flask import Config
from src.core.metaclass.Singleton import Singleton


class EnvironmentService(metaclass=Singleton):
    __env: Config = None

    def initialize(self, app):
        # Environment Config
        env_config = os.getenv('APP_SETTINGS', 'src.config.DevelopmentConfig')
        app.config.from_object(env_config)

        # Sql Alchemy Config
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


def serve_env() -> EnvironmentService:
    return EnvironmentService()