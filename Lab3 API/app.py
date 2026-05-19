from flask import Flask,jsonify,request
from db import db
from views.user import *
from config import *
from models import User

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRES_URI
db.init_app(app)

with app.app_context():
    db.create_all()




@app.route('/')
def api():
    user = {
        'id':1,
        'name': 'mohamed',
        'age': 14
    }
    return jsonify(user)

'''# @app.route('/api/all-users')
# def all_users():
#     users=User.query.all()
#     data=[]
#     for user in users:
#         data.append({
#             'Id':user.id,
#             'Name':user.name,
#             'Age' : user.age,
#          })
#     return jsonify(data)'''

# all_users_view=UserView.as_view('user_view')
# app.add_url_rule('/api/all-users',view_func=all_users_view)





'''# @app.route('/api/user/<int:id>')

# def get_user(id):
#     user=User.query.get(id)
#     if user:
#         data={
#             'Id':user.id,
#             'Name':user.name,
#             'Age' : user.age,
#          }
#         return jsonify(data)
#     return jsonify({'message': 'User Not Found'}), 404'''

# user_details_view=UserDetails.as_view('user_details')
# app.add_url_rule('/api/user/<int:id>',view_func=user_details_view)

'''@app.route('/api/add-user',methods=['POST'])
def add_user():
    data= request.get_json()
    new_user= User(name=data['name'],age=data['age'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User Added Successfully'}),201'''
# user_add_view=UserAddView.as_view('user_add')
# app.add_url_rule('/api/add-user',view_func=user_add_view)





'''@app.route('/api/update-user/<int:id>',methods=['PUT'])
def updateuser(id):
    user= User.query.get(id)
    data= request.get_json()
    user.name=data['name']
    user.age=data['age']
    db.session.commit()
    return jsonify({'message': 'User Updated Successfully'}),201'''

# user_update_view=UserUpdateView.as_view('user_update')
# app.add_url_rule('/api/update-user/<int:id>',view_func=user_update_view)




'''@app.route('/api/delete-user/<int:id>',methods=['DELETE'])
def deleteuser(id):
    user= User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User DEleted Successfully'}),200'''
# user_delete_view=UserDeleteView.as_view('user_delete')
# app.add_url_rule('/api/delete-user/<int:id>',view_func=user_delete_view)

user_view=UserAPI.as_view('user_view')
user_id=UserApiId.as_view('user_id')

app.add_url_rule('/api/users',view_func=user_view,methods=['GET','POST'])
app.add_url_rule('/api/users/<int:id>',view_func=user_id,methods=['GET','PUT','DELETE'])



if __name__=='__main__':
    app.run(debug=True)
