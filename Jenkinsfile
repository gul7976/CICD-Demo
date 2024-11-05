pipeline {
    agent any
    
    environment {
        // Define any environment variables here
        // Example: MY_ENV_VAR = 'value'
    }

    stages {
        stage('Checkout') {
            steps {
                // Check out code from a repository
                git branch: 'main', url: 'https://github.com/your-repo/your-project.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    // Commands to build the project
                    // Example for a Maven project:
                    sh 'mvn clean install'
                    
                    // Example for a Node.js project:
                    // sh 'npm install'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Commands to run tests
                    // Example for a Maven project:
                    sh 'mvn test'
                    
                    // Example for a Node.js project:
                    // sh 'npm test'
                }
            }
            post {
                always {
                    // Archive test reports, logs, etc., regardless of test results
                    junit '**/target/surefire-reports/*.xml' // Example for JUnit test results
                }
            }
        }

        stage('Static Analysis') {
            steps {
                script {
                    // Run static analysis tools, if applicable
                    // Example for a Java project with SonarQube:
                    sh 'mvn sonar:sonar -Dsonar.projectKey=your_project_key'
                }
            }
        }

        stage('Deploy') {
            when {
                branch 'main' // Deploy only if the branch is 'main'
            }
            steps {
                script {
                    // Commands to deploy the project
                    // This could be a shell script or an API call to your deployment service
                    
                    // Example deployment:
                    sh './deploy.sh'
                }
            }
        }
    }

    post {
        success {
            // Actions to perform after a successful build
            echo 'Build succeeded!'
        }
        failure {
            // Actions to perform after a failed build
            echo 'Build failed!'
        }
        always {
            // Actions to perform regardless of build success/failure
            // Example: Clean up, send notifications
            cleanWs() // Clean the workspace
        }
    }
}
