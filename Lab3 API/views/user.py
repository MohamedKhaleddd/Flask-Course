from flask.views import MethodView
from flask import jsonify,request
from models import User
from db import db


'''# class UserView(MethodView):
#     def get(self):
#         users=User.query.all()
#         data=[]
#         for user in users:
#             data.append({
#                 'Id':user.id,
#                 'Name':user.name,
#                 'Age' : user.age,
#             })
#         return jsonify(data)
    

# class UserDetails(MethodView):
#     def get(id):
#         user=User.query.get(id)
#         if user:
#             data={
#             'Id':user.id,
#             'Name':user.name,
#             'Age' : user.age,
#          }
#             return jsonify(data)
#         return jsonify({'message': 'User Not Found'}), 404

# class UserAddView(MethodView):
#     def post(self):
#         data= request.get_json()
#         new_user= User(name=data['name'],age=data['age'])
#         db.session.add(new_user)
#         db.session.commit()
#         return jsonify({'message': 'User Added Successfully'}),201




# class UserUpdateView(MethodView):
#     def put(self,id):
#         user= User.query.get(id)
#         data= request.get_json()
#         user.name=data['name']
#         user.age=data['age']
#         db.session.commit()
#         return jsonify({'message': 'User Updated Successfully'}),201



# class UserDeleteView(MethodView):
#     def delete (self,id):
#         user= User.query.get_or_404(id)
#         db.session.delete(user)
#         db.session.commit()
#         return jsonify({'message': 'User DEleted Successfully'}),200'''




class UserAPI(MethodView):
    
    
    #all
    def get(self):
        users=User.query.all()
        data=[]
        for user in users:
            data.append({
                'Id':user.id,
                'Name':user.name,
                'Age' : user.age,
            })
        return jsonify(data)
    
    
    
    
    
    #Add
    def post(self):
        data= request.get_json()
        new_user= User(name=data['name'],age=data['age'])
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User Added Successfully'}),201
    
    
   

class UserApiId(MethodView):
    def get(id):
        user=User.query.get(id)
        if user:
            data={
            'Id':user.id,
            'Name':user.name,
            'Age' : user.age,
         }
            return jsonify(data)
        return jsonify({'message': 'User Not Found'}), 404
    
    
    
    
    #update
    def put(self,id):
        user= User.query.get(id)
        data= request.get_json()
        user.name=data['name']
        user.age=data['age']
        db.session.commit()
        return jsonify({'message': 'User Updated Successfully'}),201
    
    
   
    #delete
    def delete (self,id):
        user= User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User DEleted Successfully'}),200


    
