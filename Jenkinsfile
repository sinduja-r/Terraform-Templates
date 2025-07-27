pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/sinduja-r/Terraform-Templates.git'
            }
        }

        stage('Set Up Python Environment') {
            steps {
                sh '''
                    python3 -m venv ${VENV_DIR}
                    source ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                '''
            }
        }

        stage('Run Misconfiguration Analyzer') {
            steps {
                sh '''
                    source ${VENV_DIR}/bin/activate
                    python3 iac_misconfig_scanner.py
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
