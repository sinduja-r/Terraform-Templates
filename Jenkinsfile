pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/YOUR-USERNAME/iac-analyzer.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                sh '''
                    python3 -m venv ${VENV_DIR}
                    source ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Misconfiguration Analyzer') {
            steps {
                sh '''
                    source ${VENV_DIR}/bin/activate
                    python3 analyzer.py
                '''
            }
        }
    }

    post {
        success {
            echo 'Misconfiguration check completed successfully!'
        }
        failure {
            echo 'Pipeline failed during analysis.'
        }
    }
}
