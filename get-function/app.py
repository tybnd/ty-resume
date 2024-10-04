import json
import boto3
import decimal
import logging

# Initialize logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('cloud-resume-challenge')

# Custom encoder for Decimal
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

def lambda_handler(event, context):
    try:
        # Log the incoming event
        logger.info(f"Received event: {json.dumps(event)}")

        # Default visitor ID
        visitor_id = '123'
        if 'queryStringParameters' in event and event['queryStringParameters'] and 'ID' in event['queryStringParameters']:
            visitor_id = event['queryStringParameters']['ID']

        # Retrieve visitor count from DynamoDB
        response = table.get_item(Key={'ID': visitor_id})

        if 'Item' not in response:
            return {
                'statusCode': 404,
                'headers': {
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Headers': 'OPTIONS,POST,GET,PUT',
                    'Access-Control-Allow-Methods': 'Content-Type,Authorization'
                },
                'body': json.dumps({'message': 'Visitor count not found'})
            }

        visitor_count = response['Item']['VisitorCount']
        logger.info(f"Retrieved visitor count: {visitor_count}")

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'OPTIONS,POST,GET,PUT',
                'Access-Control-Allow-Methods': 'Content-Type,Authorization'
            },
            'body': json.dumps({
                'message': 'Visitor count retrieved successfully',
                'visitorCount': visitor_count
            }, cls=DecimalEncoder)
        }

    except Exception as e:
        logger.error(f"Error retrieving visitor count: {str(e)}", exc_info=True)
        return {
            'statusCode': 500,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'OPTIONS,POST,GET,PUT',
                'Access-Control-Allow-Methods': 'Content-Type,Authorization'
            },
            'body': json.dumps({'message': 'Internal Server Error', 'error': str(e)})
        }
