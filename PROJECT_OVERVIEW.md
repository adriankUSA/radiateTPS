# RadiateTPS - Project Overview & Capabilities

## 🎯 Project Purpose
**RadiateTPS** is a **web-based Radiation Treatment Planning System (TPS)** designed to bring advanced proton and photon radiation therapy planning capabilities to the browser. Built on **OpenTPS** (an open-source treatment planning framework), this project aims to make radiation therapy research and planning accessible through a modern web interface.

---

## 🏗️ Current Architecture

### **Backend (Flask/Python)**
- **Framework**: Flask web server
- **Core Dependency**: OpenTPS (for dose calculations)
- **Medical Imaging**: pydicom for DICOM file handling
- **Visualization**: matplotlib for image generation
- **Data Processing**: NumPy, SciPy

### **Frontend (HTML/CSS/JavaScript)**
- **Static HTML pages** with modern UI
- **Plotly.js** for interactive 3D visualizations
- **RESTful API** communication with backend

---

## ✅ What the Codebase CAN Do (Currently Working)

### 1. **Patient Management** ✅
- **Create patients** with:
  - Name (first, middle, last)
  - Patient ID
  - Birth date
  - Sex (M/F)
- **Load/List patients** from JSON storage
- **Storage**: Local JSON files in `patientData/` directory

**API Endpoints:**
- `POST /patients/patients/create` - Create new patient
- `GET /patients/patients/load` - Load all patients

### 2. **DICOM Dataset Management** ✅
- **List available datasets** from `datasets/` folder
- **Load specific datasets** (currently has 1 sample: `ProKnows_2018_TROG_Plan_Study_SRS_Brain`)
- **Extract ROI (Region of Interest) names** from RT Structure files
- **Upload DICOM folders** via web interface

**API Endpoints:**
- `GET /load_data/datasets` - List all datasets
- `GET /load_data/<dataset_name>` - Load specific dataset and get ROIs
- `GET /load_data/datasets/<dataset_name>/rois` - Get ROIs for dataset
- `POST /uploads/upload_dicom` - Upload DICOM files

### 3. **Dose Computation** ✅ (Requires OpenTPS)
When OpenTPS is properly installed, the system can:

#### **Proton Therapy Dose Calculation**
- **MCsquare Monte Carlo** dose calculator integration
- **3D dose distribution** computation
- **Multi-beam planning** (supports multiple gantry angles)
- **Beam configuration**:
  - Gantry angles (0°, 90°, 270°)
  - Couch angles
  - Spot spacing (5.0mm)
  - Layer spacing (5.0mm)
  - Target margins (5.0mm)

#### **Dose Metrics & Analysis**
- **DVH (Dose Volume Histogram)** generation
- **D95, D5** dose statistics
- **Dose uniformity** calculations (D5 - D95)
- **3D dose visualization** on CT slices

**API Endpoints:**
- `GET /tutorial/compute_dose` - Run dose computation (tutorial example)
- `GET /plotly/compute_dose` - Run dose computation with Plotly data
- `GET /tutorial/get_image` - Get generated dose images
- `GET /plotly/get_image` - Get dose visualization images

### 4. **Medical Imaging Visualization** ✅
- **CT scan display** with Hounsfield Unit (HU) mapping
- **ROI contour overlay** on CT images
- **Dose distribution overlay** on anatomical images
- **Interactive Plotly visualizations**:
  - CT slice heatmaps
  - Dose distribution heatmaps
  - ROI contour overlays
  - DVH curves

### 5. **Web Interface** ✅
- **Homepage** with project information
- **Tutorial page** with interactive features:
  - Patient creation form
  - Dataset selection dropdown
  - ROI name display
  - Interactive dose visualizations
  - Real-time dose computation triggers

---

## ⚠️ What's NOT Fully Implemented (Placeholders)

### 1. **Main API Routes** (Currently TODOs)
These routes exist but return "Not Implemented" messages:
- `POST /ct` - Upload CT scan
- `GET /ct` - Load existing CT scan
- `POST /roi` - Define new ROI
- `GET /roi` - Retrieve available ROIs
- `POST /dose` - Compute dose (main endpoint)
- `GET /results` - Retrieve stored results

### 2. **Authentication & User Management**
- Login/Signup buttons exist in UI but not functional
- No user database or session management

### 3. **Data Persistence**
- Patients stored as JSON files (not a database)
- No persistent storage for CT scans, dose plans, or results
- Images generated but not stored in database

### 4. **Production Features**
- No database integration
- No cloud storage for DICOM files
- No user authentication
- No multi-user support
- No plan saving/loading

---

## 🔬 Technical Capabilities (When OpenTPS is Installed)

### **OpenTPS Integration Features:**
1. **CT Image Processing**
   - Load DICOM CT series
   - Convert Hounsfield Units (HU) to Relative Stopping Power (RSP)
   - 3D image resampling and registration

2. **ROI (Region of Interest) Management**
   - Load RT Structure files
   - Extract contour data
   - Create binary masks
   - Calculate center of mass

3. **Treatment Plan Design**
   - **Proton plans**: `ProtonPlanDesign`
   - **Photon plans**: `PhotonPlanDesign` (available but not used)
   - Beam angle optimization
   - Spot pattern generation

4. **Dose Calculation**
   - **MCsquare** Monte Carlo simulation
   - Configurable primary particle count (default: 10 million)
   - Beam model calibration (BDL files)
   - Scanner calibration data

5. **Dose Analysis**
   - DVH computation for any ROI
   - Dose statistics (D95, D5, mean, max)
   - Dose distribution visualization
   - Multi-ROI analysis capability

---

## 📊 Sample Dataset

**ProKnows_2018_TROG_Plan_Study_SRS_Brain**
- **191 DICOM files** (.dcm)
- Contains CT images and RT Structure data
- Used for testing and demonstration

---

## 🎨 Frontend Features

### **Interactive Visualizations (Plotly)**
1. **CT + ROI + Dose Overlay**
   - Multi-layer heatmap visualization
   - CT grayscale base layer
   - ROI contour overlay (red)
   - Dose distribution overlay (color-coded)

2. **Dose Volume Histogram (DVH)**
   - Interactive line plot
   - Dose (Gy) vs Volume (%)
   - Real-time updates

3. **CT Slice Viewer**
   - 2D slice visualization
   - ROI contour overlay
   - Adjustable slice selection

---

## 🚀 Development Status

### **✅ Completed:**
- Basic Flask server setup
- Patient CRUD operations (JSON-based)
- Dataset listing and loading
- ROI extraction from DICOM
- Dose computation pipeline (with OpenTPS)
- Image generation and serving
- Interactive web visualizations
- DICOM file upload interface

### **🔄 In Progress / Needs Work:**
- Main API route implementations
- Database integration
- User authentication
- Plan persistence
- Error handling and validation
- Production deployment setup

### **📝 Known Issues (from README):**
1. **Path dependencies**: OpenTPS paths hardcoded for Windows (`C:\opentps\opentps_core`)
2. **Image generation**: Currently done on backend, should be moved to frontend
3. **GUI replication**: Need to replicate OpenTPS GUI functionality in web interface

---

## 🎯 Use Cases

### **Current Use Cases:**
1. **Research & Education**
   - Teaching radiation therapy planning concepts
   - Prototype testing for new algorithms
   - Academic research projects

2. **Dose Computation Testing**
   - Run dose calculations on sample datasets
   - Visualize dose distributions
   - Analyze DVH curves

3. **Dataset Exploration**
   - Browse available DICOM datasets
   - Extract ROI information
   - View CT images with overlays

### **Potential Future Use Cases:**
1. **Clinical Planning** (with proper validation)
2. **Multi-user collaboration**
3. **Cloud-based treatment planning**
4. **Integration with hospital PACS systems**

---

## 🔧 Dependencies

### **Core Python Libraries:**
- Flask (web framework)
- Flask-CORS (cross-origin support)
- NumPy (numerical computing)
- Matplotlib (image generation)
- pydicom (DICOM file handling)
- SciPy (scientific computing)
- SimpleITK (medical image processing)

### **External Dependencies:**
- **OpenTPS** (required for dose calculations)
  - MCsquare dose calculator
  - Scanner calibration data
  - Beam model files (BDL)

### **Frontend:**
- Plotly.js (interactive visualizations)
- Vanilla JavaScript (ES6 modules)

---

## 📈 Next Steps for Development

### **Priority 1: Core Functionality**
1. Implement main API routes (`/ct`, `/roi`, `/dose`, `/results`)
2. Add database (PostgreSQL or SQLite) for data persistence
3. Implement plan saving/loading
4. Add proper error handling

### **Priority 2: User Experience**
1. User authentication and authorization
2. Multi-user support
3. Plan history and versioning
4. Better UI/UX for treatment planning workflow

### **Priority 3: Production Readiness**
1. Cloud deployment (AWS, GCP, or Azure)
2. DICOM file cloud storage (S3, etc.)
3. Production WSGI server (Gunicorn)
4. Security hardening
5. HIPAA compliance considerations (if clinical use)

### **Priority 4: Advanced Features**
1. Real-time dose computation progress
2. Multi-ROI dose analysis
3. Plan comparison tools
4. Export capabilities (DICOM RT Dose, reports)
5. Integration with PACS systems

---

## 🎓 Academic Context

This project is being developed under **Professor Yan at UNCC** to:
- Create a viable web-based treatment planning system
- Make radiation therapy research more accessible
- Provide a platform for algorithm development and testing
- Potentially serve as a foundation for clinical tools (with proper validation)

---

## 📝 Summary

**RadiateTPS** is a **functional prototype** of a web-based TPS with:
- ✅ Working dose computation (with OpenTPS)
- ✅ Patient management
- ✅ DICOM dataset handling
- ✅ Interactive visualizations
- ⚠️ Needs: Database, authentication, main API implementation
- 🎯 Goal: Transform into a production-ready web application

The foundation is solid, but significant development is needed to make it a fully viable web application for clinical or research use.

