from src.routes.main.main_route import main
from src.routes.authentication.authentication_route import authentication
from src.routes.article.article_route import article
from src.routes.api.api_route import api


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
            self.main = main
            self.authentication = authentication
            self.article = article
            self.api = api

            app.register_blueprint(self.main)
            app.register_blueprint(self.authentication)
            app.register_blueprint(self.article)
            app.register_blueprint(self.api)
        else:
            raise Exception("This class is a singleton!")
