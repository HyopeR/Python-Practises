from flask import Blueprint
from src.core.metaclass.Singleton import Singleton
from src.routes.main.main_route import main_route
from src.routes.auth.auth_route import auth_route
from src.routes.api import api_route


class Routes(metaclass=Singleton):
    main_route: Blueprint = main_route
    auth_route: Blueprint = auth_route
    api_route: Blueprint = api_route

    def initialize(self, app):
        app.register_blueprint(self.main_route)
        app.register_blueprint(self.auth_route)
        app.register_blueprint(self.api_route)

        return Routes()
