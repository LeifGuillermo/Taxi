from flask import render_template, request, redirect, url_for, flash
from app import app


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            flash("Passwords do not match!", "danger")
            return redirect(url_for("register"))

        # TODO: hash the password and save to the user database.

        flash("Registration successful! Please login", "success")
        return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        # TODO: check the provided credentials against the database
        #  If valid, log the user in and redirect to a protected page or dashboard.

        flash("Login successful!", "success")
        return redirect(url_for("index"))
    return render_template("login.html")
