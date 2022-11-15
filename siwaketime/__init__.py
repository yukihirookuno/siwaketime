from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('siwaketime.config')
    db.init_app(app)
    
    from siwaketime.views.users import user
    app.register_blueprint(user)
    
    from siwaketime.views.entries import entry
    app.register_blueprint(entry)
    
    from siwaketime.config import Base, engine 
    Base.metadata.create_all(engine)

    return app

