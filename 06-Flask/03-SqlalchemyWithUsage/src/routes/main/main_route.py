from flask import Blueprint
from src.routes.main.main_controller import MainController

main_route = Blueprint('main', __name__, template_folder='../../templates')


@main_route.route("/", methods=['GET'])
def main():
    return MainController().main()