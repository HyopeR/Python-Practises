from flask import Blueprint, render_template

main = Blueprint('main', __name__, template_folder='../../templates')


@main.route("/", methods=['GET'])
def index():
    return render_template("index.html")


@main.route("/about", methods=['GET'])
def about():
    return render_template("about.html")


@main.route("/about/<id>", methods=['GET'])
def one_about(id):
    return "About {}".format(id)


@main.route("/articles", methods=['GET'])
def articles():
    return render_template("articles.html")


@main.route("/article/<id>", methods=['GET'])
def one_article(id):
    return "Article {}".format(id)


@main.route("/example", methods=['GET'])
def example():
    numbers = list(range(1, 10))
    users = [
        {"id": 1, "name": "John", "about": "The john about."},
        {"id": 2, "name": "Luisa", "about": "The Luisa about."},
        {"id": 3, "name": "Victor", "about": "The victor about."},
    ]

    return render_template("example.html", answer="No", operation=1, numbers=numbers, users=users)
