#!/bin/bash
# check sam deploy parameters
if [ ! -f sam_deploy_parameters.json ]; then
  echo "missing parameters"
  exit 1
fi

lambdas=1

while getopts "lf:" option; do
  case $option in
    l)
      echo "Option -l was specified."
      lambdas=0
      ;;
    f)
      file=$OPTARG
      echo "Option -f was specified with argument $file."
      ;;
    \?)
      echo "Invalid option: -$OPTARG"
      ;;
  esac
done


environment=$(jq -r '.environment' sam_deploy_parameters.json)
customstackid=$(jq -r '.ParameterOverrides.CustomStackId' sam_deploy_parameters.json)
custom_domain_id=$(jq -r '.ParameterOverrides.CustomDomainId' sam_deploy_parameters.json)
## zip a lambda file
cd resources
if [ $lambdas -eq 1 ]; then
# create s3 bucket stack
sam deploy --template-file templates/s3_bucket.yaml --stack-name flask-source-s3-bucket-${customstackid}-${environment} --parameter-overrides "customstackid=${customstackid} environment=${environment}" --capabilities CAPABILITY_NAMED_IAM
fi
# created dependencies layers for lambda
pip install -r lambdas/requirements.txt -t lambdas/build/.
python lambdas/zip_given_lambda.py
## upload lambda python code to s3
aws s3 cp lambdas/flask-lambda-copy-to-dynamodb.zip   s3://flask-sourcebucketflask-${customstackid}-${environment}/
## upload dependencies as layers to s3
aws s3 cp dependencies.zip s3://flask-sourcebucketflask-${customstackid}-${environment}/
aws s3 cp lambdas/flask-dependencies-lambda-layer.zip s3://flask-sourcebucketflask-${customstackid}-${environment}/

if [ $lambdas -eq 1 ]; then
#sam deploy --template-file templates/ec2_lambda.yaml --stack-name flask-ec2-instance-${customstackid}-${environment} --parameter-overrides "customstackid=${customstackid} environment=${environment} Keyname=ec2-${customstackid}-${environment} InstanceType=t2.micro" --capabilities CAPABILITY_NAMED_IAM
sam deploy --template-file templates/resources.yaml --stack-name flask-copy-jsondata-to-dynamodb-${customstackid}-${environment} --parameter-overrides "customstackid=${customstackid} environment=${environment}" --capabilities CAPABILITY_NAMED_IAM
fi



# resource.yaml description
# Here's an example CloudFormation template in YAML format that creates a Lambda function with an execution role that has permissions to access two S3 buckets, and also creates a trigger for the Lambda function:

#In this template, the LambdaExecutionRole resource creates an execution role for the Lambda function that allows access to both bucket1 and bucket2. The LambdaFunction resource creates the Lambda function with the specified execution role and other properties, such as the handler, runtime, and code. The LambdaS3Trigger resource creates a permission for the Lambda function to be invoked by the specified S3 buckets.
#
#To use this CloudFormation template, you can save the code to a file with a .yaml extension, such as my-cloudformation-template.yaml, and then deploy the stack using the AWS CloudFormation CLI or the AWS Management Console. When deploying the stack, you will need to specify the name of the S3 bucket where the Lambda function code is stored, as well as any other required parameters.










