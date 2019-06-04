from tests import BaseTestCase
from helpers import is_valid_book

class CrawlerHelperTest(BaseTestCase):

    def test_is_valid_book(self):
        self.assertFalse(is_valid_book(title="", author=""))
        self.assertFalse(is_valid_book(title=None, author=None))
        self.assertTrue(is_valid_book(title="Title", author="Author"))
        self.assertTrue(is_valid_book(title="", author="Author"))
        self.assertTrue(is_valid_book(title="Title", author=""))
        self.assertFalse(is_valid_book(title="Please log in to see this content from Scopus®", author=""))