from flask import Flask
from src.core.handlers.ErrorHandler import ErrorHandler
from src.helpers.error.ErrorDescriptive import ErrorDescriptive
from src.routes import Routes

app = Flask(__name__, template_folder='./src/templates')
from manage import *

RouteModule = Routes().initialize(app)


@app.errorhandler(404)
def catch_route_not_found(e):
    base_err = ErrorDescriptive.route_not_found

    err = ErrorHandler(base_err.message, base_err.key, 404, str(e))
    return err.handle()


@app.errorhandler(Exception)
def catch_error(e):
    try:
        return e.handle()
    except Exception as error:
        base_err = ErrorDescriptive.unexpected_error

        err = ErrorHandler(base_err.message, base_err.key, 400, str(error))
        return err.handle()
