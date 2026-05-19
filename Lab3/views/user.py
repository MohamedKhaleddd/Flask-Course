from flask.views import MethodView
from flask import Flask,url_for,redirect,render_template,request
from models import User
from forms import Userform
from db import db


class UserView(MethodView):
    def get(self):
        users=User.query.all()
        return render_template(
            'index.html',
            title="All Users",
            message="Users Name",
            users=users

    )

class UserAddView(MethodView):
    def get(self):
        form=Userform()
        return render_template('add-user.html',title='Add user',form=form)
    def post(self):
        form= Userform()
        if form.validate_on_submit():
            name= form.name.data
            age=form.age.data
            new_user=User(name=name,age=age)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('user_view'))



class UserUpdateView(MethodView):
    def get(self,id):
        user= User.query.get_or_404(id)
        return render_template ('update-user.html',title='Update user',user=user)
    def post(self,id):
            user= User.query.get_or_404(id)
            user.name= request.form['name']
            user.age=request.form['age']
            db.session.commit()
            return redirect(url_for('user_view'))



class UserDeleteView(MethodView):
    def get (self,id):
        user= User.query.get_or_404(id)
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('user_view'))


