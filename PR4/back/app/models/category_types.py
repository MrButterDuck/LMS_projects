from app.extensions import db

class CategoryTypes(db.Model):
    __tablename__ = 'category_types'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('Категория', db.String(100), nullable=False)
    market_categories = db.relationship('MarketCategory', back_populates='category', cascade='all, delete')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'\nid: {self.id}, Категория: {self.name}'
