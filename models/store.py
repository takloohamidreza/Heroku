from db import db
class storeModel(db.Model):

    __tablename__ = 'stores'

    id = db.Column(db.Integer,primary_key =True)
    name = db.Column(db.String(80))

    items = db.relationship('itemModel',lazy='dynamic')

    def __init__(self,name,price):
        self.name = name
    def json(self):
        return {'name':self.name,'items':[item.json() for item in self.items.all()]}

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
