import unittest
import sys
sys.path.append('../')
from meaningless import yaml_file_interface, WebExtractor, InvalidSearchError
from meaningless.bible_base_extractor import BaseExtractor


class UnitTests(unittest.TestCase):

    # Note: Tests will only be run if they are prefixed with test_ in their method name.
    #       All other methods will simply be interpreted as test helper functions.

    @staticmethod
    def get_test_translation():
        """
        A helper function to define the standardised translation for this set of tests.
        :return: Translation code
        :rtype: str
        """
        return 'WEB'

    @staticmethod
    def get_test_directory(translation='WEB'):
        """
        A helper function to determine the working directory for this set of unit tests
        :param translation: Translation code for the tests. For example, 'NIV', 'ESV', 'NLT'
        :type translation: str
        :return: Directory path containing readable files
        :rtype: str
        """
        return './static/unit_tests_bible_list_extractor/{0}'.format(translation)

    @staticmethod
    def get_test_file_extension():
        """
        A helper function to consolidate the file extension used for the extractor
        :return: File extension with the leading dot
        :rtype: str
        """
        return '.yaml'

    def test_get_passage_list_from_string(self):
        bible = WebExtractor(output_as_list=True)
        text = bible.search('1 John 1:8 - 9')
        john = ['\u2078 If we claim to be without sin, we deceive ourselves and the truth is not in us. ',
                '\u2079 If we confess our sins, he is faithful and just and will forgive us our sins and purify '
                'us from all unrighteousness.']
        self.assertEqual(john, text, 'Passage is incorrect')

    def test_get_passage_list_from_string_empty(self):
        bible = WebExtractor(output_as_list=True)
        self.assertRaises(InvalidSearchError, bible.search, '')

    def test_get_passage_list_from_string_without_passage_numbers(self):
        bible = WebExtractor(output_as_list=True, show_passage_numbers=False)
        text = bible.search('Haggai 1:3 - 4')
        haggai1 = ['Then the word of the Lord came through the prophet Haggai: ',
                   '\u201cIs it a time for you yourselves to be living in your paneled houses, '
                   'while this house remains a ruin?\u201d']
        self.assertEqual(haggai1, text, 'Passage is incorrect')

    def test_get_passage_list_from_string_nlt(self):
        bible = WebExtractor(output_as_list=True, translation='NLT')
        text = bible.search('1 John 1:8 - 9')
        john = ['\u2078 If we claim we have no sin, we are only fooling ourselves and not living in the truth. ',
                '\u2079 But if we confess our sins to him, he is faithful and just to forgive us our sins and '
                'to cleanse us from all wickedness.']
        self.assertEqual(john, text, 'Passage is incorrect')

    def test_get_passage_list(self):
        bible = WebExtractor(output_as_list=True)
        text = bible.get_passage('1 John', 1, 8)
        john = ['\u2078 If we claim to be without sin, we deceive ourselves and the truth is not in us.']
        self.assertEqual(john, text, 'Passage is incorrect')

    def test_get_passages_list(self):
        bible = WebExtractor(output_as_list=True)
        text = bible.get_passages('1 John', 1, 8, 9)
        john = ['\u2078 If we claim to be without sin, we deceive ourselves and the truth is not in us. ',
                '\u2079 If we confess our sins, he is faithful and just and will forgive us our sins and purify '
                'us from all unrighteousness.']
        self.assertEqual(john, text, 'Passage is incorrect')

    def test_get_chapter_list(self):
        bible = WebExtractor(output_as_list=True)
        text = bible.get_chapter('Ecclesiastes', 11)
        eccl11 = ['Ship your grain across the sea;\n'
                  '    after many days you may receive a return.\n',
                  '\u00b2 Invest in seven ventures, yes, in eight;\n'
                  '    you do not know what disaster may come upon the land. \n',
                  '\u00b3 If clouds are full of water,\n'
                  '    they pour rain on the earth.\n'
                  'Whether a tree falls to the south or to the north,\n'
                  '    in the place where it falls, there it will lie.\n',
                  '\u2074 Whoever watches the wind will not plant;\n'
                  '    whoever looks at the clouds will not reap. \n',
                  '\u2075 As you do not know the path of the wind,\n'
                  '    or how the body is formed in a mother\u2019s womb,\n'
                  'so you cannot understand the work of God,\n'
                  '    the Maker of all things. \n',
                  '\u2076 Sow your seed in the morning,\n'
                  '    and at evening let your hands not be idle,\n'
                  'for you do not know which will succeed,\n'
                  '    whether this or that,\n'
                  '    or whether both will do equally well. \n',
                  '\u2077 Light is sweet,\n'
                  '    and it pleases the eyes to see the sun.\n',
                  '\u2078 However many years anyone may live,\n'
                  '    let them enjoy them all.\nBut let them remember the days of darkness,\n'
                  '    for there will be many.\n'
                  '    Everything to come is meaningless. \n',
                  '\u2079 You who are young, be happy while you are young,\n'
                  '    and let your heart give you joy in the days of your youth.\n'
                  'Follow the ways of your heart\n'
                  '    and whatever your eyes see,\n'
                  'but know that for all these things\n'
                  '    God will bring you into judgment.\n',
                  '\u00b9\u2070 So then, banish anxiety from your heart\n'
                  '    and cast off the troubles of your body,\n'
                  '    for youth and vigor are meaningless.'
                  ]
        self.assertEqual(eccl11, text, 'Passage is incorrect')

    def test_get_chapters_list(self):
        bible = WebExtractor(output_as_list=True)
        text = bible.get_chapters('1 John', 1, 2)
        john = bible.get_chapter('1 John', 1) + bible.get_chapter('1 John', 2)
        # Getting multiple sequential chapters should be the same as appending multiple chapters manually
        self.assertEqual(john, text, 'Passage is incorrect')

    def test_get_passage_range_list(self):
        bible = WebExtractor(output_as_list=True)
        text = bible.get_passage_range('Ecclesiastes', 9, 18, 10, 1)
        eccl = ['\u00b9\u2078 Wisdom is better than weapons of war,\n'
                '    but one sinner destroys much good.',
                'As dead flies give perfume a bad smell,\n'
                '    so a little folly outweighs wisdom and honor.'
                ]
        self.assertEqual(eccl, text, 'Passage is incorrect')

    def test_get_book_list(self):
        bible = WebExtractor(output_as_list=True, translation=self.get_test_translation())
        text = bible.get_book('Philemon')
        static_file = '{0}/test_get_book_list.txt'.format(self.get_test_directory())
        with open(static_file, 'r', encoding='utf-8') as file:
            phil = file.read()
        # To avoid having to paste the entire contents of Philemon in the test, this is tested by joining all the
        # lines of the list into a single string and comparing against a test file
        self.assertEqual(phil, ''.join(text), 'Passage is incorrect')

    def test_get_passage_range_list_from_same_chapter(self):
        bible = WebExtractor(output_as_list=True)
        text = bible.get_passage_range('1 John', 1, 8, 1, 9)
        john = ['\u2078 If we claim to be without sin, we deceive ourselves and the truth is not in us. ',
                '\u2079 If we confess our sins, he is faithful and just and will forgive us our sins and purify '
                'us from all unrighteousness.']
        self.assertEqual(john, text, 'Passage is incorrect')

    def test_get_passages_list_with_stripped_whitespace(self):
        bible = WebExtractor(output_as_list=True, strip_excess_whitespace_from_list=True)
        text = bible.get_passages('Ecclesiastes', 11, 6, 7)
        eccl11 = ['\u2076 Sow your seed in the morning,\n'
                  '    and at evening let your hands not be idle,\n'
                  'for you do not know which will succeed,\n'
                  '    whether this or that,\n'
                  '    or whether both will do equally well.',
                  '\u2077 Light is sweet,\n'
                  '    and it pleases the eyes to see the sun.'
                  ]
        # These two passages are normally in a poetic format, each ending with a newline.
        # Toggling the flag parameter should not preserve these newline characters, but the inner newlines are kept.
        self.assertEqual(eccl11, text, 'Passage is incorrect')

    def test_get_chapter_list_with_ascii_punctuation(self):
        bible = WebExtractor(output_as_list=True, translation=self.get_test_translation(), use_ascii_punctuation=True)
        text = bible.get_chapter('Ecclesiastes', 2)
        static_file = '{0}/test_get_chapter_list_with_ascii_punctuation.txt'.format(self.get_test_directory())
        with open(static_file, 'r', encoding='utf-8') as file:
            eccl = file.read()
        # This chapter doesn't have Unicode single quotes, but should have the other translated characters
        self.assertEqual(eccl, ''.join(text), 'Passage is incorrect')

    def test_get_multiple_passage_list_from_string(self):
        bible = WebExtractor(output_as_list=True)
        text = bible.search_multiple(['1 John 1:8 - 9', 'Haggai 1:3'])
        passages = ['\u2078 If we claim to be without sin, we deceive ourselves and the truth is not in us. ',
                    '\u2079 If we confess our sins, he is faithful and just and will forgive us our sins and purify '
                    'us from all unrighteousness.\n',
                    '\u00b3 Then the word of the Lord came through the prophet Haggai:'
                    ]
        # The last passage of the first set ends with a newline character to denote separation from the other passage
        self.assertEqual(passages, text, 'Passage is incorrect')

    def test_get_multiple_passage_list_from_string_single(self):
        bible = WebExtractor(output_as_list=True)
        text1 = bible.search('1 John 1:8 - 9')
        text2 = bible.search_multiple(['1 John 1:8 - 9'])
        # Searching multiple passages with a one-item list should be the same as invoking the search method
        self.assertEqual(text1, text2, 'Passage is incorrect')

    def test_get_multiple_passage_list_from_string_one_invalid_passage(self):
        bible = WebExtractor(output_as_list=True)
        text1 = bible.search('Haggai 1:3')
        text2 = bible.search_multiple(['Barnabas 7', 'Haggai 1:3'])
        # An invalid passage would just be ignored
        self.assertEqual(text1, text2, 'Passage is incorrect')

    # -------------- Tests with the Base Extractor --------------
    # By extension, this should also cover any classes that build off the Base Extractor

    def test_get_base_passage_list(self):
        bible = BaseExtractor(file_reading_function=yaml_file_interface.read,
                              file_extension=self.get_test_file_extension(),
                              output_as_list=True, default_directory=self.get_test_directory(),
                              translation=self.get_test_translation())
        text = bible.get_passage('1 John', 1, 8)
        john = ['\u2078 If we say that we have no sin, we deceive ourselves, and the truth is not in us. ']
        self.assertEqual(john, text, 'Passage is incorrect')

    def test_get_base_passages_list(self):
        bible = BaseExtractor(file_reading_function=yaml_file_interface.read,
                              file_extension=self.get_test_file_extension(),
                              output_as_list=True, default_directory=self.get_test_directory(),
                              translation=self.get_test_translation())
        text = bible.get_passages('1 John', 1, 8, 9)
        john = ['\u2078 If we say that we have no sin, we deceive ourselves, and the truth is not in us. ',
                '\u2079 If we confess our sins, he is faithful and righteous to forgive us the sins, '
                'and to cleanse us from all unrighteousness. ']
        self.assertEqual(john, text, 'Passage is incorrect')

    def test_get_base_chapter_list(self):
        online_bible = WebExtractor(output_as_list=True, show_passage_numbers=False,
                                    translation=self.get_test_translation())
        bible = BaseExtractor(file_reading_function=yaml_file_interface.read,
                              file_extension=self.get_test_file_extension(),
                              output_as_list=True, show_passage_numbers=False,
                              default_directory=self.get_test_directory(), translation=self.get_test_translation())
        text = bible.get_chapter('Ecclesiastes', 11)
        eccl = online_bible.get_chapter('Ecclesiastes', 11)
        # Results should be identical between the web and base extractor
        # Ignoring passage numbers, as the web extractor omits this for the first passage of each chapter
        self.assertEqual(eccl, text, 'Passage is incorrect')

    def test_get_base_chapters_list(self):
        online_bible = WebExtractor(output_as_list=True, show_passage_numbers=False,
                                    translation=self.get_test_translation())
        bible = BaseExtractor(file_reading_function=yaml_file_interface.read,
                              file_extension=self.get_test_file_extension(),
                              output_as_list=True, show_passage_numbers=False,
                              default_directory=self.get_test_directory(), translation=self.get_test_translation())
        text = bible.get_chapters('Ecclesiastes', 11, 12)
        eccl = online_bible.get_chapters('Ecclesiastes', 11, 12)
        # Results should be identical between the web and base extractor
        # Ignoring passage numbers, as the web extractor omits this for the first passage of each chapter
        self.assertEqual(eccl, text, 'Passage is incorrect')

    def test_get_base_book_list(self):
        online_bible = WebExtractor(output_as_list=True, translation=self.get_test_translation())
        bible = BaseExtractor(file_reading_function=yaml_file_interface.read,
                              file_extension=self.get_test_file_extension(),
                              output_as_list=True, default_directory=self.get_test_directory(),
                              translation=self.get_test_translation())
        text = bible.get_book('Philemon')
        eccl = online_bible.get_book('Philemon')
        # Results should be identical between the web and base extractor
        self.assertEqual(eccl, text, 'Passage is incorrect')

    def test_get_base_passage_range_list(self):
        bible = BaseExtractor(file_reading_function=yaml_file_interface.read,
                              file_extension=self.get_test_file_extension(),
                              output_as_list=True, default_directory=self.get_test_directory(),
                              translation=self.get_test_translation())
        text = bible.get_passage_range('Ecclesiastes', 9, 18, 10, 1)
        eccl = ['\u00b9\u2078 Wisdom is better than weapons of war; but one sinner destroys much good.',
                '\u00b9 Dead flies cause the oil of the perfumer to produce an evil odor;\n'
                '    so does a little folly outweigh wisdom and honor.\n'
                ]
        self.assertEqual(eccl, text, 'Passage is incorrect')

    def test_get_base_passage_range_list_with_stripped_whitespace(self):
        bible = BaseExtractor(file_reading_function=yaml_file_interface.read,
                              file_extension=self.get_test_file_extension(),
                              output_as_list=True, strip_excess_whitespace_from_list=True,
                              default_directory=self.get_test_directory(), translation=self.get_test_translation())
        text = bible.get_passage_range('Ecclesiastes', 10, 1, 10, 2)
        eccl = ['\u00b9 Dead flies cause the oil of the perfumer to produce an evil odor;\n'
                '    so does a little folly outweigh wisdom and honor.',
                '\u00b2 A wise man\u2019s heart is at his right hand,\n'
                'but a fool\u2019s heart at his left.'
                ]
        self.assertEqual(eccl, text, 'Passage is incorrect')

    def test_get_base_book_list_with_ascii_punctuation(self):
        online_bible = WebExtractor(output_as_list=True, translation=self.get_test_translation(),
                                    show_passage_numbers=False, use_ascii_punctuation=True)
        bible = BaseExtractor(file_reading_function=yaml_file_interface.read,
                              file_extension=self.get_test_file_extension(),
                              output_as_list=True, default_directory=self.get_test_directory(),
                              translation=self.get_test_translation(), show_passage_numbers=False,
                              use_ascii_punctuation=True)
        text = bible.get_book('Ecclesiastes')
        eccl = online_bible.get_book('Ecclesiastes')
        # Results should be identical between the web and base extractor
        self.assertEqual(eccl, text, 'Passage is incorrect')

if __name__ == "__main__":
    unittest.main()
