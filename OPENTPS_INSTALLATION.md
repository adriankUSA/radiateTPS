# OpenTPS Installation Guide

## ✅ Good News!

OpenTPS **IS available on PyPI**! You can install it with pip, but there are some version requirements.

## ⚠️ Python Version Requirements

- **OpenTPS 2.0.2** (latest): Requires Python **3.11** (not 3.12 or 3.13)
- **OpenTPS 1.x**: Requires Python **3.9** (not 3.10+)

**Your current Python version:** 3.13.1 (too new!)

## Installation Options

## Installation Methods

### Method 1: Clone from GitLab (Recommended - Based on README)

This is the method described in your project's README:

```bash
# 1. Clone OpenTPS repository
cd ~  # or wherever you want to install it
git clone https://gitlab.com/openmcsquare/opentps.git

# 2. Navigate to the cloned directory
cd opentps

# 3. Set up Python path
# The core module is in opentps/opentps_core
export PYTHONPATH=$PYTHONPATH:$(pwd)/opentps_core

# 4. Install OpenTPS dependencies
# Check if there's a requirements.txt or setup.py
pip install -r requirements.txt  # if it exists
# OR
pip install .  # if there's a setup.py
```

**For Mac (your system):**
```bash
# Clone to your home directory
cd ~
git clone https://gitlab.com/openmcsquare/opentps.git

# Add to Python path (add this to your ~/.zshrc or ~/.bash_profile)
export PYTHONPATH=$PYTHONPATH:~/opentps/opentps_core

# Or set it in your Flask app's environment
```

### Method 2: Install via pip (Requires Python 3.11)

**⚠️ This won't work with Python 3.13!** You need Python 3.11.

If you have Python 3.11:

```bash
# Make sure you're using Python 3.11
python3.11 --version

# Create a new virtual environment with Python 3.11
python3.11 -m venv venv311
source venv311/bin/activate  # or venv311\Scripts\activate on Windows

# Install OpenTPS
pip install opentps
```

**Latest version:** OpenTPS 2.0.2 (requires Python 3.11)

### Method 3: Install as editable package

If OpenTPS has a `setup.py`:

```bash
cd ~/opentps  # after cloning
pip install -e .
```

## Configuration for RadiateTPS

After installing OpenTPS, you need to update the path in your RadiateTPS code:

### Option 1: Update the path in code

The code already checks multiple paths:
- `C:\opentps\opentps_core` (Windows)
- `/opt/opentps/opentps_core` (Linux)
- `~/opentps/opentps_core` (Mac - your system)

So if you clone to `~/opentps`, it should work automatically!

### Option 2: Set environment variable

```bash
# Add to ~/.zshrc (since you're on Mac with zsh)
export PYTHONPATH=$PYTHONPATH:~/opentps/opentps_core

# Then reload
source ~/.zshrc
```

### Option 3: Update the path in application code

Edit `backend/application/routes/main.py` and add your path:

```python
opentps_paths = [
    r"C:\opentps\opentps_core",  # Windows default
    "/opt/opentps/opentps_core",  # Linux/Mac alternative
    os.path.expanduser("~/opentps/opentps_core"),  # User home directory
    "/Users/vidyuthashok/opentps/opentps_core",  # Your specific path
]
```

## Verification

After installation, test if OpenTPS is accessible:

```bash
cd backend
source venv/bin/activate
python -c "
import sys
sys.path.append('~/opentps/opentps_core')
try:
    from opentps.core.data import Patient
    print('✅ OpenTPS imported successfully!')
except ImportError as e:
    print(f'❌ OpenTPS not found: {e}')
"
```

## Dependencies

OpenTPS may require additional dependencies. Common ones include:
- NumPy
- SciPy
- Matplotlib
- pydicom
- SimpleITK
- CUDA (for GPU acceleration - optional)

## Troubleshooting

### "Module not found: opentps"
- Check that the path is correct
- Verify the directory structure: `opentps/opentps_core/` should exist
- Make sure `opentps_core` contains Python modules

### "Permission denied"
- Make sure you have read access to the OpenTPS directory
- Check file permissions: `chmod -R u+r ~/opentps`

### Path issues
- Use absolute paths instead of relative paths
- Check that `sys.path.append()` is called before importing

## Next Steps

1. Clone OpenTPS: `git clone https://gitlab.com/openmcsquare/opentps.git ~/opentps`
2. Verify structure: `ls ~/opentps/opentps_core`
3. Restart your Flask app
4. Check logs for "✅ OpenTPS loaded successfully"

## Resources

- OpenTPS GitLab: https://gitlab.com/openmcsquare/opentps
- OpenTPS Website: https://opentps.org
- Documentation: Check the cloned repository for README files

