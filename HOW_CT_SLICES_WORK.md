# How CT Slices Are Loaded - Technical Explanation

## 📁 Where the 190 Slices Come From

### **Source: DICOM Files in Dataset Folder**

The 190 CT slices come from **DICOM (Digital Imaging and Communications in Medicine) files** stored in:
```
backend/datasets/ProKnows_2018_TROG_Plan_Study_SRS_Brain/
```

This folder contains approximately **190 DICOM files** (`.dcm` files), where each file represents **one CT slice**.

---

## 🔄 How It Works

### **Step 1: Dataset Contains DICOM Files**
```
datasets/ProKnows_2018_TROG_Plan_Study_SRS_Brain/
├── 1.2.826.0.1.3680043.6.11113.80068.20170905183644.6880.5.172.dcm  (Slice 1)
├── 1.2.826.0.1.3680043.6.11219.36586.20170905183631.6880.5.19.dcm   (Slice 2)
├── 1.2.826.0.1.3680043.6.11893.99074.20170905183643.6880.5.157.dcm  (Slice 3)
├── ... (approximately 190 DICOM files total)
└── (last slice DICOM file)
```

Each `.dcm` file is a **single CT slice** from the original medical scan.

---

### **Step 2: OpenTPS Reads All DICOM Files**

When you call:
```python
data_objects = readData(dataset_path)
```

OpenTPS's `readData()` function:
1. **Scans the dataset folder** for all DICOM files
2. **Reads each DICOM file** using pydicom
3. **Combines them** into a single 3D CT image object
4. **Creates a CTImage object** with a 3D numpy array

The result is a **3D array** with shape `[512, 512, 190]`:
- **512 × 512** = Pixel dimensions of each slice (width × height)
- **190** = Number of slices (Z dimension)

---

### **Step 3: CT Image Object Structure**

```python
ct_image.imageArray.shape  # Returns: (512, 512, 190)

# Access individual slices:
ct_image.imageArray[:, :, 0]   # Slice 0 (first slice)
ct_image.imageArray[:, :, 1]   # Slice 1
ct_image.imageArray[:, :, 95]  # Slice 95 (middle)
ct_image.imageArray[:, :, 189] # Slice 189 (last slice)
```

Each slice is a **2D array** of Hounsfield Units (HU):
- Values around **-1000 HU** = Air
- Values around **0 HU** = Water/Soft tissue
- Values **> 0 HU** = Denser tissue (bone, contrast, etc.)

---

### **Step 4: When You Request a Slice**

When you call:
```
GET /ct/4/slice/95
```

The code:
1. **Loads the dataset** again using `readData(dataset_path)`
2. **Extracts the CTImage** from the loaded data
3. **Gets slice 95** from the 3D array: `ct_image.imageArray[:, :, 95]`
4. **Transposes it** for display: `.transpose(1, 0)`
5. **Converts to list** and returns as JSON

---

## 📊 Data Flow Diagram

```
DICOM Files (190 files)
    ↓
OpenTPS readData()
    ↓
CTImage Object (3D array: 512×512×190)
    ↓
Extract Slice [:, :, slice_num]
    ↓
2D Array (512×512)
    ↓
Transpose & Convert to JSON
    ↓
API Response
    ↓
Frontend CT Viewer
```

---

## 💾 Storage Details

### **What's Stored in Database:**
- **CTScan record** stores:
  - `file_path`: Path to dataset folder
  - `dataset_name`: "ProKnows_2018_TROG_Plan_Study_SRS_Brain"
  - `slice_count`: 190 (metadata)
  - `grid_size`: [512, 512, 190] (metadata)
  - `spacing`: [0.468, 0.468, 1.0] mm (voxel spacing)
  - `origin`: [-120.0, -120.0, -797.5] (image origin)

### **What's NOT Stored:**
- ❌ The actual CT image data (not stored in database)
- ❌ Individual slice arrays (not cached)

### **Why Not Store It?**
- **Size**: 512 × 512 × 190 = ~100 million pixels
- **Memory**: Would require ~400MB+ per CT scan
- **Efficiency**: Load on-demand is more efficient

---

## 🔄 Current Implementation

### **Every Slice Request:**
1. Loads the entire dataset from disk
2. Reads all 190 DICOM files
3. Extracts the requested slice
4. Returns it

**Pros:**
- ✅ Simple implementation
- ✅ Always up-to-date
- ✅ No caching complexity

**Cons:**
- ⚠️ Slower (loads dataset each time)
- ⚠️ Could be optimized with caching

---

## 🚀 Potential Optimizations

### **Option 1: Cache CT Image in Memory**
```python
# Cache the CTImage object after first load
ct_image_cache = {}

def get_ct_slice(ct_id, slice_num):
    if ct_id not in ct_image_cache:
        # Load once, cache it
        data_objects = readData(dataset_path)
        ct_image_cache[ct_id] = next(...)
    
    # Extract slice from cached image
    ct_slice = ct_image_cache[ct_id].imageArray[:, :, slice_num]
```

### **Option 2: Pre-extract All Slices**
- Extract all 190 slices when CT is loaded
- Store as individual files or in database
- Faster retrieval, but uses more storage

### **Option 3: Slice Range Caching**
- Cache recently requested slices
- Keep last N slices in memory
- Good balance of speed and memory

---

## 📝 Summary

**The 190 slices come from:**
1. ✅ **190 DICOM files** in the dataset folder
2. ✅ **OpenTPS reads them** and combines into a 3D array
3. ✅ **Each slice request** extracts one 2D slice from the 3D array
4. ✅ **No slices are generated** - they're all from the original medical scan

**The dataset is a real medical imaging dataset** (ProKnows 2018 TROG Plan Study SRS Brain), containing actual patient CT scan data with 190 axial slices through the brain.

---

## 🔍 Verify It Yourself

```bash
# Count DICOM files
find backend/datasets/ProKnows_2018_TROG_Plan_Study_SRS_Brain -name "*.dcm" | wc -l

# Should return approximately 190
```

Each `.dcm` file = 1 CT slice = 1 of the 190 slices you can view!

