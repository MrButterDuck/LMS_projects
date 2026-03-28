from app.extensions import db

class MarketCategory(db.Model):
    __tablename__ = 'market_category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_id = db.Column(db.Integer, db.ForeignKey('category_types.id'))
    model_id = db.Column(db.Integer, db.ForeignKey('car_model.id'))

    category = db.relationship('CategoryTypes', back_populates='market_categories')
    model = db.relationship('CarModel', back_populates='market_categories')

    def __init__(self, category_id, model_id):
        self.category_id = category_id
        self.model_id = model_id

    def __repr__(self):
        return f'\nid: {self.id}, category_id: {self.category_id}, model_id: {self.model_id}'
