from unittest.mock import MagicMock

import requests

from crawlers import concordia_crawler
from tests.data import expected_concordia_crawler_data
from .crawlers_base_test import CrawlersBaseTestCase


class ConcordiaCrawlerTest(CrawlersBaseTestCase):
    resource_file_name = "concordia_crawler_test_content"


    def test_crawler_availability(self):
        mocked_request_lib = requests
        mocked_response = self.MockedHTTPResponse(content=self.load_test_content_as_bytes())
        mocked_request_lib.get = MagicMock(return_value=mocked_response)

        actual_crawler_data = concordia_crawler.crawl("query", [])
        self.assertEqual(expected_concordia_crawler_data, actual_crawler_data)
