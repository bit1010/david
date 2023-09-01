pipeline {
	agent any
	stages {
		stage("build") {
			steps {	
				sh 'docker build -t david:latest .'
			}
		}			
		stage("deploy") {
			steps {	
				sh 'docker tag david:latest bit1010/david:latest'
				
				sh 'docker login -u bit1010 -p dckr_pat__Ljf_O9QXl2-tLwadueYD98IoFQ'

				sh 'docker push bit1010/david:latest'		
							
			    withKubeConfig([credentialsId: 'kubectl-deploy-credentials', serverUrl: 'https://192.168.49.2:8443']) {
				sh 'kubectl apply -f service.yaml'
			    }
			}
		}
	}	
	post {
		always {
			echo 'building..'
		}
		success {
	    		echo 'success'
			
			sh 'docker rmi bit1010/david:latest'
			sh 'docker rmi david:latest'
		}
		failure {
	    		echo 'failure'
		}
	}
}
