import os
from flask import Flask
from src.core.handlers.ErrorHandler import ErrorHandler
from src.routes.index import Routes
from src.services.EnvironmentService import EnvironmentService
from src.services.AlchemyService import AlchemyService

app = Flask(__name__, template_folder='./src/templates')

# Environment configuration.
env_config = os.getenv('APP_SETTINGS', 'config.DevelopmentConfig')
app.config.from_object(env_config)
env = EnvironmentService().initialize(app.config)

print(env.get_one("POSTGRES_URI"))
app.config['SQLALCHEMY_DATABASE_URI'] = env.get_one("POSTGRES_URI")
db = AlchemyService().initialize(app)


routes = Routes().initialize(app)


@app.errorhandler(404)
def catch_route_not_found(e):
    err = ErrorHandler("Route is not found.", "route_not_found", status_code=404)
    return err.handle()


@app.errorhandler(Exception)
def catch_error(e):
    try:
        return e.handle()
    except Exception as error:
        print(error)
        err = ErrorHandler("Unexpected error.", "unexpected_error", status_code=400)
        return err.handle()


if __name__ == "__main__":
    app.run()
