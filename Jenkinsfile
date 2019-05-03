pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo 'Building'
                sh 'git config --global http.proxy http://proxyuser:proxypwd@proxy.server.com:8080'
            }
        }
        stage ("Test"){
            steps{
               sh 'python -m Pyautomators -f json -o .testejp.json'
            }
        }
    }
}
