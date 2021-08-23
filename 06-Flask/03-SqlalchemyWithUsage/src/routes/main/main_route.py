from flask import Blueprint
from src.services.EnvironmentService import EnvironmentService
from src.routes.main.main_controller import MainController

main_route = Blueprint('main', __name__, template_folder='../../templates')


@main_route.route("/", methods=['GET'])
def main():
    secret_key = EnvironmentService().get_one("YOUR_KEY")

    return MainController().main()
