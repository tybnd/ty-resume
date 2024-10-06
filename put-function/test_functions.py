import unittest
from app import lambda_handler  # Adjust the import as necessary based on your project structure

class TestPutFunction(unittest.TestCase):

    def test_lambda_handler(self):
        # Simulate the event for the PUT request
        event = {
            "httpMethod": "PUT",
            "pathParameters": {
                "ID": "123"  # As per your function's setup
            },
            "body": '{"VisitorCount": "*" }'  # Example of what your PUT request body might contain
        }
        context = {}  # Mock context

        # Call the lambda_handler with the simulated event and context
        response = lambda_handler(event, context)

        # Define the expected response using "Test Successful"
        expected_response = {
            "statusCode": 200,
            "body": '{"message": "Test Successful", "updatedAttributes": {"VisitorCount": "TEST"}}'
        }

        # Assert that the response body matches the expected body
        self.assertEqual(response['body'], expected_response['body'])

        # Optionally, also check if statusCode is 200
        self.assertEqual(response['statusCode'], 200)

if __name__ == '__main__':
    unittest.main()
