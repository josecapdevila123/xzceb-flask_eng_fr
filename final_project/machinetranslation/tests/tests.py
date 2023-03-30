import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    
    def test_english_to_french_translation(self):
        # Test for the translation of the world ‘Hello’
        result = english_to_french('Hello')
        self.assertEqual(result, 'Bonjour')
        
    def test_french_to_english_translation(self):
        # Test for the translation of the world ‘Bonjour’
        result = french_to_english('Bonjour')
        self.assertEqual(result, 'Hello')
        
    def test_english_to_french_translation_custom_input(self):
        # Test for the translation of custom English text
        result = english_to_french('This is a test.')
        self.assertNotEqual(result, 'This is a test.')
        
    def test_french_to_english_translation_custom_input(self):
        # Test for the translation of custom French text
        result = french_to_english('Ceci est un test.')
        self.assertNotEqual(result, 'Ceci est un test.')
        
if __name__ == '__main__':
    unittest.main()
