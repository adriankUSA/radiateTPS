# Current Project Capabilities - RadiateTPS

## 🎯 What This Project Can Do Right Now

### ✅ **Fully Functional Features**

#### **1. Patient Management**
- ✅ **Create patients** via API or web interface
  - Store: ID, name, birth date, sex
  - Save to SQLite database
  - Backward compatible with JSON files
  
- ✅ **List/View patients**
  - Get all patients via API
  - View in dashboard
  - Patient data persists in database

**API Endpoints:**
- `POST /patients/create` - Create new patient
- `GET /patients/load` - List all patients

---

#### **2. CT Scan Management**
- ✅ **Load CT scans from datasets**
  - Supports OpenTPS dataset format
  - Extracts CT metadata (slice count, spacing, grid size)
  - Stores in database with patient association
  
- ✅ **List available datasets**
  - Discover datasets in `/datasets` folder
  - Currently supports: `ProKnows_2018_TROG_Plan_Study_SRS_Brain`
  
- ✅ **View CT scan information**
  - Get CT scans by patient ID
  - Get CT scans by CT scan ID
  - View metadata (slices, dimensions, spacing)

**API Endpoints:**
- `GET /load_data/datasets` - List available datasets
- `GET /load_data/<dataset_name>` - Load dataset and get ROI names
- `POST /ct` - Upload/load CT scan from dataset
- `GET /ct?patient_id=X` - Get CT scans for patient
- `GET /ct?ct_scan_id=X` - Get specific CT scan

---

#### **3. ROI (Region of Interest) Management**
- ✅ **Extract ROI names from datasets**
  - Automatically identifies ROIs in RT Structure files
  - Returns list of available ROIs (targets, OARs, normal structures)
  
- ✅ **Store ROI data**
  - ROIs linked to patients and CT scans
  - Database storage for ROI metadata

**API Endpoints:**
- `GET /load_data/<dataset_name>` - Returns ROI names
- `POST /roi` - Create ROI (from dataset)
- `GET /roi?patient_id=X` - Get ROIs for patient

**Current Dataset ROIs:**
- 6 GTVs (Gross Tumor Volumes)
- 10 OARs (Organs at Risk): Eyes, Lenses, Optic Nerves, Chiasm, Hippocampus, Brainstem
- 4 Normal structures: Brain, Normal Brain, BODY, Bones

---

#### **4. Treatment Plan Creation**
- ✅ **Create treatment plans**
  - Configure multiple beams
  - Set gantry angles, couch angles
  - Configure spot spacing, layer spacing, target margin
  - Select plan type (Proton/Photon)
  - Link to patient, CT scan, and target ROI
  
- ✅ **Store plans in database**
  - Full plan configuration saved
  - Plan history and versioning support
  - Query plans by patient or plan ID

**API Endpoints:**
- `POST /plans` - Create new treatment plan
- `GET /plans` - List all plans
- `GET /plans/<id>` - Get specific plan details

**Plan Configuration:**
- Plan name, type (Proton/Photon)
- Multiple beams with gantry/couch angles
- Spot spacing (default: 5.0 mm)
- Layer spacing (default: 5.0 mm)
- Target margin (default: 5.0 mm)
- Target ROI selection

---

#### **5. Dose Computation** (Requires OpenTPS)
- ✅ **Compute dose distributions**
  - Uses OpenTPS MCsquare dose calculator
  - Supports proton therapy planning
  - Computes 3D dose distribution
  
- ✅ **Generate DVH (Dose-Volume Histogram)**
  - Calculates dose statistics for ROIs
  - D95, D5, mean, max dose values
  - Dose-volume histogram data
  
- ✅ **Store dose results**
  - Saves computation results to database
  - Links to plan, CT scan, and ROI
  - Stores visualization images

**API Endpoints:**
- `POST /dose` - Compute dose for a plan
- `GET /results?plan_id=X` - Get dose computation results
- `GET /get_image?image=filename.png` - Get visualization images

**Dose Statistics:**
- D95 (dose to 95% of volume)
- D5 (dose to 5% of volume)
- Mean dose
- Max dose
- Uniformity (D5 - D95)

---

#### **6. Web Interface (MVP)**

##### **Dashboard** (`/dashboard.html`)
- ✅ View statistics (active plans, patients, CT scans, completed)
- ✅ List recent plans with quick actions
- ✅ List recent patients
- ✅ Quick navigation to CT viewer and plan creation

##### **CT Viewer** (`/viewer-ct.html`)
- ✅ Display CT scan with overlays
- ✅ Slice navigation slider (UI ready)
- ✅ Window/Level controls (UI ready)
- ✅ ROI overlay toggle
- ✅ Dose overlay toggle
- ✅ Multi-planar view buttons (Axial/Coronal/Sagittal - UI ready)
- ✅ Navigate to plan creation

**Note:** Currently uses sample data from `/plotly/compute_dose` for visualization. Real CT slice loading coming next.

##### **Plan Creation** (`/plan-create.html`)
- ✅ Form-based plan configuration
- ✅ Patient and CT scan selection
- ✅ Dynamic beam management (add/remove beams)
- ✅ Beam parameter configuration
- ✅ Plan preview summary
- ✅ Save plan or save & compute dose

##### **Results Viewer** (`/plan-results.html`)
- ✅ Display dose statistics (D95, D5, mean, max)
- ✅ Interactive DVH chart (Plotly.js)
- ✅ Dose distribution visualization
- ✅ Tabbed interface (Dose/DVH/Statistics)
- ✅ Slice navigation

##### **Dose Computation** (`/plan-compute.html`)
- ✅ Progress indicator
- ✅ Status messages
- ✅ Auto-polling for completion
- ✅ Auto-redirect to results when done

---

### 🔧 **Technical Capabilities**

#### **Database**
- ✅ SQLite database with full schema
- ✅ Models: Patient, CTScan, ROI, TreatmentPlan, DoseResult
- ✅ Relationships and foreign keys
- ✅ Automatic table creation

#### **API Architecture**
- ✅ RESTful API design
- ✅ JSON request/response format
- ✅ Error handling and validation
- ✅ CORS enabled for frontend access

#### **OpenTPS Integration**
- ✅ Optional OpenTPS support (graceful degradation)
- ✅ Dataset loading via OpenTPS
- ✅ Dose computation via MCsquare
- ✅ DVH generation
- ✅ Works without OpenTPS (limited mode)

#### **Data Persistence**
- ✅ Database storage for all entities
- ✅ Backward compatibility with JSON files
- ✅ File upload support (DICOM - structure ready)

---

### 📊 **Current Workflow**

#### **Complete Treatment Planning Workflow:**

1. **Create Patient**
   ```
   POST /patients/create
   → Patient stored in database
   ```

2. **Load CT Scan**
   ```
   POST /ct (with dataset_name)
   → CT scan loaded and stored
   ```

3. **View CT Scan**
   ```
   GET /ct?patient_id=X
   → Open viewer-ct.html
   → View CT with overlays
   ```

4. **Create Treatment Plan**
   ```
   POST /plans
   → Configure beams and parameters
   → Plan saved to database
   ```

5. **Compute Dose**
   ```
   POST /dose (with plan_id)
   → OpenTPS computes dose
   → Results stored in database
   ```

6. **View Results**
   ```
   GET /results?plan_id=X
   → View DVH, statistics, dose distribution
   ```

---

### 🎨 **User Interface Features**

- ✅ **Dark theme** medical software design
- ✅ **Responsive layout** (desktop optimized)
- ✅ **Interactive visualizations** (Plotly.js)
- ✅ **Navigation** between pages
- ✅ **Form validation** and error handling
- ✅ **Loading states** and progress indicators
- ✅ **Consistent styling** across all pages

---

### 📈 **What's Working End-to-End**

#### **✅ Fully Functional:**
1. Patient creation and management
2. CT scan loading from datasets
3. ROI extraction from datasets
4. Treatment plan creation
5. Dose computation (with OpenTPS)
6. Results viewing with DVH
7. Database persistence
8. API endpoints

#### **⚠️ Partially Functional (MVP):**
1. CT Viewer - UI complete, uses sample data
2. Slice navigation - UI ready, needs real data endpoint
3. Window/Level - UI ready, needs implementation
4. Multi-planar views - UI ready, needs implementation

#### **🔜 Coming Next:**
1. Real CT slice loading endpoint
2. Proper slice navigation
3. Window/Level application
4. ROI editor
5. Plan comparison
6. Export functionality
7. Authentication

---

### 🚀 **How to Use Right Now**

#### **Via Web Interface:**
1. Start server: `./run.sh` or `cd backend && python app.py`
2. Open: `http://localhost:5001/dashboard.html`
3. Create patient → Load CT → Create Plan → Compute Dose → View Results

#### **Via API:**
```bash
# Create patient
curl -X POST http://localhost:5001/patients/create \
  -H "Content-Type: application/json" \
  -d '{"id": "P001", "name": "Test", "birthDate": "1990-01-01", "sex": "M"}'

# Load CT scan
curl -X POST http://localhost:5001/ct \
  -H "Content-Type: application/json" \
  -d '{"patient_id": "P001", "dataset_name": "ProKnows_2018_TROG_Plan_Study_SRS_Brain", "name": "Brain CT"}'

# Create plan
curl -X POST http://localhost:5001/plans \
  -H "Content-Type: application/json" \
  -d '{"patient_id": "P001", "ct_scan_id": 1, "plan_name": "Test Plan", ...}'

# Compute dose
curl -X POST http://localhost:5001/dose \
  -H "Content-Type: application/json" \
  -d '{"plan_id": 1}'

# Get results
curl http://localhost:5001/results?plan_id=1
```

---

### 📋 **Summary**

**This is a functional treatment planning system MVP that can:**
- ✅ Manage patients and CT scans
- ✅ Create treatment plans with multiple beams
- ✅ Compute dose distributions (with OpenTPS)
- ✅ Generate and view DVH curves
- ✅ Store all data in a database
- ✅ Provide a web interface for all operations

**It's ready for:**
- ✅ Testing and validation
- ✅ Demonstration
- ✅ Further development
- ✅ Integration with additional features

**It needs:**
- 🔄 Real CT slice loading (currently uses sample data)
- 🔄 Enhanced CT viewer features
- 🔄 ROI editor
- 🔄 Authentication
- 🔄 Production deployment

---

**Bottom Line:** You have a working treatment planning system that can create plans, compute doses, and view results. The core workflow is functional end-to-end! 🎉

