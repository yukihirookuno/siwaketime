from siwaketime import db
from siwaketime.config import Base 

class Genre_count(Base):
    __tablename__ = 'genre_counts'
    genre_counts_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    gannbari_count = db.Column(db.Integer, nullable=False)
    asobi_count = db.Column(db.Integer, nullable=False)
    muda_count = db.Column(db.Integer, nullable=False)

    def __init__(self, ganbari_count = None, asobi_count =None, muda_count = None
        ):
        self.gannbari_count = ganbari_count,
        self.asobi_count = asobi_count,
        self.muda_count = muda_count

    #def __repr__(self):
    #    return '<Genre_count genre_count_id :{} ganbari_count :{} asobi_count :{} muda_count:{}>'.format(
    #        self.gannbari_count, self.asobi_count, self.muda_count
    #    )