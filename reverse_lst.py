import sys
sys.path.append("D:\Python Programs")
import reverse_list

import unittest
class Test_rev(unittest.TestCase):
    def testcase_1(self):
        self.assertListEqual(reverse_list.reverse([1,2,3,4]),[4,3,2,1])

if __name__=="__main__":
    unittest.main()
