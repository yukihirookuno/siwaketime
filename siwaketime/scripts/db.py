from flask_script import Command
from siwaketime import db


class InitDB(Command):
    "データベースの作成"


    def run(self):
        db.create_all()