pipeline {
	agent any
	stages {
		stage("init") {
			steps {
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
			}
		}
		stage("deploy") {
			steps {
				sh "docker-compose up -d"
			}
		}
	}
}
