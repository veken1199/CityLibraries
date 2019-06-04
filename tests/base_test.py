from flask import json
import requests
from flask_testing import TestCase

from database.setup import reset_db
from main import create_app, db


class BaseTestCase(TestCase):
    db = None
    client = None

    def create_app(self):
        # pass in test configuration
        app, db = create_app('config.TestingConfig')
        self.db = db
        self.client = app
        reset_db()
        return app

    def setUp(self):
        pass

    def tearDown(self):
        db.session.remove()
        pass

    # helper function to send post request
    def post(self, url, data):
        return self.client.post(url, data=json.dumps(data),
                                content_type='application/json',
                                charset='UTF-8',
                                follow_redirects=True)
    def get(self, url):
        return self.client.get(url)

    class MockedHTTPResponse:
        def __init__(self, content="", json_data={}, status=200, text=""):
            self.content = content
            self.json_data = json_data
            self.status = status
            self.text = text

        def json(self):
            return self.json_data
