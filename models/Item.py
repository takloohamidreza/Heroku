from db import db
class itemModel(db.Model):

    __tablename__ = 'items'

    id = db.Column(db.Integer,primary_key =True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.INTEGER,db.ForeignKey('stores.id'))
    store = db.relationship('storeModel')

    def __init__(self,name,price,store_id):
        self.name = name
        self.price = price
        self.store_id = store_id
    def json(self):
        return {'name':self.name,'price':self.price}

    @staticmethod
    def find_by_name(name):
        return itemModel.query.filter_by(name=name).first()

    @staticmethod
    def save_to_db(item):
        db.session.add(item)
        db.session.commit()

    @staticmethod
    def delete_from_db(item):
        db.session.delete(item)
        db.session.commit()
