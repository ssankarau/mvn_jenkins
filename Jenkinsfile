pipeline {
  agent any
  stages {
    stage("BUILD"){
      steps {
        sh 'mvn -B -DskipTests clean package'
    }
    stage("Test"){
      steps {
        sh 'mvn test'
    }    
  }
}
