import sys
sys.path.append("D:\Python Programs")

import vowels_in_string

import unittest
class Test_vowelss(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(vowels_in_string.vowels("lagnaer"),['a','e'])

if __name__=="__main__":
    unittest.main()
