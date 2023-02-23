import sys
sys.path.append("D:\Python Programs")

import tupleswap

import unittest
class Test_swap(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(tupleswap.tswap((1,2),(10,20)),((10,20),(1,2)))

if __name__=="__main__":
    unittest.main()
