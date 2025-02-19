from flask import Flask, jsonify, send_file
import os
import numpy as np
import matplotlib.pyplot as plt
from opentps.core.data.images import CTImage
from opentps.core.data.plan import PhotonPlanDesign
from opentps.core.processing.doseCalculation.protons.mcsquareDoseCalculator import MCsquareDoseCalculator

app = Flask(__name__)

# Dummy data path (replace with real CT scan data)
CT_PATH = "path_to_ct_data"

@app.route("/load_data", methods=["GET"])
def load_data():
    # Simulating loading CT image
    ct = CTImage()
    ct.load(CT_PATH)
    return jsonify({"message": "CT Data Loaded Successfully"})

@app.route("/compute_dose", methods=["GET"])
def compute_dose():
    # Simulating dose calculation
    plan = PhotonPlanDesign()
    mc2 = MCsquareDoseCalculator()
    dose_image = mc2.computeDose(plan)
    
    # Save the dose image
    plt.imshow(dose_image.imageArray[:, :, 50], cmap="jet")
    plt.colorbar()
    output_path = "static/SimpleDose.png"
    plt.savefig(output_path)
    
    return jsonify({"message": "Dose Computation Completed!"})

if __name__ == "__main__":
    app.run(debug=True)
