from flask import Blueprint
from src.core.metaclass.Singleton import Singleton
from src.routes.main.main_route import main_route
from src.routes.task.task_route import task_route


class Routes(metaclass=Singleton):
    main_route: Blueprint = main_route
    task_route: Blueprint = task_route

    def initialize(self, app):
        app.register_blueprint(self.main_route)
        app.register_blueprint(self.task_route)

        return Routes()
