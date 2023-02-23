

import sys
sys.path.append("D:\Python Programs")

import wordcount

import unittest
class Test_avg(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(wordcount.wcount("i am lagnar from avanigadda"),5)

if __name__=="__main__":
    unittest.main()
