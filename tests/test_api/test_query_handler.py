from unittest.mock import MagicMock

import api.query_handler as query_handler
from classes import ThreadsManager
from constants import get_default_city_name
from database import CrawlerCacheModel
from tests import BaseTestCase
from tests.data import expected_udm_crawler_data, expected_uqam_crawler_data, expected_concordia_crawler_data


class QueryHandlerTest(BaseTestCase):
    def test_query_handler_api_with_empty_query(self):
        res = self.get('/query')
        self.assertStatus(res, 422)
        self.assertEqual("Query is invalid", res.json['message'])
        self.assertTrue(res.json['has_error'])

    def test_query_handler_api_with_empty_city(self):
        query_handler._process_query = MagicMock(return_value=[{"data": "test"}])
        res = self.get('/query?query=test2')
        self.assertStatus(res, 200)
        query_handler._process_query.assert_called_with('test2', get_default_city_name())

    def test_query_handler_api_caches_results(self):
        mocked_thread_manager = ThreadsManager
        mocked_thread_manager.init_thread_pool = MagicMock(return_value=[{"data": "test"}])
        res = self.get('/query?query=test2&city=MTL')
        self.assertStatus(res, 200)
        mocked_thread_manager.init_thread_pool.assert_called()

        # check the database
        crawler_record = CrawlerCacheModel.get_cache_crawlers_record_for('test2', 'MTL')
        self.assertEqual(crawler_record.content, [{"data": "test"}])

        # do another request, but this time the cache will be used instead of thread_manager
        mocked_thread_manager.init_thread_pool.reset_mock()
        res = self.get('/query?query=test2&city=MTL')
        self.assertStatus(res, 200)
        self.assertEqual([{"data": "test"}], res.json['data'])
        mocked_thread_manager.init_thread_pool.assert_not_called()


def get_mocked_concordia_crawler():
    return expected_concordia_crawler_data


def get_mocked_udm_crawler():
    return expected_udm_crawler_data


def get_mocked_uqam_crawler():
    return expected_uqam_crawler_data
