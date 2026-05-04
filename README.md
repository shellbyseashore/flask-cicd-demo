# flask-cicd-demo
A Flask web application with a full CI/CD pipeline using GitHub Actions, Docker, and Azure.

Project Structure
flask-cicd-demo/
├── .github/
│   └── workflows/
│       └── ci.yml        # GitHub Actions CI/CD pipeline
├── app/
│   └── main.py           # Flask application
├── tests/
│   └── test_main.py      # Pytest test suite
├── Dockerfile            # Docker image definition
├── requirements.txt      # Python dependencies
└── README.md

Features

Flask web app with a dark-themed dashboard UI
Live server clock
Health check endpoint
REST API endpoint
Fully containerized with Docker
Automated CI/CD pipeline with GitHub Actions
Deployed on Azure VM


API Endpoints
MethodEndpointDescriptionGET/Returns the HTML dashboardGET/apiReturns {"message": "Hello from my app!"}GET/healthReturns {"status": "ok"}

CI/CD Pipeline
Every push to main triggers 3 automated jobs in order:
test → docker → deploy
JobWhat it doestestRuns pytest — must pass before anything elsedockerBuilds and pushes Docker image to Docker HubdeploySSHs into Azure VM and runs the latest container

Running Locally
1. Clone the repo
bashgit clone https://github.com/shellbyseashore0/flask-cicd-demo.git
cd flask-cicd-demo
2. Install dependencies
bashpip install -r requirements.txt
3. Run the app
bashpython app/main.py
Visit http://localhost:5000
4. Run tests
bashpython -m pytest tests/test_main.py -v

Running with Docker
bashdocker build -t flask-cicd-demo .
docker run -p 5000:5000 flask-cicd-demo

GitHub Secrets Required
SecretDescriptionDOCKER_USERNAMEDocker Hub usernameDOCKER_PASSWORDDocker Hub access tokenSERVER_HOSTAzure VM public IPSERVER_USERAzure VM usernameSERVER_SSH_KEYPrivate SSH key for Azure VM

Tech Stack

Backend — Python, Flask
Testing — Pytest
Containerization — Docker
CI/CD — GitHub Actions
Cloud — Microsoft Azure (Ubuntu VM)
