from siwaketime import db
from datetime import datetime

from siwaketime.config import Base , JST

class Entry(Base):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False, server_default='人生')
    memo = db.Column(db.Text)
    hour = db.Column(db.Float, nullable=False)
    genre = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DateTime)

    def __init__(self, title=None, memo=None, hour=None, genre=None, user_id=None, username= None, created_at= None):
        self.title = title
        self.memo = memo
        self.hour = hour
        self.genre = genre
        self.user_id = user_id
        self.username = username
        self.created_at = created_at

    def __repr__(self):
        return '<Entry id:{} title:{} memo:{} hour:{} genre:{} user_id:{} username:{} created_at:{}>'.format(self.id, self.title, self.memo, self.hour, self.genre, self.user_id, self.user_id, self.created_at) 


