from flask_script import Command
from siwaketime import db
from siwaketime.config import engine
from siwaketime.config import Base

class InitDB(Command):
    "データベースの作成"


    def run(self):
        Base.metadata.create_all(bind=engine)