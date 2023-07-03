import json
import boto3
import os
import time

dynamodb = boto3.resource('dynamodb')
table_name = os.getenv("DYNAMODB_TABLE_NAME", "")
table = dynamodb.Table(table_name)


def lambda_handler(event, context):
    print(event)
    data = event['body']
    data["id"] = event["id"]
    timestamp = int(time.time() * 1000)  # current timestamp in milliseconds
    data["sortkey"] = str(timestamp)
    table.put_item(Item=data)

    response = {
        'statusCode': 200,
        'body': json.dumps({'message': 'Data copied to DynamoDB table successfully'})
    }

    return response


"""
In this example, the Lambda function receives data from an API POST call as a JSON-encoded string in the event parameter. We use the json module to deserialize the JSON string into a Python dictionary called data.

We then use the boto3 library to create a connection to the DynamoDB resource and get a reference to the DynamoDB table specified by table_name. We use the put_item() method of the table object to insert the data dictionary into the table.

Finally, we construct a response object that includes a 200 status code and a message indicating that the data was successfully copied to the DynamoDB table. The response object is returned from the Lambda function to the API Gateway endpoint.

Note that you'll need to configure the API Gateway endpoint to trigger this Lambda function when a POST request is received. You can use the CloudFormation template example I provided in my previous answer as a starting point.

"""
