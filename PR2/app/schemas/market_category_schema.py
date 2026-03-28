from app.extensions import ma, db
from app.models import MarketCategory
from app.schemas.category_schema import CategorySchema

class MarketCategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MarketCategory
        load_instance = True
        sqla_session = db.session

    category = ma.Nested("CategorySchema", dump_only=True)

market_category_schema = MarketCategorySchema()
market_categories_schema = MarketCategorySchema(many=True)
