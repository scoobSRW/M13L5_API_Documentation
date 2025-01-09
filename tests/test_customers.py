import unittest
from unittest.mock import patch
import requests

BASE_URL = "http://127.0.0.1:5000"  # Update if running on a different port or domain

class TestCustomerEndpoints(unittest.TestCase):
    CUSTOMER_URL = f"{BASE_URL}/api/customers"

    @patch("requests.post")
    def test_create_customer(self, mock_post):
        # Simulate a successful response
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {
            "message": "Customer created successfully"
        }

        payload = {"name": "Alice", "email": "alice@example.com", "phone": "1234567890"}
        response = requests.post(self.CUSTOMER_URL, json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertIn("Customer created successfully", response.json()["message"])

    @patch("requests.get")
    def test_get_customers(self, mock_get):
        # Simulate a successful response
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [
            {"id": 1, "name": "Alice", "email": "alice@example.com", "phone": "1234567890"},
            {"id": 2, "name": "Bob", "email": "bob@example.com", "phone": "0987654321"}
        ]

        response = requests.get(self.CUSTOMER_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

if __name__ == "__main__":
    unittest.main()
