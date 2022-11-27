from flask_script import Command
from app.__init__ import db
from app.config import engine
from app.config import Base

class InitDB(Command):
    "データベースの作成"


    def run(self):
        Base.metadata.create_all(bind=engine)