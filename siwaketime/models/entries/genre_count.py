from siwaketime.myapp.app import db
from siwaketime.config import Base 

class Genre_count(Base):
    __tablename__ = 'genre_counts'
    genre_counts_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    doryoku_count = db.Column(db.Integer, nullable=False)
    asobi_count = db.Column(db.Integer, nullable=False)
    muda_count = db.Column(db.Integer, nullable=False)
    kihon_count = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(30), nullable=False)

    def __init__(self, doryoku_count = None, asobi_count =None, muda_count = None, kihon_count=None, username = None
        ):
        self.doryoku_count = doryoku_count,
        self.asobi_count = asobi_count,
        self.muda_count = muda_count,
        self.kihon_count = kihon_count,
        self.username = username
