from .crawlers_base_test import CrawlersBaseTestCase
import requests
from crawlers import uqam_crawler
from unittest.mock import MagicMock
from tests.data import expected_uqam_crawler_data


class UqamCrawlerTest(CrawlersBaseTestCase):
    resource_file_name = "uqam_crawler_test_content"

    def test_crawler_availability(self):
        mocked_request_lib = requests
        mocked_response = self.MockedHTTPResponse(content=self.load_test_content_as_bytes())
        mocked_request_lib.get = MagicMock(return_value=mocked_response)

        actual_crawler_data = uqam_crawler.crawl("query", [])
        self.assertEqual(expected_uqam_crawler_data, actual_crawler_data)
