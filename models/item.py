import sqlite3
from db import db

class ItemModel(db.Model):

    # SQL Alchemy defintions
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    # SQL Alchemy relation
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def __repr__(self):
        return (f"<ItemModel({self.name!r}, {self.price}, {self.store_id})>")

    def json(self):
        return {'name': self.name, 'price': self.price, 'store_id': self.store_id}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name LIMIT 1

    def save_to_db(self): # replace the insert and update methods by the SQL alchemy UPSERT
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self): # enable record exclusion
        db.session.delete(self)
        db.session.commit()

