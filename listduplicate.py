import sys
sys.path.append("D:\Python Programs")

import duplicatelist

import unittest
class Test_duplicate(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(duplicatelist.duplicate(([1,2,3,1,4,51,1,2,76,51])),([1, 2, 3, 4, 51, 76]))

if __name__=="__main__":
    unittest.main()
