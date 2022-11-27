from flask import Flask , Blueprint
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object('app.config')

db = SQLAlchemy()
db.init_app(app)


from app.config import Base, engine 
Base.metadata.create_all(engine)



