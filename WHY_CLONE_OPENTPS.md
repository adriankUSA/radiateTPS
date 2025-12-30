# Why Clone OpenTPS? (FAQ)

## 🤔 Your Concerns

**Q: Will cloning OpenTPS affect my GitHub repository?**  
**A: No!** OpenTPS is a completely separate project. Cloning it is like downloading a library - it doesn't touch your radiateTPS repository at all.

**Q: Will it duplicate anything?**  
**A: No!** OpenTPS is a dependency, not part of your project. Think of it like:
- Installing a Python package (but from source instead of PyPI)
- Like `node_modules` in Node.js projects
- Like downloading a library to use in your code

## 📦 What is OpenTPS?

OpenTPS is a **separate, independent project** created by researchers. Your radiateTPS project **uses** OpenTPS as a dependency to do dose calculations.

- **OpenTPS repository**: https://gitlab.com/openmcsquare/opentps
- **Your repository**: https://github.com/vidyuthdev/radiateOPENTPS_working

They're completely separate!

## 🔍 What Happens When You Clone?

When you run:
```bash
cd ~
git clone https://gitlab.com/openmcsquare/opentps.git
```

This creates a **new folder** in your home directory:
```
~/opentps/          ← New folder (separate from your project)
  └── opentps_core/ ← The Python modules your app needs
```

Your radiateTPS project stays exactly where it is:
```
~/Documents/radiateTPS/radiateTPS_working/  ← Your project (unchanged)
  └── backend/
      └── application/
          └── routes/
              └── main.py  ← This imports from OpenTPS
```

## 🎯 How Your App Uses It

Your code imports OpenTPS like this:
```python
from opentps.core.data import Patient
from opentps.core.data.images import CTImage
```

Python looks for `opentps` in:
1. Your virtual environment (if installed via pip - but that doesn't work with Python 3.13)
2. Paths you specify (like `~/opentps/opentps_core`)

## ✅ What Gets Cloned?

- **OpenTPS source code** - The treatment planning system code
- **NOT your radiateTPS code** - Your project stays separate
- **NOT your GitHub repo** - Completely independent

## 📁 Where Should You Clone It?

You can clone it anywhere! Common locations:

1. **Home directory** (recommended):
   ```bash
   cd ~
   git clone https://gitlab.com/openmcsquare/opentps.git
   ```
   Creates: `~/opentps/`

2. **Separate projects folder**:
   ```bash
   cd ~/Documents
   git clone https://gitlab.com/openmcsquare/opentps.git
   ```
   Creates: `~/Documents/opentps/`

3. **Next to your project** (also fine):
   ```bash
   cd ~/Documents/radiateTPS
   git clone https://gitlab.com/openmcsquare/opentps.git
   ```
   Creates: `~/Documents/radiateTPS/opentps/` (separate from radiateTPS_working)

## 🚫 What WON'T Happen

- ❌ OpenTPS won't be added to your GitHub repository
- ❌ Your radiateTPS code won't be duplicated
- ❌ Nothing will be pushed to your GitHub
- ❌ Your repository structure won't change
- ❌ No files will be modified in your project

## 🔒 Your Repository is Safe

Your `.gitignore` file (if you have one) doesn't need to include OpenTPS because:
- OpenTPS is cloned **outside** your project folder
- It's a separate Git repository
- Your radiateTPS project just **references** it, doesn't include it

## 💡 Analogy

Think of it like this:
- **Your radiateTPS project** = Your car
- **OpenTPS** = The engine parts you buy from a supplier
- **Cloning OpenTPS** = Buying the engine parts and storing them in your garage
- Your car (project) uses the engine (OpenTPS) but the engine stays in the garage (separate folder)

## ✅ Summary

**Cloning OpenTPS:**
- ✅ Safe - won't affect your repository
- ✅ Separate - it's a different project
- ✅ Temporary - you can delete it anytime
- ✅ Standard practice - many projects depend on external libraries

**Your radiateTPS project:**
- ✅ Stays exactly the same
- ✅ Still works without OpenTPS (in limited mode)
- ✅ Just needs to know where OpenTPS is located

## 🎯 Next Steps

1. Clone OpenTPS: `cd ~ && git clone https://gitlab.com/openmcsquare/opentps.git`
2. Your app will automatically find it at `~/opentps/opentps_core`
3. Restart your Flask app
4. Done! No changes to your repository needed.

