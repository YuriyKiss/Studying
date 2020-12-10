from application import app, db

from flask import request, jsonify
from flask_login import login_required, current_user

from models.flight import Flight, FlightSchema
from models.order import Order, OrderSchema

# Initialize schemas
flight_schema = FlightSchema()
flights_schema = FlightSchema(many=True)

order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)


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
        f_id = orders.first().get_flight_id()
        flight = Flight.query.filter_by(id=f_id)

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
