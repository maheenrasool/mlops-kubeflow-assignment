pipeline {
    agent any

    stages {

        stage('Environment Setup') {
            steps {
                echo 'Setting up environment'
                checkout scm

                bat """
                python -m venv venv
                call venv\\Scripts\\activate
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                """
            }
        }

        stage('Pipeline Syntax Check') {
            steps {
                echo 'Checking pipeline script for syntax errors'

                bat """
                call venv\\Scripts\\activate
                python -m py_compile src/pipeline.py
                python -m py_compile src/pipeline_components.py
                """
            }
        }

        stage('Run MLflow Pipeline') {
            steps {
                echo 'Running ML pipeline to verify workflow'

                bat """
                call venv\\Scripts\\activate
                python src/pipeline.py
                """
            }
        }
    }

    post {
        always {
            echo 'Jenkins pipeline finished'
        }
    }
}
