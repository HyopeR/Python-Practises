from flask import Blueprint, render_template, request, redirect, url_for

from src.routes.authentication.authentication_controller import AuthenticationController
from src.services.forms.RegisterForm import RegisterForm

authentication = Blueprint('authentication', __name__, template_folder='../../templates')


@authentication.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate():



        # Url for metodu ile bir metodun ilişkili olduğu rotaya gidilebilir.
        return redirect(url_for('main.index'))
    else:
        AuthenticationController(form).register()
        return render_template("register.html", form=form)


@authentication.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
    else:
        return render_template("login.html")
