from flask import Flask
from .extensions import db, ma
from .config import DevelopmentConfig

from .routes import title, building, aggregate


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.json.ensure_ascii = False

    db.init_app(app)
    ma.init_app(app)

    app.register_blueprint(title.bp_title, url_prefix="/api/v1/title")
    app.register_blueprint(building.building_bp, url_prefix="/api/v1/buildings")
    app.register_blueprint(aggregate.aggregate_bp, url_prefix="/api/v1/aggregate")

    return app
