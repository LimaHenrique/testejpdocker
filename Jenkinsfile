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
               bat 'start cmd.exe python -m Pyautomators -f json -o .testejp.json'
            }
        }
    }
}
