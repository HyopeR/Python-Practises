from flask import Flask
from src.core.handlers.ErrorHandler import ErrorHandler
from src.routes import Routes

app = Flask(__name__, template_folder='./src/templates')
from manage import *

RouteModule = Routes().initialize(app)


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
