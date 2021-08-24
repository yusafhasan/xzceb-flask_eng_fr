
import unittest

from translator import englishToFrench, frenchToEnglish


class TestEnglishtoFrench(unittest.TestCase):
    """Class for first unit test"""
    def test1(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
        self.assertEqual(englishToFrench(''), '')


class TestFrenchtoEnglish(unittest.TestCase):
    """class for second unit test"""
    def test1(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')
        self.assertEqual(frenchToEnglish(''), '')

unittest.main()
    