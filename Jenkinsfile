//CODE_CHANGES = getGitChanges()

pipeline {

    agent any
    environment {
        NEW_VERSION = '1.3.0'
    }

    stages {

        stage("build") {
            /* when{
                expression{
                    BRANCH_NAME == 'dev' && CODE_CHANGES == true
                }
            } */

            steps {
                //echo "${BRANCH}"
                echo "${BRANCH_NAME}"
                echo "${env.CHANGE_BRANCH}"

            }
        }

        stage("test") {
            when{
                expression{
                    BRANCH_NAME == 'dev' || BRANCH_NAME == 'master'
                }
            }

            steps {
                echo 'testing the application...'

            }
        }

        stage("deploy") {

            steps {
                echo 'deploying the application...'

            }
        }
    }
    /* post {
        
        always{
            // 
        }
        success{
            //
        }
        failure{
            //
        }
    } */

}
