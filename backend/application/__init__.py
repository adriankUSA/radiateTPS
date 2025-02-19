from flask import Flask
from flask_cors import CORS  # For frontend compatibility
from application.routes.main import main  # Import the main route

def create_app():
    app = Flask(__name__)

    # Enable CORS (for frontend access)
    CORS(app)

    # Register Blueprints
    app.register_blueprint(main)  # Ensure this is correct

    return app
