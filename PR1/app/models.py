from .extensions import db


class CarMake(db.Model):
    __tablename__ = 'car_make'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('Марка', db.String(100), nullable=False)
    models = db.relationship('CarModel', cascade='all, delete')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'\nid: {self.id}, Марка: {self.name}'


class CarModel(db.Model):
    __tablename__ = 'car_model'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('Модель', db.String(100), nullable=False)
    make_id = db.Column(db.Integer, db.ForeignKey('car_make.id'))
    features = db.relationship('CarFeatures', cascade='all, delete')
    market_categories = db.relationship('MarketCategory', cascade='all, delete')

    def __init__(self, name, make_id):
        self.name = name
        self.make_id = make_id

    def __repr__(self):
        return f'\nid: {self.id}, Модель: {self.name}'


class CategoryTypes(db.Model):
    __tablename__ = 'category_types'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('Категория', db.String(100), nullable=False)
    market_categories = db.relationship('MarketCategory', cascade='all, delete')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'\nid: {self.id}, Категория: {self.name}'


class MarketCategory(db.Model):
    __tablename__ = 'market_category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category_types.id'))
    model_id = db.Column(db.Integer, db.ForeignKey('car_model.id'))

    def __init__(self, category_id, model_id):
        self.category_id = category_id
        self.model_id = model_id

    def __repr__(self):
        return f'\nid: {self.id}, category_id: {self.category_id}, model_id: {self.model_id}'


class TransmissionTypes(db.Model):
    __tablename__ = 'transmission_types'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('Трансмиссия', db.String(100), nullable=False)
    features = db.relationship('CarFeatures', cascade='all, delete')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'\nid: {self.id}, Трансмиссия: {self.name}'


class DrivenWheelsTypes(db.Model):
    __tablename__ = 'driven_wheels_types'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('Привод', db.String(100), nullable=False)
    features = db.relationship('CarFeatures', cascade='all, delete')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'\nid: {self.id}, Привод: {self.name}'


class VehicleTypes(db.Model):
    __tablename__ = 'vehicle_types'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('Тип кузова', db.String(100), nullable=False)
    features = db.relationship('CarFeatures', cascade='all, delete')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'\nid: {self.id}, Тип кузова: {self.name}'


class CarFeatures(db.Model):
    __tablename__ = 'car_features'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model_id = db.Column(db.Integer, db.ForeignKey('car_model.id'))
    year = db.Column('Год', db.Integer)
    transmission_id = db.Column(db.Integer, db.ForeignKey('transmission_types.id'))
    driven_wheels_id = db.Column(db.Integer, db.ForeignKey('driven_wheels_types.id'))
    vehicle_type_id = db.Column(db.Integer, db.ForeignKey('vehicle_types.id'))
    number_of_doors = db.Column('Количество дверей', db.Integer)
    engine_cylinders = db.Column('Цилиндры двигателя', db.Integer)
    engine_hp = db.Column('Мощность (HP)', db.Float)

    def __init__(self, model_id, year, transmission_id, driven_wheels_id,
                 vehicle_type_id, number_of_doors, engine_cylinders, engine_hp):
        self.model_id = model_id
        self.year = year
        self.transmission_id = transmission_id
        self.driven_wheels_id = driven_wheels_id
        self.vehicle_type_id = vehicle_type_id
        self.number_of_doors = number_of_doors
        self.engine_cylinders = engine_cylinders
        self.engine_hp = engine_hp

    def __repr__(self):
        return f'\nid: {self.id}, model_id: {self.model_id}, year: {self.year}'