# Import application, database, Flight model and scheme, validator file and functions from flask and sqlalchemy
# to operate with queries
from app import app, db, login_m
from flight import Flight, FlightSchema
from user import User, UserSchema
from nothing_to_look_at import encode

from flask import request, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy import desc, cast, text, or_
from validation.validator import Validator

# Initialize schemas
flight_schema = FlightSchema()
flights_schema = FlightSchema(many=True)

user_schema = UserSchema()


# Create a Flight
@app.route('/api/flights', methods=['POST'])
@login_required
def add_flight():
    for a in Flight.query:
        if request.json["id"] == a.id:
            return jsonify({'status': 404, 'error': "ID already exits"}), 404

    data = []
    for a in Flight.get_attributes():
        if a != "user_id":
            data.append(request.json[a])
    data.append(current_user.id)

    new_flight = Flight(*data)

    respond = new_flight.get_data_integrity()
    if not respond == []:
        return jsonify({'status': 404, 'errors': respond}), 404

    db.session.add(new_flight)
    db.session.commit()

    data = flight_schema.dump(new_flight)
    return jsonify({'status': 201, 'message': 'Flight created successfully'}, {'flight': data}), 201


# Get All Flights
@app.route('/api/flights', methods=['GET'])
@login_required
def get_flights():
    sort_by = request.args.get("sort_by", type=str)
    sort_type = request.args.get("sort_type", type=str)
    search = request.args.get("search", type=str)
    offset = request.args.get("offset", type=int)
    limit = request.args.get("limit", type=int)

    all_flights = Flight.query.filter_by(user_id=current_user.id)

    for i in Flight.get_attributes():
        if i == sort_by:
            break
        if i == "company":
            sort_by = None

    if sort_by and sort_type == "desc":
        all_flights = all_flights.order_by(desc(sort_by))
    elif sort_by:
        all_flights = all_flights.order_by(text(sort_by))

    if search:  # На цей запис я витратив набагато більше часу, ніж того хотів би
        all_flights = all_flights.filter(or_(*[cast(getattr(Flight, x), db.String).
                                             like(f"%{search}%".lower()) for x in Flight.get_attributes()]))

    paginate_flights = all_flights.paginate(offset, limit)

    result = flights_schema.dump(paginate_flights.items)
    return jsonify({"status": 200, "message": "Successfully got flights", "sort": [sort_by, sort_type],
                    "search": search, "count": len(paginate_flights.items)}, {"info": result}), 200


# Get Single Flight
@app.route('/api/flights/<id_>', methods=['GET'])
@login_required
def get_flight(id_):
    flight = Flight.query.filter_by(user_id=current_user.id, id=id_).first()

    check = Validator.check_id(id_, flight)
    if check is not None:
        return jsonify(check), 404

    data = flight_schema.dump(flight)
    return jsonify({"status": 200, "message": "Successfully found flight"}, {"info": data}), 200


# Update a Flight
@app.route('/api/flights/<id_>', methods=['PUT'])
@login_required
def update_flight(id_):
    update_f = Flight.query.get(id_)

    check = Validator.check_id(id_, update_f)
    if check is not None:
        return jsonify(check), 404

    for attr in Flight.get_attributes():
        getattr(update_f, "set_" + attr)(request.json[attr])

    respond = update_f.get_data_integrity()
    if not respond == []:
        return jsonify({'status': 404, 'errors': respond}), 404

    db.session.commit()

    data = flight_schema.dump(update_f)
    return jsonify({"status": 200, "message": "Successfully changed flight"}, {"info": data}), 200


# Delete Flight
@app.route('/api/flights/<id_>', methods=['DELETE'])
@login_required
def delete_flight(id_):
    flight = Flight.query.get(id_)

    check = Validator.check_id(id_, flight)
    if check is not None:
        return jsonify(check), 404

    db.session.delete(flight)
    db.session.commit()

    data = flight_schema.dump(flight)
    return jsonify({"status": 200, "message": "Flight has been successfully deleted"}, {"info": data}), 200


# ------------------------------------------------------------------------------------------------------------ #
@app.route('/api/users', methods=['POST'])
def register_user():
    data = [User.query.count() + 1]
    for a in User.get_attributes():
        if a != "id":
            data.append(request.json[a])

    new_user = User(*data)

    respond = new_user.get_data_integrity()
    if not respond == []:
        return jsonify({'status': 404, 'errors': respond}), 404

    db.session.add(new_user)
    db.session.commit()

    info = user_schema.dump(new_user)
    return jsonify({'status': 201, 'message': 'User created successfully'}, {'user_info': info}), 201


@app.route('/api/login', methods=['POST'])
def login_u():
    for user in User.query:
        if user.get_mail() != request.json["email"]:
            continue
        else:
            if user.get_pass() == encode(request.json["password"]):
                login_user(user)
                return jsonify({'status': 201, 'message': 'User logged in successfully'}), 200
    return jsonify({'status': 404, 'message': 'Either email or password is incorrect'}), 404


@login_m.user_loader
def login(u_id):
    return User.query.get(u_id)


@app.route('/api/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({'status': 200, 'message': "User log out successfully"}), 200


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
