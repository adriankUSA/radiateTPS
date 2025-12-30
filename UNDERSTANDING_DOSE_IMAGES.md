# Understanding SimpleDose.png - Axes Explained

## 📊 The Image Has TWO Plots Side-by-Side

---

## 🖼️ **LEFT PLOT: 2D Dose Distribution Map**

This shows **WHERE** the radiation dose was delivered in a 2D slice (like looking at a slice of bread).

### **X-Axis (Horizontal, 0 to 140)**
- **What it is:** Left-to-right position in the patient/phantom
- **Simple explanation:** How far left or right you are looking
- **Units:** Pixels or millimeters (depends on CT scan spacing)
- **Think of it like:** Moving left or right across the image

### **Y-Axis (Vertical, 0 to 140)**
- **What it is:** Top-to-bottom position in the patient/phantom
- **Simple explanation:** How far up or down you are looking
- **Units:** Pixels or millimeters (depends on CT scan spacing)
- **Think of it like:** Moving up or down in the image

### **What the Colors Mean:**
- **Blue/Purple (low values):** Low or no dose
- **Green/Yellow (middle values):** Medium dose
- **Orange/Red (high values):** High dose
- **The color bar (0 to 16):** Shows dose intensity (likely in Gray units or percentage)

### **What You're Looking At:**
- The **dark blue area** = Air or low-density material (little/no dose)
- The **lighter blue area** = Water or tissue (some dose)
- The **square outline** = Target volume (tumor/ROI)
- The **bright yellow/orange** inside the square = High dose to the target
- The **colored gradient** around it = How dose spreads from the target

**In Simple Terms:** This is like a heat map showing where radiation was delivered. Hot colors = more radiation, cool colors = less radiation.

---

## 📈 **RIGHT PLOT: Dose-Volume Histogram (DVH)**

This shows **HOW MUCH** of the target volume received **HOW MUCH** dose.

### **X-Axis: "Dose (Gy)" (0 to 100)**
- **What it is:** Amount of radiation dose
- **Simple explanation:** How much radiation was given
- **Units:** Gray (Gy) - a unit of radiation dose
- **Think of it like:** Moving from low dose (left) to high dose (right)

### **Y-Axis: "Volume (%)" (0 to 100)**
- **What it is:** Percentage of the target volume
- **Simple explanation:** How much of the tumor/ROI received that dose or more
- **Units:** Percentage (%)
- **Think of it like:** 100% = the entire target, 50% = half the target, 0% = none of the target

### **What the Blue Line Shows:**
The curve answers: **"What percentage of the target received at least X amount of dose?"**

**Example Reading:**
- At **10 Gy** on X-axis → **100%** on Y-axis
  - Meaning: **100% of the target received at least 10 Gy**
  
- At **15 Gy** on X-axis → **~50%** on Y-axis
  - Meaning: **50% of the target received at least 15 Gy**
  
- At **20 Gy** on X-axis → **0%** on Y-axis
  - Meaning: **0% of the target received 20 Gy or more**
  - This is the **maximum dose** to the target

### **What This Tells You:**
- **Steep drop = Uniform dose** (most of target gets similar dose)
- **Gradual drop = Non-uniform dose** (dose varies across target)
- **D95** = Dose that 95% of the target received (important metric!)
- **D5** = Dose that 5% of the target received (hot spots)

**In Simple Terms:** This is like a report card showing how evenly the radiation was distributed. A steep, smooth curve = good, uniform coverage.

---

## 🎯 **Putting It Together**

### **Left Plot Answers:**
- **"Where did the radiation go?"**
- Shows the spatial distribution
- Like a map of radiation delivery

### **Right Plot Answers:**
- **"How well was the target covered?"**
- Shows the dose statistics
- Like a quality report

### **Together They Show:**
1. **Spatial distribution** (left) - WHERE the dose is
2. **Dose statistics** (right) - HOW MUCH dose was delivered

---

## 📏 **Real-World Analogy**

**Left Plot (Dose Map):**
- Like a **weather map** showing where it rained
- Colors show intensity (light rain = blue, heavy rain = red)
- X and Y are like latitude and longitude (position)

**Right Plot (DVH):**
- Like a **grade distribution** in a class
- X-axis = Grade (0-100)
- Y-axis = How many students got that grade or higher
- Shows if grades are uniform (steep curve) or spread out (gradual curve)

---

## 🔍 **Key Metrics from the DVH**

From the code, these important values are calculated:

- **D95** = Dose that 95% of the target received
  - **Why important:** Ensures most of the target gets enough dose
  
- **D5** = Dose that 5% of the target received  
  - **Why important:** Shows hot spots (areas getting too much dose)
  
- **D5 - D95** = Dose uniformity
  - **Why important:** Smaller difference = more uniform dose (better!)

---

## 💡 **Quick Reference**

| Plot | X-Axis | Y-Axis | What It Shows |
|------|--------|--------|--------------|
| **Left (Dose Map)** | Position (left-right) | Position (up-down) | WHERE dose was delivered |
| **Right (DVH)** | Dose (Gy) | Volume (%) | HOW MUCH dose to HOW MUCH volume |

---

## 🎓 **For Your Project**

When you display these images in your web application:
- **Left plot:** Use for interactive CT viewer with dose overlay
- **Right plot:** Use for dose analysis and plan evaluation
- **Both together:** Give complete picture of treatment quality

The axes help users understand:
- **Spatial context** (where in the body)
- **Dose coverage** (how well the target was treated)
- **Plan quality** (uniformity, hot spots, cold spots)

