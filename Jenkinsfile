pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        DOCKER_IMAGE = "yourdockerhubusername/multi-container-flask"
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
                    // Build images defined in docker-compose.yml
                    sh 'docker-compose build'
                }
            }
        }

        stage('Run Containers for Testing') {
            steps {
                script {
                    sh 'docker-compose up -d'
                    // Wait a bit for containers to start
                    sh 'sleep 10'
                    // Test Flask response
                    sh 'curl -f http://localhost:5000 || exit 1'
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
                sh 'docker-compose down'
            }
        }
    }

    post {
        always {
            echo "Pipeline complete!"
        }
    }
}
