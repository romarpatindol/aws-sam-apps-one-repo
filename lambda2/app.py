import json
"""
Sample lambda function with dependencies specified in requirements.txt

When using the ff. SAM commands:
"sam build" command - SAM will install dependencies based on requirements.txt.
"sam deploy --guided" - SAM will deploy the API Gateway and Lambda functions, as well as any dependencies.
"""

# import requests

def lambda_handler(event, context):

    if ('pathParameters' not in event):
        return {
            'statusCode': 400,
            'headers': {},
            'body': json.dumps({'msg': 'Bad Request'})
        }

    # method: GET
    if (event['httpMethod'] == 'GET'):

        personId = event['queryStringParameters']['personId']

        return {
            "statusCode": 200,
            "body": json.dumps({
                "personId": personId + " from Lambda2!" ,
            }),
        }
