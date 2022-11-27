from __init__ import db
from app.config import Base 

class Title(Base):
    __tablename__ = 'titles'
    titles_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title_am12 = db.Column(db.String(30))
    title_am1 = db.Column(db.String(30))
    title_am2 = db.Column(db.String(30))
    title_am3 = db.Column(db.String(30))
    title_am4 = db.Column(db.String(30))
    title_am5 = db.Column(db.String(30))
    title_am6 = db.Column(db.String(30))
    title_am7 = db.Column(db.String(30))
    title_am8 = db.Column(db.String(30))
    title_am9 = db.Column(db.String(30))
    title_am10 = db.Column(db.String(30))
    title_am11 = db.Column(db.String(30))
    title_pm12 = db.Column(db.String(30))
    title_pm1 = db.Column(db.String(30))
    title_pm2 = db.Column(db.String(30))
    title_pm3 = db.Column(db.String(30))
    title_pm4 = db.Column(db.String(30))
    title_pm5 = db.Column(db.String(30))
    title_pm6 = db.Column(db.String(30))
    title_pm7 = db.Column(db.String(30))
    title_pm8 = db.Column(db.String(30))
    title_pm9 = db.Column(db.String(30))
    title_pm10 = db.Column(db.String(30))
    title_pm11  = db.Column(db.String(30))

    def __init__(self, title_am12 = None, title_am1 = None, title_am2 = None, title_am3 = None, title_am4 = None, 
        title_am5 = None, title_am6 = None,title_am7 = None,title_am8 = None, title_am9 = None, title_am10 = None, 
        title_am11 = None, title_pm12 = None, title_pm1 = None, title_pm2 = None,title_pm3 = None,title_pm4 = None, 
        title_pm5 = None, title_pm6 = None, title_pm7 = None, title_pm8 = None, title_pm9 = None, title_pm10 = None, title_pm11 = None
        ):
        self.title_am12 = title_am12,
        self.title_am1 = title_am1,
        self.title_am2 = title_am2,
        self.title_am3 = title_am3,
        self.title_am4 = title_am4,
        self.title_am5 = title_am5,
        self.title_am6 = title_am6,
        self.title_am7 = title_am7,
        self.title_am8 = title_am8,
        self.title_am9 = title_am9,
        self.title_am10 = title_am10,
        self.title_am11 = title_am11,
        self.title_pm12 = title_pm12,
        self.title_pm1 = title_pm1,
        self.title_pm2 = title_pm2,
        self.title_pm3 = title_pm3,
        self.title_pm5 = title_pm5,
        self.title_pm6 = title_pm6,
        self.title_pm7 = title_pm7,
        self.title_pm8 = title_pm8,
        self.title_pm9 = title_pm9,
        self.title_pm10 = title_pm10,
        self.title_pm11 = title_pm11