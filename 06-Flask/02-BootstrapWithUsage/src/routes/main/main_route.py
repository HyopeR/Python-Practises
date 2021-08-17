from flask import Blueprint, render_template
from src.core.decorators.login_required import login_required
from src.routes.main.main_controller import MainController

main = Blueprint('main', __name__, template_folder='../../templates')


@main.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@main.route("/about", methods=['GET'])
def about():
    return render_template("about.html")


@main.route("/dashboard", methods=['GET'])
@login_required
def dashboard():
    status, data = MainController().dashboard()
    return render_template("dashboard.html", articles=data) if status else render_template("dashboard.html")


@main.route("/example", methods=['GET'])
def example():
    numbers = list(range(1, 10))
    users = [
        {"id": 1, "name": "John", "about": "The john about."},
        {"id": 2, "name": "Luisa", "about": "The Luisa about."},
        {"id": 3, "name": "Victor", "about": "The victor about."},
    ]

    return render_template("example.html", answer="No", operation=1, numbers=numbers, users=users)
