import unittest
import sys
sys.path.append('../')
from meaningless import JSONExtractor, yaml_file_interface

# These tests just test for certain components which differ from the base extractor


class UnitTests(unittest.TestCase):

    # Note: Tests will only be run if they are prefixed with test_ in their method name.
    #       All other methods will simply be interpreted as test helper functions.

    def test_json_extractor_settings(self):
        bible = JSONExtractor()
        self.assertEqual(bible.file_extension, '.json', 'Extension is incorrect')
        self.assertEqual(bible.file_reading_function.__name__, yaml_file_interface.read.__name__,
                         'Name of reading function is incorrect')

if __name__ == "__main__":
    unittest.main()
