import boto3
import paramiko

"""
To copy files from S3 to an EC2 instance using AWS Lambda, you can use the Boto3 library in Python, along with the Paramiko library to transfer files over SSH. Here's an example Lambda function that downloads a file from S3 and transfers it to an EC2 instance using SSH:

In this function, the lambda_handler function is the entry point for the Lambda function. It takes an event object and a context object as input parameters. The event object contains information about the S3 bucket name, file name, and EC2 instance ID. The context object contains information about the Lambda function's execution environment.

The function first sets up the S3 and EC2 clients, then downloads the file from S3 to the Lambda function's local file system using the download_file method of the S3 client.

Next, the function sets up an SSH client using the Paramiko library and connects to the EC2 instance using the instance ID. The instance IP address is obtained from the EC2 client's describe_instances method.

Finally, the function transfers the file to the EC2 instance using SFTP, and then closes the SSH connection.


"""
def lambda_handler(event, context):
    # Set up S3 and EC2 clients
    s3 = boto3.client('s3')
    ec2_client = boto3.client('ec2')

    # Get the instance ID from the event object
    instance_id = event['instance_id']

    # Download the file from S3
    bucket_name = event['bucket_name']
    file_name = event['file_name']
    local_file_path = '/tmp/' + file_name
    s3.download_file(bucket_name, file_name, local_file_path)

    # Set up SSH client
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # Connect to the EC2 instance using the instance ID
    response = ec2_client.describe_instances(InstanceIds=[instance_id])
    instance_ip = response['Reservations'][0]['Instances'][0]['PublicIpAddress']
    ssh.connect(instance_ip, username='ec2-user', key_filename='/path/to/ssh/key.pem')

    # Transfer the file using SFTP
    sftp = ssh.open_sftp()
    sftp.put(local_file_path, '/path/to/remote/directory/' + file_name)
    sftp.close()

    # Close the SSH connection
    ssh.close()

    return {
        'message': 'File transfer complete'
    }
