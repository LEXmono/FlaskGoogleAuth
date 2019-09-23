from flask import Flask
from flask_google_auth.config import config

app = Flask(__name__)
app = Flask(__name__)
app.debug = config.DEBUG
app.secret_key = config.FLASK_SECRET_KEY

from flask_google_auth import views as views # noqa: E402