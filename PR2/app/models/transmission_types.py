from app.extensions import db

class TransmissionTypes(db.Model):
    __tablename__ = 'transmission_types'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('Трансмиссия', db.String(100), nullable=False)
    features = db.relationship('CarFeatures', back_populates='transmission', cascade='all, delete')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'\nid: {self.id}, Трансмиссия: {self.name}'
