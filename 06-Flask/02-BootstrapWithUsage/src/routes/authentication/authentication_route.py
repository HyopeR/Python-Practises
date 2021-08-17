from flask import Blueprint, render_template, request, redirect, url_for, session

from src.routes.authentication.authentication_controller import AuthenticationController
from src.services.forms.RegisterForm import RegisterForm
from src.services.forms.LoginForm import LoginForm

authentication = Blueprint('authentication', __name__, template_folder='../../templates')


@authentication.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():
        AuthenticationController().register(form)

        # Url for metodu ile bir metodun ilişkili olduğu rotaya gidilebilir.
        return redirect(url_for('authentication.login'))
    else:
        return render_template("register.html", form=form)


@authentication.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate():
        login_success, data = AuthenticationController().login(form)
        route = "main.index" if login_success else "authentication.login"

        if login_success:
            session["logged_in"] = True
            session["username"] = data["username"]

        return redirect(url_for(route))
    else:
        return render_template("login.html", form=form)


@authentication.route("/logout", methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('main.index'))

