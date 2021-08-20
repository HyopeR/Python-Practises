import os
from flask import Flask
from src.core.handlers.ErrorHandler import ErrorHandler
from src.routes.index import Routes
from src.services.EnvironmentService import EnvironmentService
from src.services.AlchemyService import AlchemyService
from src.services.MigrationService import MigrationService

app = Flask(__name__, template_folder='./src/templates')

# Environment configuration.
env_config = os.getenv('APP_SETTINGS', 'src.config.DevelopmentConfig')
app.config.from_object(env_config)

# İnitialize services.
environment_service = EnvironmentService().initialize(app)
db = AlchemyService().initialize(app).db
import manage
routes_service = Routes().initialize(app)


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