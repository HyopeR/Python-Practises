from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    numbers = list(range(1, 10))
    users = [
        {"id": 1, "name": "John", "about": "The john about."},
        {"id": 2, "name": "Luisa", "about": "The Luisa about."},
        {"id": 3, "name": "Victor", "about": "The victor about."},
    ]

    return render_template("index.html", answer="No", operation=1, numbers=numbers, users=users)


@app.route("/about", methods=['GET'])
def about():
    return render_template("about.html")


@app.route("/about/<id>", methods=['GET'])
def one_about(id):
    return "About {}".format(id)


@app.route("/articles", methods=['GET'])
def articles():
    return render_template("articles.html")


@app.route("/article/<id>", methods=['GET'])
def one_article(id):
    return "Article {}".format(id)


if __name__ == "__main__":
    app.run(debug=True)
