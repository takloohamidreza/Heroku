from flask_restful import Resource
from models.store import storeModel

class Store(Resource):
    def get(self,name):
        store = storeModel.find_by_name(name)
        if store:
            return store.json()
        return {'message':'store has not found'}
    def post(self,name):
        if storeModel.find_by_name(name):
            return {'message':'a store with name of {} is exist'.format(name)}
        store = storeModel(name)
        return store.json()


class StoreList(Resource):
    def get(self):
        return {'stores':[store.json() for store in storeModel.query.all()]}
