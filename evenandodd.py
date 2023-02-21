import sys
sys.path.append("D:\Python Programs")
import evenandoddinlist

import unittest
class Test_numbers(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(evenandoddinlist.evenodd([1,99,10,28,77,37,88]),([10, 28, 88], [1, 99, 77, 37]))

if __name__=="__main__":
    unittest.main()
