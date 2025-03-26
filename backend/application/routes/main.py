import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import math 
import pydicom
from flask import Blueprint, request, jsonify, send_from_directory

# OpenTPS Imports
sys.path.append(r"C:\opentps\opentps_core")
from opentps.core.data import Patient
from opentps.core.data.images import CTImage, ROIMask
from opentps.core.data.plan import PhotonPlanDesign, ProtonPlanDesign
from opentps.core.processing.doseCalculation.protons.mcsquareDoseCalculator import MCsquareDoseCalculator
from opentps.core.processing.doseCalculation.doseCalculationConfig import DoseCalculationConfig
from opentps.core.io import mcsquareIO
from opentps.core.io.scannerReader import readScanner
from opentps.core.processing.imageProcessing.resampler3D import resampleImage3DOnImage3D, resampleImage3D
from opentps.core.data import DVH

# Define Blueprint
main = Blueprint("main", __name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ==========================
# 🏥 Patient Management
# ==========================
@main.route("/patients", methods=["POST", "GET"])
def manage_patients():
    if request.method == "POST":
        # TODO: Create a new patient
        return jsonify({"message": "Create patient (Not Implemented)"})
    elif request.method == "GET":
        # TODO: Retrieve patient list
        return jsonify({"message": "Get patients (Not Implemented)"})

# ==========================
# 📄 Load CT Data
# ==========================
@main.route("/ct", methods=["POST", "GET"])
def manage_ct():
    if request.method == "POST":
        # TODO: Upload a CT scan
        return jsonify({"message": "Upload CT (Not Implemented)"})
    elif request.method == "GET":
        # TODO: Load an existing CT scan
        return jsonify({"message": "Load CT (Not Implemented)"})

# ==========================
# 🎯 ROI Management
# ==========================
@main.route("/roi", methods=["POST", "GET"])
def manage_roi():
    if request.method == "POST":
        # TODO: Define a new ROI
        return jsonify({"message": "Create ROI (Not Implemented)"})
    elif request.method == "GET":
        # TODO: Retrieve available ROIs
        return jsonify({"message": "Get ROIs (Not Implemented)"})

# ==========================
# ☢️ Compute Dose
# ==========================
@main.route("/dose", methods=["POST"])
def compute_dose():
    # TODO: Compute dose based on selected parameters
    return jsonify({"message": "Compute dose (Not Implemented)"})

# ==========================
# 📊 Retrieve Results
# ==========================
@main.route("/results", methods=["GET"])
def get_results():
    # TODO: Retrieve stored CT/dose images and DVH data
    return jsonify({"message": "Get results (Not Implemented)"})

@main.route("/get_image")
def get_image():
    output_path = os.path.join(os.getcwd(), "Output")
    print(f"Looking for image at: {output_path}")
    return send_from_directory(output_path, "SimpleDose.png")

