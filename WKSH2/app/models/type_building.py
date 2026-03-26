from app.extensions import db

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
