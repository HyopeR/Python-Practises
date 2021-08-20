from flask import Flask
from src.core.handlers.ErrorHandler import ErrorHandler
from src.routes import Routes
from src.services.EnvironmentService import EnvironmentService
from src.services.AlchemyService import AlchemyService
from src.services.MigrationService import MigrationService
from src.services.ModelService import ModelService

app = Flask(__name__, template_folder='./src/templates')

# İnitialize services.
environment_service = EnvironmentService().initialize(app)
db = AlchemyService().initialize(app).db

from src.models import metadata
model_service = ModelService().initialize(metadata)
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
