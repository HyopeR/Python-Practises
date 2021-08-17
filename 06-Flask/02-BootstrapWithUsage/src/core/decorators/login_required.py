from flask import redirect, url_for, session, flash
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorate(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, **kwargs)
        else:
            flash("Please login to view this page.", "warning")
            return redirect(url_for("authentication.login"))

    return decorate
