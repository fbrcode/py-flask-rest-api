import sqlite3
from db import db

class StoreModel(db.Model):

    # SQL Alchemy defintions
    __tablename__ = 'stores'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # SQL Alchemy relation
    #items = db.relationship('ItemModel') # more expensive on write time
    # lazy=dynamic means that the object won't be created right away
    # in this case store model is created when we access the data, so this is the preferred mode
    items = db.relationship('ItemModel', lazy='dynamic') # more expensive on read time 

    def __init__(self, name):
        self.name = name

    def json(self):
        #return {'name': self.name, 'items': [item.json() for item in self.items]} # more expensive on write time
        # .all() is a query builder, so table access happen every time json() method is called
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]} # more expensive on read time (table access)

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM stores WHERE name=name LIMIT 1

    def save_to_db(self): # replace the insert and update methods by the SQL alchemy UPSERT
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self): # enable record exclusion
        db.session.delete(self)
        db.session.commit()

