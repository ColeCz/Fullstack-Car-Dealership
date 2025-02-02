from flask import Flask
from flask_cors import CORS

import app.db
import app.main
import app.auth
import app.transaction
import app.vehicle
import app.part
import app.vendor
import app.reports
import app.vehicle_details


def create_app():
    app = Flask(__name__)
    CORS(
        app,
        supports_credentials=True,  # Enable credentials support (100% necessary for auth)
        resources={
            r"/*": {  # Apply to all routes
                "origins": "http://3.147.185.195:8080",  # Frontend origin
                "allow_credentials": True,
                "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
                "allow_headers": ["Content-Type", "Authorization"],
            }
        },
    )

    db.init_pool(app)

    app.secret_key = "2a678c251a30e17249729a70012c88445cb117ba1e74d2c475c0186cd3a06053"

    app.register_blueprint(main.blueprint)
    app.register_blueprint(auth.blueprint, url_prefix="/auth")
    app.register_blueprint(transaction.blueprint, url_prefix="/transaction")
    app.register_blueprint(vehicle.blueprint, url_prefix="/vehicle")
    app.register_blueprint(part.blueprint, url_prefix="/part")
    app.register_blueprint(vendor.blueprint, url_prefix="/vendor")
    app.register_blueprint(reports.blueprint, url_prefix="/reports")
    app.register_blueprint(vehicle_details.blueprint, url_prefix="/vehicle_details")

    return app
