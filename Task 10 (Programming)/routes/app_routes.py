# Import application, database, Flight model and scheme, validator file and functions from flask and sqlalchemy
# to operate with queries
from application import app, db, login_m
from validation.codes import validate

from models.flight import Flight, FlightSchema
from models.user import User, UserSchema
from models.order import Order, OrderSchema

from flask import request, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from sqlalchemy import desc, cast, text, or_

# Initialize schemas
flight_schema = FlightSchema()
flights_schema = FlightSchema(many=True)

user_schema = UserSchema()

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)


# Create a Flight
@app.route('/api/flights', methods=['POST'])
@login_required
def add_flight():
    if current_user.get_role() != "admin":
        return jsonify({'status': 404, 'error': "User has no admin permissions"})

    for a in Flight.query:
        if request.json["id"] == a.id:
            return jsonify({'status': 404, 'error': "ID already exits"})

    data = []
    for a in Flight.get_attributes():
        data.append(request.json[a])

    new_flight = Flight(*data)

    respond = new_flight.get_data_integrity()
    if not respond == []:
        return jsonify({'status': 404, 'errors': respond})

    db.session.add(new_flight)
    db.session.commit()

    data = flight_schema.dump(new_flight)
    return jsonify({'status': 201, 'message': 'Flight created successfully'}, {'flight': data})


# Get All Flights
@app.route('/api/flights', methods=['GET'])
@login_required
def get_flights():
    sort_by = request.args.get("sort_by", type=str)
    sort_type = request.args.get("sort_type", type=str)
    search = request.args.get("search", type=str)
    offset = request.args.get("offset", type=int)
    limit = request.args.get("limit", type=int)

    all_flights = Flight.query

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
                                             ilike(f"%{search}%".lower()) for x in Flight.get_attributes()]))

    paginate_flights = all_flights.paginate(offset, limit)

    result = flights_schema.dump(paginate_flights.items)
    return jsonify({"status": 200, "message": "Successfully got flights", "sort": [sort_by, sort_type],
                    "search": search, "count": len(paginate_flights.items)}, {"info": result})


# Get Single Flight
@app.route('/api/flights/<id_>', methods=['GET'])
@login_required
def get_flight(id_):
    flight = Flight.query.filter_by(id=id_).first()

    if flight is not None:
        return jsonify({"status": 200, "message": "Successfully found flight"},
                       {"info": flight_schema.dump(flight)})

    return {'status': 404, 'error': "The flight has not been found"}


# Update a Flight
@app.route('/api/flights/<id_>', methods=['PUT'])
@login_required
def update_flight(id_):
    if current_user.get_role() != "admin":
        return jsonify({'status': 404, 'error': "User has no admin permissions"})

    flight = Flight.query.filter_by(id=id_).first()

    if flight is not None:
        for attr in Flight.get_attributes():
            if attr != "id":
                getattr(flight, "set_" + attr)(request.json[attr])

        respond = flight.get_data_integrity()
        if not respond == []:
            return jsonify({'status': 404, 'errors': respond})

        db.session.commit()

        return jsonify({"status": 200, "message": "Successfully changed flight"},
                       {"info": flight_schema.dump(flight)})

    return {'status': 404, 'error': "The flight with such ID has not been found"}


# Delete Flight
@app.route('/api/flights/<id_>', methods=['DELETE'])
@login_required
def delete_flight(id_):
    if current_user.get_role() != "admin":
        return jsonify({'status': 404, 'error': "User has no admin permissions"})

    flight = Flight.query.filter_by(id=id_).first()

    if flight is not None:
        db.session.delete(flight)
        db.session.commit()

        return jsonify({"status": 200, "message": "Flight has been successfully deleted"},
                       {"info": flight_schema.dump(flight)})

    return {'status': 404, 'error': "The flight with such ID has not been found"}


# ------------------------------------------------------------------------------------------------------------ #
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


# ------------------------------------------------------------------------------------------------------------ #


@app.route('/api/orders', methods=['POST'])
@login_required
def create_order():
    order_id = request.json["flight_id"]
    order_amount = request.json["amount"]

    if Flight.query.get(order_id).get_places() - order_amount < 0:
        return jsonify({'status': 404, 'errors': "There is not enough places in the plane"})
    new_order = Order(Order.query.count() + 1, current_user.get_id(), order_id, order_amount)

    respond = new_order.get_data_integrity()
    if not respond == []:
        return jsonify({'status': 404, 'errors': respond})

    Flight.query.get(order_id).set_places_amount(order_amount)

    db.session.add(new_order)
    db.session.commit()

    return jsonify({'status': 201, 'message': 'Order created successfully'},
                   {'order_info': order_schema.dump(new_order)})


@app.route('/api/orders', methods=['GET'])
@login_required
def get_orders():
    if current_user.get_role() != "admin":
        orders = Order.query.filter_by(user_id=current_user.get_id())
    else:
        orders = Order.query

    if orders is not None:
        return jsonify({"status": 200, "message": "Successfully got your orders"}, {"info": orders_schema.dump(orders)})

    return jsonify({"status": 404, "message": "You haven't done any orders yet"})


@app.route('/api/orders/<id_>', methods=['GET'])
@login_required
def get_order(id_):
    if current_user.get_role() != "admin":
        orders = Order.query.filter_by(user_id=current_user.get_id(), id=id_)
    else:
        orders = Order.query.filter_by(id=id_)

    if orders is not None:
        f_id = orders.first().get_flight_id()
        flight = Flight.query.filter_by(id=f_id).first()

        return jsonify({"status": 200, "message": "Successfully got your order"}, {"info": orders_schema.dump(orders)},
                       {"order": flight_schema.dump(flight)})

    return jsonify({"status": 404, "message": "This order id does not exist"})
