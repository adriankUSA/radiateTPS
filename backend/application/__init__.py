from flask import Flask
from flask_cors import CORS  # Import CORS
from application.config import config

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    CORS(app)  # Enable CORS

    from application.routes.main import main
    app.register_blueprint(main)

    return app
