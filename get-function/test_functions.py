import unittest
from app import lambda_handler

class TestGetFunction(unittest.TestCase):

    def test_lambda_handler(self):
        # Define the event and context for the test
        event = {
            "httpMethod": "GET",
            "pathParameters": {
                "ID": "123"  # Adjust according to your function's expected input
            }
        }
        context = {}  # Empty context unless your Lambda requires something specific

        # Call the lambda_handler function with the test event and context
        response = lambda_handler(event, context)

        # Define the expected response structure (adjust according to your function's output)
        expected_response = {
            "statusCode": 200,
            "headers": {
                    "Access-Control-Allow-Headers": "Content-Type",
                    "Access-Control-Allow-Methods": "OPTIONS,POST,GET,PUT",
                    "Access-Control-Allow-Origin": "*"
                },
            "body": '{"message": "Your expected output here"}',  # Adjust based on actual response
            # If your function returns headers, include them here:
            # "headers": {"Content-Type": "application/json"}
        }

        # Assert the response matches the expected output
        self.assertEqual(response['statusCode'], expected_response['statusCode'])
        self.assertEqual(response['body'], expected_response['body'])
        # If you're testing headers, assert them too:
        # self.assertEqual(response['headers'], expected_response['headers'])

if __name__ == '__main__':
    unittest.main()
