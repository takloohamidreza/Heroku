from Resources.user import Usermodel
# users=[
#     Usermodel('hamid','asdf',1)
# ]
#
# username_mapping = {u.username:u for u in users}
# userid_mapping ={u.id:u for u in users}

def authentiacte(username, password):
    user =Usermodel.find_by_user(username)
    if user and user.password == password:
        return user
def identity(payload):
    user_id = payload['identity']
    return Usermodel.find_by_id(user_id)
