from flask_sqlalchemy import SQLAlchemy
from app import app
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///'+os.path.join(basedir,'school.db')
app.config['SECRET_KEY']='thisisverysecret'
db = SQLAlchemy(app)

class Roles(db.Model):
    role_id = db.Column(db.Integer,primary_key=True)
    role_name = db.Column(db.String)

class Users(db.Model):
    user_id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String,unique=True)
    password = db.Column(db.String)
    user_role = db.Column(db.Integer,db.ForeignKey('roles.role_id'))
    marks_got = db.relationship('Marks',backref='student')

class Marks(db.Model):
    marks_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    student_id = db.Column(db.Integer,db.ForeignKey('users.user_id'))
    maths = db.Column(db.Float,default=0)
    physics = db.Column(db.Float,default=0)
    chemistry = db.Column(db.Float,default=0)
