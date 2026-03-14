from flask import Flask
from .config import DevelopmentConfig
from .extensions import db
from .models import Country, City, Building, TypeBuilding
from .crud import create, read, update, delete
# Импортируем маршруты
from app.view import main

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)

    app.app_context().push()
    db.create_all()
    b_list = ['Небоскреб', 'Антенная мачта', 'Бетонная башня', 'Радиомачта', 'Гиперболоидная башня', 'Дымовая труба', 'Решётчатая мачта', 'Башня', 'Мост']
    for b in b_list:
        break
        create(TypeBuilding(b)) 
    # read(TypeBuilding)
    # update(TypeBuilding, 9, name="Мосты")
    # delete(TypeBuilding, 9,)


    app.register_blueprint(main)
    return app

    