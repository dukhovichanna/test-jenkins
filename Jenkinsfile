//CODE_CHANGES = getGitChanges()

pipeline {

    agent any
    environment {
        NEW_VERSION = '1.3.0'
    }

    stages {
        /* stage('Git Checkout') {
            agent any
            steps{
                script{
                    scmVars checkout scm
                }
            }
        } */

        stage("build") {
            /* when{
                expression{
                    BRANCH_NAME == 'dev' && CODE_CHANGES == true
                }
            } */

            steps {
                //echo "${BRANCH}"
                echo BRANCH_NAME
                echo env.CHANGE_BRANCH
                sh '''
                    #!bin/bash
                    PR_NUMBER=${CHANGE_ID##*/}
                    API_URL=${CHANGE_URL}/api/json
                    SOURCE_BRANCH=$(curl -s $API_URL |jq -r ".actions[0].parameters[0].value)
                    echo "Source branch: $SOURCE_BRANCH"
                '''

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
