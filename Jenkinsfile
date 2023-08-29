pipeline {
	agent any
	stages {
		stage("build") {
			steps {	
				sh 'docker build -t david:latest .'
			}
		}	
	}	
	post {
		always {
			echo 'building..'
		}
		success {
	    		echo 'success'
			
			sh 'docker rmi david:latest'
		}
		failure {
	    		echo 'failure'
		}
	}
}
