import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

# resource is everything that is exposed by the API

class UserRegister(Resource):
    parser = reqparse.RequestParser() # using the parser we only accept the items defined in the API
    parser.add_argument('username', 
        type=str, 
        required=True, 
        help="Username cannot left blank"
    )
    parser.add_argument('password', 
        type=str, 
        required=True, 
        help="Password cannot left blank"
    )

    def post(self):
        data = UserRegister.parser.parse_args()
        
        if UserModel.find_by_username(data['username']): # if username is not None:
            return {"message": "A user with that username already exists"}

        user = UserModel(**data) # unpack mode for UserModel(data['username'], data['password'])
        user.save_to_db()
        
        return {"message": "User created successfully"}, 201 # 201 code when item is created
