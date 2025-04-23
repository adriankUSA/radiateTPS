import os
import json
from flask import Blueprint, request, jsonify

patient_routes = Blueprint('patient_routes', __name__)

PATIENT_DIR = os.path.join("patientData")

@patient_routes.route("/patients/create", methods=["POST"])
def create_patient():
    data = request.json
    name = data.get("name")
    patient_id = data.get("id")
    birth_date = data.get("birthDate")
    sex = data.get("sex")

    if not os.path.exists(PATIENT_DIR):
        os.makedirs(PATIENT_DIR)

    patient_json = {
        "name": name,
        "id": patient_id,
        "birthDate": birth_date,
        "sex": sex
    }

    path = os.path.join(PATIENT_DIR, f"{patient_id}.json")
    with open(path, "w") as f:
        json.dump(patient_json, f)

    return jsonify({"success": True, "message": f"Patient {name} saved."})

@patient_routes.route("/patients/load", methods=["GET"])
def load_patients():
    if not os.path.exists(PATIENT_DIR):
        return jsonify([])

    patient_files = [f for f in os.listdir(PATIENT_DIR) if f.endswith(".json")]
    patients = []

    for filename in patient_files:
        with open(os.path.join(PATIENT_DIR, filename), "r") as f:
            patient = json.load(f)
            patients.append(patient)

    return jsonify(patients)
