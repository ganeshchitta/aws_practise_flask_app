import boto3

client = boto3.client('apigateway')
# get_rest_apis() will return dict with key items containing api dicts
response = client.get_rest_api(restApiId='pp2qfncgdk')
endpoint_url = response
print(endpoint_url)


# import requests
#
# res = requests.post("https://pp2qfncgdk.execute-api.ap-south-1.amazonaws.com/dev/flaskresource1", data={"body":{}})
#
# print(res.json())