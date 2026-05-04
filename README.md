# Flask CI/CD Demo

A Flask web application with a full CI/CD pipeline using GitHub Actions, Docker, and Azure.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Flask](https://img.shields.io/badge/Flask-latest-lightgrey)
![Docker](https://img.shields.io/badge/Docker-containerized-2496ED)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-black)
![Azure](https://img.shields.io/badge/Deployed-Azure%20VM-0078D4)

## Live Demo

http://40.82.157.202:5000

---

## Project Structure

```
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
```

---

## Features

- Flask web app with a dark-themed dashboard UI
- Live server clock
- Health check endpoint
- REST API endpoint
- Fully containerized with Docker
- Automated CI/CD pipeline with GitHub Actions
- Deployed on Azure VM

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Returns the HTML dashboard |
| GET | `/api` | Returns `{"message": "Hello from my app!"}` |
| GET | `/health` | Returns `{"status": "ok"}` |

---

## CI/CD Pipeline

Every push to `main` triggers 3 automated jobs in order:

```
test → docker → deploy
```

| Job | What it does |
|-----|-------------|
| `test` | Runs pytest — must pass before anything else |
| `docker` | Builds and pushes Docker image to Docker Hub |
| `deploy` | SSHs into Azure VM and runs the latest container |

---

## Running Locally

**1. Clone the repo**
```bash
git clone https://github.com/shellbyseashore0/flask-cicd-demo.git
cd flask-cicd-demo
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
python app/main.py
```

Visit `http://localhost:5000`

**4. Run tests**
```bash
python -m pytest tests/test_main.py -v
```

---

## Running with Docker

```bash
docker build -t flask-cicd-demo .
docker run -p 5000:5000 flask-cicd-demo
```

---

## GitHub Secrets Required

| Secret | Description |
|--------|-------------|
| `DOCKER_USERNAME` | Docker Hub username |
| `DOCKER_PASSWORD` | Docker Hub access token |
| `SERVER_HOST` | Azure VM public IP |
| `SERVER_USER` | Azure VM username |
| `SERVER_SSH_KEY` | Private SSH key for Azure VM |

---

## Tech Stack

- **Backend** — Python, Flask
- **Testing** — Pytest
- **Containerization** — Docker
- **CI/CD** — GitHub Actions
- **Cloud** — Microsoft Azure (Ubuntu VM)
