import sys
sys.path.append("D:\Python Programs")
import mergelists

import unittest
class Test_merge(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(mergelists.merge([1,2,3,4,5],[5,6,7,8,9,1]),[1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 1])

if __name__=="__main__":
    unittest.main()
