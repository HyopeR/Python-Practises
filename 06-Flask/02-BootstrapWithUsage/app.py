from flask import Flask
from src.helpers.mysql.MysqlService import MysqlService
from src.core.handlers.ErrorHandler import ErrorHandler
from src.routes.index import Routes

app = Flask(__name__, template_folder='./src/templates')
app.secret_key = "ybblog"

mysql = MysqlService.get_instance(app)
routes = Routes.get_instance(app)


# @app.errorhandler(404)
# def catch_route_not_found(e):
#     err = ErrorHandler("Route is not found.", "route_not_found", status_code=404)
#     return err.handle()
#
#
# @app.errorhandler(Exception)
# def catch_error(e):
#     try:
#         return e.handle()
#     except Exception:
#         err = ErrorHandler("Unexpected error.", "unexpected_error", status_code=400)
#         return err.handle()


if __name__ == "__main__":
    app.run(debug=True)
