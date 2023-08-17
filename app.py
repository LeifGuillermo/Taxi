import logging
from app.views.routes import *
from app.views.users import *

logging.basicConfig(level=logging.DEBUG)
app.config.from_pyfile("../secrets.cfg")


if __name__ == "__main__":
    app.run(debug=True)
