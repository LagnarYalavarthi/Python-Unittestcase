import sys
sys.path.append("D:\Python Programs")

import characters_in_string

import unittest
class Test_res(unittest.TestCase):
    def testcas_1(self):
        self.assertEqual(characters_in_string.totalch("lagnar"),6)
    def testcase_2(self):
        self.assertEqual(characters_in_string.totalch(""),0)

if __name__=="__main__":
    unittest.main()

