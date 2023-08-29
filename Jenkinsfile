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
			}
		}		
		stage("deploy") {
			steps {	
				sh 'kubectl apply -f service.yaml'				
			}
		}
	}	
	post {
		always {
			echo 'building..'
		}
		success {
	    		echo 'success'
		}
		failure {
	    		echo 'failure'
		}
	}
}
