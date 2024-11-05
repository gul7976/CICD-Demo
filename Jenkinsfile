pipeline { agent { label 'your-slave-label' } stages { stage('Clone Repository') { steps { git url: 'https://github.com/gul7976/CICD-Demo', branch: 'main' } } stage('Install Dependencies') { steps { sh ''' pip install pytest ''' } } stage('Run Tests') { steps { sh 'pytest test_add_numbers.py' } } } post { always { echo 'Build finished' } } }

 
