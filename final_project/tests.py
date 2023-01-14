import unittest

from translator import englishToFrench, frenchToEnglish

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') 
        self.assertEqual(englishToFrench(null), null)
        

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish('Hello'), 'Bonjour') 
        self.assertEqual(frenchToEnglish(null), null)

        
unittest.main()