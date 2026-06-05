from app.extensions import db

class VehicleTypes(db.Model):
    __tablename__ = 'vehicle_types'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('Тип кузова', db.String(100), nullable=False)
    features = db.relationship('CarFeatures', back_populates='vehicle_type', cascade='all, delete')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'\nid: {self.id}, Тип кузова: {self.name}'
