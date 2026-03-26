from app.extensions import db

class Building(db.Model):
    __tablename__ = 'building'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column('Название', db.String(200))
    type_building_id = db.Column(db.Integer, db.ForeignKey('type_building.id'))
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    year = db.Column(db.Integer)
    height = db.Column(db.Float)

    city = db.relationship("City")
    type_building = db.relationship("TypeBuilding")

    def __init__(self, title, type_building_id, city_id, year, height):
        self.title = title
        self.type_building_id = type_building_id
        self.city_id = city_id
        self.year = year
        self.height = height

    def __repr__(self):
        return f'\nid: {self.id}, Тип: {self.title}'
