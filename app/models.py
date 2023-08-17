from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

from flask_login import UserMixin


class Driver(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    base_rate = db.Column(db.Float, nullable=False)
    tax_rate = db.Column(db.Float, nullable=False)
    distance_to_pickup_fee = db.Column(db.Float, nullable=False)
    shared_ride_discount = db.Column(db.Float, nullable=False)
    is_shared_ride = db.Column(db.Boolean, nullable=False, default=False)
    bookings = db.relationship("Booking", backref="driver", lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<Driver {self.username}>"


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    bookings = db.relationship("Booking", backref="passenger", lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"<User {self.username}>"


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    driver_id = db.Column(db.Integer, db.ForeignKey("driver.id"), nullable=True)
    pickup_location = db.Column(db.String(120), nullable=False)
    dropoff_location = db.Column(db.String(120), nullable=False)
    pickup_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_cancelled = db.Column(db.Boolean, nullable=False, default=False)
    is_completed = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"<Booking {self.id} by User {self.user_id}>"
