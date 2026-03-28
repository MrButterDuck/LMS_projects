from app.extensions import db

class CarMake(db.Model):
    __tablename__ = 'car_make'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('Марка', db.String(100), nullable=False)
    models = db.relationship('CarModel', back_populates='make', cascade='all, delete')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'\nid: {self.id}, Марка: {self.name}'
