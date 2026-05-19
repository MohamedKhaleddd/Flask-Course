from db import db

class User(db.Model):
    __tablename__= 'users'
    id= db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String,nullable=False)
    age= db.Column(db.Integer,nullable=False)
    # posts=db.relationship('Post')

    def __repr__(self):
        return f"User Info : (Id= {self.id} || Name = {self.name} || Age= {self.age})"
    

# class Post(db.Model):
#     __tablename__='posts'

#     id= db.Column(db.Integer,primary_key=True)
#     title=db.Column(db.String(100),nullable=False)
#     content=db.Column(db.Text,nullable=False)
#     user_id=db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
#     comments=db.relationship('Comment')
#     tags= db.relationship('Tag')


# class Comment(db.Model):
#     id= db.Column(db.Integer,primary_key=True)
#     content=db.Column(db.Text,nullable=False)
#     post_id=db.Column(db.Integer,db.ForeignKey('posts.id'),nullable=False)


# class Tag(db.Model):
#     id= db.Column(db.Integer,primary_key=True)
#     name=db.Column(db.String(50),nullable=False)