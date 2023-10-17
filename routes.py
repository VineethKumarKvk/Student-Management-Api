from app import app
from models import *
from flask import request,jsonify
from werkzeug.security import check_password_hash,generate_password_hash
from flask_jwt_extended import JWTManager,create_access_token,jwt_required,get_jwt_identity

app.config['JWT_SECRET_KEY']='thisisjwtsecretkey'
jwt = JWTManager(app)


@app.route('/testing',methods=['GET'])
@jwt_required()
def testing_the_api():
    return get_jwt_identity()


@app.route('/register',methods=['POST'])
def register():
    user_name = request.form.get('username')
    password = request.form.get('password')
    role_id = request.form.get('roleid')
    user_id = request.form.get('userid')
    existing_user = Users.query.filter_by(user_id=user_id,user_name=user_name).first()
    if existing_user:
        return jsonify(message='user already registered'),409
    new_user = Users(user_id=user_id,user_name=user_name,user_role=role_id,password=generate_password_hash(password,method='pbkdf2:SHA256',salt_length=3))
    db.session.add(new_user)
    db.session.commit()
    return jsonify(message='New user registered with id:'+str(new_user.user_id)),201

@app.route('/getMarks',methods=['GET'])
def getMarks():
    user_id = request.args.get('userid')
    result = db.session.query(Marks,Users,Roles).join(Users,Marks.student_id==Users.user_id).join(Roles,Users.user_role==Roles.role_id).filter(Marks.student_id==user_id).all()
    if result:
        output = []
        for marks,users,roles in result:
            data = {
                roles.role_name+' Name':users.user_name,
                'Marks':{
                    'Maths':marks.maths,
                    'Physics':marks.physics,
                    'chemistry':marks.chemistry
                },
            }
            output.append(data)
        return jsonify(output),200
    return jsonify(message='Results not found'),404


@app.route('/addMarks',methods=['POST'])
@jwt_required()
def add_marks():
    logged_username = get_jwt_identity()
    logged_user = Users.query.filter_by(user_name=logged_username).first()
    if(logged_user.user_role==2 or logged_user.user_role == 1):
        math_marks = request.form.get('math')
        physics_marks = request.form.get('physics')
        chemistry_marks = request.form.get('chemistry')
        student_id = request.form.get('studentid')
        exising_user = Users.query.filter_by(user_id=student_id).first()
        if not exising_user:
            return jsonify(message='student is not registered'),404
        if exising_user:
            if exising_user.user_role != 3:
                return jsonify(message='The user is not a student'),403

        existing_marks = Marks.query.filter_by(student_id=student_id).first()
        if existing_marks:
            existing_marks.maths = math_marks
            existing_marks.physics = physics_marks
            existing_marks.chemistry = chemistry_marks
            db.session.commit()
            return jsonify(message='Marks are updated'),200
        new_marks = Marks(student_id=student_id,maths=math_marks,physics=physics_marks,chemistry=chemistry_marks)
        db.session.add(new_marks)
        db.session.commit()
        return jsonify(message='Marks added'),201
    return jsonify(message='Not Authorised to add Marks'),403

#this route is added to practice relationships
@app.route('/UserMarks',methods=['GET'])
@jwt_required()
def getMarksByUser():
    username = get_jwt_identity()
    existingUser = Users.query.filter_by(user_name=username).first()
    if existingUser:
        userData = {
            'Username':existingUser.user_name,
            'Marks':[{"Math":x.maths,"Physics":x.physics,"chemistry":x.chemistry} for x in existingUser.marks_got]
        }
        return jsonify(userData),200
    return '',404
    
    
        



@app.route('/login',methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user_exists = Users.query.filter_by(user_name=username).first()
    if user_exists:
        if(check_password_hash(user_exists.password,password)):
            token = create_access_token(identity=user_exists.user_name)
            return jsonify(token=token)
    return 'Invalid creds',404
    


     