from app import db

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    genre = db.Column(db.String)
    # book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    # books = db.relationship("Genre", back_populates="genres")

@classmethod
def from_dict(cls, data_dict):
    return cls(genre=data_dict["genre"])

def to_dict(self):
    return dict(
                id=self.id,
                genre=self.genre_id
            )