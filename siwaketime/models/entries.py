from siwaketime import db
from datetime import datetime

class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False, server_default='人生')
    memo = db.Column(db.Text)
    hour = db.Column(db.Float, nullable=False)
    genre = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime)

    def __init__(self, title=None, memo=None, hour=None, genre=None):
        self.title = title
        self.memo = memo
        self.hour = hour
        self.genre = genre
        self.created_at = datetime.utcnow()

    def __repr__(self):
        return '<Entry id:{} title:{} memo:{} hour:{} genre:{}>'.format(self.id, self.title, self.memo, self.hour, self.genre) 


