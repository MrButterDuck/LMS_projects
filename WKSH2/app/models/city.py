from app.extensions import db
from app.models.country import Country

class City(db.Model):
    __tablename__ = 'city'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('Город', db.String(100))
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    building = db.relationship("Building", cascade='all, delete')


    def __init__(self, name, country_id):
        self.name = name
        self.country_id = country_id

    def __repr__(self):
        return f'\nid: {self.id}, Тип: {self.name}'
