pipeline {
	agent any
	stages {
		stage("Checkout") {
			steps {
				checkout scm
			}
		}
		stage("build") {
			steps {	
				sh 'docker build -t david:${BUILD_NUMBER} .'
			}
		}		
		stage("deploy") {
			steps {	
				sh 'docker tag david:${BUILD_NUMBER} bit1010/david:${BUILD_NUMBER}'
				sh 'docker tag david:${BUILD_NUMBER} bit1010/david:latest'
			}
		}
	}
}
