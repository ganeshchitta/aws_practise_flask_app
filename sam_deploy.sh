##sam build
## zip a lambda file
cd lambdas
# create s3 bucket stack
sam deploy --template-file ../s3_bucket.yaml --stack-name source-s3-bucket --capabilities CAPABILITY_NAMED_IAM
# created dependencies layers for lambda
#pip install -r requirements.txt -t build/.
python zip_given_lambda.py
#
## upload lambda python code to s3
aws s3 cp "copytodynamodbcode.zip"   s3://sourcebucketflask/
## upload dependecies as layers to s3
aws s3 cp "dependencies.zip" s3://sourcebucketflask/
aws s3 cp "flaskdependencies.zip" s3://sourcebucketflask/

sam deploy --template-file ../ec2_lambda.yaml --stack-name source-ec2-lambda --capabilities CAPABILITY_NAMED_IAM
sam deploy --template-file ../resources.yaml --stack-name copy-jsondata-to-dynamodb --capabilities CAPABILITY_NAMED_IAM
















# resource.yaml description
# Here's an example CloudFormation template in YAML format that creates a Lambda function with an execution role that has permissions to access two S3 buckets, and also creates a trigger for the Lambda function:

#In this template, the LambdaExecutionRole resource creates an execution role for the Lambda function that allows access to both bucket1 and bucket2. The LambdaFunction resource creates the Lambda function with the specified execution role and other properties, such as the handler, runtime, and code. The LambdaS3Trigger resource creates a permission for the Lambda function to be invoked by the specified S3 buckets.
#
#To use this CloudFormation template, you can save the code to a file with a .yaml extension, such as my-cloudformation-template.yaml, and then deploy the stack using the AWS CloudFormation CLI or the AWS Management Console. When deploying the stack, you will need to specify the name of the S3 bucket where the Lambda function code is stored, as well as any other required parameters.





