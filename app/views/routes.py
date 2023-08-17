from flask import render_template, redirect, url_for, flash
from sqlalchemy.sql.functions import current_user

from app import app, db
from app.forms import BookingForm, RegistrationForm
from app.models import Booking, User

from flask_login import current_user, login_required


@app.route("/dashboard")
@login_required
def dashboard():
    return "Welcome to your dashboard, {}".format(current_user.username)


@app.route("/")
@app.route("/book", methods=["GET", "POST"])
def book():
    form = BookingForm()
    if form.validate_on_submit():
        booking = Booking(
            pickup_location=form.pickup_location.data,
            dropoff_location=form.dropoff_location.data,
            pickup_time=form.pickup_time.data,
        )
        booking.user_id = current_user.id
        db.session.add(booking)
        db.session.commit()
        flash("Your booking has been made!", "success")
        return redirect(url_for("dashboard)"))
    return render_template("book.html", title="Book", form=form)  # added this line


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for("book"))
    return render_template("register.html", title="Register", form=form)
