pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('82111275-dd6d-4a33-a546-59d523e386bc')
        DOCKER_IMAGE = "harsha0306/multi-container-flask"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Harsha-03-Shri/multi-container-app.git'
            }
        }

    stage('Build Images') {
        steps {
            script {
                bat 'docker-compose build'
                bat 'docker tag multi-container-pipeline-web:latest %DOCKER_IMAGE%:latest'
            }
        }
    }

        stage('Run Containers for Testing') {
            steps {
                script {
                    bat 'docker-compose up -d'
                    bat 'sleep 10'
                    bat 'curl -f http://localhost:8000 || exit 1'
                }
            }
        }

    stage('Push Web Image to Docker Hub') {
        steps {
            script {
                bat 'docker login -u %DOCKERHUB_CREDENTIALS_USR% -p %DOCKERHUB_CREDENTIALS_PSW%'
                bat 'docker push %DOCKER_IMAGE%:latest'
            }
        }
    }

        stage('Cleanup Containers') {
            steps {
                bat 'docker-compose down --volumes --remove-orphans'
            }
        }

        // Optional deploy
        // stage('Deploy') {
        //     steps {
        //         script {
        //             sh '''
        //             docker pull ${DOCKER_IMAGE}:latest
        //             docker stop flask_prod || true
        //             docker rm flask_prod || true
        //             docker run -d -p 8000:8000 --name flask_prod ${DOCKER_IMAGE}:latest
        //             '''
        //         }
        //     }
        // }
    }

    post {
        always {
            echo "Pipeline complete!"
        }
    }
}
