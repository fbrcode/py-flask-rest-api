from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from models.item import ItemModel

# resource is everything that is exposed by the API

class Item(Resource):
    parser = reqparse.RequestParser() # using the parser we only accept the items defined in the API
    parser.add_argument('price', 
        type=float, 
        required=True, 
        help="This field cannot left blank"
    )
    parser.add_argument('store_id', 
        type=int, 
        required=True, 
        help="Every item needs a store id"
    )

    @jwt_required()
    def get(self, name):
        """ get an item """
        item = ItemModel.find_by_name(name)
        if item: # if item is not None
            return item.json(), 200 # 200 code for OK

        return {'message': 'Item not found'}, 404 # 404 code when the item is not found
    
    @jwt_required()
    def post(self, name):
        """ add an item """
        # first look for errors, then stop or continue
        if ItemModel.find_by_name(name): # if an item already exists
            return {'message': "An item with name '{}' already exists.".format(name)}, 400 # 400 code is bad request, the client should not ask for this

        data = Item.parser.parse_args()
        item = ItemModel(name, **data) # unpack mode for ItemModel(name, data['price'], data['store_id'])

        try:
            item.save_to_db()
        except:
            return {'message': 'An error occurred inserting the item'}, 500 # 500 code is internal server error

        return item.json(), 201 # 201 code when item is created

    @jwt_required()
    def delete(self, name):
        """ delete an item """
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {'message': 'Item deleted'}, 200 # Ok
        
        return {'message': 'Item not found'}, 404 # 404 code when the item is not found

    @jwt_required()
    def put(self, name):
        """ create or update an item """
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)

        if item: # if is not none
            item.price = data['price'] # update item price
        else: # new item if not exists
            item = ItemModel(name, **data) # unpack mode for ItemModel(name, data['price'], data['store_id'])
        
        item.save_to_db()

        return item.json(), 200 # Ok


class ItemList(Resource):
    @jwt_required()
    def get(self):
        #return {'items': list(map(lambda x: x.json(), ItemModel.query.all()))}, 200 # using lambda function
        return {'items': [item.json() for item in ItemModel.query.all()]}, 200 # using list comprehension
