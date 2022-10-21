from siwaketime import db
from siwaketime.config import Base

class User(Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    hash = db.Column(db.Text, nullable=False)

    def __init__(self, username=None, hash=None):
        self.username = username
        self.hash = hash

    def __repr__(self):
        return '<Entry id:{} username:{} hash:{}>'.format(self.id, self.username, self.hash) 