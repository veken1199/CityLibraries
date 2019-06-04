from helpers import is_allowed_file_extension
import constants
from tests import BaseTestCase

class FileManagerTest(BaseTestCase):
    def test_allowed_file_extensions(self):
        for extension in constants.ALLOWED_EXTENSIONS:
            filename = 'filename.{}'.format(extension)
            self.assertTrue(is_allowed_file_extension(filename))

    def test_not_allowed_file_extensions(self):
        for extension in ['video', 'mp3', 'mp4', 'avi', 'pdf', 'html']:
            filename = 'filename.{}'.format(extension)
            self.assertFalse(is_allowed_file_extension(filename))

