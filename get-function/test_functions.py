import unittest
from app import lambda_handler  # Adjust the import as necessary based on your project structure

class TestGetFunction(unittest.TestCase):

    def test_lambda_handler(self):
        # Simulate the event for the GET request
        event = {
            "httpMethod": "GET",
            "pathParameters": {
                "ID": "123"  # As per your function's setup
            }
        }
        context = {}  # Mock context

        # Call the lambda_handler with the simulated event and context
        response = lambda_handler(event, context)

        # Define the expected response
        expected_body = '{"message": "Visitor count retrieved successfully", "visitorCount": "*" }'
        expected_status_code = 200

        # Assert body and statusCode separately
        self.assertEqual(response['body'], expected_body)
        self.assertEqual(response['statusCode'], expected_status_code)

        # Define the expected headers based on actual values returned by your function
        expected_headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT',
            'Access-Control-Allow-Headers': 'Content-Type,Authorization'
        }

        # Check that the expected headers are present (ignoring order)
        for key, value in expected_headers.items():
            self.assertEqual(response['headers'][key], value)

if __name__ == '__main__':
    unittest.main()
