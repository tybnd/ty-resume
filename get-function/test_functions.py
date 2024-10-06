import unittest
from app import lambda_handler

class TestGetFunction(unittest.TestCase):
    
    def test_lambda_handler(self):
        # Define a test event with 'isTest' set to True
        event = {
            "httpMethod": "GET",
            "pathParameters": {
                "ID": "123"
            },
            "isTest": True  # This will trigger the test response
        }
        context = {}  # You can define a mock context if needed

        # Call the lambda_handler with the test event and context
        response = lambda_handler(event, context)

        # Expected test response
        expected_response = {
            "statusCode": 200,
            "body": '{"message": "Test Successful", "visitorCount": "TEST" }',
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET,PUT",
                "Access-Control-Allow-Headers": "Content-Type,Authorization"
            }
        }

        self.assertEqual(response, expected_response)

if __name__ == '__main__':
    unittest.main()
