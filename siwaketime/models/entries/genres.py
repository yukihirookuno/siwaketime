from siwaketime import db
from siwaketime.config import Base 

class Genre(Base):
    __tablename__ = 'genres'
    genres_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genre_am12 = db.Column(db.String(10), nullable=False)
    genre_am1 = db.Column(db.String(10),nullable=False)
    genre_am2 = db.Column(db.String(10),nullable=False)
    genre_am3 = db.Column(db.String(10),nullable=False)
    genre_am4 = db.Column(db.String(10),nullable=False)
    genre_am5 = db.Column(db.String(10),nullable=False)
    genre_am6 = db.Column(db.String(10),nullable=False)
    genre_am7 = db.Column(db.String(10),nullable=False)
    genre_am8 = db.Column(db.String(10),nullable=False)
    genre_am9 = db.Column(db.String(10),nullable=False)
    genre_am10 = db.Column(db.String(10),nullable=False)
    genre_am11 = db.Column(db.String(10),nullable=False)
    genre_pm12 = db.Column(db.String(10),nullable=False)
    genre_pm1 = db.Column(db.String(10),nullable=False)
    genre_pm2 = db.Column(db.String(10),nullable=False)
    genre_pm3 = db.Column(db.String(10),nullable=False)
    genre_pm4 = db.Column(db.String(10),nullable=False)
    genre_pm5 = db.Column(db.String(10),nullable=False)
    genre_pm6 = db.Column(db.String(10),nullable=False)
    genre_pm7 = db.Column(db.String(10),nullable=False)
    genre_pm8 = db.Column(db.String(10),nullable=False)
    genre_pm9 = db.Column(db.String(10),nullable=False)
    genre_pm10 = db.Column(db.String(10),nullable=False)
    genre_pm11 = db.Column(db.String(10),nullable=False)

    def __init__(self, genre_am12 = None, genre_am1 = None, genre_am2 = None, genre_am3 = None, genre_am4 = None,
        genre_am5 = None,genre_am6 = None,genre_am7 = None,genre_am8 = None,genre_am9 = None,genre_am10 = None, 
        genre_am11 = None,genre_pm12 = None,genre_pm1 = None,genre_pm2 = None,genre_pm3 = None,genre_pm4 = None,
        genre_pm5 = None,genre_pm6 = None,genre_pm7 = None,genre_pm8 = None,genre_pm9 = None,genre_pm10 = None,genre_pm11 = None
        ):
        self.genre_am12 = genre_am12,
        self.genre_am1 = genre_am1,
        self.genre_am2 = genre_am2,
        self.genre_am3 = genre_am3,
        self.genre_am4 = genre_am4,
        self.genre_am5 = genre_am5,
        self.genre_am6 = genre_am6,
        self.genre_am7 = genre_am7,
        self.genre_am8 = genre_am8,
        self.genre_am9 = genre_am9,
        self.genre_am10 = genre_am10,
        self.genre_am11 = genre_am11,
        self.genre_pm12 = genre_pm12,
        self.genre_pm1 = genre_pm1,
        self.genre_pm2 = genre_pm2,
        self.genre_pm3 = genre_pm3,
        self.genre_pm4 = genre_pm4,
        self.genre_pm5 = genre_pm5,
        self.genre_pm6 = genre_pm6,
        self.genre_pm7 = genre_pm7,
        self.genre_pm8 = genre_pm8,
        self.genre_pm9 = genre_pm9,
        self.genre_pm10 = genre_pm10,
        self.genre_pm11 = genre_pm11

    #def __repr__(self):
    #    return '<Genre genres_id :{} genre_am12 :{} genre_am1 :{} genre_am2 :{} genre_am3 :{} genre_am4 :{} genre_am5 :{} genre_am6 :{} genre_am_7 :{} genre_am8 :{} genre_am9 :{} genre_am10 :{} genre_am11 :{} genre_pm12 :{} genre_pm1 :{} genre_pm2 :{} genre_pm3 :{} genre_pm4 :{} genre_pm5 :{} genre_pm6:{} genre_pm7 :{} genre_pm8 :{} genre_pm9 :{} genre_pm10 :{} genre_pm11 :{}>'.format(
    #        self.genres_id, self.genre_am12, self.genre_am1, self.genre_am2, self.genre_am3, self.genre_am4, self.genre_am5, self.genre_am6, self.genre_am7, self.genre_am8, 
    #        self.genre_am9, self.genre_am10, self.genre_am11, self.genre_pm12, self.genre_pm1, self.genre_pm2, self.genre_pm3, self.genre_pm4, self.genre_pm5, self.genre_pm6, 
    #        self.genre_pm7, self.genre_pm8, self.genre_pm9, self.genre_pm10, self.genre_pm11
    #   ) 