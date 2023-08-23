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
				echo BUILD_NUMBER
			}
		}
	}
}
