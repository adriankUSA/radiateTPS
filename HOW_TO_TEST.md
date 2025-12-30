# How to Test the API - Quick Guide

## 🖥️ Where to Run curl Commands

### Option 1: Terminal (Mac/Linux)

1. **Open Terminal:**
   - Press `Cmd + Space` (Spotlight)
   - Type "Terminal"
   - Press Enter

2. **Navigate to your project** (optional, but helpful):
   ```bash
   cd ~/Documents/radiateTPS/radiateTPS_working
   ```

3. **Make sure Flask is running:**
   ```bash
   # In a separate terminal window, or background:
   cd ~/Documents/radiateTPS/radiateTPS_working
   ./run.sh
   ```

4. **Paste curl commands in Terminal:**
   - Copy the curl command from the checklist
   - Paste into Terminal
   - Press Enter
   - See the response

### Option 2: VS Code Integrated Terminal

1. **Open VS Code** in your project folder
2. **Open Terminal:**
   - Press `` Ctrl + ` `` (backtick) OR
   - Go to: Terminal → New Terminal
3. **Paste curl commands** directly there

### Option 3: Browser (Easier for GET requests)

For **GET requests**, you can just use your browser:
- `http://127.0.0.1:5000/patients/load`
- `http://127.0.0.1:5000/load_data/datasets`
- `http://127.0.0.1:5000/ct?patient_id=P001`

### Option 4: Postman (GUI tool)

1. Download Postman: https://www.postman.com/downloads/
2. Create a new request
3. Set method (GET/POST)
4. Enter URL: `http://127.0.0.1:5000/patients/create`
5. Add JSON body for POST requests
6. Click Send

---

## 📝 Example: Step-by-Step

### Test 1: Create a Patient

1. **Open Terminal** (Cmd + Space → "Terminal")

2. **Copy this command:**
   ```bash
   curl -X POST http://127.0.0.1:5000/patients/create \
     -H "Content-Type: application/json" \
     -d '{"name":"John Doe","id":"P001","birthDate":"1990-01-01","sex":"M"}'
   ```

3. **Paste into Terminal** and press Enter

4. **You should see:**
   ```json
   {
     "message": "Patient John Doe saved.",
     "success": true
   }
   ```

### Test 2: Load Patients

1. **In Terminal, type:**
   ```bash
   curl http://127.0.0.1:5000/patients/load
   ```

2. **Press Enter**

3. **You should see:**
   ```json
   [
     {
       "birthDate": "1990-01-01",
       "id": "P001",
       "name": "John Doe",
       "sex": "M"
     }
   ]
   ```

---

## 🎯 Quick Test Commands

Copy and paste these one at a time:

```bash
# 1. Check if server is running
curl http://127.0.0.1:5000/

# 2. List datasets
curl http://127.0.0.1:5000/load_data/datasets

# 3. Create a patient
curl -X POST http://127.0.0.1:5000/patients/create \
  -H "Content-Type: application/json" \
  -d '{"name":"Test Patient","id":"TEST001","birthDate":"1990-01-01","sex":"M"}'

# 4. Load patients
curl http://127.0.0.1:5000/patients/load
```

---

## 💡 Tips

1. **Multi-line commands:** The `\` at the end of lines means "continue on next line"
   - You can paste the whole thing at once
   - Or type it all on one line (remove the `\`)

2. **Pretty JSON output:** Add `| python3 -m json.tool` to format:
   ```bash
   curl http://127.0.0.1:5000/patients/load | python3 -m json.tool
   ```

3. **Check if server is running:**
   ```bash
   # Should return HTML (the homepage)
   curl http://127.0.0.1:5000/
   ```

4. **If you get "Connection refused":**
   - Flask server isn't running
   - Start it with: `./run.sh`

---

## 🌐 Testing in Browser

For **GET requests**, just open in browser:

- Homepage: `http://127.0.0.1:5000/`
- Tutorial: `http://127.0.0.1:5000/tutorial.html`
- List datasets: `http://127.0.0.1:5000/load_data/datasets`
- Load patients: `http://127.0.0.1:5000/patients/load`

**Note:** POST requests need curl or Postman (browser can't send POST easily)

---

## 🐛 Troubleshooting

### "command not found: curl"
- curl should be built-in on Mac
- If missing, install: `brew install curl`

### "Connection refused"
- Flask server isn't running
- Start it: `cd backend && source venv/bin/activate && python app.py`

### "No response"
- Check Flask terminal for errors
- Make sure you're using the correct URL
- Check that Flask is running on port 5000

---

## ✅ Quick Verification

Run this to verify everything works:

```bash
# Test 1: Server is running
curl http://127.0.0.1:5000/ | head -5

# Test 2: API endpoint works
curl http://127.0.0.1:5000/patients/load

# Test 3: Create something
curl -X POST http://127.0.0.1:5000/patients/create \
  -H "Content-Type: application/json" \
  -d '{"name":"Quick Test","id":"QT001","birthDate":"2000-01-01","sex":"M"}'
```

If all three work, you're good to go! 🎉

