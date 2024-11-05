pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Check out code from the repository
                git branch: 'main', url: 'https://github.com/your-repo/your-project.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    // Example build step if needed, such as installing dependencies
                    // For Python projects, you might install dependencies here:
                    sh 'pip install -r requirements.txt || true' // If no requirements file, it will skip
                }
            }
        }

        stage('Run Addition Script and Tests') {
            steps {
                script {
                    // Run the addition script
                    sh 'python3 add_numbers.py'
                    
                    // Run the test cases and capture test results
                    sh 'python3 -m unittest test_add_numbers.py'
                }
            }
            post {
                always {
                    // Archive test reports if applicable (you could use XML output for advanced reporting)
                    junit '**/test-reports/*.xml' // Uncomment if using a test report output in XML
                }
            }
        }

        stage('Static Analysis') {
            steps {
                script {
                    // Run static analysis tools, if needed
                    // Example: flake8 for Python linting
                    sh 'flake8 .'
                }
            }
        }

        stage('Deploy') {
            when {
                branch 'main' // Only deploy if on the main branch
            }
            steps {
                script {
                    // Example deployment step (adjust as needed for your environment)
                    sh './deploy.sh'
                }
            }
        }
    }

    post {
        success {
            echo 'Build succeeded!'
        }
        failure {
            echo 'Build failed!'
        }
        always {
            cleanWs() // Clean workspace after build
        }
    }
}
