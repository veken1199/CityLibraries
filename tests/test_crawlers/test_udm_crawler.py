from unittest.mock import MagicMock

import requests

from crawlers import udm_crawler
from tests.data import expected_udm_crawler_data
from .crawlers_base_test import CrawlersBaseTestCase

class UdmCrawlerTest(CrawlersBaseTestCase):
    resource_file_name = "udm_crawler_test_content"

    def test_crawler_availability(self):
        mocked_request_lib = requests
        mocked_response = self.MockedHTTPResponse(json_data=self.load_test_content_as_json())
        mocked_request_lib.get = MagicMock(return_value=mocked_response)

        actual_crawler_data = udm_crawler.crawl("query", [])
        self.assertEqual(expected_udm_crawler_data, actual_crawler_data)
