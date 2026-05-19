from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def welcome():
    return "<h1>Welcome Home</h1>"

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

users= [

    {'id':1,'name':'Mohamed','age':30},
    {'id':2,'name':'Ahmed','age':20},
    {'id':3,'name':'Khaled','age':40}

]

#--------------------------LIST-------------------------------
@app.route('/users',methods=['GET'])
def all_users():
    data=f'''
        <h1>Users Name</h1>
        <ul>
    '''
    for i in range (len(users)):
        data+=f'<li> {users[i]['name']} </li>'
    data += '</ul>'
    return data
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
    return render_template(
        'index.html',
        title="All Users",
        message="Users Name",
        users=users

    )


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





if __name__== '__main__':
    app.run(debug=True)