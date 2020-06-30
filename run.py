from app import app
from db import db

# run the application on heroku
db.init_app(app)

# create database tables
@app.before_first_request
def create_tables():
    db.create_all()
