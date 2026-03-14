from .extensions import db

class Country(db.Model):
    __tablename__ = 'country'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('Страна', db.String(100), nullable=False)
    cities = db.relationship("City", cascade='all, delete')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'\nid: {self.id}, Тип: {self.name}'

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

class Building(db.Model):
    __tablename__ = 'building'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column('Название', db.String(200))
    type_building_id = db.Column(db.Integer, db.ForeignKey('type_building.id'))
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'))
    year = db.Column(db.Integer)
    height = db.Column(db.Float)

    def __init__(self, title, type_building_id, city_id, year, height):
        self.title = title
        self.type_building_id = type_building_id
        self.city_id = city_id
        self.year = year
        self.height = height

    def __repr__(self):
        return f'\nid: {self.id}, Тип: {self.title}'

class TypeBuilding(db.Model):
    __tablename__ = 'type_building'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('Наименование', db.String(200))
    building = db.relationship("Building", cascade='all, delete')

    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return f'\nid: {self.id}, Тип: {self.name}'