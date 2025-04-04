
export async function fetchDoseData() {
    console.log("Running fetchDoseData");
    try {
        const response = await fetch('/plotly/compute_dose');

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const data = await response.json();

        console.log("Received dose data:", data);

        const ct = data.ct_slice;
        const mask = data.mask_slice;
        const dose = data.dose_slice;
        const dvh = data.dvh;

        const layout1 = {
            title: 'CT Slice with Dose Overlay',
            xaxis: { title: 'X Axis' },
            yaxis: { title: 'Y Axis' },
            showlegend: false
        };

        const heatmap = {
            z: ct,
            type: 'heatmap',
            colorscale: 'Greys',
            showscale: false,
            opacity: 0.6    // Try 0.6 or 0.7 instead of full opacity
        };
        

        const doseMap = {
            z: dose,
            type: 'heatmap',
            colorscale: 'Jet',
            opacity: 0.5
        };

        const maskContour = {
            z: mask,
            type: 'contour',
            line: { color: 'red', width: 2 },
            showscale: false
        };

        Plotly.newPlot('plotly-ct-dose', [heatmap, maskContour, doseMap], layout1);

        const layout2 = {
            title: 'Dose Volume Histogram',
            xaxis: { title: 'Dose (Gy)' },
            yaxis: { title: 'Volume (%)' }
        };

        const dvhPlot = {
            x: dvh.dose_values,
            y: dvh.volume_percentages,
            type: 'scatter',
            mode: 'lines+markers',
            name: 'Target ROI'
        };

        Plotly.newPlot('plotly-dvh', [dvhPlot], layout2);

        const layoutDoseOverlay = {
            title: 'CT Slice + Dose + ROI Mask (Dummy Data)',
            xaxis: { title: 'X Axis', showgrid: false },
            yaxis: { title: 'Y Axis', showgrid: false },
            showlegend: false
        };
        
        const ctLayer = {
            z: ct,
            type: 'heatmap',
            colorscale: 'Greys',
            showscale: false,
            opacity: 1.0,
            hoverinfo: 'skip'
        };
        
        const maskLayer = {
            z: mask,
            type: 'heatmap',
            colorscale: [[0, 'rgba(0,0,0,0)'], [1, 'rgba(255,0,0,0.4)']],  // transparent red
            showscale: false,
            opacity: 1.0,
            hoverinfo: 'skip'
        };
        
        const doseLayer = {
            z: dose,
            type: 'heatmap',
            colorscale: 'Jet',
            showscale: true,
            opacity: 0.4,
            colorbar: {
                title: 'Dose (Gy)'
            },
            hoverinfo: 'skip'
        };
        
        Plotly.newPlot('plotly-ct-overlay', [ctLayer, doseLayer, maskLayer], layoutDoseOverlay);

        console.log("Finished plotting dose data");

    } catch (error) {
        console.error("Error fetching dose data:", error);
    }
}

export async function uploadDicomFolder() {
    const input = document.getElementById("dicom-folder");
    const formData = new FormData();
    for (let file of input.files) {
        formData.append("dicom_folder", file);
    }

    const res = await fetch("/roi/upload_dicom", {
        method: "POST",
        body: formData
    });

    const data = await res.json();
    const ul = document.getElementById("roi-list");
    ul.innerHTML = "";
    if (data.roi_names) {
        data.roi_names.forEach(name => {
            const li = document.createElement("li");
            li.textContent = name;
            ul.appendChild(li);
        });
    } else {
        ul.innerHTML = `<li>Error: ${data.error}</li>`;
    }
}

export async function loadDatasets() {
    const ul = document.getElementById("dataset-list");
    ul.innerHTML = "Loading...";

    try {
        const res = await fetch("/load_data/datasets");
        const data = await res.json();

        ul.innerHTML = ""; // Clear loading message

        if (data.datasets) {
            data.datasets.forEach(name => {
                const li = document.createElement("li");
                li.textContent = name;
                li.onclick = () => alert(`Selected dataset: ${name}`);
                ul.appendChild(li);
            });
        } else {
            ul.innerHTML = `<li>Error: ${data.error}</li>`;
        }
    } catch (err) {
        console.error("Failed to load datasets", err);
        ul.innerHTML = `<li>Fetch error</li>`;
    }
}

export async function listDatasets() {
    const response = await fetch('/load_data/datasets');
    const data = await response.json();
  
    const dropdown = document.getElementById("datasetDropdown");
    dropdown.innerHTML = "";

    // Default placeholder option
    const defaultOption = document.createElement("option");
    defaultOption.value = "";
    defaultOption.textContent = "-- Select a dataset --";
    defaultOption.disabled = true;
    defaultOption.selected = true;
    defaultOption.hidden = true;
    dropdown.appendChild(defaultOption);
  
    if (data.datasets) {
      data.datasets.forEach(name => {
        const option = document.createElement("option");
        option.value = name;
        option.textContent = name;
        dropdown.appendChild(option);
      });
    } else {
      console.error("Error loading datasets:", data.error);
    }
  }
  

  export async function loadSelectedDataset() {
    const dropdown = document.getElementById("datasetDropdown");
    const datasetName = dropdown.value;
    
    const response = await fetch(`/load_data/load_dataset?name=${datasetName}`);
    const result = await response.json();

    if (result.success && result.files) {
        const fileUrls = result.files;

        // Convert URLs to Blob/File objects
        const dicomBlobs = await Promise.all(
            fileUrls.map(async (url) => {
                const res = await fetch(url);
                const blob = await res.blob();
                const fileName = url.split("/").pop();
                return new File([blob], fileName);
            })
        );

        // Display in viewer
        await loadCTImageViewer(dicomBlobs);
    }
}


// Core logic: fetch ROI names for a given dataset
export async function fetchROINames(datasetName) {
    try {
        const response = await fetch(`/load_data/datasets/${datasetName}/rois`);
        const data = await response.json();

        if (data.roi_names) {
            console.log("ROI names:", data.roi_names);
            const roiList = document.getElementById("roi-list");
            roiList.innerHTML = "";
            data.roi_names.forEach(name => {
                const li = document.createElement("li");
                li.textContent = name;
                roiList.appendChild(li);
            });
        } else {
            console.error("Error loading ROI names:", data.error);
        }
    } catch (error) {
        console.error("Failed to fetch ROI names:", error);
    }
}

// Wrapper: fetch using the selected dataset from dropdown
export function fetchROINamesFromDropdown() {
    const dataset = document.getElementById("datasetDropdown").value;
    if (!dataset) {
        alert("Please select a dataset first.");
        return;
    }
    fetchROINames(dataset);
}


// Set external dependencies
cornerstoneWADOImageLoader.external.cornerstone = cornerstone;
cornerstoneWADOImageLoader.external.dicomParser = dicomParser;

cornerstoneTools.external.cornerstone = cornerstone;
cornerstoneTools.init();

export async function loadCTImageViewer(files) {
    const viewer = document.getElementById("dicom-viewer");

    cornerstone.enable(viewer);

    // Load first image in series
    const imageFile = files.find(file => file.name.endsWith(".dcm") || file.name.endsWith(".IMA"));
    if (!imageFile) {
        console.error("No DICOM files found");
        return;
    }

    const imageId = cornerstoneWADOImageLoader.wadouri.fileManager.add(imageFile);
    const image = await cornerstone.loadImage(imageId);

    cornerstone.displayImage(viewer, image);
}


