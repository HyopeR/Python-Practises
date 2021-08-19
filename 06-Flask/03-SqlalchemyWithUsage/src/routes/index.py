from flask import Blueprint
from src.core.metaclass.Singleton import Singleton
from src.routes.main.main_route import main_route


class Routes(metaclass=Singleton):
    main_route: Blueprint = main_route

    def initialize(self, app):
        app.register_blueprint(self.main_route)

        return Routes()
