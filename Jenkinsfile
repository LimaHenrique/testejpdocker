pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo 'Building'
                git 'https://github.com/LimaHenrique/testejpdocker'
                sh '''
                git fetch --tags --progress origin +refs/heads/master:refs/remotes/origin/master --prune
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
