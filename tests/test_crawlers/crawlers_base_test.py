import json
import os

from tests import BaseTestCase


class CrawlersBaseTestCase(BaseTestCase):
    resource_file_name = None

    def load_test_content_as_bytes(self):
        if self.resource_file_name:
            file = open(os.path.join(self.get_path_to_assets(), self.resource_file_name), 'rb')
            content = file.read()
            file.close()
            return content

    def load_test_content_as_json(self):
        if self.resource_file_name:
            file = open(os.path.join(self.get_path_to_assets(), self.resource_file_name))
            content = json.load(file)
            file.close()
            return content

    def get_path_to_assets(self):
        """
        This function is used to return the current directory path
        :return: str: path to assets
        """
        root_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(root_dir,'assets')