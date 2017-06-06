from flask import Flask, Response, request, jsonify
import unittest
from app import app


class WebService(unittest.TestCase):
    """Tests for web service wrapper"""

    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def testWebServiceData(self):
        result = self.client.get('/search?term=World%20of%20Health%20Chiropractor&location=Powell')
        self.assertEqual(result.status_code, 200)
        self.assertIn("homberg-chiropractic-and-wellness-knoxville", result.data)

if __name__ == "__main__":
    unittest.main()
