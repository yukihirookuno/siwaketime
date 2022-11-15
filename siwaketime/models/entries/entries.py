from siwaketime import db
from siwaketime.config import engine, Base 
import sys

class Entry(Base):
    __tablename__ = 'entries'
    entry_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.Text, nullable=False)
    text= db.Column(db.Text)
    user_id = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(30), nullable=False)

    def __init__(self, date = None, text = None, user_id = None,username = None,
        ):
        self.date = date,
        self.text = text,
        self.user_id = user_id,
        self.username = username

    #def __repr__(self):
    #    return '<Entry entry_id :{} date :{} text :{} user_id :{} username :{}>'.format(
    #        self.date, self.text, self.user_id, self.username
    #    ) 