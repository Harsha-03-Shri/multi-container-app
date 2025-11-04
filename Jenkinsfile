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
                    url: 'https://github.com/yourusername/multi-container-app.git'
            }
        }

        stage('Build Images') {
            steps {
                script {
                    sh 'docker-compose build'
                    sh 'docker tag multi-container-app-web:latest ${DOCKER_IMAGE}:latest'
                }
            }
        }

        stage('Run Containers for Testing') {
            steps {
                script {
                    sh 'docker-compose up -d'
                    sh 'sleep 10'
                    sh 'curl -f http://localhost:8000 || exit 1'
                }
            }
        }

        stage('Push Web Image to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', DOCKERHUB_CREDENTIALS) {
                        def image = docker.image("${DOCKER_IMAGE}:latest")
                        image.push()
                    }
                }
            }
        }

        stage('Cleanup Containers') {
            steps {
                sh 'docker-compose down --volumes --remove-orphans'
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
