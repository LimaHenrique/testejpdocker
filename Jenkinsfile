pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo 'Building'
                sh '''
                git config --global --unset http.proxy 
                git config --global --unset https.proxy
                '''
            }
        }
        stage ("Test"){
            steps{
               sh 'python -m Pyautomators -f json -o .testejp.json'
            }
        }
    }
}
