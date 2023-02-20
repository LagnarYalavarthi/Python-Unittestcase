import sys
sys.path.append("D:\Python Programs")

import alphanumcount

import unittest
class Test_counts(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(alphanumcount.ncount("lagnar12345"),(6, 5))

    def testcase2(self):
        self.assertEqual(alphanumcount.ncount(""),"string is empty")

if __name__=="__main__":
    unittest.main()
