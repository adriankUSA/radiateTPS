# MVP Roadmap - Fast Track to Product Launch

## 🎯 MVP Focus: Core Treatment Planning Workflow

**Goal:** Get a working product to market ASAP focusing on the essential workflow:
1. **View CT scans** → 2. **Create treatment plans** → 3. **View results**

---

## ✅ What We Already Have (Backend)

- ✅ Database with all models
- ✅ API endpoints for CT, Plans, Dose, Results
- ✅ OpenTPS integration working
- ✅ Dose computation functional
- ✅ DVH generation working

## 🚀 What We Need to Build (Frontend)

### **Priority 1: Core Screens (Week 1)**

#### **1. CT Viewer** (`/viewer/ct/:ct_id`)
**Must Have:**
- Display CT slice with dose overlay
- Slice navigation (scroll/slider)
- Window/Level adjustment
- ROI contour overlay toggle
- Dose overlay toggle
- Basic zoom/pan

**Nice to Have:**
- Multi-planar views (Axial, Coronal, Sagittal)
- Measurement tools
- Export image

#### **2. Plan Creation** (`/plans/new`)
**Must Have:**
- Select patient and CT scan
- Select target ROI
- Add/remove beams
- Configure beam parameters:
  - Gantry angle
  - Couch angle
  - Spot spacing
  - Layer spacing
  - Target margin
- Visual beam placement preview
- Save plan
- Compute dose button

**Nice to Have:**
- Beam templates
- Auto-optimization
- Plan validation

#### **3. Results Viewer** (`/results/:plan_id`)
**Must Have:**
- Dose distribution visualization
- DVH chart (interactive)
- Dose statistics table (D95, D5, mean, max)
- Slice-by-slice navigation
- Export report

**Nice to Have:**
- Plan comparison
- Multi-ROI DVH
- Dose constraint overlays

---

## 📋 MVP Feature List

### **Essential Features (Must Have)**
- [x] Backend API (done)
- [ ] CT Viewer page
- [ ] Plan Creation page
- [ ] Results Viewer page
- [ ] Navigation between pages
- [ ] Connect to API endpoints
- [ ] Loading states
- [ ] Error handling
- [ ] Basic authentication (simple login)

### **Can Wait (Phase 2)**
- Patient management UI (use API directly for now)
- ROI editor (import from datasets for now)
- Plan comparison
- Advanced visualizations
- User settings
- Mobile responsive (desktop first)

---

## 🏗️ Technical Stack for MVP

### **Frontend Framework:**
- **Option 1: React** (recommended for speed)
  - React Router for navigation
  - Material-UI or Ant Design for components
  - Plotly.js for visualizations (already using)
  
- **Option 2: Vue.js** (also good)
  - Vue Router
  - Vuetify or Element Plus
  
- **Option 3: Keep it simple** (fastest)
  - Vanilla JS with modern ES6
  - Use existing Plotly.js
  - Simple routing with hash or query params

### **Recommendation:**
Start with **Option 3 (Vanilla JS)** for fastest MVP, then migrate to React if needed.

---

## 📐 MVP Screen Structure

```
/ (Home/Login - simple)
  ↓
/dashboard (quick patient/plan list)
  ↓
/viewer/ct/:ct_id (CT Viewer)
  ↓
/plans/new?ct_id=X (Plan Creation)
  ↓
/results/:plan_id (Results Viewer)
```

---

## 🎨 MVP UI Design (Minimal)

### **CT Viewer Layout:**
```
┌─────────────────────────────────────┐
│ [← Back] CT Viewer    [Settings]    │
├─────────────────────────────────────┤
│                                     │
│      [CT Image + Dose Overlay]      │
│                                     │
│  Slice: [━━━━━━━━━━━━━━━━━━━━] 75/150│
│  Window: [400] Level: [50]          │
│  [ROI] [Dose] [Reset View]          │
│                                     │
└─────────────────────────────────────┘
```

### **Plan Creation Layout:**
```
┌─────────────────────────────────────┐
│ [← Back] New Plan                   │
├──────────┬──────────────────────────┤
│          │                          │
│ Config   │  [CT Preview with Beams] │
│          │                          │
│ Patient: │                          │
│ [Select] │  Beam 1: 0°              │
│          │  Beam 2: 90°            │
│ CT Scan: │  Beam 3: 270°           │
│ [Select] │                          │
│          │  [Add Beam] [Remove]     │
│ Target:  │                          │
│ [Select] │                          │
│          │  Beam Parameters:        │
│ Beams:   │  Gantry: [0]°            │
│ [Add]    │  Couch:  [0]°            │
│          │  Spot:   [5.0] mm        │
│          │  Layer:  [5.0] mm        │
│          │                          │
│ [Save]   │  [Compute Dose]          │
│ [Cancel] │                          │
│          │                          │
└──────────┴──────────────────────────┘
```

### **Results Viewer Layout:**
```
┌─────────────────────────────────────┐
│ [← Back] Plan Results: Plan A       │
├──────────┬──────────────────────────┤
│          │                          │
│ Stats    │  [Dose Distribution]     │
│          │                          │
│ D95: 95Gy│  [Slice Navigator]       │
│ D5:  98Gy│                          │
│ Mean:96Gy│  [Axial View]            │
│ Max: 99Gy│                          │
│          │                          │
│ DVH      │  Dose Statistics:         │
│ [Chart]  │  • Target: 95-98 Gy      │
│          │  • Coverage: 100%         │
│          │                          │
│          │  [Export] [Compare]       │
│          │                          │
└──────────┴──────────────────────────┘
```

---

## ⚡ Quick Start Implementation Plan

### **Day 1-2: CT Viewer**
- Create `/viewer/ct/:ct_id` page
- Integrate Plotly for CT display
- Add slice navigation
- Connect to `/ct` API endpoint

### **Day 3-4: Plan Creation**
- Create `/plans/new` page
- Build form for plan parameters
- Add beam configuration UI
- Connect to `/plans` POST endpoint

### **Day 5-6: Results Viewer**
- Create `/results/:plan_id` page
- Display dose visualization
- Add DVH chart (Plotly)
- Show dose statistics
- Connect to `/results` API endpoint

### **Day 7: Integration & Polish**
- Connect all pages with navigation
- Add loading states
- Error handling
- Basic styling
- End-to-end testing

---

## 🚀 Deployment Strategy

### **Phase 1: MVP Launch (This Week)**
- Deploy to simple hosting (Render, Railway, or Fly.io)
- Basic authentication (simple login)
- Core workflow working
- Documentation for users

### **Phase 2: Quick Improvements (Week 2)**
- Better error messages
- Performance optimization
- More visualizations
- User feedback

### **Phase 3: Production Polish (Week 3-4)**
- Full authentication system
- User management
- Advanced features
- Mobile responsive

---

## 📝 MVP Success Criteria

**MVP is ready when:**
- ✅ User can view CT scan with dose overlay
- ✅ User can create a treatment plan
- ✅ User can compute dose
- ✅ User can view results with DVH
- ✅ Complete workflow works end-to-end
- ✅ No critical bugs
- ✅ Deployed and accessible online

**Can launch without:**
- ❌ Patient management UI (use API)
- ❌ ROI editor (use dataset imports)
- ❌ Plan comparison
- ❌ Advanced features
- ❌ Mobile optimization (desktop works)

---

## 🎯 Next Steps

1. **Start with CT Viewer** - Most visual, sets foundation
2. **Then Plan Creation** - Core functionality
3. **Finally Results** - Shows value
4. **Connect everything** - Complete workflow
5. **Deploy** - Get it live!

Let's start building! 🚀

