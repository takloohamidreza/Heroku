from flask_restful import Resource,reqparse
from models.user import Usermodel
class RegistorUser(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='This field must fill')
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This field must fill')
    def post(self):
        data =RegistorUser.parser.parse_args()
        if Usermodel.find_by_user(data['username']):
            return {'message': 'a user with this name has already exist'}
        user = Usermodel(data['username'],data['password'])
        try:
            user.save_to_db(user)
        except:
            return {'message':'an error occoured in insert user to database'}
        return user.json(),201
