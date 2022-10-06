from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('siwaketime.config')

db = SQLAlchemy(app)

from siwaketime.views.users import user
app.register_blueprint(user)

from siwaketime.views.entries import entry
app.register_blueprint(entry)

