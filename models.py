from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,String,Integer,Float,ForeignKey
from app import app
import os
from sqlalchemy.orm import relationship

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///'+os.path.join(basedir,'school.db')
app.config['SECRET_KEY']='thisisverysecret'
db = SQLAlchemy(app)

class Roles(db.Model):
    role_id = Column(Integer,primary_key=True)
    role_name = Column(String)

class Users(db.Model):
    user_id = Column(Integer,primary_key=True)
    user_name = Column(String,unique=True)
    password = Column(String)
    user_role = Column(Integer,ForeignKey('roles.role_id'))
    marks_got = relationship('Marks',backref='student')

class Marks(db.Model):
    marks_id = Column(Integer,primary_key=True,autoincrement=True)
    student_id = Column(Integer,ForeignKey('users.user_id'))
    maths = Column(Float,default=0)
    physics = Column(Float,default=0)
    chemistry = Column(Float,default=0)
