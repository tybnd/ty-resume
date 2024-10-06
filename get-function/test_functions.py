import unittest
from app import lambda_handler  # Adjust the import as necessary based on your project structure

class TestGetFunction(unittest.TestCase):
    
    def test_lambda_handler(self):
        # Define the event and context you want to simulate
        event = {
            "httpMethod": "GET",
            "pathParameters": {
                "ID": "123"  # Adjust according to your function's expected input
            }
        }
        context = {}  # You can define a mock context if needed

        # Call the lambda_handler with the test event and context
        response = lambda_handler(event, context)

        # Expected response based on real function output
        expected_response = {
            "statusCode": 200,
            "body": '{"message": "Visitor count retrieved successfully", "visitorCount": 147.0}',
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "OPTIONS,POST,GET,PUT",
                "Access-Control-Allow-Headers": "Content-Type,Authorization"
            }
        }

        self.assertEqual(response, expected_response)

if __name__ == '__main__':
    unittest.main()
