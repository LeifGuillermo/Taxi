# Do not change order of statements in this file.
# Some lines depend on other lines.

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object("config")

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.models import *

from flask_login import LoginManager

login_manager = LoginManager()
login_manager.init_app(app)
