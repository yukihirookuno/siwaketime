from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object('app.config')

db = SQLAlchemy()
db.init_app(app)

from app.views.users import user
app.register_blueprint(user)

from app.views.entries import entry
app.register_blueprint(entry)

from app.config import Base, engine 
Base.metadata.create_all(engine)



