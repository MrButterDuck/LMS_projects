from app.extensions import ma, db
from app.models import CategoryTypes

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CategoryTypes
        load_instance = True
        sqla_session = db.session

category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)
