#!groovy
pipeline{
    agent any
    stages {
        stage ("Build"){
            steps{
                echo 'Building'
                git 'https://github.com/LimaHenrique/testejp'
                bat '''
                bat start cmd.exe pip install python-jenkins
                start cmd.exe python -m pip install --upgrade pip
                start cmd.exe pip install virtualenv
                start cmd.exe virtualenv env
                start cmd.exe env//Scripts//activate
                '''
            }
        }
        stage ("Test"){
            steps{
               bat '''
               start cmd.exe python -m Pyautomators -f json -o .testejp.json
               '''
            }
        }
    }
}
