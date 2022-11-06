from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    # genres = db.relationship("Genre", secondary="books_genre" back_populates="genres")

    @classmethod
    def from_dict(cls, data_dict):
        return cls(title=data_dict["title"], 
            description=data_dict["description"])

    def to_dict(self):
        book_dict = dict(
                        id=self.id,
                        title=self.title,
                        description=self.description
                        )
        if self.genres:
            genre_names = [genre.name for genre in self.genres]
            book_dict["genres"] = genre_names
        return book_dict