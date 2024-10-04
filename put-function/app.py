import json
import logging
import boto3
from botocore.exceptions import ClientError
from decimal import Decimal

logger = logging.getLogger()
logger.setLevel(logging.INFO)

dynamodb = boto3.resource('dynamodb')
table_name = 'cloud-resume-challenge'  # Replace with your actual table name
table = dynamodb.Table(table_name)

# Function to handle conversion of Decimal types to int or float
class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return int(obj)  # or float(obj) if needed
        return super(DecimalEncoder, self).default(obj)

def lambda_handler(event, context):
    logger.info(f"Received event: {json.dumps(event)}")
    
    id_value = '123'  # Hardcoded ID
    
    try:
        # Increment VisitorCount by 1
        response = table.update_item(
            Key={'ID': id_value},
            UpdateExpression='SET VisitorCount = if_not_exists(VisitorCount, :start) + :increment',
            ExpressionAttributeValues={
                ':start': 0,
                ':increment': 1
            },
            ReturnValues='UPDATED_NEW'
        )
        
        logger.info(f"Update response: {response}")
        
        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET,PUT",
                "Access-Control-Allow-Headers": "Content-Type,Authorization"
            },
            "body": json.dumps({
                "message": "VisitorCount updated successfully",
                "updatedAttributes": response['Attributes']
            }, cls=DecimalEncoder)  # Use custom encoder to handle Decimal type
        }
        
    except ClientError as e:
        logger.error(f"Error updating item: {e.response['Error']['Message']}")
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET,PUT",
                "Access-Control-Allow-Headers": "Content-Type,Authorization"
            },
            "body": json.dumps({
                "message": f"Error updating VisitorCount: {e.response['Error']['Message']}"
            })
        }
