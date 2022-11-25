from siwaketime.app import db
from siwaketime.config import Base

class User(Base):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    hash = db.Column(db.Text, nullable=False)

    def __init__(self, username=None, hash=None):
        self.username = username
        self.hash = hash