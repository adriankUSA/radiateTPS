# Testing the CT Viewer

## 🎯 Where to Test

### **1. CT Viewer Page**
**URL:** `http://localhost:5001/viewer-ct.html`

You can access it with different parameters:
- `http://localhost:5001/viewer-ct.html?ct_id=1` - View specific CT scan
- `http://localhost:5001/viewer-ct.html?patient_id=P001` - View CT scans for a patient
- `http://localhost:5001/viewer-ct.html` - Will try to load any available CT scan

### **2. From Dashboard**
**URL:** `http://localhost:5001/dashboard.html`
- Click on a patient → Opens CT Viewer
- Or click "View CT" button on a patient

---

## 📋 Step-by-Step Testing Guide

### **Step 1: Create a Patient (if needed)**

**Option A: Via API**
```bash
curl -X POST http://localhost:5001/patients/create \
  -H "Content-Type: application/json" \
  -d '{
    "id": "P001",
    "name": "Test Patient",
    "birthDate": "1990-01-01",
    "sex": "M"
  }'
```

**Option B: Via Dashboard**
1. Go to `http://localhost:5001/dashboard.html`
2. Click "+ New Patient"
3. Fill in patient details

---

### **Step 2: Load a CT Scan**

**Option A: Load from Dataset (if OpenTPS is available)**

```bash
# First, check available datasets
curl http://localhost:5001/load_data/datasets

# Load a CT scan from a dataset
curl -X POST http://localhost:5001/ct \
  -H "Content-Type: application/json" \
  -d '{
    "patient_id": "P001",
    "dataset_name": "ProKnows_2018_TROG_Plan_Study_SRS_Brain",
    "name": "Brain CT Scan"
  }'
```

**Option B: Use the Load Data Endpoint**
```bash
# This loads the dataset and returns ROI names
curl http://localhost:5001/load_data/ProKnows_2018_TROG_Plan_Study_SRS_Brain?patient_id=P001
```

**Note:** For MVP, the CT viewer currently uses sample data from `/plotly/compute_dose` endpoint for visualization.

---

### **Step 3: View the CT Scan**

1. **Direct Access:**
   - Open: `http://localhost:5001/viewer-ct.html?patient_id=P001`
   - Or: `http://localhost:5001/viewer-ct.html?ct_id=1`

2. **From Dashboard:**
   - Go to `http://localhost:5001/dashboard.html`
   - Find your patient in the list
   - Click "View CT" button

---

## 🧪 What to Test

### **CT Viewer Features:**

1. **✅ Slice Navigation**
   - Use the slider to navigate through slices
   - Check that slice number updates
   - (Note: Currently shows sample data, slice navigation will load real data in future)

2. **✅ Window/Level Adjustment**
   - Adjust Window value (default: 400)
   - Adjust Level value (default: 50)
   - Click "Reset" to restore defaults

3. **✅ Overlay Toggles**
   - Click "ROI" button to toggle ROI contours
   - Click "Dose" button to toggle dose overlay
   - Check that overlays appear/disappear

4. **✅ View Selection**
   - Click "Axial", "Coronal", or "Sagittal"
   - (Note: Currently only Axial view is implemented)

5. **✅ Create Plan Button**
   - Click "Create Plan from this CT"
   - Should navigate to plan creation page with CT ID

---

## 🔍 API Endpoints for CT Scans

### **Get CT Scans**
```bash
# Get all CT scans
GET http://localhost:5001/ct

# Get CT scans for a specific patient
GET http://localhost:5001/ct?patient_id=P001

# Get specific CT scan
GET http://localhost:5001/ct?ct_scan_id=1
```

**Response:**
```json
{
  "success": true,
  "ct_scans": [
    {
      "id": 1,
      "patient_id": "P001",
      "name": "Brain CT Scan",
      "slice_count": 150,
      "dataset_name": "ProKnows_2018_TROG_Plan_Study_SRS_Brain",
      "created_at": "2025-12-26T..."
    }
  ],
  "count": 1
}
```

### **Upload/Load CT Scan**
```bash
POST http://localhost:5001/ct
Content-Type: application/json

{
  "patient_id": "P001",
  "dataset_name": "ProKnows_2018_TROG_Plan_Study_SRS_Brain",
  "name": "My CT Scan"
}
```

---

## 🎨 Current Limitations (MVP)

### **What Works:**
- ✅ CT Viewer page loads
- ✅ Displays sample CT data with overlays
- ✅ Slice slider UI
- ✅ Window/Level controls UI
- ✅ ROI/Dose toggle buttons
- ✅ Navigation to plan creation

### **What's Simplified:**
- ⚠️ Currently uses sample data from `/plotly/compute_dose` endpoint
- ⚠️ Slice navigation doesn't load new slices yet (uses same data)
- ⚠️ Window/Level adjustment not fully implemented (UI ready, logic pending)
- ⚠️ Multi-planar views (Coronal/Sagittal) not implemented yet

### **What's Coming:**
- 🔄 Real CT slice loading from database
- 🔄 Proper slice navigation
- 🔄 Window/Level application
- 🔄 Multi-planar reconstruction

---

## 🚀 Quick Test Script

Here's a complete test flow:

```bash
# 1. Create a patient
curl -X POST http://localhost:5001/patients/create \
  -H "Content-Type: application/json" \
  -d '{"id": "P001", "name": "Test Patient", "birthDate": "1990-01-01", "sex": "M"}'

# 2. Check if patient was created
curl http://localhost:5001/patients/load

# 3. Load a CT scan (if you have OpenTPS and datasets)
curl -X POST http://localhost:5001/ct \
  -H "Content-Type: application/json" \
  -d '{"patient_id": "P001", "dataset_name": "ProKnows_2018_TROG_Plan_Study_SRS_Brain", "name": "Brain CT"}'

# 4. Get CT scans
curl http://localhost:5001/ct?patient_id=P001

# 5. Open in browser
# http://localhost:5001/viewer-ct.html?patient_id=P001
```

---

## 🐛 Troubleshooting

### **"No CT scans found"**
- Make sure you've loaded a CT scan first using the `/ct` POST endpoint
- Check that the patient_id matches

### **"Failed to load CT scan"**
- Check browser console (F12) for errors
- Verify the Flask server is running on port 5001
- Check that API endpoints are responding

### **CT Viewer shows placeholder**
- This is normal if no CT data is loaded
- The viewer uses sample data from `/plotly/compute_dose` for MVP
- In production, it will load real CT slice data

### **Controls not working**
- Make sure JavaScript is enabled
- Check browser console for errors
- Try refreshing the page

---

## 📝 Next Steps for Full Implementation

To make the CT viewer fully functional:

1. **Create CT Slice Endpoint:**
   ```python
   @main.route("/ct/<int:ct_id>/slice/<int:slice_num>")
   def get_ct_slice(ct_id, slice_num):
       # Return CT slice data as JSON
   ```

2. **Update `loadCTImage()` function:**
   - Replace `/plotly/compute_dose` with real CT slice endpoint
   - Load slice based on `currentSlice` value

3. **Implement Window/Level:**
   - Apply window/level transformation to CT data
   - Update display in real-time

4. **Add Multi-planar Views:**
   - Implement coronal and sagittal slice extraction
   - Update `setView()` function

---

## ✅ Testing Checklist

- [ ] CT Viewer page loads
- [ ] Can navigate to viewer from dashboard
- [ ] Slice slider appears and moves
- [ ] Window/Level controls are visible
- [ ] ROI toggle button works
- [ ] Dose toggle button works
- [ ] "Create Plan" button navigates correctly
- [ ] API endpoints return CT scan data
- [ ] No console errors in browser

---

**Happy Testing! 🎉**

