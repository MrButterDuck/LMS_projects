from flask import Flask
from .config import DevelopmentConfig
from .extensions import db
from .crud import create, read, update, delete
# Импортируем маршруты
from app.view import main

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)

    app.app_context().push()
    db.create_all()

    app.register_blueprint(main)
    return app

    