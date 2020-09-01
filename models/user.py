from db import db
class Usermodel(db.Model):


    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key =True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def json(self):
        return {'username':self.username,'password':self.password}

    @staticmethod
    def save_to_db(user):
        db.session.add(user)
        db.session.commit()
    @staticmethod
    def find_by_user(username):
        return Usermodel.query.filter_by(username=username).first()

    @staticmethod
    def find_by_id(_id):
        return Usermodel.query.filter_by(id=_id)
