pipeline {
	agent any
	stages {
		stage("init") {
			steps {
				sh 'init'
			}
		}
		stage("Checkout") {
			steps {
				checkout scm
			}
		}
		stage("Build") {
			steps {
				sh 'docker-compose build web'
			}
		}
		stage("test") {			
			steps {
				sh 'test'
			}
		}
		stage("Tag and Push") {
			steps {				
				sh 'docker Tag and Push'
			}
		}
		stage("deploy") {
			steps {
				sh 'docker-compose up -d'
			}
		}
	}
}
