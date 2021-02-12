from application import app, db

from models.flight import Flight, FlightSchema

from flask import request, jsonify
from flask_login import current_user, login_required
from sqlalchemy import desc, cast, text, or_

# Initialize schemas
flight_schema = FlightSchema()
flights_schema = FlightSchema(many=True)


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
