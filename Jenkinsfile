#!groovy
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
               bat 'python -m Pyautomators -f json -o .testejp.json'
            }
        }
    }
}
