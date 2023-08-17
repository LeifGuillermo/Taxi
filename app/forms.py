from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField,
    DateTimeField,
    ValidationError,
    BooleanField,
)

from wtforms.validators import data_required, email, equal_to
from app.models import User


class BookingForm(FlaskForm):
    pickup_location = StringField("Pickup Location", validators=[data_required()])
    dropoff_location = StringField("Dropoff Location", validators=[data_required()])
    pickup_time = DateTimeField(
        "Pickup Time", validators=[data_required()], format="%Y-%m-%d %H:%M"
    )
    submit = SubmitField("Book Now")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[data_required()])
    password = PasswordField("Password", validators=[data_required()])
    remember_me = BooleanField("Remember Me")
    submit = SubmitField("Sign In")


# noinspection PyMethodMayBeStatic
class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[data_required()])
    email = StringField("Email", validators=[data_required(), email()])
    password = PasswordField("Password", validators=[data_required()])
    password2 = PasswordField(
        "Repeat Password", validators=[data_required(), equal_to("password")]
    )
    submit = SubmitField("Register")

    def validate_username(self, username_field):  # Renamed parameter to avoid shadowing
        user = User.query.filter_by(username=username_field.data).first()
        if user is not None:
            raise ValidationError("Please use a different username.")

    def validate_email(self, email_field):  # Renamed parameter to avoid shadowing
        user = User.query.filter_by(email=email_field.data).first()
        if user is not None:
            raise ValidationError("Please use a different email address.")
