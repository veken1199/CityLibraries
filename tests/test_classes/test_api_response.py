from classes import ApiResponse
from tests import BaseTestCase
import json

class TestApiResponse(BaseTestCase):

    def test_ApiResponse_properties(self):
        data = {"hello": "hello"}
        status_code = 6000
        message = "test"
        has_error = True

        expected_response = dict(data=data, status_code=status_code, message=message, has_error=has_error)

        resp = ApiResponse(data=data, message=message, has_error=has_error, status_code=status_code)
        self.assertEqual(data, resp.data)
        self.assertEqual(message, resp.message)
        self.assertEqual(has_error, resp.has_error)

        actual_resp, actual_status_error = resp.send()
        self.assertEqual(status_code, actual_status_error)
        self.assertDictEqual(expected_response, json.loads(actual_resp))

