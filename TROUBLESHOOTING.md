# Troubleshooting Guide - "Denied Out" Issues

## Common Issues and Solutions

### 1. CORS (Cross-Origin Resource Sharing) Errors
**Symptoms:** Browser console shows CORS errors, API calls fail from frontend

**Solution:** ✅ Fixed - CORS is now enabled in `app.py`

**Test:**
```bash
curl -H "Origin: http://localhost:3000" \
     -H "Access-Control-Request-Method: POST" \
     -H "Access-Control-Request-Headers: Content-Type" \
     -X OPTIONS http://127.0.0.1:5000/ct
```

### 2. Database Permission Errors
**Symptoms:** "Permission denied" when accessing database

**Solution:**
```bash
cd backend
chmod 644 radiate_tps.db
chmod 755 .
```

### 3. File Permission Errors
**Symptoms:** Can't write to uploads/ or Output/ folders

**Solution:**
```bash
cd backend
chmod -R u+w uploads/ Output/
```

### 4. Port Already in Use
**Symptoms:** "Address already in use" error

**Solution:**
```bash
# Kill existing Flask processes
pkill -f "python.*app.py"
# Or kill process on port 5000
kill -9 $(lsof -ti:5000)
```

### 5. Database Locked Errors
**Symptoms:** "database is locked" errors

**Solution:**
- Make sure only one Flask instance is running
- Check for uncommitted transactions
- Restart the Flask server

### 6. Missing Dependencies
**Symptoms:** Import errors, module not found

**Solution:**
```bash
cd backend
source venv/bin/activate
pip install flask flask-cors flask-sqlalchemy sqlalchemy
```

### 7. Browser Console Errors
**Check browser console (F12) for:**
- CORS errors
- 404 Not Found
- 500 Internal Server Error
- Network errors

### 8. Testing API Endpoints

**Test if server is running:**
```bash
curl http://127.0.0.1:5000/
```

**Test CT endpoint:**
```bash
curl http://127.0.0.1:5000/ct
```

**Test with CORS headers:**
```bash
curl -X POST http://127.0.0.1:5000/ct \
  -H "Content-Type: application/json" \
  -H "Origin: http://localhost:3000" \
  -d '{"patient_id":"test"}'
```

## Quick Diagnostic Commands

```bash
# Check if Flask is running
ps aux | grep "python.*app.py"

# Check port 5000
lsof -ti:5000

# Test database access
cd backend
source venv/bin/activate
python -c "from app import app; app.app_context().push(); from application.models import db; db.create_all(); print('OK')"

# Check file permissions
ls -la backend/radiate_tps.db
ls -la backend/uploads/
ls -la backend/Output/
```

## Common Error Messages

### "Patient with ID X not found"
- **Cause:** Patient doesn't exist in database
- **Solution:** Create patient first using `/patients/patients/create`

### "OpenTPS required to load from dataset"
- **Cause:** OpenTPS not installed
- **Solution:** Install OpenTPS or use endpoints that don't require it

### "database is locked"
- **Cause:** Multiple processes accessing database
- **Solution:** Stop all Flask instances, restart

### "Permission denied"
- **Cause:** File permission issues
- **Solution:** Run `chmod -R u+w backend/`

## Getting Help

If you're still getting "denied out", please provide:
1. Exact error message
2. Where it appears (browser console, terminal, etc.)
3. What action triggers it
4. Full stack trace if available

