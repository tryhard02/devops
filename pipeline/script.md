
1. **Create a New Item using Pipeline in Jenkins**
2. **Scroll down to find text edior**
3. **Paste the code down below and Save it**

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                sh 'mvn clean install'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                sh 'python -m unittest discover'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}

```
