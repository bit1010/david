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
				
				sh 'docker login -u bit1010 -p dckr_pat__Ljf_O9QXl2-tLwadueYD98IoFQ'

				sh 'docker push bit1010/david:${BUILD_NUMBER}'
				sh 'docker push bit1010/david:latest'

				sh 'kubectl apply -f service.yaml'
			}
		}
	}
}
