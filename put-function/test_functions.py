import unittest
from unittest.mock import patch
from app import lambda_handler  # Adjust the import as necessary

class TestPutFunction(unittest.TestCase):
    @patch('boto3.resource')  # Mock boto3 to avoid real DynamoDB calls
    def test_lambda_handler(self, mock_dynamodb):
        # Setup mock return value
        mock_table = mock_dynamodb.return_value.Table.return_value
        mock_table.update_item.return_value = {
            'Attributes': {'VisitorCount': 148}
        }

        # Define the expected output (no specific visitor count)
        expected_status_code = 200
        expected_message = "VisitorCount updated successfully"

        # Run the lambda handler function
        response = lambda_handler({}, {})

        # Assertions: Check if the response is successful
        self.assertEqual(response['statusCode'], expected_status_code)
        self.assertIn('message', response['body'])
        self.assertIn(expected_message, response['body'])

if __name__ == '__main__':
    unittest.main()
