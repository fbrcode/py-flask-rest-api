from flask_restful import Resource
from flask_jwt import jwt_required

from models.store import StoreModel

class Store(Resource):
    @jwt_required()
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200 # status ok, which is the default (optional)
        return {'message': 'Store not found'}, 404 # return means a tuple with body and status code

    @jwt_required()
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': 'A store with name {} already exists'.format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occurred while creating a store'}, 500

        return store.json(), 201

    @jwt_required()
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        
        return {'message': 'Store deleted'}


class StoreList(Resource):
    @jwt_required()
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}
