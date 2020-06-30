# source ./venv/bin/activate
# pip install Flask-RESTful
# pip install Flask-JWT (JSON Web Tokens for obfuscation and authentication)
# pip install Flask-SQLAlchemy

# installed libraries
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

# local libraries
from db import db
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'my secret'
api = Api(app)

# create the endpoint /auth
jwt = JWT(app, authenticate, identity)

# add resources the the endpoint
api.add_resource(Store, '/store/<string:name>') # i.e.: http://127.0.0.1:5000/store/ecomm
api.add_resource(StoreList, '/stores')          # i.e.: http://127.0.0.1:5000/stores
api.add_resource(Item, '/item/<string:name>') # i.e.: http://127.0.0.1:5000/item/salt
api.add_resource(ItemList, '/items')          # i.e.: http://127.0.0.1:5000/items
api.add_resource(UserRegister, '/register')   #  i.e.: http://127.0.0.1:5000/register

if __name__ == '__main__': # this gives the ability to import app.py without runing the application
    db.init_app(app)
    app.run(port=5000, debug=True)

# (on terminal)
# source venv/bin/activate
# python app.py 



