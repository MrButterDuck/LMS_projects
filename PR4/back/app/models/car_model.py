from app.extensions import db

class CarModel(db.Model):
    __tablename__ = 'car_model'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('Модель', db.String(100), nullable=False)
    make_id = db.Column(db.Integer, db.ForeignKey('car_make.id'))

    make = db.relationship('CarMake', back_populates='models')
    features = db.relationship('CarFeatures', back_populates='model', cascade='all, delete')
    market_categories = db.relationship('MarketCategory', back_populates='model', cascade='all, delete')

    def __init__(self, name, make_id):
        self.name = name
        self.make_id = make_id

    def __repr__(self):
        return f'\nid: {self.id}, Модель: {self.name}, make_id: {self.make_id}'
