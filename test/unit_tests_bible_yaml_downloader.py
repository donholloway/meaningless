import unittest
import sys
import os
import filecmp
sys.path.append('../src/')
from meaningless import bible_yaml_downloader
from meaningless.utilities import yaml_file_interface


class UnitTests(unittest.TestCase):

    # Note: Tests will only be run if they are prefixed with test_ in their method name.
    #       All other methods will simply be interpreted as test helper functions.

    def test_yaml_download(self):
        bible_yaml_downloader.yaml_download('Philemon', file_location='./tmp/test_yaml_download/')
        self.assertTrue(filecmp.cmp('./tmp/test_yaml_download/NIV/Philemon.yaml',
                                    './static/NIV/test_yaml_download.yaml'),
                        'Files do not match')

    def test_yaml_download_without_passage_numbers(self):
        bible_yaml_downloader.yaml_download('Philemon',
                                            file_location='./tmp/test_yaml_download_without_passage_numbers/',
                                            show_passage_numbers=False)
        self.assertTrue(filecmp.cmp('./tmp/test_yaml_download_without_passage_numbers/NIV/Philemon.yaml',
                                    './static/NIV/test_yaml_download_without_passage_numbers.yaml'),
                        'Files do not match')

    def test_yaml_download_invalid_book(self):
        bible_yaml_downloader.yaml_download('Barnabas', file_location='./tmp/test_yaml_download_invalid_book/')
        # An invalid book should fail fast and not bother with downloading
        self.assertFalse(os.path.exists('./tmp/test_yaml_download_invalid_book/'), 'File should not have downloaded')

    def test_yaml_download_nlt(self):
        bible_yaml_downloader.yaml_download('Philemon', file_location='./tmp/test_yaml_download_nlt/',
                                            translation='NLT')
        self.assertTrue(filecmp.cmp('./tmp/test_yaml_download_nlt/NLT/Philemon.yaml',
                                    './static/NLT/test_yaml_download_nlt.yaml'),
                        'Files do not match')

    def test_yaml_download_omitted_passage(self):
        bible_yaml_downloader.yaml_download('Romans', file_location='./tmp/test_yaml_download_omitted_passage/',
                                            translation='NLT')
        text = yaml_file_interface.read('./tmp/test_yaml_download_omitted_passage/NLT/Romans.yaml')['Romans'][16][24]
        self.assertEqual('', text, 'Files do not match')

    def test_yaml_download_with_stripped_whitespaces(self):
        bible_yaml_downloader.yaml_download('Philemon',
                                            file_location='./tmp/test_yaml_download_with_stripped_whitespaces/',
                                            strip_whitespaces=True)
        self.assertTrue(filecmp.cmp('./tmp/test_yaml_download_with_stripped_whitespaces/NIV/Philemon.yaml',
                                    './static/NIV/test_yaml_download_with_stripped_whitespaces.yaml'),
                        'Files do not match')

if __name__ == "__main__":
    unittest.main()
