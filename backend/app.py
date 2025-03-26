import os
from flask import Flask, send_from_directory
from application.routes.main import main
from application.routes.tutorial1 import tutorial
from application.routes.plotly_tutorial import plotly_tutorial

# Get absolute path to the frontend folder
frontend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../frontend"))

app = Flask(__name__, static_folder=frontend_path, static_url_path="")

# Register blueprints
app.register_blueprint(main)
app.register_blueprint(tutorial, url_prefix="/tutorial")
app.register_blueprint(plotly_tutorial, url_prefix="/plotly")

# Serve index.html at root
@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

# Serve all other static files
@app.route("/<path:path>")
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

@app.route("/tutorial.html")
def tutorial_page():
    return send_from_directory(app.static_folder, "tutorial.html")


if __name__ == "__main__":
    app.run(debug=True)
