# Testing Checklist - RadiateTPS

Use this checklist to verify everything is working after our implementation.

## ✅ Prerequisites Check

- [ ] Flask server starts without errors
- [ ] OpenTPS loads successfully (check for "✅ OpenTPS loaded successfully" in terminal)
- [ ] Database file exists: `backend/radiate_tps.db`
- [ ] Can access homepage: `http://127.0.0.1:5000/`
- [ ] Can access tutorial page: `http://127.0.0.1:5000/tutorial.html`

---

## 🏥 1. Patient Management

### Create Patient
- [ ] **Via Web UI:**
  - Go to `http://127.0.0.1:5000/tutorial.html`
  - Click "Create Patient" button
  - Fill in: First Name, Last Name, Patient ID, Birth Date, Sex
  - Click "Save Patient"
  - Should see success message
 
- [ ] **Via API (curl):**
  ```bash
  curl -X POST http://127.0.0.1:5000/patients/create \
    -H "Content-Type: application/json" \
    -d '{"name":"John Doe","id":"P001","birthDate":"1990-01-01","sex":"M"}'
  ```
  - Should return: `{"success": true, "message": "Patient John Doe saved."}`

### Load Patients
- [ ] **Via Web UI:**
  - Click "Load Patient" button
  - Should see list of created patients

- [ ] **Via API:**
  ```bash
  curl http://127.0.0.1:5000/patients/load
  ```
  - Should return JSON array of patients

---

## 📄 2. CT Scan Management

### List Available Datasets
- [ ] **Via API:**
  ```bash
  curl http://127.0.0.1:5000/load_data/datasets
  ```
  - Should return: `{"datasets": ["ProKnows_2018_TROG_Plan_Study_SRS_Brain"]}`

### Upload CT Scan from Dataset
- [ ] **Via API:**
  ```bash
  # First, create a patient (use ID from step 1)
  # Then upload CT:
  curl -X POST http://127.0.0.1:5000/ct \
    -H "Content-Type: application/json" \
    -d '{
      "patient_id": "P001",
      "dataset_name": "ProKnows_2018_TROG_Plan_Study_SRS_Brain",
      "name": "Brain CT Scan"
    }'
  ```
  - Should return: `{"success": true, "message": "CT scan 'Brain CT Scan' uploaded successfully", "ct_scan": {...}}`

### Get CT Scans
- [ ] **Via API:**
  ```bash
  curl "http://127.0.0.1:5000/ct?patient_id=P001"
  ```
  - Should return list of CT scans for that patient

---

## 🎯 3. ROI Management

### Get ROIs from Dataset
- [ ] **Via API:**
  ```bash
  curl http://127.0.0.1:5000/load_data/ProKnows_2018_TROG_Plan_Study_SRS_Brain
  ```
  - Should return ROI names from the dataset

### Create ROI
- [ ] **Via API:**
  ```bash
  curl -X POST http://127.0.0.1:5000/roi \
    -H "Content-Type: application/json" \
    -d '{
      "patient_id": "P001",
      "ct_scan_id": 1,
      "name": "Target",
      "roi_type": "Target",
      "color": "255,0,0"
    }'
  ```
  - Should return: `{"success": true, "message": "ROI 'Target' created successfully", "roi": {...}}`

### List ROIs
- [ ] **Via API:**
  ```bash
  curl "http://127.0.0.1:5000/roi?patient_id=P001"
  ```
  - Should return list of ROIs

---

## 💾 4. Treatment Plan Management

### Create Plan
- [ ] **Via API:**
  ```bash
  curl -X POST http://127.0.0.1:5000/plans \
    -H "Content-Type: application/json" \
    -d '{
      "patient_id": "P001",
      "ct_scan_id": 1,
      "plan_name": "Test Plan",
      "plan_type": "Proton",
      "beam_names": ["Beam1", "Beam2", "Beam3"],
      "gantry_angles": [0, 90, 270],
      "couch_angles": [0, 0, 0],
      "spot_spacing": 5.0,
      "layer_spacing": 5.0,
      "target_margin": 5.0
    }'
  ```
  - Should return: `{"success": true, "message": "Plan 'Test Plan' saved successfully", "plan": {...}}`

### List Plans
- [ ] **Via API:**
  ```bash
  curl "http://127.0.0.1:5000/plans?patient_id=P001"
  ```
  - Should return list of plans

### Get Specific Plan
- [ ] **Via API:**
  ```bash
  curl http://127.0.0.1:5000/plans/1
  ```
  - Should return plan details with associated dose results

---

## ☢️ 5. Dose Computation

### Compute Dose
- [ ] **Via API:**
  ```bash
  curl -X POST http://127.0.0.1:5000/dose \
    -H "Content-Type: application/json" \
    -d '{
      "plan_id": 1
    }'
  ```
  - **Note:** This requires OpenTPS and may take several minutes
  - Should return: `{"success": true, "message": "Dose computation completed", "result": {...}}`
  - Check terminal for computation progress

### Alternative: Compute with Parameters
- [ ] **Via API:**
  ```bash
  curl -X POST http://127.0.0.1:5000/dose \
    -H "Content-Type: application/json" \
    -d '{
      "patient_id": "P001",
      "ct_scan_id": 1,
      "plan_name": "Quick Dose Test",
      "plan_type": "Proton",
      "beam_names": ["Beam1"],
      "gantry_angles": [0],
      "couch_angles": [0],
      "spot_spacing": 5.0,
      "layer_spacing": 5.0,
      "target_margin": 5.0
    }'
  ```

---

## 📊 6. Results Retrieval

### Get Dose Results
- [ ] **Via API:**
  ```bash
  curl "http://127.0.0.1:5000/results?plan_id=1"
  ```
  - Should return dose results with DVH data

### Get Results by Patient
- [ ] **Via API:**
  ```bash
  curl "http://127.0.0.1:5000/results?patient_id=P001"
  ```
  - Should return all results for that patient

### Get Visualization Image
- [ ] **Via API:**
  ```bash
  curl http://127.0.0.1:5000/get_image?image=dose_result_1_*.png
  ```
  - Should return the dose visualization image

---

## 🌐 7. Frontend Functionality

### Homepage
- [ ] Navigate to `http://127.0.0.1:5000/`
- [ ] Page loads without errors
- [ ] Navigation links work
- [ ] "Try a Tutorial" button works

### Tutorial Page
- [ ] Navigate to `http://127.0.0.1:5000/tutorial.html`
- [ ] Page loads without errors
- [ ] "Create Patient" form appears when clicked
- [ ] Can create patient via form
- [ ] "Load Patient" button works
- [ ] Dataset dropdown populates
- [ ] Can select dataset and load ROIs
- [ ] Dose computation visualizations appear (if dose was computed)

---

## 🔧 8. Error Handling

### Test Invalid Requests
- [ ] **Create patient without ID:**
  ```bash
  curl -X POST http://127.0.0.1:5000/patients/create \
    -H "Content-Type: application/json" \
    -d '{"name":"Test"}'
  ```
  - Should return error message

- [ ] **Upload CT for non-existent patient:**
  ```bash
  curl -X POST http://127.0.0.1:5000/ct \
    -H "Content-Type: application/json" \
    -d '{"patient_id":"INVALID","dataset_name":"test"}'
  ```
  - Should return: `{"error": "Patient with ID INVALID not found"}`

- [ ] **Get CT scans for invalid patient:**
  ```bash
  curl "http://127.0.0.1:5000/ct?patient_id=INVALID"
  ```
  - Should return empty array (not crash)

---

## 🗄️ 9. Database Verification

### Check Database File
- [ ] Database file exists: `backend/radiate_tps.db`
- [ ] File has reasonable size (> 0 bytes)

### Verify Data Persistence
- [ ] Create a patient
- [ ] Restart Flask server
- [ ] Load patients - should still see the patient you created

---

## 🚀 10. OpenTPS Integration

### Verify OpenTPS is Loaded
- [ ] Check Flask server startup logs
- [ ] Should see: `✅ OpenTPS loaded successfully`
- [ ] Should NOT see: `⚠️ OpenTPS not available`

### Test OpenTPS Features
- [ ] Load dataset with ROIs (requires OpenTPS)
- [ ] Compute dose (requires OpenTPS)
- [ ] Generate DVH data (requires OpenTPS)

---

## 📝 Quick Test Script

Run this to test the basic workflow:

```bash
# 1. Create patient
PATIENT_ID="TEST$(date +%s)"
curl -X POST http://127.0.0.1:5000/patients/create \
  -H "Content-Type: application/json" \
  -d "{\"name\":\"Test Patient\",\"id\":\"$PATIENT_ID\",\"birthDate\":\"1990-01-01\",\"sex\":\"M\"}"

# 2. List datasets
curl http://127.0.0.1:5000/load_data/datasets

# 3. Upload CT (replace PATIENT_ID with actual ID from step 1)
curl -X POST http://127.0.0.1:5000/ct \
  -H "Content-Type: application/json" \
  -d "{\"patient_id\":\"$PATIENT_ID\",\"dataset_name\":\"ProKnows_2018_TROG_Plan_Study_SRS_Brain\",\"name\":\"Test CT\"}"

# 4. Get CT scans
curl "http://127.0.0.1:5000/ct?patient_id=$PATIENT_ID"

# 5. Get ROIs
curl http://127.0.0.1:5000/load_data/ProKnows_2018_TROG_Plan_Study_SRS_Brain

# 6. Load patients
curl http://127.0.0.1:5000/patients/load
```

---

## ✅ Success Criteria

Everything is working if:
- ✅ All API endpoints return proper JSON (not HTML error pages)
- ✅ Database persists data between server restarts
- ✅ OpenTPS loads without errors
- ✅ Frontend can create patients and load data
- ✅ Error messages are clear and helpful
- ✅ No crashes or 500 errors

---

## 🐛 Common Issues

### "OpenTPS not available"
- Check that `~/opentps/opentps_core` exists
- Verify path in `backend/application/routes/main.py`
- Restart Flask server

### "405 Method Not Allowed"
- Check the exact endpoint URL
- Verify HTTP method (GET vs POST)
- Check blueprint registration in `app.py`

### "Patient not found"
- Create patient first before using patient_id
- Check patient ID spelling/case

### "Database locked"
- Stop all Flask instances
- Restart server

### CORS errors in browser
- Verify CORS is enabled in `app.py`
- Check browser console for specific error

---

## 📊 Test Results Template

```
Date: ___________
Tester: ___________

Prerequisites: [ ] Pass [ ] Fail
Patient Management: [ ] Pass [ ] Fail
CT Scan Management: [ ] Pass [ ] Fail
ROI Management: [ ] Pass [ ] Fail
Plan Management: [ ] Pass [ ] Fail
Dose Computation: [ ] Pass [ ] Fail
Results Retrieval: [ ] Pass [ ] Fail
Frontend: [ ] Pass [ ] Fail
Error Handling: [ ] Pass [ ] Fail
Database: [ ] Pass [ ] Fail
OpenTPS: [ ] Pass [ ] Fail

Notes:
_______________________________________
_______________________________________
```

