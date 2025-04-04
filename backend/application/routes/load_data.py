from flask import Blueprint, request, jsonify
import os
from opentps.core.io.dataLoader import readData

load_data = Blueprint("load_data", __name__)

@load_data.route("/<dataset_name>", methods=["GET"])
def load_specific_dataset(dataset_name):  # ✅ Renamed
    try:
        dataset_dir = os.path.join(os.getcwd(), "datasets", dataset_name)
        data = readData(dataset_dir)

        if len(data) < 2:
            return jsonify({"error": "Dataset missing RT Struct or CT"}), 400

        rt_struct = next((d for d in data if d.__class__.__name__ == "RTStruct"), None)

        roi_names = [contour.name for contour in rt_struct.contours]

        return jsonify({
            "dataset": dataset_name,
            "roi_names": roi_names,
            "message": f"{dataset_name} loaded successfully!"
        })
    except Exception as e:
        return jsonify({"error": str(e)})

@load_data.route("/datasets", methods=["GET"])
def list_datasets():
    datasets_path = os.path.join(os.getcwd(), "datasets")
    try:
        folders = [f for f in os.listdir(datasets_path) if os.path.isdir(os.path.join(datasets_path, f))]
        return jsonify({"datasets": folders})
    except Exception as e:
        return jsonify({"error": str(e)})

@load_data.route('/datasets/<dataset_name>/rois')
def get_roi_names(dataset_name):
    folder = os.path.join('datasets', dataset_name)
    data = readData(folder)

    rt_struct = next((d for d in data if d.__class__.__name__ == "RTStruct"), None)

    if rt_struct is None:
        return jsonify({"error": "RTStruct not found"}), 404

    try:
        # Safely extract ROI names
        roi_names = [contour.name for contour in rt_struct.contours]
        return jsonify({"roi_names": roi_names})
    except Exception as e:
        return jsonify({"error": f"Failed to extract ROI names: {str(e)}"}), 500

@load_data.route("/load_dataset", methods=["GET"])
def load_dataset():
    dataset_name = request.args.get("name")
    dataset_path = os.path.join("datasets", dataset_name)

    dicom_files = []
    for root, _, files in os.walk(dataset_path):
        for file in files:
            if file.lower().endswith(".dcm"):
                relative_path = os.path.join(root, file)
                url_path = f"/static_datasets/{dataset_name}/{file}"
                dicom_files.append(url_path)

    return jsonify({"success": True, "files": dicom_files})

from flask import send_from_directory

@load_data.route('/static_datasets/<dataset>/<filename>')
def serve_dicom(dataset, filename):
    return send_from_directory(os.path.join("datasets", dataset), filename)

