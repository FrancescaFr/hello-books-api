from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)

    @classmethod
    def from_dict(cls, data_dict):
        return cls(title=data_dict["title"], 
            description=data_dict["description"])

    def to_dict(self):
        return dict(
                    id=self.id,
                    title=self.title,
                    description=self.description
                )