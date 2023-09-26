from app import app
from models import *
from werkzeug.security import generate_password_hash,check_password_hash

@app.cli.command('dbcreate')
def db_create():
    db.create_all()
    print('created')

@app.cli.command('dbdrop')
def db_drop():
    db.drop_all()
    print('dropped')

@app.cli.command('dbseed')
def db_seed():
    roles_data = [
        {'role_id':1,'role_name':'principal'},
        {'role_id':2,'role_name':'Teacher'},
        {'role_id':3,'role_name':'Student'}
    ]
    user_data = [
        {'user_id':1,'user_name':'student1','password':generate_password_hash('1234',method='pbkdf2:SHA256',salt_length=3),'user_role':3},
        {'user_id':2,'user_name':'student2','password':generate_password_hash('1234',method='pbkdf2:SHA256',salt_length=3),'user_role':3},
        {'user_id':3,'user_name':'principal','password':generate_password_hash('1234',method='pbkdf2:SHA256',salt_length=3),'user_role':1},
        {'user_id':4,'user_name':'teacher1','password':generate_password_hash('1234',method='pbkdf2:SHA256',salt_length=3),'user_role':2},
        {'user_id':5,'user_name':'teacher2','password':generate_password_hash('1234',method='pbkdf2:SHA256',salt_length=3),'user_role':2}
    ]

    marks_data = [
        {'student_id':1,'maths':100,'physics':95,'chemistry':90},
        {'student_id':2,'maths':100,'physics':98,'chemistry':99}
    ]
    db.session.bulk_insert_mappings(Roles,roles_data)
    db.session.bulk_insert_mappings(Users,user_data)
    db.session.bulk_insert_mappings(Marks,marks_data)
    db.session.commit()
    print('seeded')