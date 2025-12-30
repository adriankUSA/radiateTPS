# Quick Test - Next Steps

## ✅ You're Getting JSON Output - That's Great!

This means:
- ✅ Flask server is running
- ✅ API endpoints are working
- ✅ Database is connected
- ✅ Routes are responding correctly

## 🎯 What to Test Next

### 1. Create a Patient (POST request)

```bash
curl -X POST http://127.0.0.1:5000/patients/create \
  -H "Content-Type: application/json" \
  -d '{"name":"Test Patient","id":"TEST001","birthDate":"1990-01-01","sex":"M"}'
```

**Expected output:**
```json
{
  "message": "Patient Test Patient saved.",
  "success": true
}
```

### 2. Load the Patient You Just Created

```bash
curl http://127.0.0.1:5000/patients/load
```

**Expected output:**
```json
[
  {
    "birthDate": "1990-01-01",
    "id": "TEST001",
    "name": "Test Patient",
    "sex": "M"
  }
]
```

### 3. Test Dataset Loading

```bash
curl http://127.0.0.1:5000/load_data/datasets
```

**Expected output:**
```json
{
  "datasets": [
    "ProKnows_2018_TROG_Plan_Study_SRS_Brain"
  ]
}
```

### 4. Test Web Interface

Open in your browser:
- `http://127.0.0.1:5000/` - Homepage
- `http://127.0.0.1:5000/tutorial.html` - Tutorial page with forms

## 📊 Understanding JSON Output

If you see JSON like:
```json
{
  "success": true,
  "data": [...]
}
```
✅ **That's success!**

If you see:
```json
{
  "error": "Something went wrong"
}
```
⚠️ **That's an error message** - but the API is still working, just telling you what's wrong.

If you see HTML:
```html
<!DOCTYPE html>...
```
❌ **That's an error page** - something went wrong with the route.

## 🚀 Full Workflow Test

Try this complete workflow:

```bash
# 1. Create a patient
curl -X POST http://127.0.0.1:5000/patients/create \
  -H "Content-Type: application/json" \
  -d '{"name":"John Doe","id":"P001","birthDate":"1990-01-01","sex":"M"}'

# 2. Verify patient was created
curl http://127.0.0.1:5000/patients/load

# 3. List available datasets
curl http://127.0.0.1:5000/load_data/datasets

# 4. Upload CT scan (replace P001 with your patient ID)
curl -X POST http://127.0.0.1:5000/ct \
  -H "Content-Type: application/json" \
  -d '{"patient_id":"P001","dataset_name":"ProKnows_2018_TROG_Plan_Study_SRS_Brain","name":"Brain CT"}'

# 5. Get CT scans for patient
curl "http://127.0.0.1:5000/ct?patient_id=P001"
```

## 💡 Pro Tips

1. **Pretty print JSON:**
   Add `| python3 -m json.tool` to any curl command:
   ```bash
   curl http://127.0.0.1:5000/patients/load | python3 -m json.tool
   ```

2. **Check server logs:**
   Look at the terminal where Flask is running - it shows all requests

3. **Test in browser:**
   For GET requests, just open the URL in your browser

## ✅ Success Indicators

You know everything is working when:
- ✅ JSON responses (not HTML error pages)
- ✅ `"success": true` in responses
- ✅ Data persists (create something, restart server, it's still there)
- ✅ No errors in Flask terminal
- ✅ Web interface loads and works

## 🎉 You're Ready!

Since you're getting JSON output, you're all set! Try the workflow above to test the full system.

