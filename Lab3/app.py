from flask import Flask,url_for,redirect,render_template,request

from db import db
from config import *
from models import User
from forms import Userform
from views.user import *

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = POSTGRES_URI
app.config['SECRET_KEY']= SECRECT_KEY
db.init_app(app)

with app.app_context():
    db.create_all()


user_view=UserView.as_view('user_view')

app.add_url_rule('/',view_func=user_view)
app.add_url_rule('/users',view_func=user_view)


@app.route('/about')
def about():
    return "<h1>About Page</h1>"

@app.route('/contact')
def contact():
    return "<h1>Contact Page</h1>"

@app.route('/service')
def service():
    return "<h1>Service Page</h1>"

@app.route('/user/<username>')
def username(username):
    print (type(username))
    return f"Welcome {username}"

@app.route('/user/<username>/<int:age>')
def userage(username,age):
    return f"Welcome {username}, age= {age}"

#------------------------------ADD (Insert)---------------------
@app.route('/add_user/<name>',methods=['GET','POST'])
def add_user(name):
    newuser= {'id':len(users)+1,'name':name,'age':50}
    users.append(newuser)
    return f"User {name} added successfully \n {users}"

# ----------------------------DELETE-------------------------
@app.route('/delete_user/<int:id>',methods=['DELETE','GET'])
def delete_user(id):
    for user in users:
        if user['id']==id:
            users.remove(user)

    data = f'''
        <h1>All Users After Delete: </h1>
        <ul>
    '''
    for i in range (len(users)):
        data+=f'<li>{users[i]['name']}</li>'
    data += '</ul>'
    return data

#----------------------------------UPDATE-----------------------
@app.route('/update_user/<int:id>/edit/<name>',methods=['PUT','GET'])
def update_user(id,name):
    for user in users:
        if user['id']==id:
            user['name']=name
    
    data=f'''
        <h1>Users list after update: </h1>
        <ul>
    '''
    for i in range (len(users)):
        data += f"<li>{users[i]['name']}</li>" 
    
    data +='</ul>'
    return data

#--------------------------------List With HTML----------------------
@app.route('/all_users')
def all_users_html():
    users=User.query.all()
    return render_template(
        'index.html',
        title="All Users",
        message="Users Name",
        users=users

    )

#----------------------------Profile------------------------------
@app.route('/profile/<username>')
def profile(username):

    user_data={}
    for user in users:
        if user['name']==username:
            user_data=user
            return render_template(
                'profile.html',
                title=f"{username} Profile",
                message=f"{username} Info",
                user=user_data
            )
        
    return render_template(
        '404.html',
        title="404 Page",
        message="User Not Found"
        )

#-----------------------------------Insert format------------------
# @app.route('/add-user',methods=['GET','POST'])
# def add_user_format():
#     form= Userform()
#     if form.validate_on_submit():
#         name= form.name.data
#         age=form.age.data
#         new_user=User(name=name,age=age)
#         db.session.add(new_user)
#         db.session.commit()
#         return redirect(url_for('all_users_html'))
#     return render_template('add-user.html',title='Add user',form=form)

add_user_view=UserAddView.as_view('add_user_view')
app.add_url_rule('/add-user',view_func=add_user_view,methods=['GET','POST'])

#-----------------------------Update with form------------------
# @app.route("/update_user/<int:id>",methods=['GET','POST'])
# def update_user_form(id):
#     user= User.query.get_or_404(id)
#     if request.method=='POST' or request.method=='PUT':
#         user.name= request.form['name']
#         user.age=request.form['age']
#         db.session.commit()
#         return redirect(url_for('all_users_html'))
#     return render_template ('update-user.html',title='Update user',user=user)

update_user_view=UserUpdateView.as_view('update_user_view')
app.add_url_rule('/update_user/<int:id>',view_func=update_user_view,methods=['GET','POST'])

#------------------------__DElete with form---------------------

# @app.route('/delete/<int:id>')
# def delete(id):
#     user= User.query.get_or_404(id)
#     db.session.delete(user)
#     db.session.commit()
#     return redirect(url_for('all_users_html'))

delete_user_view= UserDeleteView.as_view('delete_user_view')
app.add_url_rule('/delete/<int:id>',view_func=delete_user_view,methods=['GET'])

            







if __name__== '__main__':
    app.run(debug=True)