pipeline {
	agent any
	stages {
		stage("build") {
			steps {	
				sh 'docker build -t david:${BUILD_NUMBER} .'
			}
		}	
	}	
	post {
		always {
			echo 'building..'
		}
		success {
	    		echo 'success'
			
			sh 'docker rmi david:${BUILD_NUMBER}'
		}
		failure {
	    		echo 'failure'
		}
	}
}
