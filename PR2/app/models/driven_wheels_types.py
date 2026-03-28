from app.extensions import db

class DrivenWheelsTypes(db.Model):
    __tablename__ = 'driven_wheels_types'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('Привод', db.String(100), nullable=False)
    features = db.relationship('CarFeatures', back_populates='driven_wheels', cascade='all, delete')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'\nid: {self.id}, Привод: {self.name}'
