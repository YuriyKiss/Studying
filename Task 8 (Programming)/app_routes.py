from app import app, db
from flight import Flight, FlightSchema

from flask import request, jsonify
from sqlalchemy import desc, cast, text, or_
from validation.validator import Validator

# Init schema
flight_schema = FlightSchema()
flights_schema = FlightSchema(many=True)


# Create a Flight
@app.route('/api/flights', methods=['POST'])
def add_flight():
    for a in Flight.query:
        if request.json["id"] == a.id:
            return jsonify({'status': 404, 'errors': "ID already exits"}), 404

    data = []
    for a in Flight.get_attributes():
        data.append(request.json[a])

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
def get_flights():
    sort_by = request.args.get("sort_by", type=str)
    sort_type = request.args.get("sort_type", type=str)
    search = request.args.get("search", type=str)
    offset = request.args.get("offset", type=int)
    limit = request.args.get("limit", type=int)

    all_flights = Flight.query

    if sort_by != any(Flight.get_attributes()):
        sort_by = None

    if sort_type and sort_by and sort_type == "desc":
        all_flights = all_flights.order_by(desc(sort_by))
    elif sort_by:
        all_flights = all_flights.order_by(text(sort_by))

    if search:
        all_flights = all_flights.filter(or_(cast(Flight.id, db.String).like(f"%{search}%"),
                                             Flight.departure_country.like(f"%{search}%"),
                                             Flight.arrival_country.like(f"%{search}%"),
                                             cast(Flight.departure_time, db.String).like(f"%{search}%"),
                                             cast(Flight.arrival_time, db.String).like(f"%{search}%"),
                                             cast(Flight.ticket_price, db.String).like(f"%{search}%"),
                                             Flight.company.like(f"%{search}%")))
    if limit is None:
        limit = 100
    if offset is None:
        offset = 1
    paginate_flights = all_flights.paginate(offset, limit)

    result = flights_schema.dump(paginate_flights.items)
    return jsonify({"status": 200, "message": "Successfully got flights", "sort": [sort_by, sort_type],
                    "search": search, "count": len(paginate_flights.items)}, {"info": result}), 200


# Get Single Flight
@app.route('/api/flights/<id_>', methods=['GET'])
def get_flight(id_):
    flight = Flight.query.get(id_)

    check = Validator.check_id(id_, flight)
    if check is not None:
        return jsonify(check), 404

    data = flight_schema.dump(flight)
    return jsonify({"status": 200, "message": "Successfully found flight"}, {"info": data}), 200


# Update a Flight
@app.route('/api/flights/<id_>', methods=['PUT'])
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
def delete_flight(id_):
    flight = Flight.query.get(id_)

    check = Validator.check_id(id_, flight)
    if check is not None:
        return jsonify(check), 404

    db.session.delete(flight)
    db.session.commit()

    data = flight_schema.dump(flight)
    return jsonify({"status": 200, "message": "Flight has been successfully deleted"}, {"info": data}), 200


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
