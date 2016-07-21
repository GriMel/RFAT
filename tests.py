from rfat import *
import unittest
from taglib import File
import shutil

class TestTransliterate(unittest.TestCase):
    """
    Class for testing transliterate function
    """
    def test_ukrainian_symbols(self):
        """
        Ukrainian symbols are properly transliterated
        """
        string = "Минає ніч від’їзду"
        expected = "Minaye nich vid’yizdu"
        self.assertEqual(transliterate(string), expected)

    def test_empty_string(self):
        """
        Empty string should return empty string
        """
        string = ""
        expected = ""
        self.assertEqual(transliterate(string), expected)

    def test_no_cyrillic_string(self):
        """
        If no cyrillic string should return string unchanged
        """
        string = "test"
        expected = "test"
        self.assertEqual(transliterate(string), expected)


class TestRenamer(unittest.TestCase):
    """
    Test filename translation
    """

    def tearDown(self):
        """
        Remove all mp3s
        """
        audios = filter(lambda x: x.endswith(".mp3"), os.listdir())
        if audios:
            for audio in audios:
                os.remove(audio)

    def test_filename_transliterate(self):
        """
        Given audio filename with cyrillic symbols shouldn't change extension
        """
        string = "тест.mp3"
        expected = "test.mp3"
        self.assertEqual(transliterate(string), expected)

    def test_bunch_of_files(self):
        """
        Bunch of files should be properly renamed
        """
        bunch = ["1.тест.mp3", "2.smash.mp3", "3.дdд.mp3"]
        expected = ["1.test.mp3", "2.smash.mp3", "3.ddd.mp3"]
        for audio in bunch:
            f = open(audio, 'w+')
            f.close()
        audios = filter(lambda x: x.endswith(".mp3"), os.listdir())
        for audio in audios:
            rename_audio(audio)
        audios = filter(lambda x: x.endswith(".mp3"), os.listdir())
        for a, b in zip(audios, expected):
            print(a, b)
        for filename, expectation in zip(audios, expected):
            self.assertEqual(filename, expectation)

if __name__ == "__main__":
    unittest.main()
