from flask import Blueprint, request, jsonify
import os
from opentps.core.io.dataLoader import readData

upload_routes = Blueprint("upload_routes", __name__)

@upload_routes.route("/upload_dicom", methods=["POST"])
def upload_dicom():
    # Save uploaded files
    folder = "uploads/dicom_temp"
    os.makedirs(folder, exist_ok=True)

    files = request.files.getlist("dicom_folder")
    for f in files:
        f.save(os.path.join(folder, f.filename))

    # Read and parse DICOM folder
    try:
        data = readData(folder)
        rt_struct = data[0]
        roi_names = rt_struct.getROINames()
        return jsonify({"roi_names": roi_names})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@upload_routes.route("/test_rois", methods=["GET"])
def test_rois():
    ctImagePath = os.path.join(os.getcwd(), "datasets", "data")
    data = readData(ctImagePath)
    rt_struct = data[0]
    roi_names = rt_struct.getROINames()
    return jsonify({"roi_names": roi_names})

