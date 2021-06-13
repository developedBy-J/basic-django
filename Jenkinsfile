pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'python3 manage.py test'
            }
        }
        stage('Deploy') {
            steps {
                sh 'sshpass -p akash_123 ssh -o StrictHostKeyChecking=no deployment-user@192.168.56
                .101 \
                "source my-venv/bin/activate;\
                cd basic-django;\
                git pull origin main;\
                pip3 install -r requirements.txt --no-warn-script-location;\
                python manage.py migrate;\
                deactivate;\
                sudo systemctl restart nginx;\
                sudo systemctl restart gunicorn;"'
            }
        }
    }
}