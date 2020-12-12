from application import app

from routes.order_routes import *
from routes.user_routes import *
from routes.flight_routes import *

# Run Server
if __name__ == '__main__':
    app.run(debug=True)
