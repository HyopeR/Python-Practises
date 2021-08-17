from flask import Blueprint, render_template, request, redirect, url_for, session
from src.core.decorators.login_required import login_required

from src.routes.article.article_controller import ArticleController
from src.services.forms.ArticleForm import ArticleForm

article = Blueprint('article', __name__, template_folder='../../templates')


@article.route("/articles", methods=['GET'])
def articles():
    status, data = ArticleController().articles()

    return render_template("articles.html", articles=data) if status else render_template("articles.html")


@article.route("/article/<id>", methods=['GET'])
def one_article(id):
    status, data = ArticleController().one_article(id)
    return render_template("article.html", article=data) if status else render_template("article.html")


@article.route("/article/add", methods=['GET', 'POST'])
@login_required
def add_article():
    form = ArticleForm(request.form)

    if request.method == "POST" and form.validate():
        status = ArticleController().add_article(form)

        if status:
            return redirect(url_for("main.dashboard"))

    else:
        return render_template("set_article.html", form=form, type="Add")


@article.route("/article/update/<id>", methods=['GET', 'POST'])
@login_required
def update_article(id):
    status, data = ArticleController().update_article(id, None)

    if request.method == "POST":
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        form = ArticleForm(request.form)
        status, data = ArticleController().update_article(id, form)
        return redirect(url_for("main.dashboard"))
    else:
        if status:
            form = ArticleForm()
            form.title.data = data["title"]
            form.content.data = data["content"]
            return render_template("set_article.html", form=form, type="Update")

        return redirect(url_for("main.index"))


@article.route("/article/delete/<id>", methods=['GET'])
@login_required
def delete_article(id):
    status = ArticleController().delete_article(id)
    return redirect(url_for('main.dashboard')) if status else redirect(url_for('main.index'))
