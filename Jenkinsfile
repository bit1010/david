pipeline {
	agent any
	stages {
		stage("Checkout") {
			steps {
				checkout scm
			}
		}
		stage("deploy") {
			steps {	
				sh 'kubectl apply -f service.yaml'				
			}
		}
	}
}
