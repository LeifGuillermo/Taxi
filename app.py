from flask import render_template
from app import app

from app.routes import register, login


@app.route("/")
def hello_world():
    return render_template("hello.html")


if __name__ == "__main__":
    app.run(debug=True)
