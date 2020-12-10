from application import app, db, login_m

from models.user import User, UserSchema
from validation.codes import validate

from flask import request, jsonify
from flask_login import login_user, logout_user, login_required

# Initialize schemas
user_schema = UserSchema()


@app.route('/api/users', methods=['POST'])
def register_user():
    if User.query.filter_by(first_name=request.json["first_name"],
                            last_name=request.json["last_name"]).first() is not None:
        return jsonify({'status': 404, 'errors': "Such username is already in use"})
    if User.query.filter_by(email=request.json["email"]).first() is not None:
        return jsonify({'status': 404, 'errors': "This email has already been used"})
    new_user = User(*[User.query.count() + 1,
                      *[request.json[f"{attr}"] for attr in User.get_attributes() if attr != "id" and attr != "role"],
                      "user"])

    respond = new_user.get_data_integrity()
    if not respond == []:
        return jsonify({'status': 404, 'errors': respond})

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'status': 201, 'message': 'User created successfully'},
                   {'user_info': user_schema.dump(new_user)})


@app.route('/api/login', methods=['POST'])
def login_u():
    user = User.query.filter_by(email=request.json["email"]).first()
    if user is not None:
        if validate(user.get_pass(), request.json["password"]):
            login_user(user)
            return jsonify({'status': 201, 'message': 'User logged in successfully'})
    else:
        return jsonify({'status': 404, 'message': 'Either email or password is incorrect'})


@login_m.user_loader
def login(u_id):
    return User.query.get(u_id)


@app.route('/api/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({'status': 200, 'message': "User log out successfully"})
