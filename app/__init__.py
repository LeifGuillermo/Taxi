from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# run export FLASK_APP=app -> can also update it in the .bashrc file to prevent having to do it every time.
app = Flask(__name__)
app.config.from_object("config")
app.config["SECRET_KEY"]

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class TaxiRide(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pickup_location = db.Column(db.String(128))
    dropoff_location = db.Column(db.String(128))
    fare = db.Column(db.Float)
