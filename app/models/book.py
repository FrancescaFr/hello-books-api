from app import db

class Book(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)

    @classmethod
    def from_dict(cls,input_data):
        return cls(
                    title=input_data["title"],
                    description=input_data["description"],
                )

    def to_dict(self):
        return dict(
                    id=self.id,
                    title=self.title,
                    description=self.description,
                )