import json

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
            'headers': {},
            "body": json.dumps({
                "personId": personId + " from Lambda1!" ,
            }),
        }
