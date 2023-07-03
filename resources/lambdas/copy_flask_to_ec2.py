import boto3
import os

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    ec2 = boto3.client('ec2')
    instance_id = os.environ['INSTANCE_ID']
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    local_file_path = '/tmp/' + object_key.split('/')[-1]
    s3.download_file(bucket_name, object_key, local_file_path)
    ec2.upload_file(local_file_path, instance_id, '/home/ec2-user/' + object_key.split('/')[-1])

    return {"status": "Successfully copied to EC2 instance"}
