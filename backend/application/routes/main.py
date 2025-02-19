from flask import Blueprint, jsonify

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return jsonify({"message": "Welcome to radiateTPS!"})

@main.route("/status")
def status():
    return jsonify({"status": "OK", "version": "1.0"})
