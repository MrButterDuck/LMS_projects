from app.extensions import db

class CarFeatures(db.Model):
    __tablename__ = 'car_features'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model_id = db.Column(db.Integer, db.ForeignKey('car_model.id'))
    year = db.Column('year', db.Integer)
    transmission_id = db.Column(db.Integer, db.ForeignKey('transmission_types.id'))
    driven_wheels_id = db.Column(db.Integer, db.ForeignKey('driven_wheels_types.id'))
    vehicle_type_id = db.Column(db.Integer, db.ForeignKey('vehicle_types.id'))
    number_of_doors = db.Column('number_of_doors', db.Integer)
    engine_cylinders = db.Column('engine_cylinders', db.Integer)
    engine_hp = db.Column('engine_hp', db.Float)

    model = db.relationship('CarModel', back_populates='features')
    transmission = db.relationship('TransmissionTypes', back_populates='features')
    driven_wheels = db.relationship('DrivenWheelsTypes', back_populates='features')
    vehicle_type = db.relationship('VehicleTypes', back_populates='features')

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
