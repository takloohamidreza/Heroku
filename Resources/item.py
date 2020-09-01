from flask_restful import Resource,reqparse
from flask_jwt import jwt_required
from models.Item import itemModel
class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
    type = float,
    required = True,
    help = 'this field can not be empty'
    )
    parser.add_argument('store_id',
    type = int,
    required = True,
    help = 'every item need a store_id'
        )

    @jwt_required()
    def get(self,name):
        item = itemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message':'item not found'},404
    def post(self,name):
        if itemModel.find_by_name(name):
            return {'message':'item already has exist with name of {}'.format(name)},400

        data = Item.parser.parse_args()
        item = itemModel(name , data['price'],data['store_id'])

        try:
            itemModel.save_to_db(item)
        except:
            return {'message':'an error occoured in post method'},500
        return item.json(),201

    def delete(self,name):
        item = itemModel.find_by_name(name)
        if item:
            itemModel.delete_from_db(item)
        return {'message':'item reomved'}
    def put(self,name):
        data = Item.parser.parse_args
        item = itemModel.find_by_name(name)

        if item is None:
            item = itemModel(name,data['price'],data['store_id'])
        else:
            item.price = data['price']
        item.save_to_db(item)
        return item.json()

class ItemList(Resource):
    def get(self):
        return {'items':item.json() for item in itemModel.query.all()}
