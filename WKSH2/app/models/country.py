from app.extensions import db

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
