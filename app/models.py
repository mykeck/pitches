import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import loginManager
from datetime import datetime


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255),unique = True,nullable = False)
    email  = db.Column(db.String(255),nullable = False)
    secure_password = db.Column(db.String(255),nullable = False)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    posts = db.relationship("Post",backref = "user",lazy = "dynamic")
    comment = db.relationship('Comment', backref='user', lazy='dynamic')
    upvote = db.relationship('Upvote',backref='user',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='user',lazy='dynamic')

    
    @property
    def set_password(self):
        raise AttributeError('you cannot read the passord attribute')

    @set_password.setter
    def password(self, password):
        self.secure_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.secure_password,password) 
    
    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    
    def __repr__(self):
        return f'User {self.username}' 


class post(db.Model):
    __tablename__= "posts"



    id = db.Column(db.Integer,primary_key = True)
    post_title = db.Column(db.String)
    author = db.Column(db.String(255))
    post_content = db.Column(db.String)
    posted_at = db.Column(db.DateTime,default=datetime.utcnow)
    category = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comments = db.relationship("Comment",backref = "post",lazy = "dynamic")
    upvote = db.relationship('Upvote',backref='post',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='post',lazy='dynamic')


    def save(self):
        db.session.add(self)
        db.session.commit()


    @classmethod
    def get_user_post(cls,id):
        posts = post.query.filter_by(user_id = id).all()
        return posts

    @classmethod 
    def get_all_post(cls):
        return Post.query.order_(Post.posted_at.asc()).all()

    def __repr__(self):
        return f"Post('{self.Post_title}', '{self.posted_at}')"                      
    
