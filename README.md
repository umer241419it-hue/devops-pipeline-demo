# DevOps Pipeline Demo

> **College Experiment:** To design and implement an end-to-end DevOps pipeline.

This project demonstrates a complete CI/CD pipeline using **Git**, **GitHub**, **Jenkins**, and **Docker** to automatically test, build, and deploy a containerized Python Flask web application.

---

## 1. Project Overview

The objective of this experiment is to automate the software delivery lifecycle from source code commit to container deployment. Every change pushed to the repository triggers Jenkins to:
1. Pull the latest code from GitHub.
2. Install required dependencies.
3. Execute automated unit tests using `pytest`.
4. Build a lightweight Docker container image.
5. Deploy (or recreate) the running Docker container.
6. Verify that the application and its `/health` check endpoint respond successfully.

---

## 2. Technologies Used

- **Source Code Management:** Git & GitHub
- **Continuous Integration / Continuous Delivery (CI/CD):** Jenkins (Declarative Pipeline)
- **Programming Language & Framework:** Python 3 & Flask
- **Automated Testing:** pytest
- **Containerization & Deployment:** Docker
- **Operating System Platform:** Windows (with native Docker Desktop and Jenkins support)

---

## 3. Project Structure

```text
devops-pipeline-demo/
│
├── app.py              # Flask web application with '/' and '/health' routes
├── requirements.txt    # Application and testing dependencies
├── test_app.py         # Automated pytest test cases
├── Dockerfile          # Multi-platform Docker configuration for containerization
├── Jenkinsfile         # Declarative Jenkins CI/CD pipeline definition
├── .gitignore          # Git ignore rules for Python, pytest, and IDE files
└── README.md           # Documentation, execution guide, and lab instructions
```

---

## 4. End-to-End DevOps Pipeline Flow

```text
Developer
   ↓
GitHub
   ↓
Jenkins
   ↓
Checkout
   ↓
Install Dependencies
   ↓
Run Tests
   ↓
Build Docker Image
   ↓
Deploy Container
   ↓
Verify Application
```

---

## 5. Running the Application Locally (Without Docker)

### Step 1: Create and Activate a Virtual Environment
In your terminal / PowerShell:
```bash
python -m venv venv
# On Windows PowerShell:
.\venv\Scripts\Activate.ps1
# Or on Command Prompt:
.\venv\Scripts\activate.bat
```

### Step 2: Install Dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### Step 3: Run the Flask App
```bash
python app.py
```

### Step 4: Access in Browser
Open your browser and visit:
- Application UI: [http://localhost:5000](http://localhost:5000)
- Health Check: [http://localhost:5000/health](http://localhost:5000/health)

---

## 6. Running Automated Tests

Run the test suite using `pytest`:

```bash
pytest
```
Or with verbose output:
```bash
python -m pytest test_app.py -v
```

### What is tested?
1. `test_home_page_status_code`: Confirms `/` returns HTTP 200.
2. `test_home_page_content`: Confirms the page displays "DevOps Pipeline Demo" and "Application deployed successfully through the DevOps pipeline."
3. `test_health_status_code`: Confirms `/health` returns HTTP 200.
4. `test_health_response_payload`: Confirms the JSON response contains `status: "healthy"` and `service: "devops-pipeline-demo"`.

---

## 7. Building the Docker Image

To build the Docker image locally:

```bash
docker build -t devops-pipeline-demo .
```

To verify the image was created:
```bash
docker images devops-pipeline-demo
```

---

## 8. Running the Docker Container

### Step 1: Stop and remove any existing container with the same name
```bash
docker stop devops-pipeline-demo
docker rm devops-pipeline-demo
```

### Step 2: Run the container in detached mode mapped to port 5000
```bash
docker run -d -p 5000:5000 --name devops-pipeline-demo devops-pipeline-demo
```

### Step 3: Check running containers
```bash
docker ps
```

---

## 9. Jenkins Pipeline Setup & Configuration

### Prerequisites on Jenkins (Windows)
1. **Python**: Ensure Python 3 is installed and added to the Windows System `PATH`.
2. **Docker Desktop**: Ensure Docker Desktop is running and the `docker` command is accessible from the command line.
3. **Jenkins Service Account Permissions**: If Jenkins runs as a Windows Service (`Local System`), make sure it has permissions to access the Docker daemon. Alternatively, run Jenkins via:
   ```cmd
   java -jar jenkins.war
   ```
   under your local user account.

### Configuring the Job in Jenkins
1. Open Jenkins dashboard (`http://localhost:8080`).
2. Click **New Item** &rarr; Select **Pipeline** &rarr; Name it `devops-pipeline-demo` &rarr; Click **OK**.
3. Under **Pipeline**:
   - **Definition**: Select `Pipeline script from SCM`.
   - **SCM**: Select `Git`.
   - **Repository URL**: Enter your GitHub repository URL (e.g. `https://github.com/<your-username>/devops-pipeline-demo.git`).
   - **Branch Specifier**: `*/main` or `*/master`.
   - **Script Path**: `Jenkinsfile`.
4. Click **Save**.
5. Click **Build Now** to execute the pipeline.

---

## 10. Jenkins Pipeline Stages Breakdown

| Stage | Name | Description |
|---|---|---|
| **Stage 1** | **Checkout** | Clones/pulls latest source code revision from the Git repository. |
| **Stage 2** | **Install Dependencies** | Updates `pip` and installs packages from `requirements.txt`. |
| **Stage 3** | **Run Tests** | Executes `pytest` test suite. The pipeline halts if any test fails. |
| **Stage 4** | **Build Docker Image** | Builds Docker image tagged as `devops-pipeline-demo:latest`. |
| **Stage 5** | **Deploy Container** | Gracefully cleans up previous container and deploys the new container on port 5000. |
| **Stage 6** | **Verify Deployment** | Queries `http://localhost:5000/health` to confirm the containerized application is running and healthy. |

---

## 11. Verification and Expected Outputs

### 1. Browser Verification
Visit [http://localhost:5000](http://localhost:5000) in your web browser:
- You will see the heading: **DevOps Pipeline Demo**
- You will see: **Application deployed successfully through the DevOps pipeline.**
- Pipeline flow indicators and environment status badges.

### 2. JSON Health Endpoint
Visit [http://localhost:5000/health](http://localhost:5000/health):
```json
{
  "message": "Application is running smoothly",
  "service": "devops-pipeline-demo",
  "status": "healthy"
}
```

### 3. Docker Status Command
```bash
docker ps --filter "name=devops-pipeline-demo"
```
Output confirms:
- **STATUS:** Up
- **PORTS:** `0.0.0.0:5000->5000/tcp`
