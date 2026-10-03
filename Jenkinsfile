pipeline {
    agent any

    environment {
        IMAGE_NAME = 'devops-pipeline-demo:latest'
        CONTAINER_NAME = 'devops-pipeline-demo'
        PORT = '5000'
    }

    stages {
        stage('Checkout') {
            steps {
                echo '=== Stage 1: Checking out source code ==='
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '=== Stage 2: Installing Python dependencies ==='
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                echo '=== Stage 3: Running automated unit tests with pytest ==='
                bat 'python -m pytest test_app.py -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "=== Stage 4: Building Docker image ${IMAGE_NAME} ==="
                bat "docker build -t %IMAGE_NAME% ."
            }
        }

        stage('Deploy Container') {
            steps {
                echo "=== Stage 5: Deploying Docker container ${CONTAINER_NAME} ==="
                // Stop and remove previous container instance if it exists
                bat "docker stop %CONTAINER_NAME% 2>nul || ver >nul"
                bat "docker rm %CONTAINER_NAME% 2>nul || ver >nul"
                // Run new container mapped to port 5000
                bat "docker run -d -p %PORT%:%PORT% --name %CONTAINER_NAME% %IMAGE_NAME%"
            }
        }

        stage('Verify Deployment') {
            steps {
                echo '=== Stage 6: Verifying container health and responsiveness ==='
                // Wait briefly for container startup and query the /health endpoint
                bat 'powershell -Command "Start-Sleep -Seconds 3; $resp = Invoke-RestMethod -Uri http://localhost:5000/health; Write-Host (\'Application Health Status: \' + $resp.status); if ($resp.status -ne \'healthy\') { exit 1 }"'
            }
        }
    }

    post {
        success {
            echo '====================================================='
            echo ' DevOps Pipeline Executed Successfully! '
            echo ' Application URL: http://localhost:5000'
            echo ' Health Endpoint: http://localhost:5000/health'
            echo '====================================================='
        }
        failure {
            echo 'Pipeline failed. Please review the stage logs above.'
        }
    }
}
