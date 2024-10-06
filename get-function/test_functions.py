import unittest
from unittest.mock import patch, MagicMock
from app import lambda_handler

class TestGetFunction(unittest.TestCase):
    
    @patch('app.dynamodb.Table')  # Mock the DynamoDB table
    def test_lambda_handler(self, mock_table):
        # Mock the DynamoDB get_item method to return a visitor count of 147.0
        mock_table.return_value.get_item.return_value = {
            'Item': {'VisitorCount': 147.0}
        }

        # Test event and context
        event = {}  # Define a dummy event if needed
        context = {}  # Define a dummy context if needed

        # Expected response body
        expected_body = '{"message": "Visitor count retrieved successfully", "visitorCount": 147.0}'
        expected_response = {
            'statusCode': 200,
            'body': expected_body,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type,Authorization',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT'
            }
        }

        # Call the lambda function
        response = lambda_handler(event, context)

        # Assertions
        self.assertEqual(response['body'], expected_body)
        self.assertEqual(response['statusCode'], expected_response['statusCode'])
        self.assertEqual(response['headers'], expected_response['headers'])

if __name__ == '__main__':
    unittest.main()
