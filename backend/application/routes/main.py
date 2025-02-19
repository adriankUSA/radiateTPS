import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import pydicom
from flask import Blueprint, request, jsonify

# Append OpenTPS to sys.path (Only once here)
sys.path.append(r"C:\opentps\opentps_core")

# OpenTPS imports
from opentps.core.data.images import CTImage
from opentps.core.data.plan import PhotonPlanDesign
from opentps.core.processing.doseCalculation.protons.mcsquareDoseCalculator import MCsquareDoseCalculator

# Create Blueprint
main = Blueprint("main", __name__)

# ==========================
# 📤 Main Route
# ==========================
@main.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to RadiateTPS!"})

# ==========================
# 📄 Load CT Data Route
# ==========================
@main.route("/load_data", methods=["GET"])
def load_data():
    """Loads a CT image from a given path."""
    CT_PATH = "path_to_ct_data"
    ct = CTImage()
    ct.load(CT_PATH)
    return jsonify({"message": "CT Data Loaded Successfully"})

# ==========================
# ☢️ Compute Dose Route
# ==========================
@main.route("/compute_dose", methods=["GET"])
def compute_dose():
    """Performs dose computation using OpenTPS."""
    plan = PhotonPlanDesign()
    mc2 = MCsquareDoseCalculator()
    dose_image = mc2.computeDose(plan)

    # Save dose image
    plt.imshow(dose_image.imageArray[:, :, 50], cmap="jet")
    plt.colorbar()
    output_path = "static/SimpleDose.png"
    plt.savefig(output_path)

    return jsonify({"message": "Dose Computation Completed!", "image": output_path})
