# radiateTPS
Browser based cancer and radiation treatment planning system based on OpenTPS source code.

# Setup Instructions
1. Clone the repo 
    git clone https://github.com/adriankUSA/radiateTPS.git

2. Create a Virtual Environment: 
    python -m venv radiate-venv

3. Activate the environment:
Windows CMD/VS Code Terminal: backend\radiate-venv\Scripts\activate
Mac/Linux: source backend\venv/bin/activate

4. Install dependencies: 
    pip install -r requirements.txt

5. Whenever a new package is installed, run: 
    pip freeze >> backend/requirements.txt or
    This one overwrites it pip freeze > backend/requirements.txt

