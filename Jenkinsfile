pipeline {
    agent any

    stages {

        stage('Environment Setup') {
            steps {
                echo 'Setting up environment'
                checkout scm

                sh '''
                python -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Pipeline Syntax Check') {
            steps {
                echo 'Checking pipeline script for syntax errors'

                sh '''
                . venv/bin/activate
                python -m py_compile src/pipeline.py
                python -m py_compile src/pipeline_components.py
                '''
            }
        }

        stage('Run MLflow Pipeline') {
            steps {
                echo 'Running ML pipeline to verify workflow'

                sh '''
                . venv/bin/activate
                python src/pipeline.py
                '''
            }
        }
    }

    post {
        always {
            echo 'Jenkins pipeline finished'
        }
    }
}
