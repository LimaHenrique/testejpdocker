pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo 'Building'
            }
        }
        stage ("Test"){
            steps{
               sh 'python -m Pyautomators -f json -o .testejp.json'
            }
        }
    }
}
