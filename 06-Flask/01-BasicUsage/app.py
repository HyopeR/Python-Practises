from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    number = 10
    article = {"title": 'Hello World!!!', "body": 'Props with dictionary.', "author": 'Tolgahan Çelik'}

    return render_template("index.html", number=number, article=article)


@app.route("/about", methods=['GET'])
def about():
    return "About Me"


@app.route("/about/<id>", methods=['GET'])
def one_about(id):
    return "About Me {}".format(id)


@app.route("/anything", methods=['GET'])
def anything():
    number = 10
    article = {"title": 'Hello World!!!', "body": 'Props with dictionary.', "author": 'Tolgahan Çelik'}

    return render_template("anything.html", number=number, article=article)


if __name__ == "__main__":
    app.run(debug=True)
