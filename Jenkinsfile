pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/gul7976/CICD-Demo.git', branch: 'main'
            }
        }

        
    }

    post {
        always {
            echo 'Build finished'
        }
    }
}
