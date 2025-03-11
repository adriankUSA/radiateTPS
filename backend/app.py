from flask import Flask
from application.routes.main import main  # Import the Blueprint
from application.routes.tutorial1 import tutorial  # Import the blueprint

app = Flask(__name__)

# Register Blueprint
app.register_blueprint(main)
app.register_blueprint(tutorial, url_prefix="/tutorial")  # Register it with a prefix


if __name__ == "__main__":
    app.run(debug=True)
