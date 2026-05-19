from db import db

class User(db.Model):
    __tablename__= 'users'
    id= db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String,nullable=False)
    age= db.Column(db.Integer,nullable=False)

    def __repr__(self):
        return f"User Info : (Id= {self.id} || Name = {self.name} || Age= {self.age})"