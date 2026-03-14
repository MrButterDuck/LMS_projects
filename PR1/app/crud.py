
from .extensions import db
from typing import Optional


def create(item):
    db.session.add(item)
    db.session.commit()

def read(model):
    query = model.query.all()
    print(query)

def update(model, item_id, **kwargs):
    item = model.query.get(item_id)
    if item:
        for key, value in kwargs.items():
            setattr(item, key, value)
        db.session.commit()
    read(model)

def delete(model, item_id):
    model.query.filter(model.id == item_id).delete()
    db.session.commit()
    read(model)

def get_or_create(model, **kwargs):
    instance = db.session.query(model).filter_by(**kwargs).first()
    if not instance:
        instance = model(**kwargs)
        db.session.add(instance)
        db.session.commit()
    return instance