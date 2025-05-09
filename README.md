# radiateTPS
Browser based cancer and radiation treatment planning system based on OpenTPS source code.

# Setup Instructions

1. Clone the project repository and the OpenTPS repository (I put both of mine towards the root of my C drive)
    git clone https://github.com/adriankUSA/radiateTPS.git
    git clone https://gitlab.com/openmcsquare/opentps.git 

2. Create a Virtual Environment (I put min in /backend): 
    python -m venv radiate-venv

3. Activate the environment:
    Windows CMD/VS Code Terminal: backend\radiate-venv\Scripts\activate
    or C:\radiateTPS\backend\radiate-venv\Scripts\activate
    or Powershell:
    & "C:\radiateTPS\backend\radiate-venv\Scripts\Activate.ps1"
    Mac/Linux: source backend\venv/bin/activate

    If you see both (base) and your (venv) active, you should be able to use this command to get rid of (base):
    conda deactivate

# Dependencies 

4. Install dependencies: 
    pip install -r requirements.txt

5. More dependencies (pydicom, scipy, SimpleITK, matplotlib, numpy, cuda, psutil)
    pip install pydicom scipy SimpleITK matplotlib numpy
    pip install cupy-cuda12x psutil

    Program/terminal will let you know if there are still any missing dependencies when you try to run the tutorial

6. Whenever a new package is installed, run:
    pip freeze > backend/requirements.txt

# Pathing

7. Pathing (File directory and pathing is a big issue, may need more/different adjustments)
    Adjust the .env file to manually specify additional paths if needed:
    PYTHONPATH=C:/opentps/opentps_core

    In /backend/routes/plotly_tutorial.py or /backend/routes/tutorial1.py, you can see this line
    sys.path.append(r"C:\opentps\opentps_core")
    Adjust as needed

# Running

8. To run the application, after activating your virtual environment, in your /backend directory, run:
    python app.py

    Navigate to http://127.0.0.1:5000/
    
    Click the tutorial page.

    Wait a couple of minutes, (the computations should be running if no errors), and then eventually the charts will load.

    If errors, likely either due to dependency issues or file pathing/connecting to OpenTPS source code.

    If successful, you should also be able to select from one sample dataset and view the ROI names.

# Next Steps Going Forward

    Computations are processed on the backedn but we still need to remove the image generation on the backend (should be simple).

    Need to look at the OpenTPS GUI code and try to replicate and simulate that. 

