from src.routes.main.main_route import main_route


class Routes:
    __instance = None

    @staticmethod
    def get_instance(app):
        """ Static access method. """
        if Routes.__instance is None:
            Routes(app)
        return Routes.__instance

    def __init__(self, app):
        if Routes.__instance is None:
            self.main_route = main_route

            app.register_blueprint(self.main_route)
        else:
            raise Exception("This class is a singleton!")
