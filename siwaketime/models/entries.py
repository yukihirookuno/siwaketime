from csv import unregister_dialect
from pickle import FALSE
from tkinter.messagebox import NO
from siwaketime import db
from datetime import datetime

class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False, server_default='人生')
    memo = db.Column(db.Text)
    hour = db.Column(db.Float, nullable=False)
    genre = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(30), nullable=False)
    created_at = db.Column(db.DateTime)

    def __init__(self, title=None, memo=None, hour=None, genre=None, user_id=None, username= None):
        self.title = title
        self.memo = memo
        self.hour = hour
        self.genre = genre
        self.user_id = user_id
        self.username = username
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Entry id:{} title:{} memo:{} hour:{} genre:{} user_id:{} username:{}>'.format(self.id, self.title, self.memo, self.hour, self.genre, self.user_id, self.user_id) 


