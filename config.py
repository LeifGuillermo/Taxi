import os

basedir = os.path.abspath(os.path.dirname(__file__))
# store database in the root directory of project with the name `data.sqlite`
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data.sqlite")
# We don't need track modifications, and setting to false suppresses a warning.
SQLALCHEMY_TRACK_MODIFICATIONS = False
