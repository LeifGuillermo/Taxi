from app import app, login_manager
from app.models import User
from app.forms import LoginForm

from flask import render_template, request, redirect, url_for, flash
from sqlalchemy.sql.functions import current_user
from flask_login import login_user, logout_user, current_user

from urllib.parse import urlsplit


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or urlsplit(next_page).netloc != "":
            next_page = url_for("dashboard")
        return redirect(next_page)
    return render_template("login.html", title="Sign In", form=form)


@login_manager.unauthorized_handler
def unauthorized():
    flash("You must be logged in to view that page.")
    return redirect(url_for("login"))
