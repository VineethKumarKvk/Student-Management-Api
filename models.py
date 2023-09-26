from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,String,Integer,Float,ForeignKey
from app import app
import os
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///'+os.path.join(basedir,'school.db')
app.config['SECRET_KEY']='thisisverysecret'
db = SQLAlchemy(app)

class Roles(db.Model):
    role_id = Column(Integer,primary_key=True)
    role_name = Column(String)

class Users(db.Model):
    user_id = Column(Integer,primary_key=True)
    user_name = Column(String)
    password = Column(String)
    user_role = Column(Integer,ForeignKey('roles.role_id'))

class Marks(db.Model):
    marks_id = Column(Integer,primary_key=True)
    student_id = Column(Integer,ForeignKey('users.user_id'))
    maths = Column(Float)
    physics = Column(Float)
    chemistry = Column(Float)
