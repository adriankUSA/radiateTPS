# Production-Level Screen Flow - RadiateTPS

## 🎯 Overview

This document outlines the complete user interface flow for a production-ready treatment planning system, following medical software best practices and modern web application design patterns.

---

## 🔐 1. Authentication & Onboarding

### **1.1 Landing Page** (`/`)
**Purpose:** First impression, marketing, login entry point

**Layout:**
- Hero section with value proposition
- Key features showcase
- "Get Started" / "Sign In" buttons
- Footer with links (About, Documentation, Support)

**User Actions:**
- Click "Sign In" → Login Screen
- Click "Get Started" → Registration Screen
- Click "Learn More" → About/Documentation

---

### **1.2 Login Screen** (`/login`)
**Purpose:** User authentication

**Layout:**
- Email/Username input
- Password input
- "Remember me" checkbox
- "Forgot password?" link
- "Sign in" button
- "Don't have an account? Sign up" link

**User Flow:**
- Enter credentials → Validate → Redirect to Dashboard
- Invalid credentials → Show error message
- Forgot password → Password reset flow

---

### **1.3 Registration Screen** (`/register`)
**Purpose:** New user account creation

**Layout:**
- Full name
- Email
- Password (with strength indicator)
- Confirm password
- Institution/Organization (optional)
- Role selection (Physicist, Dosimetrist, Physician, Researcher)
- Terms & Conditions checkbox
- "Create Account" button

**User Flow:**
- Fill form → Validate → Create account → Email verification → Login

---

### **1.4 Dashboard** (`/dashboard`)
**Purpose:** Main hub after login

**Layout:**
```
┌─────────────────────────────────────────────────┐
│ Logo | Nav Menu | User Profile | Notifications │
├─────────────────────────────────────────────────┤
│                                                   │
│  Welcome Back, [Name]                            │
│                                                   │
│  ┌─────────────┐  ┌─────────────┐  ┌──────────┐ │
│  │ Active      │  │ Pending     │  │ Completed│ │
│  │ Plans: 12   │  │ Reviews: 3  │  │ Plans: 45│ │
│  └─────────────┘  └─────────────┘  └──────────┘ │
│                                                   │
│  Recent Patients                                  │
│  ┌─────────────────────────────────────────────┐ │
│  │ [Patient List with quick actions]            │ │
│  └─────────────────────────────────────────────┘ │
│                                                   │
│  Quick Actions                                    │
│  [New Patient] [New Plan] [Upload CT]            │
│                                                   │
└─────────────────────────────────────────────────┘
```

**Key Features:**
- Statistics cards (active plans, pending reviews, etc.)
- Recent patients list
- Quick action buttons
- Recent activity feed
- Notifications panel

---

## 👥 2. Patient Management

### **2.1 Patient List** (`/patients`)
**Purpose:** Browse and search all patients

**Layout:**
```
┌─────────────────────────────────────────────────┐
│ Patients                    [+ New Patient]      │
├─────────────────────────────────────────────────┤
│ Search: [________]  Filter: [All ▼]  Sort: [▼] │
├─────────────────────────────────────────────────┤
│ ID    │ Name          │ DOB      │ Plans │ Actions│
│ P001  │ John Doe      │ 1990-01  │ 3     │ [View] │
│ P002  │ Jane Smith    │ 1985-05  │ 1     │ [View] │
└─────────────────────────────────────────────────┘
```

**Features:**
- Search by name, ID, or date
- Filter by status, date range
- Sort by various columns
- Pagination
- Bulk actions (export, archive)

**User Actions:**
- Click patient row → Patient Detail
- Click "+ New Patient" → Patient Creation Form
- Click "View" → Patient Detail

---

### **2.2 Patient Detail** (`/patients/:id`)
**Purpose:** View complete patient information

**Layout:**
```
┌─────────────────────────────────────────────────┐
│ ← Back    Patient: John Doe (P001)    [Edit] [⋮]│
├─────────────────────────────────────────────────┤
│                                                   │
│  Patient Information                             │
│  ┌─────────────────────────────────────────────┐ │
│  │ Name: John Doe                              │ │
│  │ ID: P001                                    │ │
│  │ DOB: 1990-01-01                             │ │
│  │ Sex: Male                                   │ │
│  └─────────────────────────────────────────────┘ │
│                                                   │
│  CT Scans                                         │
│  ┌─────────────────────────────────────────────┐ │
│  │ [CT Scan 1] [CT Scan 2] [+ Upload CT]     │ │
│  └─────────────────────────────────────────────┘ │
│                                                   │
│  Treatment Plans                                  │
│  ┌─────────────────────────────────────────────┐ │
│  │ [Plan 1] [Plan 2] [+ New Plan]             │ │
│  └─────────────────────────────────────────────┘ │
│                                                   │
│  Timeline/History                                 │
│  [Activity log]                                   │
│                                                   │
└─────────────────────────────────────────────────┘
```

**Tabs/Sections:**
- Overview (patient info, summary)
- CT Scans (list of scans with thumbnails)
- Treatment Plans (list of plans)
- ROIs (list of regions of interest)
- Results (dose computation results)
- History (activity log)

**User Actions:**
- Click CT scan → CT Viewer
- Click Plan → Plan Detail
- Click "+ New Plan" → Plan Creation
- Click "Edit" → Edit Patient Info

---

### **2.3 Create/Edit Patient** (`/patients/new` or `/patients/:id/edit`)
**Purpose:** Add or modify patient information

**Layout:**
- Form with validation
- Required fields marked
- Real-time validation feedback
- "Save" and "Cancel" buttons

**Fields:**
- Patient ID (auto-generated or manual)
- First Name, Middle Name, Last Name
- Date of Birth
- Sex
- Additional metadata (optional)

---

## 🏥 3. CT Scan Management

### **3.1 CT Scan Upload** (`/patients/:id/ct/upload`)
**Purpose:** Upload or load CT scan data

**Layout:**
```
┌─────────────────────────────────────────────────┐
│ Upload CT Scan for Patient: John Doe (P001)     │
├─────────────────────────────────────────────────┤
│                                                   │
│  Option 1: Upload DICOM Files                    │
│  ┌─────────────────────────────────────────────┐ │
│  │ [Drag & Drop DICOM files here]              │ │
│  │ or [Browse Files]                           │ │
│  └─────────────────────────────────────────────┘ │
│                                                   │
│  Option 2: Load from Dataset                     │
│  ┌─────────────────────────────────────────────┐ │
│  │ Select Dataset: [Dropdown ▼]                │ │
│  │ [Load Dataset]                               │ │
│  └─────────────────────────────────────────────┘ │
│                                                   │
│  Option 3: Import from PACS                      │
│  ┌─────────────────────────────────────────────┐ │
│  │ [Connect to PACS] [Search]                   │ │
│  └─────────────────────────────────────────────┘ │
│                                                   │
│  [Cancel] [Upload]                                │
│                                                   │
└─────────────────────────────────────────────────┘
```

**Features:**
- Drag & drop file upload
- Progress indicator
- DICOM validation
- Preview before upload
- Metadata extraction

**User Flow:**
- Select upload method → Upload/Select → Process → Preview → Confirm → CT Viewer

---

### **3.2 CT Viewer** (`/patients/:id/ct/:ct_id`)
**Purpose:** View and navigate CT scan

**Layout:**
```
┌─────────────────────────────────────────────────┐
│ CT Scan: Brain CT (Dec 25, 2025)                │
├──────────┬──────────────────────────────────────┤
│          │                                      │
│ Slice    │  [CT Image Display]                 │
│ Navigator│                                      │
│          │  [Zoom] [Pan] [Window/Level]        │
│ [1]      │                                      │
│ [2]      │                                      │
│ [3] ←    │                                      │
│ ...      │                                      │
│          │                                      │
│          │  ROI Overlay: [Toggle]              │
│          │  Dose Overlay: [Toggle]              │
│          │                                      │
├──────────┴──────────────────────────────────────┤
│ Axial | Coronal | Sagittal | 3D                 │
│ Window: [400] Level: [50] [Reset]               │
└─────────────────────────────────────────────────┘
```

**Features:**
- Multi-planar reconstruction (Axial, Coronal, Sagittal)
- Slice navigation (scroll wheel, slider)
- Window/Level adjustment
- Zoom and pan
- ROI overlay toggle
- Dose overlay toggle
- Measurement tools
- Export image

---

## 🎯 4. ROI Management

### **4.1 ROI List** (`/patients/:id/rois`)
**Purpose:** View and manage ROIs for a patient/CT scan

**Layout:**
```
┌─────────────────────────────────────────────────┐
│ ROIs for Patient: John Doe                      │
├─────────────────────────────────────────────────┤
│ [+ Create ROI] [Import from RT Structure]       │
├─────────────────────────────────────────────────┤
│ Name      │ Type    │ Color │ Volume │ Actions  │
│ Target    │ Target  │ Red   │ 45.2cc │ [Edit]  │
│ Brainstem │ OAR     │ Blue  │ 12.5cc │ [Edit]  │
│ Eye_L     │ OAR     │ Green │ 5.2cc  │ [Edit]  │
└─────────────────────────────────────────────────┘
```

**Features:**
- List all ROIs with metadata
- Color coding
- Volume calculations
- Import from RT Structure file
- Create new ROI manually
- Edit/Delete ROIs

**User Actions:**
- Click ROI → ROI Editor
- Click "+ Create ROI" → ROI Creation
- Click "Import" → RT Structure Import

---

### **4.2 ROI Editor** (`/patients/:id/rois/:roi_id`)
**Purpose:** Create or edit ROI contours

**Layout:**
- CT Viewer with drawing tools
- Contour editing tools (pencil, eraser, polygon, etc.)
- ROI properties panel (name, type, color)
- Slice-by-slice editing
- 3D preview

**Tools:**
- Draw contour
- Edit points
- Delete contour
- Copy between slices
- Interpolate between slices

---

## 📋 5. Treatment Planning

### **5.1 Plan List** (`/patients/:id/plans`)
**Purpose:** View all treatment plans for a patient

**Layout:**
```
┌─────────────────────────────────────────────────┐
│ Treatment Plans for Patient: John Doe           │
├─────────────────────────────────────────────────┤
│ [+ New Plan] [Compare Plans]                    │
├─────────────────────────────────────────────────┤
│ Plan Name    │ Type  │ Status    │ Date    │ ...│
│ Plan A       │ Proton│ Active    │ Dec 25  │ ...│
│ Plan B v2    │ Proton│ Draft     │ Dec 24  │ ...│
└─────────────────────────────────────────────────┘
```

**Features:**
- List all plans with status
- Plan comparison
- Version history
- Duplicate plan
- Archive/Delete

---

### **5.2 Plan Creation/Editor** (`/patients/:id/plans/new` or `/plans/:id/edit`)
**Purpose:** Create or edit treatment plan

**Layout:**
```
┌─────────────────────────────────────────────────┐
│ Treatment Plan: New Plan                        │
├──────────┬──────────────────────────────────────┤
│          │                                      │
│ Plan     │  [CT Viewer with Beams]              │
│ Config   │                                      │
│          │  Beam 1: Gantry 0°                   │
│ Plan Name│  Beam 2: Gantry 90°                  │
│ [____]   │  Beam 3: Gantry 270°                 │
│          │                                      │
│ Plan Type│  [Add Beam] [Remove Beam]            │
│ [Proton▼]│                                      │
│          │                                      │
│ Target   │  Beam Parameters                     │
│ ROI:     │  ┌────────────────────────────────┐ │
│ [Target▼]│  │ Gantry Angle: [0]°              │ │
│          │  │ Couch Angle:  [0]°              │ │
│          │  │ Spot Spacing: [5.0] mm          │ │
│ Beam     │  │ Layer Spacing:[5.0] mm          │ │
│ Config:  │  │ Target Margin:[5.0] mm          │ │
│          │  └────────────────────────────────┘ │
│ Gantry:  │                                      │
│ [0]°     │  [Save Draft] [Compute Dose]         │
│ Couch:   │                                      │
│ [0]°     │                                      │
│          │                                      │
│ [Add     │                                      │
│  Beam]   │                                      │
│          │                                      │
│ [Save]   │                                      │
│ [Cancel] │                                      │
│          │                                      │
└──────────┴──────────────────────────────────────┘
```

**Features:**
- Plan name and metadata
- Target ROI selection
- Beam configuration (multiple beams)
- Visual beam placement on CT
- Parameter adjustment
- Save as draft
- Compute dose button

**User Flow:**
- Select CT scan → Select target ROI → Add beams → Configure parameters → Save/Compute

---

### **5.3 Dose Computation** (`/plans/:id/compute`)
**Purpose:** Run dose calculation and monitor progress

**Layout:**
```
┌─────────────────────────────────────────────────┐
│ Computing Dose for Plan: Plan A                 │
├─────────────────────────────────────────────────┤
│                                                   │
│  Progress: ████████░░░░░░░░ 45%                  │
│                                                   │
│  Status: Computing dose distribution...          │
│  Estimated time remaining: 3 minutes             │
│                                                   │
│  [Cancel Computation]                            │
│                                                   │
│  Computation Details:                            │
│  • Beam 1/3: Complete                            │
│  • Beam 2/3: In progress...                      │
│  • Beam 3/3: Pending                             │
│                                                   │
└─────────────────────────────────────────────────┘
```

**Features:**
- Real-time progress bar
- Status updates
- Estimated time
- Cancel option
- Background processing (can navigate away)

**User Flow:**
- Start computation → Monitor progress → Auto-redirect to results when complete

---

## 📊 6. Results & Analysis

### **6.1 Plan Results** (`/plans/:id/results`)
**Purpose:** View dose computation results

**Layout:**
```
┌─────────────────────────────────────────────────┐
│ Plan Results: Plan A                             │
├──────────┬──────────────────────────────────────┤
│          │                                      │
│ Results  │  [Dose Distribution Overlay]          │
│ Summary  │                                      │
│          │  CT + Dose + ROI Contours            │
│ D95: 95Gy│                                      │
│ D5:  98Gy│  [Slice Navigator]                  │
│ Mean:96Gy│                                      │
│ Max: 99Gy│                                      │
│          │  [Axial] [Coronal] [Sagittal]        │
│          │                                      │
│ DVH      │  Dose Statistics                    │
│ [Chart]  │  ┌────────────────────────────────┐ │
│          │  │ Target ROI:                     │ │
│          │  │ • D95: 95.0 Gy                  │ │
│          │  │ • D5:  98.2 Gy                  │ │
│          │  │ • Mean: 96.5 Gy                 │ │
│          │  │ • Max:  99.1 Gy                 │ │
│          │  └────────────────────────────────┘ │
│          │                                      │
│          │  [Export Report] [Compare Plans]    │
│          │                                      │
└──────────┴──────────────────────────────────────┘
```

**Features:**
- Dose distribution visualization
- DVH curves for all ROIs
- Dose statistics table
- Slice-by-slice navigation
- Multi-ROI analysis
- Export capabilities
- Plan comparison

**Tabs:**
- Overview (summary statistics)
- Dose Distribution (visualization)
- DVH Analysis (curves and tables)
- Dose Statistics (detailed metrics)
- Reports (export options)

---

### **6.2 DVH Analysis** (`/plans/:id/dvh`)
**Purpose:** Detailed dose-volume histogram analysis

**Layout:**
- Interactive DVH chart (Plotly)
- Multiple ROIs on same chart
- Dose constraint overlays
- Table with dose metrics
- Export options

**Features:**
- Hover for exact values
- Zoom and pan
- Toggle ROIs on/off
- Compare with constraints
- Export as image/PDF

---

### **6.3 Plan Comparison** (`/plans/compare`)
**Purpose:** Compare multiple treatment plans

**Layout:**
- Side-by-side plan comparison
- Overlay dose distributions
- DVH comparison chart
- Statistics comparison table
- Visual difference map

**Features:**
- Select 2-4 plans to compare
- Synchronized slice navigation
- Difference visualization
- Export comparison report

---

## ⚙️ 7. Settings & Administration

### **7.1 User Settings** (`/settings`)
**Purpose:** User preferences and account management

**Sections:**
- Profile (name, email, password)
- Preferences (theme, units, default views)
- Notifications
- API Keys (if applicable)

---

### **7.2 System Administration** (`/admin`) - Admin Only
**Purpose:** System-wide configuration

**Sections:**
- User Management
- System Settings
- Dataset Management
- Audit Logs
- System Health

---

## 🎨 8. Navigation Structure

### **Main Navigation Bar** (Always Visible)
```
┌─────────────────────────────────────────────────┐
│ [Logo] [Dashboard] [Patients] [Plans] [Results] │
│                    [Settings] [Help] [Profile ▼] │
└─────────────────────────────────────────────────┘
```

### **Breadcrumbs** (Context Navigation)
```
Dashboard > Patients > John Doe > Plans > Plan A > Results
```

### **Sidebar** (When in detail views)
- Quick actions
- Related items
- Recent activity
- Shortcuts

---

## 📱 9. Responsive Design

### **Desktop (>1024px)**
- Full multi-panel layout
- Side-by-side views
- Rich interactions

### **Tablet (768px - 1024px)**
- Collapsible sidebars
- Stacked panels
- Touch-friendly controls

### **Mobile (<768px)**
- Single column layout
- Bottom navigation
- Simplified views
- Essential features only

---

## 🔄 10. User Workflows

### **Workflow 1: New Treatment Plan**
```
1. Dashboard
   ↓
2. Patients List
   ↓
3. Select/Create Patient
   ↓
4. Patient Detail
   ↓
5. Upload CT Scan
   ↓
6. CT Viewer (verify scan)
   ↓
7. Import/Define ROIs
   ↓
8. Create Treatment Plan
   ↓
9. Configure Beams
   ↓
10. Compute Dose
   ↓
11. Review Results
   ↓
12. Adjust Plan (if needed)
   ↓
13. Approve/Export Plan
```

### **Workflow 2: Review Existing Plan**
```
1. Dashboard
   ↓
2. Recent Plans / Search
   ↓
3. Plan Detail
   ↓
4. View Results
   ↓
5. DVH Analysis
   ↓
6. Compare with other plans
   ↓
7. Make adjustments
   ↓
8. Re-compute
```

### **Workflow 3: Batch Processing**
```
1. Patients List
   ↓
2. Select multiple patients
   ↓
3. Bulk actions menu
   ↓
4. Choose action (export, archive, etc.)
   ↓
5. Confirm and process
```

---

## 🎯 11. Key UI/UX Principles

### **Medical Software Best Practices:**
1. **Clear Hierarchy** - Most important info first
2. **Consistent Navigation** - Always know where you are
3. **Visual Feedback** - Loading states, progress indicators
4. **Error Prevention** - Validation, confirmations
5. **Accessibility** - WCAG 2.1 AA compliance
6. **Performance** - Fast load times, smooth interactions
7. **Data Safety** - Auto-save, undo/redo
8. **Audit Trail** - Track all changes

### **Design System:**
- **Color Scheme:**
  - Primary: Medical blue (#0066CC)
  - Success: Green (#00AA00)
  - Warning: Orange (#FF8800)
  - Error: Red (#CC0000)
  - Neutral: Grays

- **Typography:**
  - Headings: Sans-serif (clear, readable)
  - Body: Sans-serif
  - Code/Data: Monospace

- **Components:**
  - Cards for grouping
  - Modals for actions
  - Tooltips for help
  - Toast notifications
  - Progress indicators

---

## 📋 12. Screen Priority List

### **Phase 1: Core Workflow** (MVP)
1. ✅ Login/Dashboard
2. ✅ Patient List
3. ✅ Patient Detail
4. ✅ CT Upload/Viewer
5. ✅ Plan Creation
6. ✅ Dose Computation
7. ✅ Results View

### **Phase 2: Enhanced Features**
8. ROI Editor
9. Plan Comparison
10. Advanced DVH Analysis
11. Export/Reporting
12. User Settings

### **Phase 3: Advanced Features**
13. Plan Templates
14. Automation Tools
15. Collaboration Features
16. Mobile App
17. PACS Integration

---

## 🚀 Implementation Recommendations

### **Frontend Framework:**
- **React** or **Vue.js** for component-based architecture
- **React Router** or **Vue Router** for navigation
- **Material-UI** or **Vuetify** for components
- **Plotly.js** for visualizations (already in use)

### **State Management:**
- **Redux** (React) or **Vuex** (Vue) for global state
- **React Query** or **Vue Query** for API state

### **UI Library:**
- **Material Design** or **Ant Design** for medical software
- Custom components for medical imaging viewers

### **Key Pages to Build:**
1. `/dashboard` - Main hub
2. `/patients` - Patient list
3. `/patients/:id` - Patient detail
4. `/patients/:id/ct/:ct_id` - CT viewer
5. `/patients/:id/plans/new` - Plan creation
6. `/plans/:id/results` - Results view
7. `/plans/:id/dvh` - DVH analysis

---

## ✅ Success Metrics

A production-ready application should have:
- ✅ < 2 second page load times
- ✅ Intuitive navigation (users find features in < 3 clicks)
- ✅ Responsive design (works on all devices)
- ✅ Accessibility compliance (WCAG 2.1 AA)
- ✅ Error handling (graceful failures)
- ✅ Data persistence (auto-save, no data loss)
- ✅ Security (authentication, authorization, encryption)
- ✅ Performance (smooth interactions, fast computations)
- ✅ User feedback (loading states, progress indicators)

---

This screen flow provides a comprehensive roadmap for building a production-level treatment planning system interface!

