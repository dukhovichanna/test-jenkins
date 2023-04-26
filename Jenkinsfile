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
                echo 'building the application...'
                echo 'Application built'
                echo "building version ${NEW_VERSION}"
                echo "branch name - ${BRANCH_NAME}"
                echo "change branch - ${env.CHANGE_BRANCH}"

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
